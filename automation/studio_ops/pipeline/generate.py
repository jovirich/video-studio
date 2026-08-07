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


def _as_dict(value: Any) -> dict[str, Any]:
    """A record's optional sub-block, or an empty one. Records omit what is unset."""
    return value if isinstance(value, dict) else {}


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


def _constraints_from_continuity(paths: list[Path]) -> tuple[list[str], list[str], list[str]]:
    """Split continuity records into constraints, negative-prompt terms, and hard stops.

    The split is the important part. `culturally-prohibited` entries are NOT negative
    prompt terms — a negative prompt is a statistical nudge a model may ignore, and
    treating it as a safeguard is a category error with consequences outside the
    studio. They go to the operator as hard stops with an instruction to raise rather
    than to prompt around.
    """
    constraints: list[str] = []
    forbidden: list[str] = []
    hard_stops: list[str] = []

    for path in paths:
        meta = _record_meta(path)
        name = meta.get("canonical_name") or meta.get("title") or path.stem

        appearance = meta.get("appearance")
        if isinstance(appearance, dict):
            for key in ("skin_tone_reference", "facial_structure", "hair", "height_relative"):
                value = appearance.get(key)
                if _usable(value):
                    constraints.append(f"{name} — {key.replace('_', ' ')}: {value}")

        for item in meta.get("distinctive_features") or []:
            if isinstance(item, dict) and _usable(item.get("feature")):
                always = " (must be visible in every shot)" if item.get("always_visible") else ""
                constraints.append(f"{name} — {item['feature']}{always}")

        for field_name in ("forbidden_objects", "forbidden_variations"):
            for item in meta.get(field_name) or []:
                if not isinstance(item, dict):
                    continue
                term = item.get("forbidden")
                if not _usable(term):
                    continue
                if item.get("severity") == "culturally-prohibited":
                    hard_stops.append(f"{term} — {item.get('why', 'requires a ruling')}")
                else:
                    forbidden.append(str(term))

    return constraints, list(dict.fromkeys(forbidden)), list(dict.fromkeys(hard_stops))


def prepare_job(
    cfg: Config,
    *,
    card_path: Path,
    shot_path: Path | None = None,
    manifest_path: Path,
    work_dir: Path,
    continuity_paths: list[Path],
    job_dir: Path | None = None,
    vendor: str | None = None,
    seed: int | str | None = None,
    schema_dir: Path | None = None,
    candidates: int = 1,
    is_anchor: bool = False,
) -> Path:
    """Assemble a complete handoff packet for manual fulfilment.

    Everything an operator needs, in one artefact, so they never reconstruct context
    from four files — that reconstruction is exactly where the forbidden list gets
    dropped.

    Costs nothing and touches no vendor: rendering is offline and no adapter runs.

    Preparation is deliberately allowed outside the authorised phase, because it is
    free and an operator may legitimately work ahead. The packet then carries its own
    refusal on its face, so nobody fulfils an unauthorised job without seeing it.
    """
    from ..adapters.interactive import InteractiveAdapter
    from ..adapters.job import job_from_request

    # A shot record is optional. An ANCHOR has no shot: it is a prompt card whose
    # product becomes a reference, and the run plan authorises it by card id. Requiring
    # a shot here would have meant fabricating shot records that are not in the shot
    # plan, purely to satisfy a signature.
    shot: dict[str, Any] = _record_meta(shot_path) if shot_path is not None else {}
    shot_id = str(shot.get("id") or "")
    scene_id = str(shot.get("sequence") or "")
    modality = str(shot.get("modality") or "image")

    card = render_mod.load_card(card_path, schemas=schema_dir)
    card_target_early = _as_dict(card.get("target"))
    provenance_class = str(
        shot.get("provenance_class") or card_target_early.get("provenance_class") or "interpretive"
    )
    style = style_block_from_continuity(continuity_paths)
    rendered = render_mod.render(card, vendor, style_block=style)

    job_id = shot_id or rendered.card_id
    production_id = _production_of(shot_id) if shot_id else _production_of_card(rendered.card_id)
    incoming = work_dir / "incoming"
    incoming.mkdir(parents=True, exist_ok=True)

    ext = "mp4" if modality == "video" else "png"
    if shot_id:
        filename = _asset_filename(production_id, scene_id, shot_id, provenance_class, ext)
    else:
        filename = f"{production_id}_ANCHOR_{rendered.card_id}_c01.{ext}"
    candidate_names = (
        tuple(filename.replace("_c01.", f"_c{i:02d}.") for i in range(1, max(candidates, 1) + 1))
        if candidates > 1
        else ()
    )
    request = request_from_render(rendered, output_path=incoming / filename, seed=seed)

    constraints, forbidden, hard_stops = _constraints_from_continuity(continuity_paths)
    forbidden = list(dict.fromkeys([*forbidden, *rendered.negative]))
    characters, styles, records = _references(continuity_paths)

    camera: dict[str, Any] = _as_dict(shot.get("camera"))
    framing = ", ".join(
        str(camera[k]) for k in ("size", "angle", "height") if _usable(camera.get(k))
    )
    shot_framing: dict[str, Any] = _as_dict(shot.get("framing"))
    card_prompt: dict[str, Any] = _as_dict(card.get("prompt"))
    card_tool: dict[str, Any] = _as_dict(card.get("tool"))
    card_target: dict[str, Any] = _as_dict(card.get("target"))

    checklist = [
        line.strip(" -") for line in str(card.get("notes") or "").splitlines() if line.strip()
    ]
    authorised, note = _phase_status(manifest_path.parent, job_id)

    job = job_from_request(
        request,
        job_id=job_id,
        production_id=production_id,
        line=str(shot.get("line") or cfg.default_line or ""),
        scene_id=scene_id,
        shot_id=shot_id,
        modality=modality,
        creative_purpose=str(card_target.get("intent") or shot.get("description") or ""),
        continuity_records=tuple(records),
        character_references=tuple(characters),
        style_references=tuple(styles),
        evidence_constraints=tuple(str(c) for c in (shot.get("claims") or [])),
        continuity_constraints=tuple(constraints),
        negative=tuple(forbidden),
        hard_stops=tuple(hard_stops),
        framing=framing,
        lens_look=str(camera.get("lens") or card_prompt.get("camera") or ""),
        lighting=str(style.get("light") or card_prompt.get("light") or ""),
        performance=str(shot.get("description") or ""),
        # An anchor is a reference portrait, not a frame in the cut. Forcing 16:9
        # would crop a head-and-shoulders subject to a letterbox and waste most of the
        # pixels on background the anchor does not need.
        aspect_ratio=str(shot_framing.get("aspect") or ("1:1" if is_anchor else "16:9")),
        resolution_target=(
            "3840x2160"
            if modality == "video"
            else "at least 1024x1024 — the face must survive being scored at 100%"
        ),
        duration_seconds=shot.get("duration_seconds"),
        preferred_vendor=str(card_tool.get("vendor") or ""),
        preferred_model=str(card_tool.get("model") or ""),
        video=_video_brief(shot, continuity_paths) if modality == "video" else None,
        output_filename=filename,
        incoming_dir=str(incoming),
        manifest_path=str(manifest_path),
        provenance_class=provenance_class,
        acceptance_checklist=tuple(checklist),
        candidates=max(candidates, 1),
        candidate_filenames=candidate_names,
        is_anchor=is_anchor,
        authorised=authorised,
        authorisation_note=note,
    )

    adapter = InteractiveAdapter(dry_run=True, job_dir=job_dir)
    return adapter.prepare(request, job)


def _production_of_card(card_id: str) -> str:
    """Production code out of a card id, for jobs that have no shot record."""
    parts = card_id.split("-")
    return parts[2] if len(parts) > 3 else "unknown"


def _asset_filename(production: str, scene: str, shot: str, klass: str, ext: str) -> str:
    """Per standards/naming_conventions.md. The operator must not invent a name.

    A file named by whoever generated it is a file the ingest cannot place, and the
    naming convention exists so a filename still says what a thing is later.
    """
    short = {
        "reconstruction": "recon",
        "interpretive": "interp",
        "archival": "arch",
        "contemporary": "contemp",
        "graphic": "graphic",
        "text_on_screen": "text",
    }.get(klass, "interp")
    seq = scene.split("-")[-1] if scene else "000"
    num = shot.split("-")[-1] if shot else "0000"
    return f"{production}_SEQ{seq}_SHT{num}_{short}_v01.{ext}"


def _references(paths: list[Path]) -> tuple[list[Any], list[Any], list[str]]:
    """Split continuity records into character refs, style refs, and record ids.

    A record with no approved anchor yet says so in the reference itself, because an
    operator handed a job with a missing attachment will otherwise proceed without it.
    """
    from ..adapters.job import JobReference

    characters: list[Any] = []
    styles: list[Any] = []
    records: list[str] = []

    for path in paths:
        meta = _record_meta(path)
        rid = str(meta.get("id") or path.stem)
        records.append(rid)
        kind = str(meta.get("type") or "")
        is_character = kind == "continuity_character"
        refs = meta.get("references") if is_character else meta.get("reference_imagery")
        anchor = ""
        if isinstance(refs, dict):
            anchor = str(refs.get("facial_reference") or refs.get("establishing_anchor") or "")
        name = meta.get("canonical_name", rid)
        (characters if is_character else styles).append(
            JobReference(
                kind="character anchor" if is_character else "style anchor",
                ref=anchor or rid,
                path=anchor or "NOT YET APPROVED",
                note=(
                    f"{name}. Attach the approved anchor image."
                    if anchor
                    else f"{name}. NO APPROVED ANCHOR YET — this job cannot be "
                    "fulfilled until one exists and its STA id is on the record."
                ),
            )
        )
    return characters, styles, records


def _video_brief(shot: dict[str, Any], continuity_paths: list[Path]) -> Any:
    """The motion half of an image-to-video job.

    Every field exists because a clip fails in a way a frame does not: it can start
    on-model and end as somebody else, and nothing in a still brief catches that.
    """
    from ..adapters.job import VideoBrief

    gen: dict[str, Any] = _as_dict(shot.get("generation"))
    camera: dict[str, Any] = _as_dict(shot.get("camera"))

    identity: list[str] = []
    for path in continuity_paths:
        meta = _record_meta(path)
        if meta.get("type") != "continuity_character":
            continue
        name = meta.get("canonical_name", meta.get("id", ""))
        identity.append(f"{name} is the same person in the last frame as in the first")
        for item in meta.get("distinctive_features") or []:
            if isinstance(item, dict) and _usable(item.get("feature")):
                identity.append(f"{name} — {item['feature']}: present and unchanged throughout")

    movement = str(camera.get("movement") or "static")
    motivation = (
        str(camera["movement_motivation"])
        if _usable(camera.get("movement_motivation"))
        else "no motivation recorded — unmotivated drift is the signature tell of generated video"
    )

    return VideoBrief(
        source_still=str(gen.get("selected_asset") or ""),
        first_frame_continuity=(
            "The first frame must BE the source still, not a close approximation. If "
            "the surface re-interprets it, the clip is not continuous with the frame "
            "it came from and the shot cannot be cut against its neighbours."
        ),
        end_state_intent=str(shot.get("description") or ""),
        camera_movement=f"{movement} — {motivation}",
        subject_movement=str(shot.get("description") or ""),
        prohibited_motion=(
            "morphing or melting of any face or hand",
            "identity drift — the subject becoming a different person mid-clip",
            "unmotivated camera drift where the shot is specified static",
            "background geometry sliding, breathing, or reflowing",
            "objects appearing or vanishing between frames",
            "cloth or hair moving against the established light and air",
        ),
        identity_preservation=tuple(identity),
    )


def _check_phase(production_dir: Path, job_id: str, adapter_name: str) -> None:
    """Enforce the run plan at GENERATION time. Preparation is free and is not blocked.

    The refusal never consults the budget: remaining money is not permission.
    """
    from . import phases

    plan = phases.find(production_dir)
    if plan is None:
        return
    mode = ""
    try:
        from ..adapters.base import get_adapter

        mode = str(get_adapter(adapter_name).capabilities().execution_mode)
    except Exception:
        mode = ""
    plan.check(job_id, execution_mode=mode or None)


def _phase_status(production_dir: Path, job_id: str) -> tuple[bool, str]:
    """Whether the run plan authorises this job right now.

    Preparation is free and is not blocked. The packet carries the answer on its face
    so nobody fulfils an unauthorised job without seeing that they are.
    """
    from . import phases

    plan = phases.find(production_dir)
    if plan is None:
        return True, ""
    try:
        plan.check(job_id)
    except phases.PhaseError as exc:
        return False, " ".join(str(exc).split())
    return True, ""


def _production_of(shot_id: str) -> str:
    parts = shot_id.split("-")
    return parts[2] if len(parts) > 3 else "unknown"


def fulfil_job(
    cfg: Config,
    *,
    job_path: Path,
    delivered: Path,
    vendor: str,
    model: str,
    model_version: str,
    seed: int | str | None = None,
    cost_usd: float = 0.0,
    operator: str | None = None,
    notes: str = "",
    schema_dir: Path | None = None,
) -> RoundTrip:
    """Close the second half of an interactive round trip.

    The job says where the asset was meant to go, what class it is, and which manifest
    owns it — so a fulfilment does not have to be told again, and cannot be told
    something different. Everything the ingest needs comes from the job, except what
    only the operator knows: which surface actually made the file, and what it cost.

    The hash is recomputed from the delivered bytes here, and again inside
    `ingest_generation`, which refuses if the two disagree. That second check is not
    redundant: it catches a file replaced between fulfilment and storage.
    """
    from ..adapters.interactive import InteractiveAdapter

    data, error = read_yaml(job_path)
    if error is not None:
        raise RoundTripError(f"{job_path}: {error}")
    job = data or {}

    manifest_path = Path(str(job.get("manifest_path") or ""))
    if not manifest_path.is_file():
        raise RoundTripError(
            f"{job_path}: manifest_path is missing or does not exist "
            f"({manifest_path}). A fulfilment with nowhere to be recorded is not a "
            "fulfilment — the asset would exist with no provenance."
        )

    shot_id = str(job.get("shot_id") or "")
    provenance_class = str(job.get("provenance_class") or "interpretive")

    request = GenerationRequest(
        prompt_card_id=str(job.get("prompt_card_id") or ""),
        modality=str(job.get("modality") or "image"),
        # The request records the surface that ACTUALLY ran, not the mode it arrived
        # by. "interactive" is a transport, and a manifest that said the vendor was
        # "interactive" would have lost the only fact worth keeping.
        vendor=vendor,
        model=model,
        rendered_prompt=str(job.get("prompt") or ""),
        parameters=dict(job.get("parameters") or {}),
        seed=seed,
        output_path=str(delivered),
    )

    adapter = InteractiveAdapter(dry_run=False, budget_usd=max(cost_usd, 0.0) or 1.0)
    result = adapter.fulfil(
        request,
        delivered,
        vendor=vendor,
        model=model,
        model_version=model_version,
        seed=seed,
        cost_usd=cost_usd,
        operator=operator,
        notes=notes,
    )

    entry = manifest_mod.ingest_generation(
        cfg,
        manifest_path,
        result,
        provenance_class=provenance_class,
        used_in_shots=[shot_id] if shot_id else [],
        schema_dir=schema_dir,
    )

    return RoundTrip(
        shot_id=shot_id,
        prompt_card_id=request.prompt_card_id,
        rendered=RenderedPrompt(
            card_id=request.prompt_card_id,
            modality=request.modality,
            vendor=vendor,
            model=model,
            prompt=request.rendered_prompt,
            parameters=request.parameters,
            negative=tuple(job.get("negative") or ()),
        ),
        result=result,
        entry=entry,
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

    # Phase control. Refuses anything the active phase does not authorise, and does
    # not consult the budget while doing so — remaining money is not permission.
    _check_phase(manifest_path.parent, shot_id, adapter_name)

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
