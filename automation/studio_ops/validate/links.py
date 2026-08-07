"""Internal link gate.

A repository whose navigation is its primary interface needs its links to resolve.
Dead cross-references are how a four-tier structure becomes unusable in practice
regardless of how well it is designed.

Maturity: IMPLEMENTED.
"""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

from ..config import Config
from ..paths import iter_files
from ..result import Finding, GateReport, Severity, rel

GATE = "links"

# Markdown inline links. Reference-style and HTML anchors are out of scope; if they
# start appearing, extend here rather than silently under-reporting.
LINK = re.compile(r"(?<!!)\[(?P<text>[^\]]*)\]\((?P<target>[^)\s]+)(?:\s+\"[^\"]*\")?\)")

EXTERNAL = ("http://", "https://", "mailto:", "tel:", "#")

# Directories whose contents are intentionally absent from git (media, build output).
# A link into them is a specification, not a broken reference.
TOLERATED_MISSING = ("05_assets/", "masters/", "renders/", "stems/")


def run(cfg: Config) -> GateReport:
    report = GateReport(gate=GATE)
    root = cfg.root

    for path in iter_files(root, suffix=".md"):
        report.files_checked += 1
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            report.findings.append(
                Finding(GATE, Severity.ERROR, f"unreadable: {exc}", rel(path, root))
            )
            continue

        for lineno, line in enumerate(text.splitlines(), start=1):
            if line.lstrip().startswith(("    ", "\t")) or line.lstrip().startswith("```"):
                continue
            for match in LINK.finditer(line):
                target = match.group("target")
                if target.startswith(EXTERNAL):
                    continue
                _check_target(cfg, path, target, lineno, report)

    return report


def _check_target(cfg: Config, source: Path, target: str, lineno: int, report: GateReport) -> None:
    root = cfg.root
    clean = unquote(target.split("#", 1)[0])
    if not clean:
        return  # pure anchor within the same document

    if clean.startswith("/"):
        report.findings.append(
            Finding(
                GATE,
                Severity.WARNING,
                f"absolute link '{target}' — use a relative path",
                rel(source, root),
                lineno,
                rule="relative-links",
                hint="Absolute links break when the repository is cloned elsewhere.",
            )
        )
        return

    resolved = (source.parent / clean).resolve()

    if resolved.exists():
        return

    if any(tol in clean for tol in TOLERATED_MISSING):
        return  # media path, intentionally not in git

    # A link to a directory is valid if the directory exists, with or without a
    # trailing slash; .resolve() handles both, so reaching here means it does not.
    report.findings.append(
        Finding(
            GATE,
            Severity.ERROR,
            f"broken internal link: {target}",
            rel(source, root),
            lineno,
            rule="dead-link",
            hint=f"Resolves to {rel(resolved, root)}, which does not exist.",
        )
    )
