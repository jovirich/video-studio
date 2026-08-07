"""ID allocation, and the refusals that keep it honest.

Implements [standards/id_system.md](../../../standards/id_system.md). IDs are
permanent, never reused, never renumbered — and records reference each other by ID
*string*, not by path. That is the whole reason this module is written to refuse
rather than to guess: a duplicated ID does not break a reference, it silently
re-points it at whichever record wins, and nothing downstream reports an error.
`validate --sources`, the gate that would notice, is NOT BUILT. So the exception
raised here is the only thing standing between a hand-typed ID and an audit trail
that is quietly, permanently wrong.

Two places where the specification admits more than one reading, and the reading
taken:

1. **Serials are allocated per (TYPE, SCOPE), episode excluded.** The spec's SERIAL
   row says "monotonically allocated per (TYPE, SCOPE)" and lists EPISODE as a
   separate part of the grammar. A per-episode counter would be a new concept, so it
   is not introduced. A consequence worth having: a shot serial is unique across a
   whole line, so a mistyped episode code cannot resolve to a real other shot.
2. **The collision guard is scoped to the (TYPE, SCOPE) being allocated.** Refusing
   every allocation in the repository because one unrelated namespace is broken would
   make the toolkit unusable at exactly the moment it is most needed. `find_collisions`
   is exported unfiltered for a repository-wide audit.

This module reads front matter itself rather than calling `frontmatter.read`, because
that reader splits on the bare substring `---` and several record templates open with
a `# -----` banner comment inside the front matter block. A scanner that misses a
record's ID would hand out an ID that is already taken, which is the failure this
module exists to prevent.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from ..config import Config
from ..frontmatter import is_template
from ..paths import iter_files

# `PC` is two letters; the spec's "three-letter code" is aspiration, not fact.
# Scope is a line code (`NG`), `STUDIO`, `PLAT`, or a pack scope (`GFT`, `BIB`).
# `SEQ` serials are three digits so that a mistyped shot ID fails its pattern
# instead of resolving to a real sequence — hence the 3..4 range here.
ID_PATTERN = re.compile(
    r"^(?P<id_type>[A-Z]{2,3})"
    r"-(?P<scope>[A-Z]{2,6})"
    r"(?:-(?P<episode>S\d{2}E\d{2}|EXP\d{3}))?"
    r"-(?P<serial>\d{3,4})$"
)

SCOPE_PATTERN = re.compile(r"^[A-Z]{2,6}$")

# `S01E01` is the broadcast form. `EXP001` is the laboratory form — see
# episode.schema.json and _common.schema.json, where every episode-scoped ID
# pattern carries both alternatives.
EPISODE_PATTERN = re.compile(r"^(?:S\d{2}E\d{2}|EXP\d{3})$")

STUDIO_SCOPE = "STUDIO"

DEFAULT_SERIAL_WIDTH = 4
SERIAL_WIDTH: dict[str, int] = {"SEQ": 3}

# Types whose ID embeds a production code. `PC` is the exception that proves the
# rule: episode-scoped in a production, studio-scoped in prompts/.
EPISODE_SCOPED: frozenset[str] = frozenset({"SHT", "SEQ", "PC", "AST", "FCK", "CUE"})

RECORD_SUFFIXES: frozenset[str] = frozenset({".md", ".yaml", ".yml"})

FRONTMATTER_DELIM = "---"


class IdError(Exception):
    """Base for every refusal in this module."""


class IdCollisionError(IdError):
    """The same ID is carried by two different files.

    Raised instead of allocating, because allocating on top of a corrupt namespace
    compounds damage that cannot be undone: once a reference has been written
    against the wrong record, nothing in the repository records which one was meant.
    """

    def __init__(
        self,
        message: str,
        duplicates: dict[str, list[Path]],
        gaps: list[int],
    ) -> None:
        super().__init__(message)
        self.duplicates = duplicates
        self.gaps = gaps


@dataclass(frozen=True)
class ParsedId:
    """One decomposed identifier. `width` is preserved so round-tripping is exact."""

    raw: str
    id_type: str
    scope: str
    serial: int
    episode: str | None
    width: int

    @property
    def key(self) -> tuple[str, str]:
        """The allocation key. Deliberately excludes the episode — see module docstring."""
        return (self.id_type, self.scope)


def parse_id(s: str) -> ParsedId | None:
    """Decompose an ID. Returns None for anything that is not one.

    Non-IDs are common and legitimate — `LINE-NG`, `STU-AFH`, `EP-NG-EXP001` all
    identify things that are not serial-allocated records. Returning None rather
    than raising keeps the scanner from treating a control record as corruption.
    """
    if not isinstance(s, str):
        return None
    match = ID_PATTERN.match(s.strip())
    if match is None:
        return None
    serial = match.group("serial")
    return ParsedId(
        raw=match.group(0),
        id_type=match.group("id_type"),
        scope=match.group("scope"),
        serial=int(serial),
        episode=match.group("episode"),
        width=len(serial),
    )


def format_id(id_type: str, scope: str, serial: int, episode: str | None = None) -> str:
    """Compose an ID from its parts, zero-padded to the width the type uses."""
    width = SERIAL_WIDTH.get(id_type, DEFAULT_SERIAL_WIDTH)
    parts = [id_type, scope]
    if episode:
        parts.append(episode)
    parts.append(f"{serial:0{width}d}")
    return "-".join(parts)


# --------------------------------------------------------------------- scanning


def _read_meta(path: Path) -> dict[str, Any]:
    """Structured head of a record: YAML front matter, or a whole YAML file.

    Returns `{}` for anything unparseable. One malformed file must not stop a scan
    over four hundred good ones — but see `scan_unreadable` for the case where that
    silence would be dangerous.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    raw = _frontmatter_block(text) if path.suffix == ".md" else text
    if raw is None:
        return {}
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def _frontmatter_block(text: str) -> str | None:
    """The text between the opening and closing `---` *lines*.

    Line-anchored on purpose. Several record templates open their front matter with
    a `# ------------` banner comment, and a substring split on `---` truncates the
    block at that banner — losing the `id:` field that follows it.
    """
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != FRONTMATTER_DELIM:
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == FRONTMATTER_DELIM:
            return "".join(lines[1:i])
    return None


def _ids_in(path: Path) -> set[str]:
    """Every ID this file *claims*, from its fields — never from its name.

    Filenames lie. A record copied from another record keeps the old ID in its name
    long after the field was corrected, and vice versa. The field is the identity.
    """
    meta = _read_meta(path)
    found: set[str] = set()

    value = meta.get("id")
    if isinstance(value, str):
        found.add(value.strip())

    # An asset manifest is a ledger of many identities rather than one record, and
    # AST serials exist nowhere else. Missing them would re-issue a live asset ID.
    assets = meta.get("assets")
    if isinstance(assets, list):
        for entry in assets:
            if isinstance(entry, dict):
                asset_id = entry.get("asset_id")
                if isinstance(asset_id, str):
                    found.add(asset_id.strip())

    return found


def build_index(root: Path) -> dict[str, list[Path]]:
    """Map every allocated ID in the tree to the files that claim it.

    A list rather than a path: the whole point is to see when there is more than one.
    Templates are excluded — their placeholder IDs (`SRC-XX-0000`) are meant to
    collide with each other and belong to no scope.
    """
    index: dict[str, list[Path]] = {}
    for path in iter_files(root):
        if path.suffix not in RECORD_SUFFIXES or is_template(path):
            continue
        for raw in _ids_in(path):
            index.setdefault(raw, []).append(path)
    return index


def _matches(raw: str, id_type: str | None, scope: str | None) -> ParsedId | None:
    parsed = parse_id(raw)
    if parsed is None:
        return None
    if id_type is not None and parsed.id_type != id_type:
        return None
    if scope is not None and parsed.scope != scope:
        return None
    return parsed


def scan_existing(root: Path, id_type: str, scope: str) -> set[int]:
    """Every serial already allocated for a (type, scope) pair.

    Scans YAML files and markdown front matter alike, and finds IDs by their `id:`
    field. Episode is not part of the key: `SHT-NG-S01E01-0142` and
    `SHT-NG-EXP001-0143` share one serial space. See the module docstring.
    """
    return {
        parsed.serial
        for raw in build_index(root)
        if (parsed := _matches(raw, id_type, scope)) is not None
    }


def find_collisions(
    root: Path, id_type: str | None = None, scope: str | None = None
) -> dict[str, list[Path]]:
    """IDs claimed by more than one file. Unfiltered, this is a repository audit."""
    return _collisions(build_index(root), id_type, scope)


def _collisions(
    index: dict[str, list[Path]], id_type: str | None, scope: str | None
) -> dict[str, list[Path]]:
    return {
        raw: sorted(paths)
        for raw, paths in index.items()
        if len(paths) > 1 and _matches(raw, id_type, scope) is not None
    }


def find_gaps(existing: set[int]) -> list[int]:
    """Serials missing below the highest allocated one.

    Records are never deleted — a retired record keeps its ID as a tombstone — so a
    gap means a serial was skipped, which means somebody typed an ID. On its own
    that is suspicious rather than fatal; combined with a collision it is the
    signature the spec names.
    """
    if not existing:
        return []
    return sorted(set(range(1, max(existing) + 1)) - existing)


def next_serial(existing: set[int]) -> int:
    """The next serial. Highest plus one — never the lowest free one.

    Filling a gap would re-issue a serial that a tombstone or a lost file may still
    hold, which is precisely the reuse the ID system forbids.
    """
    return max(existing) + 1 if existing else 1


# ------------------------------------------------------------------- allocation


def allocate(cfg: Config, id_type: str, scope: str, episode: str | None = None) -> str:
    """Allocate the next ID for a (type, scope) pair, or refuse.

    Refuses on a duplicate before it refuses on anything else, because every other
    check is meaningless over a namespace that is already ambiguous.
    """
    _check_scope(scope)
    _check_episode(id_type, scope, episode)

    index = build_index(cfg.root)
    duplicates = _collisions(index, id_type, scope)
    existing = {
        parsed.serial for raw in index if (parsed := _matches(raw, id_type, scope)) is not None
    }

    if duplicates:
        gaps = find_gaps(existing)
        raise IdCollisionError(
            _collision_message(cfg.root, id_type, scope, duplicates, gaps), duplicates, gaps
        )

    return format_id(id_type, scope, next_serial(existing), episode)


def _check_scope(scope: str) -> None:
    if not SCOPE_PATTERN.match(scope):
        raise IdError(
            f"scope {scope!r} is not a scope code. Expected a line code in caps without "
            f"the country prefix ('NG', 'GH'), '{STUDIO_SCOPE}' for cross-line entities, "
            "or a registered pack scope. See standards/id_system.md."
        )


def _check_episode(id_type: str, scope: str, episode: str | None) -> None:
    """An episode-scoped ID without an episode is a different ID, not a shorter one."""
    wants_episode = id_type in EPISODE_SCOPED and scope != STUDIO_SCOPE
    if wants_episode and not episode:
        raise IdError(
            f"{id_type} is episode-scoped: allocating one needs a production code "
            "(S01E01, or EXP001 for a laboratory production)."
        )
    if not wants_episode and episode:
        raise IdError(
            f"{id_type}-{scope} is not episode-scoped; drop the episode {episode!r}. "
            f"Episode-scoped types are {', '.join(sorted(EPISODE_SCOPED))}."
        )
    if episode and not EPISODE_PATTERN.match(episode):
        raise IdError(
            f"production code {episode!r} is neither the broadcast form S01E01 nor the "
            "laboratory form EXP001."
        )


def _collision_message(
    root: Path,
    id_type: str,
    scope: str,
    duplicates: dict[str, list[Path]],
    gaps: list[int],
) -> str:
    width = SERIAL_WIDTH.get(id_type, DEFAULT_SERIAL_WIDTH)
    lines = [
        f"Refusing to allocate {id_type}-{scope}-*: "
        f"{len(duplicates)} ID(s) are claimed by more than one file."
    ]
    for raw, paths in sorted(duplicates.items()):
        lines.append(f"  {raw}")
        lines.extend(f"    {_rel(p, root)}" for p in paths)
    lines.append(
        "A duplicate ID does not break a reference — it re-points every reference at "
        "whichever file wins. Decide which record keeps the ID, give the other a NEW "
        "serial (never a reused one), and update what points at it."
    )
    if gaps:
        shown = ", ".join(f"{g:0{width}d}" for g in gaps[:10])
        more = "" if len(gaps) <= 10 else f" (+{len(gaps) - 10} more)"
        lines.append(
            f"Serial(s) {shown}{more} are also missing below the highest allocated. "
            "A gap together with a collision is the signature of hand-edited IDs "
            "(standards/id_system.md § Allocation) — assume more than one ID is wrong "
            "and audit the whole namespace with find_collisions()."
        )
    return "\n".join(lines)


def _rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)
