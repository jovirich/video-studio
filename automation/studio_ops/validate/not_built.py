"""Gates that are specified but not implemented.

These exist as explicit NOT_BUILT reports rather than as absent commands, and they
exit non-zero. A validator that returns "OK" because it does nothing is worse than no
validator at all: it manufactures confidence that nothing checked anything.

Each entry records what it will check and what has to exist first, so the gap is
visible rather than folded into a green build.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..config import Config
from ..result import Finding, GateReport, GateState, Severity


@dataclass(frozen=True)
class Planned:
    gate: str
    will_check: str
    blocked_on: str


PLANNED: dict[str, Planned] = {
    "sources": Planned(
        gate="sources",
        will_check=(
            "Every {{CLM-*}} reference in a script resolves to a claim record; every "
            "claim's evidence meets the corroboration requirement for its confidence "
            "register; independence is asserted on every 'established' claim."
        ),
        blocked_on="No claim or source records exist yet. Requires an open line.",
    ),
    "canon": Planned(
        gate="canon",
        will_check=(
            "Prohibited language patterns; unsourced superlatives and bare figures; "
            "generated assets carrying the 'archival' provenance class; missing "
            "labels on reconstruction shots; a person signing two gates on one "
            "production."
        ),
        blocked_on=(
            "standards/schemas/prohibited_patterns.json has not been generated from "
            "standards/prohibited_language.md."
        ),
    ),
    "prompts": Planned(
        gate="prompts",
        will_check=(
            "Vendor cheat sheets older than 90 days flagged stale; prompt cards "
            "targeting a vendor whose terms_checked date is missing or expired."
        ),
        blocked_on="No prompt cards exist yet.",
    ),
    "delivery": Planned(
        gate="delivery",
        will_check=(
            "Delivered media against standards/delivery_specs.md: resolution, frame "
            "rate, loudness, true peak, caption validity, stem completeness."
        ),
        blocked_on="Requires ffprobe integration and a delivered package to check.",
    ),
    "packs": Planned(
        gate="packs",
        will_check=(
            "Every gate declared in a pack's gates.yaml has a checklist file that "
            "exists; every document listed in pack.yaml exists; no pack rule loosens "
            "a core rule."
        ),
        blocked_on="pack.schema.json has not been written.",
    ),
}


def run(cfg: Config, gate: str) -> GateReport:
    planned = PLANNED[gate]
    report = GateReport(gate=gate, state=GateState.NOT_BUILT)
    report.findings.append(
        Finding(
            gate,
            Severity.ERROR,
            f"NOT BUILT — this gate does not exist yet. Will check: {planned.will_check}",
            rule="not-built",
            hint=f"Blocked on: {planned.blocked_on}",
        )
    )
    return report
