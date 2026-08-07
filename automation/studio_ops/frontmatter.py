"""YAML front matter handling.

Kept separate from the validators so the parse failure mode is uniform: a malformed
document produces a finding, never a traceback that stops the whole run.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

DELIM = "---"


@dataclass(frozen=True)
class Document:
    path: Path
    meta: dict[str, Any]
    body: str
    has_frontmatter: bool
    error: str | None = None


def read(path: Path) -> Document:
    """Read a markdown document, parsing front matter if present.

    A parse error is returned on the Document rather than raised — one bad file
    should not abort a validation run over four hundred good ones.

    The closing delimiter is matched as a WHOLE LINE, not as a substring.

    That distinction is not pedantry. An earlier version split on the bare string
    `---`, which meant any front matter containing a banner comment — `# --------` —
    terminated at the banner. Eleven of thirteen record templates use exactly that
    style, so their `id` and `type` fields parsed as empty. And because
    `validate --schemas` routes records by their `type` field, a real record built
    from one of those templates would have passed the schema gate *by being
    invisible to it*: no error, no warning, simply never checked.

    A gate that silently skips what it cannot see is worse than no gate. Hence the
    regression test in test_validators.py.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return Document(path, {}, "", False, f"unreadable: {exc}")

    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != DELIM:
        return Document(path, {}, text, False)

    for index in range(1, len(lines)):
        if lines[index].strip() == DELIM:
            block = "".join(lines[1:index])
            body = "".join(lines[index + 1 :])
            break
    else:
        return Document(path, {}, text, False, "front matter opened but not closed")

    try:
        meta = yaml.safe_load(block) or {}
    except yaml.YAMLError as exc:
        return Document(path, {}, body, True, f"invalid YAML front matter: {exc}")

    if not isinstance(meta, dict):
        return Document(path, {}, body, True, "front matter is not a mapping")

    return Document(path, meta, body, True)


def read_yaml(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    """Read a standalone YAML file. Returns (data, error)."""
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError) as exc:
        return None, f"unreadable: {exc}"
    except yaml.YAMLError as exc:
        return None, f"invalid YAML: {exc}"
    if raw is None:
        return {}, None
    if not isinstance(raw, dict):
        return None, "top level is not a mapping"
    return raw, None


def write(path: Path, meta: dict[str, Any], body: str) -> None:
    """Write a document with front matter, preserving key order."""
    dumped = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).rstrip()
    path.write_text(f"{DELIM}\n{dumped}\n{DELIM}\n{body.lstrip()}", encoding="utf-8")


def is_template(path: Path) -> bool:
    """Templates are exempt from most record rules; they are meant to be incomplete."""
    return path.name.startswith("_TEMPLATE_") or "_TEMPLATE_" in path.parts
