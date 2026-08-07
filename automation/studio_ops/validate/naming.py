"""Naming convention gate.

Enforces standards/naming_conventions.md. These rules exist so that sorting,
globbing, and cross-platform sync all behave, and so a filename still says what a
thing is eighteen months later.

Maturity: IMPLEMENTED.
"""

from __future__ import annotations

import re
from pathlib import Path

from ..config import Config
from ..paths import iter_files
from ..result import Finding, GateReport, Severity, rel

GATE = "naming"

# Version markers that are not versions. Matched as whole words so that legitimate
# content words ("copyright", "golden") are not caught.
BANNED_WORDS = re.compile(
    r"(?<![a-z0-9])(final|latest|new|old|copy|backup|untitled|temp|tmp|asdf|"
    r"draft\d*|version\d*|v\d+_\d+)(?![a-z0-9])",
    re.IGNORECASE,
)

# `test` is a banned marker in content filenames and a required prefix in test code.
# Source trees carry their own conventions, so they are exempt from the content rules.
CODE_DIRS = ("automation/", "tests/")

NON_ASCII = re.compile(r"[^\x00-\x7F]")

# Dates that are not ISO-8601. DD-MM-YYYY and MM-DD-YYYY are indistinguishable,
# which is precisely the problem.
NON_ISO_DATE = re.compile(r"(?<!\d)(\d{2})[-_](\d{2})[-_](\d{4})(?!\d)")

MAX_PATH_LEN = 180

# Paths whose names are set by external tools and are not ours to rename.
EXEMPT_DIRS = frozenset({".git", ".github", ".vscode", "node_modules", ".venv"})
EXEMPT_NAMES = frozenset(
    {
        "README.md",
        "ROADMAP.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "Makefile",
        "PULL_REQUEST_TEMPLATE.md",
        "MEMORY.md",
    }
)


def run(cfg: Config) -> GateReport:
    report = GateReport(gate=GATE)
    root = cfg.root

    for path in iter_files(root):
        if any(part in EXEMPT_DIRS for part in path.parts):
            continue
        report.files_checked += 1
        relpath = rel(path, root)
        name = path.name

        if len(relpath) > MAX_PATH_LEN:
            report.findings.append(
                Finding(
                    GATE,
                    Severity.ERROR,
                    f"path is {len(relpath)} characters; limit is {MAX_PATH_LEN}",
                    relpath,
                    rule="path-length",
                    hint="Windows still enforces a total path limit; deep trees break sync tools.",
                )
            )

        if " " in relpath:
            report.findings.append(
                Finding(
                    GATE,
                    Severity.ERROR,
                    "path contains a space",
                    relpath,
                    rule="no-spaces",
                    hint="Use underscores between fields and hyphens within a field.",
                )
            )

        if NON_ASCII.search(relpath):
            report.findings.append(
                Finding(
                    GATE,
                    Severity.ERROR,
                    "path contains non-ASCII characters",
                    relpath,
                    rule="ascii-only",
                    hint="Diacritics belong in the content, never the path — platforms "
                    "normalise them differently and sync tools corrupt them.",
                )
            )

        is_code = relpath.startswith(CODE_DIRS) and path.suffix in {".py", ".toml", ".cfg"}
        if name not in EXEMPT_NAMES and not is_code and BANNED_WORDS.search(path.stem):
            match = BANNED_WORDS.search(path.stem)
            assert match is not None
            report.findings.append(
                Finding(
                    GATE,
                    Severity.ERROR,
                    f"filename contains banned version marker '{match.group(0)}'",
                    relpath,
                    rule="numeric-versions",
                    hint="Versions are numeric and zero-padded: _v01, _v02.",
                )
            )

        if NON_ISO_DATE.search(name):
            report.findings.append(
                Finding(
                    GATE,
                    Severity.ERROR,
                    "filename contains a non-ISO date",
                    relpath,
                    rule="iso-dates",
                    hint="Dates are YYYY-MM-DD. Locale order is ambiguous.",
                )
            )

        _check_template_not_filled(path, relpath, report)

    return report


def _check_template_not_filled(path: Path, relpath: str, report: GateReport) -> None:
    """Catch a template that was filled in place instead of copied.

    The most common real mistake in this repository's workflow: someone opens the
    template, fills it in, and saves over it. Caught here before the template is lost.
    """
    if not path.name.startswith("_TEMPLATE_") or path.suffix not in {".md", ".yaml", ".yml"}:
        return
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return
    head = text[:600]
    if "status: locked" in head or "status: review" in head:
        report.findings.append(
            Finding(
                GATE,
                Severity.ERROR,
                "template has a non-draft status — it was probably filled in place",
                relpath,
                rule="template-not-filled",
                hint="Copy the template to a new file. Restore this one from git.",
            )
        )
