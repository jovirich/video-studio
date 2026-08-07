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
    """
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return Document(path, {}, "", False, f"unreadable: {exc}")

    if not text.startswith(DELIM):
        return Document(path, {}, text, False)

    parts = text.split(DELIM, 2)
    if len(parts) < 3:
        return Document(path, {}, text, False, "front matter opened but not closed")

    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        return Document(path, {}, parts[2], True, f"invalid YAML front matter: {exc}")

    if not isinstance(meta, dict):
        return Document(path, {}, parts[2], True, "front matter is not a mapping")

    return Document(path, meta, parts[2], True)


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
