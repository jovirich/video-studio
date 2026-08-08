"""Validation gates.

Each gate is a module exposing `run(cfg) -> GateReport`. Gates are independent so a
single run reports every failure at once rather than stopping at the first.
"""

from __future__ import annotations

from collections.abc import Callable

from ..config import Config
from ..result import GateReport, RunReport
from . import links, naming, not_built, prompts, reality, root_hygiene, schemas, templates

# Implemented gates.
IMPLEMENTED: dict[str, Callable[[Config], GateReport]] = {
    "schemas": schemas.run,
    "naming": naming.run,
    "links": links.run,
    "root-hygiene": root_hygiene.run,
    "reality": reality.run,
    "prompts": prompts.run,
    "templates": templates.run,
}

# Specified but not implemented. Listed so `--all` reports the gap rather than
# silently running a subset and looking green.
UNBUILT: tuple[str, ...] = ("sources", "canon", "packs", "delivery")

ALL_GATES: tuple[str, ...] = tuple(IMPLEMENTED) + UNBUILT


def run_gates(cfg: Config, gates: list[str]) -> RunReport:
    report = RunReport()
    for gate in gates:
        if gate in IMPLEMENTED:
            report.add(IMPLEMENTED[gate](cfg))
        elif gate in UNBUILT:
            report.add(not_built.run(cfg, gate))
        else:
            raise KeyError(f"unknown gate: {gate}")
    return report


__all__ = ["ALL_GATES", "IMPLEMENTED", "UNBUILT", "run_gates"]
