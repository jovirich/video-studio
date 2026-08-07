"""Conform — the refusal that makes traceability real. NOT BUILT.

Runs between edit and delivery. For every clip in the timeline it asks one question:

    does this resolve to an entry in the production's manifest?

If any clip does not, conform fails and names it. There is no flag to proceed
anyway, because a flag to proceed anyway is how a guarantee becomes a preference.

Checks, when built:

- Every timeline clip resolves to a manifest asset.
- Generated assets carry prompt card, seed, tool, and model version.
- `reconstruction` assets carry an `evidence_basis`.
- No asset has `rights_status: pending`.
- Required labels are applied, per the active pack's disclosure mode.
- Frame-rate conform method is recorded per clip (`native`, `retime`,
  `frame-blend`, `optical-flow`) — optical-flow artefacts survive grading and are
  checked at picture lock, so the method has to be knowable.

Canon: core/01_provenance_and_ai_disclosure.md, standards/delivery_specs.md
Status: docs/status.md
"""

from __future__ import annotations

from pathlib import Path

NOT_BUILT = "pipeline.conform is NOT BUILT. See docs/status.md."


class ConformNotBuiltError(NotImplementedError):
    """Raised by every function here."""


def conform(production_dir: Path, timeline: Path) -> list[str]:
    """Verify the timeline against the manifest. Returns findings. NOT BUILT."""
    raise ConformNotBuiltError(NOT_BUILT)
