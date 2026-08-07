"""Record scaffolder: copy a template, stamp an allocated ID, refuse to overwrite.

The failure this exists to prevent is not typing effort. It is hand-allocated IDs —
which fail quietly, because a collided ID does not break a reference, it re-points it
(see `ids.py`). Every other thing this module does is in service of making the
allocator the only way a record comes into existence.

Destinations are a table, not a chain of conditionals, so that moving a record type's
home is one line and so that the set of supported types is readable at a glance. The
paths come from `templates/records/README.md` and from the "copy to" line at the head
of each template; where those two disagreed, the template won, because it is the
thing a person reads while doing the work.
"""

from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any

import yaml

from ..config import Config
from .ids import EPISODE_SCOPED, STUDIO_SCOPE, allocate

# kebab-case, ASCII, no version markers. Rejected here rather than written and then
# caught by `validate --naming`, because by then the ID is spent.
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

FRONTMATTER_DELIM = "---"


class Base(StrEnum):
    """Which directory a destination is relative to."""

    LINE = "line"
    PRODUCTION = "production"
    STUDIO = "studio"
    REPO = "repo"


@dataclass(frozen=True)
class RecordSpec:
    """Everything the scaffolder needs to know about one record type."""

    id_type: str
    template: str  # repo-relative
    base: Base
    destination: str  # relative to `base`
    suffix: str = ".md"
    # Where this type lives when its scope is STUDIO rather than a line. `None`
    # means the repository does not define a home for it, and the scaffolder says so
    # rather than inventing one.
    studio_home: tuple[Base, str] | None = None


RECORD_TYPES: dict[str, RecordSpec] = {
    "source": RecordSpec(
        "SRC", "templates/records/_TEMPLATE_source_record.md", Base.LINE, "sources/records"
    ),
    "claim": RecordSpec("CLM", "templates/records/_TEMPLATE_claim.md", Base.LINE, "sources/claims"),
    "character": RecordSpec(
        "CHR", "templates/records/_TEMPLATE_character.md", Base.LINE, "characters/profiles"
    ),
    "location": RecordSpec(
        "LOC", "templates/records/_TEMPLATE_location.md", Base.LINE, "locations/profiles"
    ),
    "timeline_event": RecordSpec(
        "EVT", "templates/records/_TEMPLATE_timeline_event.md", Base.LINE, "timeline/events"
    ),
    "open_question": RecordSpec(
        "QST", "templates/records/_TEMPLATE_open_question.md", Base.LINE, "research/open_questions"
    ),
    "fact_check": RecordSpec(
        "FCK", "templates/records/_TEMPLATE_fact_check.md", Base.LINE, "research/fact_checks"
    ),
    "advisory_ruling": RecordSpec(
        "ADV", "templates/records/_TEMPLATE_advisory_ruling.md", Base.LINE, "advisory/rulings"
    ),
    # "alongside the line's corrections log" (templates/records/README.md); every
    # line.yaml points `corrections_log` at the studio bible, so that is alongside.
    "correction": RecordSpec(
        "COR", "templates/records/_TEMPLATE_correction.md", Base.STUDIO, "bible"
    ),
    "style_anchor": RecordSpec(
        "STA", "templates/records/_TEMPLATE_style_anchor.md", Base.LINE, "style/anchors"
    ),
    "continuity_character": RecordSpec(
        "CNC",
        "templates/records/_TEMPLATE_continuity_character.md",
        Base.LINE,
        "continuity/characters",
    ),
    "continuity_location": RecordSpec(
        "CNL",
        "templates/records/_TEMPLATE_continuity_location.md",
        Base.LINE,
        "continuity/locations",
    ),
    "shot": RecordSpec(
        "SHT",
        "templates/production/03_storyboard/_TEMPLATE_shot.yaml",
        Base.PRODUCTION,
        "03_storyboard/shots",
        suffix=".yaml",
    ),
    "prompt_card": RecordSpec(
        "PC",
        "templates/production/04_prompts/_TEMPLATE_card.prompt.yaml",
        Base.PRODUCTION,
        "04_prompts",
        suffix=".prompt.yaml",
        # A card reusable across productions is not in any production.
        studio_home=(Base.REPO, "prompts"),
    ),
}


class ScaffoldError(Exception):
    """Base for every refusal in this module."""


class UnknownRecordTypeError(ScaffoldError):
    pass


class DestinationError(ScaffoldError):
    """The repository does not say where this record goes, or the place is missing."""


class RecordExistsError(ScaffoldError, FileExistsError):
    """Refusing to overwrite. An existing record is somebody's work."""


@dataclass(frozen=True)
class LineContext:
    """The resolved home of a scope: its line, and the studio the line sits under."""

    scope: str
    line_code: str  # the `line:` field value — `ng-nigeria`, or `studio`
    line_dir: Path | None
    studio_dir: Path | None


def new_record(
    cfg: Config,
    record_type: str,
    scope: str,
    *,
    slug: str | None = None,
    episode: str | None = None,
    dry_run: bool = False,
) -> Path:
    """Create one record from its template and return the path written.

    `dry_run` still allocates, so the path it returns is the path that would be
    written — a dry run that guessed the ID would be answering a different question.
    It writes nothing and creates no directories.
    """
    spec = _spec(record_type)
    _check_slug(slug)
    context = _resolve_line(cfg, scope)

    record_id = allocate(cfg, spec.id_type, scope, episode)

    dest_dir = _destination(cfg, spec, context, episode)
    stem = f"{record_id}_{slug}" if slug else record_id
    path = dest_dir / f"{stem}{spec.suffix}"

    if path.exists():
        raise RecordExistsError(
            f"{path} already exists. Refusing to overwrite — a record is somebody's "
            "work, and the ID it carries may already be referenced."
        )
    if dry_run:
        return path

    rendered = _render(
        _template_text(cfg, spec),
        spec,
        record_id=record_id,
        line_code=context.line_code,
        episode=episode,
    )
    dest_dir.mkdir(parents=True, exist_ok=True)
    # Exclusive create: between the check above and here, another process may have
    # won the same serial. Losing that race must fail, not silently overwrite.
    try:
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(rendered)
    except FileExistsError as exc:
        raise RecordExistsError(f"{path} was created by something else mid-write.") from exc
    return path


# ------------------------------------------------------------------- resolution


def _spec(record_type: str) -> RecordSpec:
    try:
        return RECORD_TYPES[record_type]
    except KeyError:
        raise UnknownRecordTypeError(
            f"no template is registered for record type {record_type!r}. "
            f"Known types: {', '.join(sorted(RECORD_TYPES))}."
        ) from None


def _check_slug(slug: str | None) -> None:
    if slug is None:
        return
    if not SLUG_PATTERN.match(slug):
        raise ScaffoldError(
            f"slug {slug!r} is not kebab-case ASCII. Underscores separate fields and "
            "hyphens separate words within one — see standards/naming_conventions.md."
        )


def _resolve_line(cfg: Config, scope: str) -> LineContext:
    """Find the line whose `id_scope` is this scope, by reading line.yaml.

    Data-driven rather than derived from the directory name, because `id_scope` is
    the field the IDs are actually minted from and the two are allowed to differ.
    """
    if scope == STUDIO_SCOPE:
        studios = cfg.layout.iter_studios()
        if len(studios) != 1:
            raise DestinationError(
                f"scope {STUDIO_SCOPE} needs exactly one studio to be unambiguous; "
                f"found {len(studios)}. Name the studio explicitly."
            )
        return LineContext(scope, "studio", None, studios[0])

    matches = [
        line
        for line in cfg.layout.iter_lines()
        if _yaml_field(line / "line.yaml", "id_scope") == scope
    ]
    if not matches:
        raise DestinationError(
            f"no production line declares `id_scope: {scope}`. Lines seen: "
            f"{', '.join(p.name for p in cfg.layout.iter_lines()) or 'none'}."
        )
    if len(matches) > 1:
        raise DestinationError(
            f"{len(matches)} lines declare `id_scope: {scope}` — "
            f"{', '.join(p.name for p in matches)}. Two lines sharing a scope means "
            "their records share a serial space; fix that before allocating anything."
        )
    line_dir = matches[0]
    code = _yaml_field(line_dir / "line.yaml", "code") or line_dir.name
    return LineContext(scope, code, line_dir, line_dir.parent.parent)


def _destination(cfg: Config, spec: RecordSpec, ctx: LineContext, episode: str | None) -> Path:
    base, relative = spec.base, spec.destination
    if ctx.scope == STUDIO_SCOPE:
        if spec.studio_home is None:
            raise DestinationError(
                f"the repository defines no home for a {STUDIO_SCOPE}-scoped "
                f"{spec.id_type} record. templates/records/README.md places this type "
                "under a line. Allocate it against a line, or register the studio-level "
                "destination in that README first."
            )
        base, relative = spec.studio_home

    if base is Base.REPO:
        return cfg.root / relative
    if base is Base.STUDIO:
        if ctx.studio_dir is None:
            raise DestinationError(f"cannot locate the studio for scope {ctx.scope}.")
        return ctx.studio_dir / relative
    if ctx.line_dir is None:
        raise DestinationError(f"cannot locate the line directory for scope {ctx.scope}.")
    if base is Base.LINE:
        return ctx.line_dir / relative
    return _production_dir(ctx.line_dir, episode) / relative


def _production_dir(line_dir: Path, episode: str | None) -> Path:
    """Find the production whose `production.yaml` declares this code.

    Matched on the field rather than the folder name so that `EXP001_laboratory-scene`
    and a future rename of that folder both resolve.
    """
    productions = line_dir / "productions"
    if episode is None:
        raise DestinationError("an episode-scoped record needs a production code.")
    candidates = (
        sorted(p for p in productions.glob("*") if p.is_dir()) if productions.is_dir() else []
    )
    for candidate in candidates:
        if _yaml_field(candidate / "production.yaml", "code") == episode:
            return candidate
    raise DestinationError(
        f"no production under {productions} declares `code: {episode}`. "
        f"Productions seen: {', '.join(p.name for p in candidates) or 'none'}."
    )


def _yaml_field(path: Path, key: str) -> str | None:
    """One top-level scalar from a control record, or None if it cannot be had."""
    if not path.is_file():
        return None
    try:
        data: Any = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, yaml.YAMLError):
        return None
    if not isinstance(data, dict):
        return None
    value = data.get(key)
    return str(value).strip() if isinstance(value, str | int) else None


# --------------------------------------------------------------------- rendering


def _template_text(cfg: Config, spec: RecordSpec) -> str:
    template = cfg.root / spec.template
    if not template.is_file():
        raise DestinationError(f"template is missing: {spec.template}")
    return template.read_text(encoding="utf-8")


def _render(
    text: str,
    spec: RecordSpec,
    *,
    record_id: str,
    line_code: str,
    episode: str | None,
    today: dt.date | None = None,
) -> str:
    """Stamp the fields the toolkit knows. Everything else stays TBD, on purpose.

    `updated` is written QUOTED. Unquoted, YAML resolves an ISO date to a `date`
    object, every schema types the field as a string, and the record then fails
    validation with a message that reads like a schema bug.
    """
    stamp = (today or dt.date.today()).isoformat()
    fields: dict[str, str] = {
        "id": record_id,
        "line": line_code,
        "updated": f'"{stamp}"',
    }
    # A shot or card left holding the template's `S00E00` would validate and point at
    # the wrong production — the same silent-mis-resolution the IDs are guarded against.
    if episode and spec.id_type in EPISODE_SCOPED:
        fields["episode"] = episode

    if spec.suffix == ".md":
        head, body = _split_frontmatter(text)
        for key, value in fields.items():
            head = _set_field(head, key, value)
        return f"{FRONTMATTER_DELIM}\n{head}{FRONTMATTER_DELIM}\n{body}"

    for key, value in fields.items():
        text = _set_field(text, key, value)
    return text


def _split_frontmatter(text: str) -> tuple[str, str]:
    """Split on `---` *lines*, not on the substring.

    Several record templates open their front matter with a `# ------------` banner,
    and a substring split truncates the block there — dropping the `id:` field that
    follows and silently writing a record with a placeholder ID.
    """
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != FRONTMATTER_DELIM:
        raise ScaffoldError("template has no front matter; it cannot be stamped.")
    for i in range(1, len(lines)):
        if lines[i].strip() == FRONTMATTER_DELIM:
            return "".join(lines[1:i]), "".join(lines[i + 1 :])
    raise ScaffoldError("template front matter is opened but never closed.")


def _set_field(text: str, key: str, value: str) -> str:
    """Replace the first top-level `key:` line, keeping any trailing comment.

    Line-oriented rather than a YAML round-trip because these templates are mostly
    comment: dumping them back through PyYAML would delete the explanations that are
    the reason anyone can fill one in.
    """
    pattern = re.compile(
        rf"^{re.escape(key)}:(?P<value>[^\n#]*?)(?P<pad>[ \t]*)(?P<comment>#[^\n]*)?$",
        re.MULTILINE,
    )
    match = pattern.search(text)
    if match is None:
        return text
    comment = match.group("comment")
    tail = f"{match.group('pad')}{comment}" if comment else ""
    return f"{text[: match.start()]}{key}: {value}{tail}{text[match.end() :]}"
