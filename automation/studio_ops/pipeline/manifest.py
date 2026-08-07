"""Asset manifest — the provenance ledger. NOT BUILT.

This module is the mechanism behind the platform's traceability guarantee. Every
other provenance claim in this repository reduces to one behaviour that lives here:

    an asset without a manifest entry cannot be conformed into an edit.

That refusal is the whole thing. Labels, disclosure statements, and published
provenance summaries are all downstream of it — they are renderings of the manifest.
If the refusal does not exist, the guarantee is documentation rather than a property
of the system.

Shape of the record: standards/schemas/asset_manifest.schema.json
Canon: core/01_provenance_and_ai_disclosure.md §4
Status: docs/status.md

Implementation order, when it is built:

1. `load` / `save` round-trip against the schema.
2. `add` — refuses an entry missing provenance for its `origin`, and refuses a
   generated asset carrying `provenance_class: archival` outright.
3. `verify` — every referenced file exists in the asset store and its SHA-256
   matches. A hash mismatch is an incident, not a warning: see
   docs/runbook/incident_response.md.
4. `freeze` — at delivery, mark immutable and emit the hash that is embedded in the
   delivered media metadata, tying a file to the exact record set that produced it.

Deliberately absent: any code path that writes an asset without a manifest entry.
There must be no such path, including a convenience one for testing.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

NOT_BUILT = (
    "pipeline.manifest is NOT BUILT. It is the mechanism behind the platform's "
    "traceability guarantee — see docs/status.md."
)


class ManifestNotBuiltError(NotImplementedError):
    """Raised by every function here, carrying the reason."""


def load(path: Path) -> dict[str, Any]:
    """Read an episode manifest. NOT BUILT."""
    raise ManifestNotBuiltError(NOT_BUILT)


def save(path: Path, manifest: dict[str, Any]) -> None:
    """Write an episode manifest, validating against the schema first. NOT BUILT."""
    raise ManifestNotBuiltError(NOT_BUILT)


def add(manifest: dict[str, Any], asset: dict[str, Any]) -> dict[str, Any]:
    """Add an asset entry.

    Must refuse: an entry missing the provenance block its `origin` requires; a
    `reconstruction` asset with no `evidence_basis`; and any generated asset
    carrying `provenance_class: archival`, which the schema also prohibits.

    NOT BUILT.
    """
    raise ManifestNotBuiltError(NOT_BUILT)


def verify(manifest: dict[str, Any], store_root: Path) -> list[str]:
    """Check every referenced file exists and its hash matches. NOT BUILT."""
    raise ManifestNotBuiltError(NOT_BUILT)


def freeze(manifest: dict[str, Any]) -> str:
    """Mark immutable at delivery; return the hash embedded in media metadata. NOT BUILT."""
    raise ManifestNotBuiltError(NOT_BUILT)
