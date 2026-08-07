"""Documentation-reality gate.

Enforces the DESIGNED / IMPLEMENTED / TESTED discipline mechanically, because the
discipline does not survive on good intentions. Documentation drifts toward
optimism by default: a command gets specified, written about in six places, and
never built — and every one of those six places reads as though it works.

The rule: **prose that names an unimplemented command must say so nearby.**

Maturity: IMPLEMENTED.
"""

from __future__ import annotations

import re

from ..config import Config
from ..paths import iter_files
from ..result import Finding, GateReport, Severity, rel

GATE = "reality"

# Commands that do not exist. Kept in step with `validate/__init__.py` UNBUILT and
# the NOT BUILT rows in automation/README.md.
UNBUILT_COMMANDS: frozenset[str] = frozenset(
    {
        "new-studio",
        "new-line",
        "new-production",
        "new-episode",
        "new-pack",
        "new-record",
        "new-prompt",
        "report",
        "promptlib",
        "pipeline",
        "status",
    }
)

# Gate flags that do not exist.
UNBUILT_FLAGS: frozenset[str] = frozenset(
    {"--sources", "--canon", "--prompts", "--packs", "--delivery", "--all"}
)

INVOCATION = re.compile(
    r"studio_ops\s+(?P<cmd>[a-z][a-z-]*)|"
    r"studio_ops\s+validate\s+(?P<flag>--[a-z-]+)"
)

# Any of these near an invocation discharges the obligation.
MARKERS = re.compile(
    r"NOT[\s_-]?BUILT|not built|DESIGNED|NOT[\s_-]?STARTED|"
    r"does not exist|unimplemented|aspirational|stub",
    re.IGNORECASE,
)

# Files whose whole purpose is to describe maturity; they are the source of truth
# rather than a consumer of it.
EXEMPT = (
    "docs/status.md",
    "automation/README.md",
    "docs/api/README.md",
    "automation/studio_ops/",
    "automation/tests/",
    "CHANGELOG.md",
)

# How far from the invocation a marker may sit and still count.
CONTEXT_LINES = 3


def run(cfg: Config) -> GateReport:
    report = GateReport(gate=GATE)
    root = cfg.root

    for path in iter_files(root, suffix=".md"):
        relpath = rel(path, root)
        if relpath.startswith(EXEMPT):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        report.files_checked += 1

        for i, line in enumerate(lines):
            for match in INVOCATION.finditer(line):
                token = match.group("cmd") or match.group("flag")
                if token is None:
                    continue
                if token == "validate":
                    continue
                if token not in UNBUILT_COMMANDS and token not in UNBUILT_FLAGS:
                    continue

                window = "\n".join(lines[max(0, i - CONTEXT_LINES) : i + CONTEXT_LINES + 1])
                if MARKERS.search(window):
                    continue

                report.findings.append(
                    Finding(
                        GATE,
                        Severity.ERROR,
                        f"names `studio_ops {token}`, which is NOT BUILT, without saying so",
                        relpath,
                        i + 1,
                        rule="unmarked-unbuilt",
                        hint=(
                            "Add a NOT BUILT marker within three lines, or describe the "
                            "manual equivalent. A command named without a marker reads "
                            "as working software."
                        ),
                    )
                )

    return report
