"""The round trip: shot record → asset with provenance.

This module is glue, deliberately thin. It owns no rules of its own; every refusal
below belongs to a module it calls. What it owns is the *order*, and the order is the
acceptance criterion for the platform:

    continuity record + shot record
        → prompt card
        → render                (promptlib — offline, no spend)
        → adapter               (guarded by dry-run and a cost ceiling)
        → asset file on disk
        → manifest entry whose sha256 matches those bytes

If that chain closes, the platform's traceability guarantee is a property of the
system rather than a claim in a document. If it does not, everything written about
provenance elsewhere in this repository is aspiration.

Two things this module refuses to do, both on purpose:

- **It never writes an asset it cannot record.** `manifest.ingest_generation` owns
  that ordering; this module does not reach past it to the store.
- **It never invents a style block.** A card inherits from somewhere real or the
  caller supplies one. Silently rendering with an empty style block would produce a
  plausible image with no lineage, which is the exact failure the card structure
  exists to prevent.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from ..adapters.base import Adapter, GenerationRequest, GenerationResult, get_adapter
from ..config import Config
from ..frontmatter import read, read_yaml
from ..promptlib import render as render_mod
from ..promptlib.registry import RenderedPrompt
from . import manifest as manifest_mod

# Shot fields that carry into the style block. A continuity record fixes how a place
# or person is rendered; those fields are exactly the ones a prompt inherits.
CONTINUITY_STYLE_KEYS: tuple[str, ...] = (
    "palette",
    "texture",
    "mood",
    "light",
    "camera",
)


class RoundTripError(RuntimeError):
    """The chain did not close. The message says which link broke."""


@dataclass(frozen=True)
class RoundTrip:
    """What one closed round trip produced, for a caller to assert against."""

    shot_id: str
    prompt_card_id: str
    rendered: RenderedPrompt
    result: GenerationResult
    entry: dict[str, Any]

    @property
    def asset_id(self) -> str:
        return str(self.entry["asset_id"])

    @property
    def sha256(self) -> str:
        return str(self.entry["sha256"])

    def hash_matches_disk(self, store_root: Path) -> bool:
        """The claim the whole platform rests on, checkable in one call."""
        from . import store

        path = store.resolve(store_root, str(self.entry["store_path"]))
        return path.is_file() and store.sha256_file(path) == self.sha256


def style_block_from_continuity(paths: list[Path]) -> dict[str, Any]:
    """Build a prompt style block from continuity records.

    Location records carry `lighting_language` and `camera_language`; character
    records carry appearance. Both may carry a palette or texture. Only fields a
    prompt can actually use are lifted — a continuity record holds a great deal that
    is for humans and for QC, and pushing all of it into a prompt would dilute the
    conditioning rather than strengthen it.
    """
    block: dict[str, Any] = {}
    negatives: list[str] = []

    for path in paths:
        meta = _record_meta(path)
        for key in CONTINUITY_STYLE_KEYS:
            value = meta.get(key)
            if isinstance(value, str) and value.strip() and value.strip() != "TBD":
                block.setdefault(key, value)

        lighting = meta.get("lighting_language")
        if isinstance(lighting, dict):
            parts = [
                str(lighting[k])
                for k in ("primary_source", "direction", "quality", "time_of_day")
                if _usable(lighting.get(k))
            ]
            if parts and "light" not in block:
                block["light"] = ", ".join(parts)

        camera = meta.get("camera_language")
        if isinstance(camera, dict) and _usable(camera.get("movement_rules")):
            block.setdefault("camera", str(camera["movement_rules"]))

        # forbidden_* is the negative list that actually compounds across a season.
        for field_name in ("forbidden_objects", "forbidden_variations"):
            for item in meta.get(field_name) or []:
                if isinstance(item, dict) and item.get("severity") != "culturally-prohibited":
                    term = item.get("forbidden")
                    if isinstance(term, str) and term.strip():
                        negatives.append(term.strip())

    if negatives:
        block["negative"] = list(dict.fromkeys(negatives))
    return block


def _usable(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and value.strip() != "TBD"


def _record_meta(path: Path) -> dict[str, Any]:
    if path.suffix in {".yaml", ".yml"}:
        data, error = read_yaml(path)
        if error is not None:
            raise RoundTripError(f"{path}: {error}")
        return data or {}
    doc = read(path)
    if doc.error:
        raise RoundTripError(f"{path}: {doc.error}")
    return doc.meta


def request_from_render(
    rendered: RenderedPrompt,
    *,
    output_path: Path,
    seed: int | str | None,
    inputs: list[str] | None = None,
    estimated_cost_usd: float = 0.0,
) -> GenerationRequest:
    """Map a rendered prompt onto a generation request.

    Field-for-field, with no interpretation. `inputs` is passed by the caller rather
    than lifted from the render, because a card's inputs carry `kind`, `weight`, and
    a rights note, and flattening them to a list of refs would drop the rights note
    silently. Dropping a rights note silently is not a trade worth making.
    """
    return GenerationRequest(
        prompt_card_id=rendered.card_id,
        modality=rendered.modality,
        vendor=rendered.vendor,
        model=rendered.model,
        rendered_prompt=rendered.prompt,
        parameters=dict(rendered.parameters),
        inputs=list(inputs or []),
        seed=seed,
        estimated_cost_usd=estimated_cost_usd,
        output_path=str(output_path),
    )


def generate_shot(
    cfg: Config,
    *,
    shot_path: Path,
    card_path: Path,
    manifest_path: Path,
    work_dir: Path,
    adapter_name: str = "local",
    continuity_paths: list[Path] | None = None,
    style_block: dict[str, Any] | None = None,
    vendor: str | None = None,
    seed: int | str | None = None,
    dry_run: bool = True,
    schema_dir: Path | None = None,
) -> RoundTrip:
    """Take one shot record through to a recorded asset.

    `dry_run` defaults to True, matching the adapter guard: a missing argument yields
    the refusing state, never the spending state.
    """
    shot = _record_meta(shot_path)
    shot_id = str(shot.get("id") or "")
    if not shot_id:
        raise RoundTripError(f"{shot_path}: shot record has no id")

    provenance_class = str(shot.get("provenance_class") or "")
    if not provenance_class:
        raise RoundTripError(
            f"{shot_id}: shot record has no provenance_class. What kind of image this "
            "is determines whether it must be labelled, and it is not inferable."
        )

    evidence_basis = [str(c) for c in (shot.get("claims") or [])]

    card = render_mod.load_card(card_path, schemas=schema_dir)

    resolved_style = style_block
    if resolved_style is None:
        if continuity_paths:
            resolved_style = style_block_from_continuity(continuity_paths)
        else:
            raise RoundTripError(
                f"{shot_id}: no style block. Supply continuity records or an explicit "
                "block — rendering with nothing inherited produces a plausible image "
                "with no lineage, which is what the card structure exists to prevent."
            )

    rendered = render_mod.render(card, vendor, style_block=resolved_style)

    adapter_cls = get_adapter(adapter_name)
    adapter: Adapter = adapter_cls.from_config(cfg, dry_run=dry_run)

    work_dir.mkdir(parents=True, exist_ok=True)
    output_path = work_dir / f"{shot_id}.png"

    request = request_from_render(rendered, output_path=output_path, seed=seed)
    result = adapter.generate(request)

    entry = manifest_mod.ingest_generation(
        cfg,
        manifest_path,
        result,
        provenance_class=provenance_class,
        used_in_shots=[shot_id],
        evidence_basis=evidence_basis or None,
        schema_dir=schema_dir,
    )

    return RoundTrip(
        shot_id=shot_id,
        prompt_card_id=rendered.card_id,
        rendered=rendered,
        result=replace(result),
        entry=entry,
    )
