"""Documentation-reality gate.

Enforces the DESIGNED / IMPLEMENTED / TESTED discipline mechanically, because the
discipline does not survive on good intentions.

Documentation drifts in **both** directions, and both are checked here:

1. **Over-claiming.** A command gets specified, written about in six places, and
   never built — and every one of those six places reads as though it works.
   Rule: prose naming an unimplemented command must say so nearby.

2. **Stale pessimism.** A command gets built, and the six places still say it does
   not exist. This is the one that actually happened: ROADMAP.md carried
   `studio_ops toolkit — NOT BUILT` for several commits after the toolkit was
   implemented and passing.
   Rule: a NOT BUILT marker may not sit next to a command that is implemented.

The second is the more dangerous failure with more than one agent on the repository.
An over-claim disappoints whoever tries the command. A stale NOT BUILT invites a
second agent to rebuild something that already exists, and gives them no way to tell
which document is current.

docs/status.md is the single authority on maturity. Everything else links to it.

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
    {"--sources", "--canon", "--prompts", "--packs", "--delivery"}
)

# Commands and flags that DO exist. Marking one NOT BUILT is stale documentation.
# Kept in step with validate/__init__.py IMPLEMENTED.
#
# `--all` belongs here. It runs, and it exits 2 *because* it includes the unbuilt
# gates — reporting the gap is its job, not evidence that it is missing. Classifying
# it as unbuilt is what produced a blanket NOT BUILT marker over the README quick
# start, where `python -m venv` and `pip install` also sat.
BUILT_FLAGS: frozenset[str] = frozenset(
    {"--schemas", "--naming", "--links", "--root-hygiene", "--reality", "--all"}
)

# The `validate --flag` alternative MUST come first. Alternation is ordered, so with
# the bare-command branch first, `studio_ops validate --naming` matched `validate` and
# the flag was never examined — which is how the stale-NOT-BUILT case went undetected
# in the first place.
INVOCATION = re.compile(
    r"studio_ops\s+validate\s+(?P<flag>--[a-z-]+)|studio_ops\s+(?P<cmd>[a-z][a-z-]*)"
)

# Any of these near an invocation discharges the obligation.
MARKERS = re.compile(
    r"NOT[\s_-]?BUILT|not built|DESIGNED|NOT[\s_-]?STARTED|"
    r"does not exist|unimplemented|aspirational|stub",
    re.IGNORECASE,
)

# Narrower than MARKERS: only the phrases that assert a thing does not exist. A
# document may legitimately say DESIGNED near a built command (describing the design);
# it may not say NOT BUILT.
STALE_MARKER = re.compile(r"NOT[\s_-]?BUILT|not built|does not exist|unimplemented", re.IGNORECASE)

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
                token = match.group("flag") or match.group("cmd")
                if token is None:
                    continue
                if token == "validate":
                    continue
                window = "\n".join(lines[max(0, i - CONTEXT_LINES) : i + CONTEXT_LINES + 1])

                if token in BUILT_FLAGS:
                    # Stale pessimism: this works, and the document says it does not.
                    #
                    # Scoped to the SAME LINE, unlike the over-claim check below. A
                    # stale verdict is written against its command — a table row, or
                    # a trailing comment. The wider window produced false positives
                    # on the common shape of a code block listing a working command
                    # on one line and an unbuilt one, correctly marked, on the next.
                    if STALE_MARKER.search(line):
                        report.findings.append(
                            Finding(
                                GATE,
                                Severity.ERROR,
                                f"marks `studio_ops validate {token}` NOT BUILT, but it is "
                                "IMPLEMENTED — stale documentation",
                                relpath,
                                i + 1,
                                rule="stale-not-built",
                                hint=(
                                    "Remove the marker. docs/status.md is the single "
                                    "authority on maturity; other documents link to it "
                                    "rather than restating a verdict."
                                ),
                            )
                        )
                    continue

                if token not in UNBUILT_COMMANDS and token not in UNBUILT_FLAGS:
                    continue

                # Over-claiming: this does not work, and the document does not say so.
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
