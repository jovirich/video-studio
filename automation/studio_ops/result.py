"""Findings are data.

Validators return `Finding` objects; rendering is somebody else's job. The same run
can print a table, emit JSON for CI, or annotate a pull request.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from enum import StrEnum
from pathlib import Path


class Severity(StrEnum):
    ERROR = "error"  # blocks a merge
    WARNING = "warning"  # requires acknowledgement, does not block
    INFO = "info"

    def __str__(self) -> str:
        return self.value


class GateState(StrEnum):
    """Maturity of a validator itself, distinct from what it finds.

    NOT_BUILT is a first-class result. A gate that reports "OK" because it does
    nothing is worse than no gate, because it manufactures false confidence.
    """

    IMPLEMENTED = "IMPLEMENTED"
    NOT_BUILT = "NOT_BUILT"

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class Finding:
    gate: str
    severity: Severity
    message: str
    path: str | None = None
    line: int | None = None
    rule: str | None = None
    hint: str | None = None

    def location(self) -> str:
        if self.path and self.line:
            return f"{self.path}:{self.line}"
        return self.path or "—"

    def to_dict(self) -> dict[str, object]:
        d = asdict(self)
        d["severity"] = str(self.severity)
        return d


@dataclass
class GateReport:
    gate: str
    state: GateState = GateState.IMPLEMENTED
    findings: list[Finding] = field(default_factory=list)
    files_checked: int = 0

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.severity is Severity.ERROR]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity is Severity.WARNING]

    @property
    def passed(self) -> bool:
        return self.state is GateState.IMPLEMENTED and not self.errors

    def to_dict(self) -> dict[str, object]:
        return {
            "gate": self.gate,
            "state": str(self.state),
            "files_checked": self.files_checked,
            "errors": len(self.errors),
            "warnings": len(self.warnings),
            "findings": [f.to_dict() for f in self.findings],
        }


@dataclass
class RunReport:
    reports: list[GateReport] = field(default_factory=list)

    def add(self, report: GateReport) -> None:
        self.reports.append(report)

    @property
    def error_count(self) -> int:
        return sum(len(r.errors) for r in self.reports)

    @property
    def warning_count(self) -> int:
        return sum(len(r.warnings) for r in self.reports)

    @property
    def not_built(self) -> list[GateReport]:
        return [r for r in self.reports if r.state is GateState.NOT_BUILT]

    def exit_code(self) -> int:
        """0 clean · 1 findings · 2 a requested gate is NOT BUILT.

        2 is distinguished from 0 deliberately: a green build that ran three of six
        gates must not look like a green build that ran six.

        Order matters. A real finding outranks a missing gate — with both present the
        caller must fix the finding first. This also means a NOT_BUILT gate must
        never emit an ERROR finding, or it masks itself as a failure and makes code 2
        unreachable. See `validate/not_built.py`.
        """
        if self.error_count:
            return 1
        if self.not_built:
            return 2
        return 0

    def to_json(self) -> str:
        return json.dumps(
            {
                "errors": self.error_count,
                "warnings": self.warning_count,
                "not_built": [r.gate for r in self.not_built],
                "gates": [r.to_dict() for r in self.reports],
            },
            indent=2,
        )


def rel(path: Path, root: Path) -> str:
    """Repo-relative POSIX path, for stable output across platforms."""
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)
