"""Repository root hygiene gate.

Exists because documentation accumulates at repo root by default, and a root with
four hundred loose markdown files is unnavigable in every IDE. The rule is enforced
mechanically rather than by review discipline, because review discipline does not
survive a deadline.

Maturity: IMPLEMENTED.
"""

from __future__ import annotations

from ..config import Config
from ..paths import IGNORE_DIRS, ROOT_DIRS, ROOT_WHITELIST, ROOT_WHITELIST_SUFFIXES
from ..result import Finding, GateReport, Severity

GATE = "root-hygiene"

# Where a stray root file most likely belongs. Suggesting a destination turns a
# rejection into an action.
SUGGESTIONS: dict[str, str] = {
    "deploy": "docs/deployment/",
    "runbook": "docs/runbook/",
    "architecture": "docs/architecture/",
    "adr": "docs/decisions/",
    "decision": "docs/decisions/",
    "security": "docs/security/",
    "audit": "docs/security/",
    "sprint": "docs/archive/sprints/",
    "week": "docs/archive/weeks/",
    "status": "docs/",
    "summary": "docs/archive/misc/",
    "report": "docs/archive/misc/",
    "notes": "docs/archive/misc/",
    "todo": "docs/archive/misc/",
    "onboarding": "docs/onboarding/",
    "training": "docs/training/",
    "checklist": "ops/checklists/",
    "schema": "standards/schemas/",
    "prompt": "prompts/",
}


def run(cfg: Config) -> GateReport:
    report = GateReport(gate=GATE)
    root = cfg.root

    for entry in sorted(root.iterdir()):
        report.files_checked += 1
        name = entry.name

        if entry.is_dir():
            # Tool caches and build output are gitignored; they are not placement errors.
            if name in IGNORE_DIRS or name.endswith((".egg-info", "_cache")):
                continue
            if name not in ROOT_DIRS:
                report.findings.append(
                    Finding(
                        GATE,
                        Severity.ERROR,
                        f"unexpected directory at repository root: {name}/",
                        name,
                        rule="root-dirs",
                        hint="Root directories are fixed by the platform contract. "
                        "See automation/studio_ops/paths.py ROOT_DIRS.",
                    )
                )
            continue

        if name in ROOT_WHITELIST:
            continue
        if any(name.endswith(suffix) for suffix in ROOT_WHITELIST_SUFFIXES):
            continue

        report.findings.append(
            Finding(
                GATE,
                Severity.ERROR,
                f"file not permitted at repository root: {name}",
                name,
                rule="root-whitelist",
                hint=_suggest(name),
            )
        )

    return report


def _suggest(name: str) -> str:
    lowered = name.lower()
    for keyword, destination in SUGGESTIONS.items():
        if keyword in lowered:
            return f"Move it to {destination}"
    return (
        "Move it into a semantic subfolder under docs/. "
        "See CONTRIBUTING.md § File placement for the whitelist."
    )
