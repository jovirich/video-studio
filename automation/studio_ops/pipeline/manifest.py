"""Asset manifest — the provenance ledger.

This module is the mechanism behind the platform's traceability guarantee. Every
other provenance claim in this repository reduces to one behaviour that lives here:

    an asset without a manifest entry cannot be conformed into an edit.

That refusal is the whole thing. Labels, disclosure statements, and published
provenance summaries are all downstream of it — they are renderings of the manifest.
If the refusal does not exist, the guarantee is documentation rather than a property
of the system.

Shape of the record: standards/schemas/asset_manifest.schema.json
Canon: core/01_provenance_and_ai_disclosure.md §4

What is here:

- `create` / `load` / `save` — a manifest round-trips through the schema. `save`
  validates first, so an invalid manifest is never written, not even partially.
- `add` — refuses a duplicate `asset_id`, refuses an entry missing the provenance
  block its `origin` requires, refuses a `reconstruction` with no `evidence_basis`,
  and refuses a generated asset carrying `provenance_class: archival` outright.
- `entry_from_generation` — the seam with the adapters. Maps a `GenerationResult`
  into a schema-valid entry, or raises. It cannot produce an entry without the
  provenance, because every field it needs is on the result type.
- `ingest_generation` — put the bytes in the store and record them, as one act.
  Bytes are written only after the entry that describes them has been validated,
  and are removed again if the manifest write fails. That ordering is what makes
  "no asset without a manifest entry" a property rather than a habit.
- `verify` — every referenced file exists in the asset store and its SHA-256
  matches. A hash mismatch is an incident, not a warning: see
  docs/runbook/incident_response.md.
- `freeze` — at delivery, mark immutable and emit the hash that is embedded in the
  delivered media metadata, tying a file to the exact record set that produced it.

Deliberately absent: any code path that writes an asset without a manifest entry.
There is no such path, including a convenience one for testing. `store.put` writes
bytes and hands back a hash; only `ingest_generation` joins bytes to a record, and
it validates the record first.

Laboratory productions are first-class here: `create(line=..., episode="EXP001")`
validates, because `asset_manifest.schema.json` gives `episode` the same `anyOf` as
`episode.schema.json` `properties.code`. EXP-001 needs a manifest before it has a
single frame, and needing one is the point.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import re
from datetime import date
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Any

import yaml

from ..adapters.base import GenerationResult
from ..config import Config
from ..paths import find_repo_root
from . import store

if TYPE_CHECKING:  # pragma: no cover - typing only
    from jsonschema import Draft202012Validator

SCHEMA_NAME = "asset_manifest.schema.json"
MANIFEST_TYPE = "asset_manifest"
DEFAULT_VERSION = "0.1.0"

# From _common.schema.json. Restated here because `add` and `entry_from_generation`
# refuse in code: the schema is only checked on demand, and a refusal that only
# happens on demand is a preference.
PROVENANCE_CLASSES: frozenset[str] = frozenset(
    {
        "archival",
        "contemporary",
        "artefact",
        "reconstruction",
        "interpretive",
        "graphic",
        "text_on_screen",
    }
)

# bible/04 §7: reconstruction and interpretive shots carry a persistent in-frame
# mark. `label.required` is derived from the class and stored, so the edit can be
# checked without recomputing it per shot.
LABELLED_CLASSES: frozenset[str] = frozenset({"reconstruction", "interpretive"})

GENERATION_ORIGIN = "generated"
ACQUISITION_ORIGINS: frozenset[str] = frozenset(
    {"licensed", "captured", "public_domain", "commissioned"}
)
ORIGINS: frozenset[str] = ACQUISITION_ORIGINS | {GENERATION_ORIGIN, "studio_library"}

RIGHTS_STATUSES: frozenset[str] = frozenset({"cleared", "pending", "not-required", "refused"})

# GenerationRequest.modality is the vendor-facing word; media_type is the schema's.
MODALITY_MEDIA_TYPES: dict[str, str] = {
    "image": "image",
    "video": "video",
    "audio": "audio",
    "voice": "audio",
    "music": "audio",
    "sfx": "audio",
    "document": "document",
    "project": "project",
}

ASSET_ID = re.compile(r"^AST-([A-Z]{2})-(S\d{2}E\d{2}|EXP\d{3})-(\d{4})$")
SCOPED_ID = re.compile(r"^[A-Z]{2,3}-([A-Z]{2})-(S\d{2}E\d{2}|EXP\d{3})-\d{3,4}$")


class ManifestError(Exception):
    """Base for every refusal from the manifest."""


class ManifestInvalidError(ManifestError):
    """The manifest does not conform to asset_manifest.schema.json."""


class ProvenanceError(ManifestError):
    """An entry whose provenance is missing, inconsistent, or prohibited."""


# ------------------------------------------------------------------ create/load


def create(
    *,
    line: str,
    episode: str,
    version: str = DEFAULT_VERSION,
    updated: str | None = None,
) -> dict[str, Any]:
    """A new, empty manifest for a production that has none yet.

    Empty is the correct starting state: a manifest with a worked example in it
    ships placeholder provenance, and placeholder provenance is worse than none
    because it validates.
    """
    return {
        "type": MANIFEST_TYPE,
        "line": line,
        "episode": episode,
        "version": version,
        "updated": updated or date.today().isoformat(),
        "frozen": False,
        "assets": [],
    }


def load(path: Path) -> dict[str, Any]:
    """Read a production manifest."""
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ManifestError(f"{path}: unreadable: {exc}") from exc
    except yaml.YAMLError as exc:
        raise ManifestInvalidError(f"{path}: invalid YAML: {exc}") from exc
    if raw is None:
        raise ManifestInvalidError(f"{path}: empty")
    if not isinstance(raw, dict):
        raise ManifestInvalidError(f"{path}: top level is not a mapping")
    return raw


def save(path: Path, manifest: dict[str, Any], *, schema_dir: Path | None = None) -> None:
    """Write a manifest, validating against the schema first.

    An invalid manifest is never written — not truncated, not half-written, not
    written and flagged. The file on disk always validates, so any reader may
    treat it as authoritative without revalidating.
    """
    errors = validate(manifest, schema_dir=_schema_dir(schema_dir, path.parent))
    if errors:
        raise ManifestInvalidError(
            f"{path}: manifest does not validate against {SCHEMA_NAME}; nothing was "
            "written.\n  - " + "\n  - ".join(errors)
        )

    text = yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True, default_flow_style=False)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.partial")
    try:
        tmp.write_text(text, encoding="utf-8")
        os.replace(tmp, path)
    except OSError:
        tmp.unlink(missing_ok=True)
        raise


# -------------------------------------------------------------------- validation


def validate(manifest: dict[str, Any], *, schema_dir: Path | None = None) -> list[str]:
    """Schema errors for this manifest, innermost path first. Empty means valid."""
    validator = _validator(_schema_dir(schema_dir, None))
    out: list[str] = []
    for error in sorted(validator.iter_errors(manifest), key=lambda e: list(e.path)):
        pointer = "/".join(str(p) for p in error.path) or "(root)"
        out.append(f"{pointer}: {error.message}")
    return out


def _schema_dir(explicit: Path | None, near: Path | None) -> Path:
    if explicit is not None:
        return explicit
    return find_repo_root(near) / "standards" / "schemas"


@lru_cache(maxsize=8)
def _validator(schema_dir: Path) -> Draft202012Validator:
    """Build a validator whose registry can resolve the sibling `$ref`s."""
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012

    if not schema_dir.is_dir():
        raise ManifestError(
            f"schema directory not found: {schema_dir}. The manifest is only "
            "meaningful against standards/schemas/."
        )

    registry: Registry[Any] = Registry()
    schema: dict[str, Any] | None = None
    for schema_file in sorted(schema_dir.glob("*.schema.json")):
        doc = json.loads(schema_file.read_text(encoding="utf-8"))
        registry = registry.with_resource(
            schema_file.name, Resource.from_contents(doc, default_specification=DRAFT202012)
        )
        if schema_file.name == SCHEMA_NAME:
            schema = doc

    if schema is None:
        raise ManifestError(f"{SCHEMA_NAME} not found in {schema_dir}")
    return Draft202012Validator(schema, registry=registry)


# --------------------------------------------------------------------------- add


def add(manifest: dict[str, Any], asset: dict[str, Any]) -> dict[str, Any]:
    """Add an asset entry, or refuse and say which rule it broke.

    Refusals here are deliberately duplicated from the schema. The schema is
    checked when someone asks; these are checked every time an entry is created,
    which is the moment the fact is still knowable.
    """
    if manifest.get("frozen"):
        raise ProvenanceError(
            "this manifest is frozen. A frozen manifest has been hashed into "
            "delivered media metadata; adding to it would make that hash a lie. "
            "Record the change as a new version of the production's manifest."
        )

    check_entry(asset)

    asset_id = str(asset.get("asset_id", ""))
    assets = manifest.setdefault("assets", [])
    if not isinstance(assets, list):
        raise ManifestInvalidError("`assets` is not a list")
    if any(str(existing.get("asset_id", "")) == asset_id for existing in assets):
        raise ProvenanceError(
            f"{asset_id} is already in this manifest. Asset IDs are permanent and "
            "never reused: a collided ID silently attaches one asset's provenance "
            "to another asset's frames."
        )

    assets.append(copy.deepcopy(asset))
    return manifest


def check_entry(asset: dict[str, Any]) -> None:
    """Raise unless this entry carries the provenance its own fields require."""
    missing = [
        field
        for field in ("asset_id", "filename", "media_type", "provenance_class", "origin")
        if not asset.get(field)
    ]
    if missing:
        raise ProvenanceError(f"entry is missing required field(s): {', '.join(missing)}")

    asset_id = str(asset["asset_id"])
    if not ASSET_ID.match(asset_id):
        raise ProvenanceError(
            f"{asset_id!r} is not a valid asset ID (AST-<LL>-<S00E00|EXP000>-<NNNN>)."
        )

    origin = str(asset["origin"])
    if origin not in ORIGINS:
        raise ProvenanceError(f"{asset_id}: unknown origin {origin!r}")

    provenance_class = str(asset["provenance_class"])
    if provenance_class not in PROVENANCE_CLASSES:
        raise ProvenanceError(f"{asset_id}: unknown provenance_class {provenance_class!r}")

    if origin == GENERATION_ORIGIN and provenance_class == "archival":
        raise ProvenanceError(
            f"{asset_id}: a generated asset can never carry provenance_class "
            "'archival'. There is no flag, no reviewer, and no deadline that permits "
            "it — the result is a fabricated historical document. "
            "core/01_provenance_and_ai_disclosure.md §2.1."
        )

    if origin == GENERATION_ORIGIN and not asset.get("generation"):
        raise ProvenanceError(
            f"{asset_id}: origin is 'generated' but there is no `generation` block. "
            "Tool, prompt card, seed, and who ran it are what make the image "
            "examinable instead of arguable."
        )
    if origin in ACQUISITION_ORIGINS and not asset.get("acquisition"):
        raise ProvenanceError(
            f"{asset_id}: origin is {origin!r} but there is no `acquisition` block. "
            "The question an acquired asset has to answer is 'may we use this, and "
            "who must be credited, in exactly which words'."
        )

    if provenance_class == "reconstruction" and not asset.get("evidence_basis"):
        raise ProvenanceError(
            f"{asset_id}: a reconstruction with an empty `evidence_basis` asserts a "
            "past that nothing in the record supports. List the claims and sources "
            "the depiction is built from."
        )

    label = asset.get("label")
    if not isinstance(label, dict) or "required" not in label:
        raise ProvenanceError(
            f"{asset_id}: no `label.required`. Disclosure state is recorded, never "
            "inferred at delivery."
        )

    rights = str(asset.get("rights_status", ""))
    if rights not in RIGHTS_STATUSES:
        raise ProvenanceError(
            f"{asset_id}: rights_status must be one of {sorted(RIGHTS_STATUSES)}, got {rights!r}"
        )


def next_asset_id(manifest: dict[str, Any]) -> str:
    """Allocate the next free asset ID for this production.

    Hand-typed asset IDs collide eventually, and a collided ID attaches one
    asset's provenance to a different asset's frames.
    """
    line = str(manifest.get("line", ""))
    episode = str(manifest.get("episode", ""))
    code = re.sub(r"[^A-Z]", "", line.upper())[:2]
    if len(code) != 2 or not re.match(r"^(S\d{2}E\d{2}|EXP\d{3})$", episode):
        raise ManifestError(
            f"cannot allocate an asset ID for line={line!r} episode={episode!r}: "
            "the ID namespace needs a two-letter line code and a production code."
        )

    prefix = f"AST-{code}-{episode}-"
    highest = 0
    for entry in manifest.get("assets", []):
        match = ASSET_ID.match(str(entry.get("asset_id", "")))
        if match and str(entry.get("asset_id", "")).startswith(prefix):
            highest = max(highest, int(match.group(3)))
    return f"{prefix}{highest + 1:04d}"


# ------------------------------------------------------------ the adapter seam


def entry_from_generation(
    result: GenerationResult,
    *,
    provenance_class: str,
    used_in_shots: list[str],
    evidence_basis: list[str] | None = None,
    rights_status: str = "not-required",
) -> dict[str, Any]:
    """Map a GenerationResult into an asset entry valid against the schema.

    Every field the schema demands of a generated asset is on `GenerationResult`,
    which is why an adapter physically cannot hand back an asset without its
    provenance. What is *not* on it — where the bytes ended up, and how large they
    are — is left absent rather than guessed; `ingest_generation` fills those in
    from the store once the bytes have actually landed.

    The `asset_id` here is provisional and derived from the content hash, because
    this function has no manifest to allocate from. Allocate the real one with
    `next_asset_id` before `add` — `ingest_generation` does.
    """
    if provenance_class not in PROVENANCE_CLASSES:
        raise ProvenanceError(f"unknown provenance_class {provenance_class!r}")
    if provenance_class == "archival":
        raise ProvenanceError(
            "a generated asset can never carry provenance_class 'archival'. The "
            "schema prohibits the combination outright and so does this function: "
            "the result would be a fabricated historical document. "
            "core/01_provenance_and_ai_disclosure.md §2.1."
        )
    if provenance_class == "reconstruction" and not evidence_basis:
        raise ProvenanceError(
            "a reconstruction requires an `evidence_basis`. An empty one means the "
            "image asserts a past that nothing in the record supports — the exact "
            "failure the reconstruction class exists to make visible."
        )
    if rights_status not in RIGHTS_STATUSES:
        raise ProvenanceError(
            f"rights_status must be one of {sorted(RIGHTS_STATUSES)}, got {rights_status!r}"
        )

    request = result.request
    entry: dict[str, Any] = {
        "asset_id": _provisional_asset_id(result, used_in_shots),
        "filename": Path(str(result.asset_path)).name,
        "sha256": _require_sha256(result.sha256),
        "media_type": _media_type(request.modality),
        "provenance_class": provenance_class,
        "used_in_shots": list(used_in_shots),
        "origin": GENERATION_ORIGIN,
        "generation": {
            "tool": {
                "vendor": request.vendor,
                "model": request.model,
                "version": result.model_version,
            },
            "prompt_card": request.prompt_card_id,
            "seed": result.seed,
            "parameters": dict(request.parameters),
            "inputs": list(request.inputs),
            "generated_at": result.generated_at,
            "generated_by": result.generated_by,
            "cost_usd": float(result.cost_usd),
        },
        "label": {
            "required": provenance_class in LABELLED_CLASSES,
            "applied": False,
        },
        "rights_status": rights_status,
    }
    if evidence_basis:
        entry["evidence_basis"] = list(evidence_basis)
    return entry


def _require_sha256(value: str) -> str:
    text = str(value).strip().lower()
    if not re.fullmatch(r"[a-f0-9]{64}", text):
        raise ProvenanceError(
            f"sha256 {value!r} is not 64 hex characters. The hash is what ties the "
            "record to the bytes; an approximate one ties it to nothing."
        )
    return text


def _media_type(modality: str) -> str:
    try:
        return MODALITY_MEDIA_TYPES[str(modality).strip().lower()]
    except KeyError:
        raise ProvenanceError(
            f"modality {modality!r} has no `media_type` in the manifest schema "
            f"(one of: {sorted(set(MODALITY_MEDIA_TYPES.values()))}). Model output "
            "that is not one of these is not an asset — it is working material."
        ) from None


def _provisional_asset_id(result: GenerationResult, used_in_shots: list[str]) -> str:
    """Derive a scoped, deterministic ID from the prompt card, else from a shot.

    Deterministic on content, so re-running the same generation proposes the same
    ID and `add` recognises it as a duplicate rather than silently doubling the
    entry. It is still provisional: see `next_asset_id`.
    """
    for candidate in (result.request.prompt_card_id, *used_in_shots):
        match = SCOPED_ID.match(str(candidate))
        if match:
            digits = int(_require_sha256(result.sha256)[:8], 16) % 10_000
            return f"AST-{match.group(1)}-{match.group(2)}-{digits:04d}"
    raise ProvenanceError(
        "cannot scope an asset ID: neither the prompt card "
        f"({result.request.prompt_card_id!r}) nor any shot in {used_in_shots!r} names "
        "a line and a production. Pass a production-scoped prompt card or shot."
    )


# ------------------------------------------------------------------- the ingest


def ingest_generation(
    cfg: Config,
    manifest_path: Path,
    result: GenerationResult,
    *,
    provenance_class: str,
    used_in_shots: list[str],
    evidence_basis: list[str] | None = None,
    rights_status: str = "not-required",
    relative_path: str | None = None,
    schema_dir: Path | None = None,
) -> dict[str, Any]:
    """Record a generated asset and store its bytes, as one act.

    Order matters and is the point:

    1. Build the entry and validate the whole manifest with it. Nothing has been
       written yet, so a bad entry costs nothing.
    2. Hash the source and check it against what the adapter claimed.
    3. Put the bytes in the store.
    4. Write the manifest — and if that fails, remove the bytes again.

    There is no ordering of these steps that leaves an asset in the store without
    a manifest entry describing it.
    """
    manifest = load(manifest_path)
    entry = entry_from_generation(
        result,
        provenance_class=provenance_class,
        used_in_shots=used_in_shots,
        evidence_basis=evidence_basis,
        rights_status=rights_status,
    )
    entry["asset_id"] = next_asset_id(manifest)

    source = Path(str(result.asset_path))
    if not source.is_file():
        raise ProvenanceError(f"{entry['asset_id']}: generated file not found at {source}")
    actual = store.sha256_file(source)
    if actual != entry["sha256"]:
        raise ProvenanceError(
            f"{entry['asset_id']}: the adapter reported {entry['sha256']} but "
            f"{source} hashes to {actual}. The record and the bytes disagree before "
            "either was stored; nothing was written."
        )

    rel = relative_path or _default_store_path(manifest, entry["filename"])
    entry["store_path"] = store.normalise_relative_path(rel)
    entry["bytes"] = source.stat().st_size

    # Dry run against the schema before any byte is written anywhere.
    trial = add(copy.deepcopy(manifest), entry)
    errors = validate(trial, schema_dir=_schema_dir(schema_dir, manifest_path.parent))
    if errors:
        raise ManifestInvalidError(
            f"{entry['asset_id']}: entry would make the manifest invalid; nothing was "
            "written.\n  - " + "\n  - ".join(errors)
        )

    stored = store.put(cfg, source, relative_path=entry["store_path"])
    add(manifest, entry)
    try:
        save(manifest_path, manifest, schema_dir=schema_dir)
    except Exception:
        if stored.created:
            stored.path.unlink(missing_ok=True)
        raise
    return entry


def _default_store_path(manifest: dict[str, Any], filename: str) -> str:
    """The conventional location for a generated asset. See the storage runbook."""
    line = manifest.get("line", "unknown-line")
    episode = manifest.get("episode", "unknown-production")
    return f"{line}/productions/{episode}/generated/{filename}"


# ------------------------------------------------------------ verify and freeze


def verify(manifest: dict[str, Any], store_root: Path) -> list[str]:
    """Check every referenced file exists and its hash matches.

    Returns findings rather than raising, because the useful output is the whole
    list: one mismatch is a file, several on one volume is the volume telling you
    something. A mismatch is an incident — see docs/runbook/incident_response.md.
    """
    findings: list[str] = []
    for entry in manifest.get("assets", []):
        if not isinstance(entry, dict):
            findings.append("assets contains a non-mapping entry")
            continue
        finding = store.check(store_root, entry)
        if finding:
            findings.append(finding)
    return findings


def freeze(manifest: dict[str, Any]) -> str:
    """Mark immutable at delivery; return the hash embedded in media metadata.

    The hash is taken over a canonical serialisation, so it depends on what the
    manifest says and not on how it happened to be written out. A file in the
    world can then be tied to the exact record set that produced it.

    Refuses to freeze a manifest that is not deliverable: an entry with no hash
    cannot be verified later, and an asset still in `rights_status: pending`
    blocks delivery outright.
    """
    blockers: list[str] = []
    for entry in manifest.get("assets", []):
        asset_id = str(entry.get("asset_id", "(no asset_id)"))
        if not entry.get("sha256") or not entry.get("store_path"):
            blockers.append(f"{asset_id}: no sha256/store_path — nothing to freeze against")
        if entry.get("rights_status") == "pending":
            blockers.append(f"{asset_id}: rights_status is 'pending' — delivery is blocked")
    if blockers:
        raise ProvenanceError(
            "manifest is not deliverable; not frozen.\n  - " + "\n  - ".join(blockers)
        )

    manifest["frozen"] = True
    return manifest_hash(manifest)


def manifest_hash(manifest: dict[str, Any]) -> str:
    """SHA-256 over a canonical serialisation of the manifest."""
    canonical = json.dumps(manifest, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
