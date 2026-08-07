"""The generation job — a portable handoff packet for manual fulfilment.

## What this is, and what it deliberately is not

A **derived view**, like a bibliography or a shot list. Assembled from records that
already exist — the prompt card, the continuity records, the shot record, the manifest
destination — and disposable: delete it, rebuild it, get the same thing.

It is **not a record**. No allocated ID, no schema, not in the reference graph, nothing
cites it. That is what keeps it inside the architecture freeze: a record type would be
a new abstraction; a work order derived from existing records is not.

The test: delete every job file in the repository and you lose nothing. Delete a prompt
card and you lose a decision.

## Why it carries so much

A job is handed to a person working a subscription UI — ChatGPT Images, Runway, Kling,
Veo — with no API between them and the model. That operator needs **one artefact** they
can work from start to finish: what to make, what must not appear, which references to
attach, what to call the file, where to put it, and what will be checked when it comes
back.

Without it they reconstruct context from four files and hope they remembered the
forbidden list. That reconstruction is where constraints get dropped, and the
constraints are the entire point of the record layer.

So the job carries **obligations as prominently as the prompt**. An operator who reads
only the job cannot accidentally bypass a rule living in a file they never opened.

## What it must never contain

Credentials, or anything that would let the job itself spend. A job is a specification
handed to a person. It is not an authorisation — and where the run plan has not
authorised the shot, the job says so on its face.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .base import GenerationRequest

JOB_FORMAT = "studio_ops/generation_job"
JOB_FORMAT_VERSION = "2"


@dataclass(frozen=True)
class JobReference:
    """One input the operator attaches to the generation surface."""

    kind: str
    ref: str
    path: str | None = None
    sha256: str | None = None
    note: str = ""


@dataclass(frozen=True)
class VideoBrief:
    """The extra half an image-to-video job needs.

    Motion is where continuity is lost most cheaply: a clip can start on-model and end
    as somebody else, and nothing in a still-image brief catches it. Every field here
    exists because a generated clip fails in a way a generated frame does not.
    """

    source_still: str = ""
    source_still_sha256: str = ""
    first_frame_continuity: str = ""
    end_state_intent: str = ""
    camera_movement: str = ""
    subject_movement: str = ""
    prohibited_motion: tuple[str, ...] = ()
    identity_preservation: tuple[str, ...] = ()


@dataclass(frozen=True)
class GenerationJob:
    """Everything needed to produce one asset, in one file.

    Field order is deliberate: what it is for, what to make, what not to make, how to
    shoot it, where it goes, and what will be checked. An operator reading top to
    bottom meets the purpose before the mechanics and the constraints before the
    prompt.
    """

    # --- identity -----------------------------------------------------------
    job_id: str
    production_id: str
    line: str
    scene_id: str = ""
    shot_id: str = ""
    prompt_card_id: str = ""

    # --- what it is for -----------------------------------------------------
    modality: str = "image"
    creative_purpose: str = ""

    # --- what it must answer to ---------------------------------------------
    continuity_records: tuple[str, ...] = ()
    character_references: tuple[JobReference, ...] = ()
    style_references: tuple[JobReference, ...] = ()
    evidence_constraints: tuple[str, ...] = ()
    continuity_constraints: tuple[str, ...] = ()

    # --- what to make -------------------------------------------------------
    prompt: str = ""
    negative: tuple[str, ...] = ()
    hard_stops: tuple[str, ...] = ()

    # --- how to shoot it ----------------------------------------------------
    framing: str = ""
    lens_look: str = ""
    lighting: str = ""
    performance: str = ""
    environment_motion: str = ""

    # --- output shape -------------------------------------------------------
    aspect_ratio: str = "16:9"
    resolution_target: str = ""
    duration_seconds: float | None = None
    seed: int | str | None = None
    model_settings: dict[str, Any] = field(default_factory=dict)
    preferred_vendor: str = ""
    preferred_model: str = ""

    # --- image-to-video only ------------------------------------------------
    video: VideoBrief | None = None

    # --- where it goes ------------------------------------------------------
    output_filename: str = ""
    incoming_dir: str = ""
    manifest_path: str = ""
    provenance_class: str = "interpretive"

    # --- what must come back ------------------------------------------------
    acceptance_checklist: tuple[str, ...] = ()
    provenance_required: tuple[str, ...] = ()

    # --- candidates ---------------------------------------------------------
    # An anchor is selected FROM candidates, not produced on the first try. Every
    # candidate is ingested and kept, including the rejected ones: a rejection is a
    # record of what this surface does wrong under these instructions, and that is
    # the most reusable thing the run produces.
    candidates: int = 1
    candidate_filenames: tuple[str, ...] = ()

    # --- what this job IS ---------------------------------------------------
    # True where the job CREATES a canonical reference rather than consuming one.
    # Without this the brief tells an operator to attach the very anchor the job
    # exists to produce, which is the kind of instruction that gets followed.
    is_anchor: bool = False

    # --- authorisation ------------------------------------------------------
    authorised: bool = True
    authorisation_note: str = ""

    format: str = JOB_FORMAT
    format_version: str = JOB_FORMAT_VERSION
    notes: str = ""

    # --- serialisation ------------------------------------------------------

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_yaml(self) -> str:
        return yaml.safe_dump(self.to_dict(), sort_keys=False, allow_unicode=True)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def write(self, path: Path) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(_HEADER + self.to_yaml(), encoding="utf-8")
        return path

    # --- the operator-facing form -------------------------------------------

    def to_operator_brief(self) -> str:
        """The job as something a person can work from, top to bottom.

        Structured so the prompt is one unbroken block that can be copied in a single
        selection. A brief that makes an operator assemble the prompt from three
        fenced fragments is a brief that will be assembled wrongly.

        Nothing is summarised away. An operator working from this must be under
        exactly the obligations of one working from the YAML, or the two paths produce
        differently-constrained assets.
        """
        out: list[str] = []
        add = out.append

        add(f"# {self.shot_id or self.job_id} — {self.modality}")
        add("")
        if not self.authorised:
            add("> ## ⛔ NOT AUTHORISED — DO NOT FULFIL THIS JOB")
            add(">")
            add(f"> {self.authorisation_note}")
            add(">")
            add("> The packet is prepared so it is ready when the phase opens. Running")
            add("> it now would spend against work that has not been approved.")
            add("")
        if self.creative_purpose:
            add(f"**What this shot is for:** {self.creative_purpose}")
            add("")
        add(
            f"Production `{self.production_id}` · scene `{self.scene_id or '—'}` · "
            f"shot `{self.shot_id or '—'}` · card `{self.prompt_card_id or '—'}`"
        )
        add("")

        # 1 — references first. They must be attached before the prompt is pasted.
        if self.is_anchor:
            add(f"## {_n(out)}. Attach nothing")
            add("")
            add("**This job CREATES a canonical reference.** There is no anchor to")
            add("attach yet — that is what you are making. Work from the prompt alone.")
            add("")
            add("Everything generated later is scored against whichever candidate is")
            add("approved here, so an ambiguity in this frame becomes an unscoreable")
            add("frame in every shot that follows.")
            add("")
        else:
            add(f"## {_n(out)}. Attach these references")
            add("")
        refs = [] if self.is_anchor else [*self.character_references, *self.style_references]
        if self.is_anchor:
            pass
        elif refs:
            for r in refs:
                line = f"- **{r.kind}** — `{r.path or r.ref}`"
                if r.sha256:
                    line += f"  \n  sha256 `{r.sha256[:16]}…`"
                if r.note:
                    line += f"  \n  {r.note}"
                add(line)
        else:
            add("- *(none — this job has no reference inputs)*")
        add("")
        if self.video and self.video.source_still:
            add(f"- **source still** — `{self.video.source_still}`")
            add("  This is the first frame. The clip must begin on it, not near it.")
            add("")

        # 2 — the prompt, as one copyable block.
        add(f"## {_n(out)}. Copy this prompt")
        add("")
        add("```text")
        add(self.prompt.strip())
        add("```")
        add("")

        if self.negative:
            add("### Negative prompt")
            add("")
            add("```text")
            add(", ".join(self.negative))
            add("```")
            add("")

        # 3 — the craft settings.
        add(f"## {_n(out)}. Settings")
        add("")
        add("| | |")
        add("|---|---|")
        for label, value in (
            ("Framing / angle", self.framing),
            ("Lens / look", self.lens_look),
            ("Lighting", self.lighting),
            ("Performance", self.performance),
            ("Environment motion", self.environment_motion),
            ("Aspect ratio", self.aspect_ratio),
            ("Resolution", self.resolution_target),
            ("Duration", f"{self.duration_seconds}s" if self.duration_seconds else ""),
            ("Seed", self.seed),
            ("Preferred vendor", self.preferred_vendor),
            ("Preferred model", self.preferred_model),
        ):
            if value not in (None, "", ()):
                add(f"| {label} | {_cell(value)} |")
        for key, value in self.model_settings.items():
            add(f"| {key} | {_cell(value)} |")
        add("")

        # 4 — motion, where it applies.
        if self.video:
            v = self.video
            add(f"## {_n(out)}. Motion brief")
            add("")
            for label, value in (
                ("First frame must match", v.first_frame_continuity),
                ("End state", v.end_state_intent),
                ("Camera movement", v.camera_movement),
                ("Subject movement", v.subject_movement),
            ):
                if value:
                    add(f"- **{label}:** {value}")
            if v.prohibited_motion:
                add("")
                add("**Prohibited motion — reject the clip if any occurs:**")
                add("")
                for item in v.prohibited_motion:
                    add(f"- {item}")
            if v.identity_preservation:
                add("")
                add("**Identity must survive the whole clip:**")
                add("")
                for item in v.identity_preservation:
                    add(f"- {item}")
            add("")

        # 5 — constraints.
        if self.continuity_constraints:
            add(f"## {_n(out)}. Continuity — these must hold")
            add("")
            for c in self.continuity_constraints:
                add(f"- {c}")
            add("")
        if self.evidence_constraints:
            add("### Evidence basis")
            add("")
            add("Everything depicted must trace to one of these. If the surface adds a")
            add("detail not grounded here, the render is wrong even if it looks right.")
            add("")
            for e in self.evidence_constraints:
                add(f"- {e}")
            add("")
        if self.hard_stops:
            add("## ⛔ Hard stops — these are not negative-prompt terms")
            add("")
            add("A negative prompt is a statistical nudge the model may ignore. These")
            add("are not that. **If any appears, delete the render and raise it.** Do")
            add("not adjust the frame and keep it, and do not try to prompt around it.")
            add("")
            for h in self.hard_stops:
                add(f"- {h}")
            add("")

        # 6 — delivery.
        add(f"## {_n(out)}. Save and hand back")
        add("")
        if self.candidates > 1:
            add(f"Generate **{self.candidates} candidates** from the same prompt.")
            add("")
            add("Hand back **every one**, including any you dislike. All of them are")
            add("ingested and kept; exactly one is later approved as canonical. A")
            add("rejected candidate is a record of what this surface does wrong under")
            add("these instructions, and that is the most reusable thing this run")
            add("produces — do not quietly discard the bad ones.")
            add("")
            add("Save each as, in order:")
            add("")
            for name in self.candidate_filenames or ():
                add(f"- `{name}`")
            add("")
            add(f"Put them all in **`{self.incoming_dir}`** and tell me they are there.")
        else:
            add(f"1. Save as **`{self.output_filename}`** — exactly this name.")
            add(f"2. Put it in **`{self.incoming_dir}`**")
            add("3. Tell me it is there, and I will ingest it.")
        add("")
        add("Do not rename, crop, or re-encode it. The file is hashed on arrival and")
        add("that hash becomes the provenance record — any edit after generation makes")
        add("the record describe a file that no longer exists.")
        add("")
        if self.provenance_required:
            add("**Tell me these when you hand it back:**")
            add("")
            for p in self.provenance_required:
                add(f"- {p}")
            add("")

        if self.acceptance_checklist:
            add(f"## {_n(out)}. It is accepted only if all of these hold")
            add("")
            for c in self.acceptance_checklist:
                add(f"- [ ] {c}")
            add("")

        add("---")
        add("")
        add(
            f"*Ingest with:* `studio_ops fulfil-job --job {self.job_id}.job.yaml "
            f"--file <path> --vendor <what made it> --model <model>`"
        )
        return "\n".join(out) + "\n"


def _n(lines: list[str]) -> int:
    """Next section number. Hard-coded numbers skipped 4 whenever a job had no motion
    brief, and a brief that miscounts its own sections is a brief someone stops
    trusting."""
    return sum(1 for ln in lines if ln.startswith("## ") and ln[3:4].isdigit()) + 1


def _cell(value: Any) -> str:
    """Flatten a value for a markdown table cell.

    Record fields are written for humans and run to several lines; a newline inside a
    cell silently breaks the table, which is the kind of defect that survives review
    because the file still renders — just wrongly.
    """
    return " ".join(str(value).split())


_HEADER = f"""# GENERATION JOB — a derived work order, not a record.
#
# Regenerable and disposable: delete it and rebuild it from the prompt card and the
# continuity records. It has no ID in the reference graph and nothing cites it.
#
# Contains no credentials and authorises no spend. It is a specification handed to an
# operator, not permission to buy anything.
#
# format: {JOB_FORMAT} v{JOB_FORMAT_VERSION}

"""


# Demanded back with the file. Each maps to a field the manifest requires, so an
# operator who reports all of these has supplied a complete provenance record and the
# ingest cannot fail for want of information.
PROVENANCE_REQUIRED: tuple[str, ...] = (
    "which surface actually produced it — the product name, not 'interactive'",
    "the model, and its exact version identifier if the surface shows one",
    "the seed, if the surface exposes one; say plainly if it does not",
    "any setting that differed from those specified above",
    "roughly what it cost, if the surface tells you",
    "whether the file was edited, cropped, or re-encoded after generation",
)


def job_from_request(
    request: GenerationRequest,
    *,
    job_id: str,
    production_id: str,
    line: str,
    **fields: Any,
) -> GenerationJob:
    """Build a job from a rendered request plus the context the renderer does not hold.

    The renderer knows the prompt. It does not know the shot, the scene, the manifest,
    or the forbidden list — those live in records it never reads. The caller supplies
    them, which is why `pipeline.generate` assembles the job rather than `promptlib`.
    """
    defaults: dict[str, Any] = {
        "prompt_card_id": request.prompt_card_id,
        "modality": request.modality,
        "prompt": request.rendered_prompt,
        "seed": request.seed,
        "model_settings": dict(request.parameters),
        "provenance_required": PROVENANCE_REQUIRED,
    }
    defaults.update(fields)
    return GenerationJob(job_id=job_id, production_id=production_id, line=line, **defaults)
