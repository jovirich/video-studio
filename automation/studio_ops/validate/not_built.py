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
    # Files whose ABSENCE is the blocker, named separately from the prose.
    #
    # Prose cannot be checked, and prose is what went stale: the `packs` gate claimed
    # to be waiting on a schema that had been written some commits earlier, and anyone
    # reading it would have written a second one. A test asserts these paths do not
    # exist, so the day one is created the claim fails loudly instead of misleading
    # quietly.
    #
    # Empty where the blocker is not a file — a missing integration, or records that
    # nobody has authored yet.
    missing_paths: tuple[str, ...] = ()


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
        missing_paths=("standards/schemas/prohibited_patterns.json",),
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
        # WAS: "pack.schema.json has not been written." That stopped being true
        # some commits ago — the schema is written and five packs validate against
        # it. Nothing is blocking this gate except the gate; saying otherwise
        # invites someone to write a schema that already exists.
        blocked_on=(
            "Nothing external. pack.schema.json exists and packs validate against it; "
            "what is missing is this gate's own implementation."
        ),
    ),
}


def run(cfg: Config, gate: str) -> GateReport:
    planned = PLANNED[gate]
    report = GateReport(gate=gate, state=GateState.NOT_BUILT)
    # WARNING, not ERROR. Nothing is wrong with the repository — the *tool* is
    # missing. The distinction is load-bearing: `RunReport.exit_code` tests errors
    # before it tests not-built, so emitting ERROR here made exit code 2
    # unreachable and every unbuilt gate indistinguishable from a real failure.
    report.findings.append(
        Finding(
            gate,
            Severity.WARNING,
            f"NOT BUILT — this gate does not exist yet. Will check: {planned.will_check}",
            rule="not-built",
            hint=f"Blocked on: {planned.blocked_on}",
        )
    )
    return report
