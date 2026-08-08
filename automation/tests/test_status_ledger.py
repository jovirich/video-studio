"""The authoritative ledger must agree with the code it describes.

`docs/status.md` declares itself the single place where a per-capability maturity
verdict lives. It was contradicting itself inside one table: `new-record`,
`promptlib render` and the provenance manifest each appeared as IMPLEMENTED in one row
and NOT BUILT (or DESIGNED, "no code writes to it") a few rows below. `validate
--prompts` was listed NOT BUILT in the same commit that implemented it.

`validate --reality` did not catch any of it. That gate checks PROSE that names a
command against what is implemented; it does not read the ledger's own rows, so the
table describing the gates was the one document exempt from the discipline it exists
to enforce.

This test closes that. It reads every `validate --X` row out of the ledger and compares
the stated verdict against the gate registry — the code, not another document.

The failure mode being prevented is specific and was named by the repository's owner:
two agents working the same repo, one reading a stale NOT BUILT and rebuilding what the
other already shipped.
"""

from __future__ import annotations

import re
from pathlib import Path

from studio_ops.config import Config
from studio_ops.validate import IMPLEMENTED, UNBUILT

LEDGER = Path("docs") / "status.md"

# A table row naming a validate gate, e.g. "| `validate --naming` | **IMPLEMENTED** | …"
ROW = re.compile(
    r"^\|\s*`validate\s+--(?P<gate>[a-z-]+)`\s*\|\s*\*\*(?P<verdict>[A-Z ]+?)\*\*",
    re.MULTILINE,
)


def _ledger_text() -> str:
    return (Config.load().root / LEDGER).read_text(encoding="utf-8")


def test_ledger_gate_verdicts_match_the_registry() -> None:
    rows = list(ROW.finditer(_ledger_text()))
    assert rows, "no validate-gate rows found in the ledger — has the table format changed?"

    for match in rows:
        gate = match.group("gate")
        verdict = match.group("verdict").strip()
        assert gate in IMPLEMENTED or gate in UNBUILT, (
            f"ledger describes `validate --{gate}`, which is not a registered gate"
        )
        built = gate in IMPLEMENTED
        if built:
            assert verdict == "IMPLEMENTED", (
                f"`validate --{gate}` is implemented in code, ledger says {verdict!r}"
            )
        else:
            assert verdict == "NOT BUILT", (
                f"`validate --{gate}` is NOT implemented, ledger says {verdict!r}"
            )


def test_every_registered_gate_appears_in_the_ledger() -> None:
    """A gate absent from the ledger is worse than one described wrongly.

    A wrong verdict is at least visible and arguable. A missing row means the
    authoritative document silently under-reports what the toolkit does, and the
    reader has no way to notice.
    """
    described = {m.group("gate") for m in ROW.finditer(_ledger_text())}
    missing = (set(IMPLEMENTED) | set(UNBUILT)) - described
    assert not missing, f"gates missing from {LEDGER}: {sorted(missing)}"


def test_ledger_does_not_contradict_itself_on_one_gate() -> None:
    """One gate, one verdict. The original defect was two rows disagreeing."""
    seen: dict[str, str] = {}
    for match in ROW.finditer(_ledger_text()):
        gate, verdict = match.group("gate"), match.group("verdict").strip()
        if gate in seen:
            assert seen[gate] == verdict, (
                f"ledger states `validate --{gate}` is both {seen[gate]!r} and {verdict!r}"
            )
        seen[gate] = verdict
