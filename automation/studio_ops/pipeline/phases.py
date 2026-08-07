"""Phase control — an allowlist that money cannot argue with.

A budget ceiling stops a run that is *expensive*. It does nothing about a run that is
*cheap and unauthorised*, which is the likelier failure: the anchors come back, they
look good, there is budget left, and someone generates shot 02 because nothing said
not to.

This module is the thing that says not to.

    Phase A   the three canonical anchors            → then STOP for approval
    Phase B   diagnostic shots 01, 04, 06, 18        → then STOP for review
    Phase C   the remaining sixteen                  → not authorised

The allowlist is per phase and is explicit. A job not named in the active phase is
refused, and **remaining budget is not a reason to proceed** — the refusal does not
consult it.

## Why a plain file rather than a record

`run_plan.yaml` is configuration for one production, like a manifest path or an asset
store root. It has no ID, nothing cites it, and deleting it authorises nothing rather
than losing something. Making it a record would add a schema and a type under an
architecture freeze, to express a list of four strings.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

PLAN_FILENAME = "run_plan.yaml"


class PhaseError(RuntimeError):
    """A generation was attempted outside the authorised phase."""


@dataclass(frozen=True)
class Phase:
    key: str
    title: str
    allowed: tuple[str, ...]
    requires_approval_before: bool
    approved: bool
    note: str = ""


@dataclass(frozen=True)
class RunPlan:
    production: str
    active_phase: str
    phases: tuple[Phase, ...]
    execution_mode: str = "api"
    vendor: str = ""
    model: str = ""

    def phase(self, key: str) -> Phase | None:
        return next((p for p in self.phases if p.key == key), None)

    @property
    def active(self) -> Phase | None:
        return self.phase(self.active_phase)

    def check(self, job_id: str, *, execution_mode: str | None = None) -> None:
        """Refuse anything the active phase does not authorise.

        Raises rather than returning a verdict, because a caller that has to remember
        to inspect a boolean is a caller that will eventually forget.
        """
        phase = self.active
        if phase is None:
            raise PhaseError(
                f"{self.production}: active phase '{self.active_phase}' is not defined "
                f"in {PLAN_FILENAME}. Nothing is authorised."
            )

        if phase.requires_approval_before and not phase.approved:
            raise PhaseError(
                f"{self.production}: phase '{phase.key}' ({phase.title}) has not been "
                "approved. The previous phase must be reviewed and signed off first. "
                f"{phase.note}".strip()
            )

        if job_id not in phase.allowed:
            allowed = ", ".join(phase.allowed) or "(nothing)"
            raise PhaseError(
                f"{self.production}: '{job_id}' is not authorised in phase "
                f"'{phase.key}'. Authorised: {allowed}.\n"
                "Remaining budget is not a reason to proceed — this check does not "
                "consult it. Advance the phase deliberately, after review."
            )

        if execution_mode and self.execution_mode and execution_mode != self.execution_mode:
            raise PhaseError(
                f"{self.production}: this run is fixed to execution mode "
                f"'{self.execution_mode}' and '{execution_mode}' was requested. "
                "Mixing modes inside one continuity run makes a drift result "
                "uninterpretable — a difference between two shots could be the "
                "mechanism or the surface, with no way to tell which."
            )


def load(path: Path) -> RunPlan:
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(raw, dict):
        raise PhaseError(f"{path}: run plan is not a mapping")
    phases = tuple(
        Phase(
            key=str(p.get("key", "")),
            title=str(p.get("title", "")),
            allowed=tuple(str(a) for a in (p.get("allowed") or [])),
            requires_approval_before=bool(p.get("requires_approval_before", False)),
            approved=bool(p.get("approved", False)),
            note=str(p.get("note", "")),
        )
        for p in (raw.get("phases") or [])
    )
    return RunPlan(
        production=str(raw.get("production", "")),
        active_phase=str(raw.get("active_phase", "")),
        phases=phases,
        execution_mode=str(raw.get("execution_mode", "")),
        vendor=str(raw.get("vendor", "")),
        model=str(raw.get("model", "")),
    )


def find(production_dir: Path) -> RunPlan | None:
    """The plan for a production, if it has one. Absence authorises nothing by itself."""
    path = production_dir / PLAN_FILENAME
    return load(path) if path.is_file() else None


def as_dict(plan: RunPlan) -> dict[str, Any]:
    return {
        "production": plan.production,
        "active_phase": plan.active_phase,
        "execution_mode": plan.execution_mode,
        "vendor": plan.vendor,
        "model": plan.model,
        "phases": [
            {
                "key": p.key,
                "title": p.title,
                "allowed": list(p.allowed),
                "requires_approval_before": p.requires_approval_before,
                "approved": p.approved,
                "note": p.note,
            }
            for p in plan.phases
        ],
    }
