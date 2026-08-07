"""The generation job — a self-contained work order for interactive execution.

## What this is, and what it deliberately is not

A **derived view**, like a bibliography or a shot list. It is assembled from records
that already exist — the prompt card, the continuity records, the shot record, the
manifest destination — and it is disposable: delete it and regenerate it, and you get
the same thing.

It is **not a record**. It has no allocated ID, it is not validated against a schema,
it is not part of the reference graph, and nothing ever cites it. That distinction is
what keeps this inside the architecture freeze: adding a record type would be a new
abstraction, and a work order derived from existing records is not one.

The test: if you deleted every job file in the repository, you would lose nothing. If
you deleted a prompt card, you would lose a decision.

## Why it exists

In interactive mode a human, or an agent working an interactive surface, does the
generating. That operator needs one artefact containing everything required to
produce one asset — the prompt, the references, the constraints, where the file goes,
and what will be checked when it comes back.

Without it the operator reconstructs context by opening four files and hoping they
remembered the forbidden list. That reconstruction is where the constraints get
dropped, and the constraints are the entire point of the record layer.

So a job carries the *obligations* as prominently as the prompt: forbidden objects,
the acceptance checklist, the provenance fields that will be demanded on return. An
operator who reads only the job cannot accidentally bypass a rule that lives in a
file they never opened.

## What it must never contain

Credentials, or anything that would let the job itself spend money. A job is a
specification handed to a person. It is not an authorisation.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .base import GenerationRequest

JOB_FORMAT = "studio_ops/generation_job"
JOB_FORMAT_VERSION = "1"


@dataclass(frozen=True)
class JobReference:
    """One input the operator must supply to the generation surface."""

    kind: str
    ref: str
    path: str | None = None
    sha256: str | None = None
    note: str = ""


@dataclass(frozen=True)
class GenerationJob:
    """Everything needed to produce one asset, in one file.

    Field order is deliberate: what to make, what not to make, where to put it, and
    what will be checked. An operator reading top to bottom encounters the
    constraints before the mechanics.
    """

    # --- identity -----------------------------------------------------------
    job_id: str
    prompt_card_id: str
    production: str
    line: str
    shot_id: str | None = None

    # --- what to make -------------------------------------------------------
    modality: str = "image"
    prompt: str = ""
    negative: tuple[str, ...] = ()
    parameters: dict[str, Any] = field(default_factory=dict)
    references: tuple[JobReference, ...] = ()

    # --- what the result must satisfy ---------------------------------------
    model_requirements: dict[str, Any] = field(default_factory=dict)
    continuity_constraints: tuple[str, ...] = ()
    forbidden: tuple[str, ...] = ()
    hard_stops: tuple[str, ...] = ()
    acceptance_checklist: tuple[str, ...] = ()

    # --- where it goes ------------------------------------------------------
    output_path: str = ""
    output_format: str = "png"
    manifest_path: str = ""
    provenance_class: str = "interpretive"

    # --- what must come back with the file ----------------------------------
    provenance_required: tuple[str, ...] = ()

    format: str = JOB_FORMAT
    format_version: str = JOB_FORMAT_VERSION
    notes: str = ""

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

    def to_operator_brief(self) -> str:
        """The job as instructions, for a surface that takes prose rather than YAML.

        Same content, different shape. Nothing is summarised away — an operator
        working from the brief must be under exactly the obligations of one working
        from the file, or the two paths produce differently-constrained assets.
        """
        lines: list[str] = [
            f"# Generation job {self.job_id}",
            "",
            f"Produce ONE {self.modality} for shot {self.shot_id or '(none)'} "
            f"in production {self.production}.",
            "",
            "## Prompt",
            "",
            self.prompt,
        ]
        if self.negative:
            lines += ["", "## Must not appear", ""]
            lines += [f"- {term}" for term in self.negative]
        if self.references:
            lines += ["", "## Reference inputs", ""]
            lines += [
                f"- **{r.kind}** `{r.ref}`"
                + (f" — {r.path}" if r.path else "")
                + (f" ({r.note})" if r.note else "")
                for r in self.references
            ]
        if self.model_requirements:
            lines += ["", "## Model requirements", ""]
            lines += [f"- {k}: {v}" for k, v in self.model_requirements.items()]
        if self.continuity_constraints:
            lines += ["", "## Continuity constraints", ""]
            lines += [f"- {c}" for c in self.continuity_constraints]
        if self.forbidden:
            lines += ["", "## Forbidden — any occurrence fails the shot", ""]
            lines += [f"- {f}" for f in self.forbidden]
        if self.hard_stops:
            lines += [
                "",
                "## HARD STOPS — not negative-prompt terms",
                "",
                "If any of these appears, delete the render. Do not adjust it and keep "
                "the frame, and do not attempt to prompt around it. Raise it instead.",
                "",
            ]
            lines += [f"- {h}" for h in self.hard_stops]
        if self.acceptance_checklist:
            lines += ["", "## Accepted only if all of these hold", ""]
            lines += [f"- [ ] {c}" for c in self.acceptance_checklist]
        lines += [
            "",
            "## Deliver",
            "",
            f"- Save as `{self.output_format}` to: `{self.output_path}`",
            "- Then hand it back to the pipeline for ingest. Do not move or rename it,",
            "  and do not re-encode it — the file is hashed on arrival and the hash is",
            "  the provenance record.",
        ]
        if self.provenance_required:
            lines += ["", "Report with the file:", ""]
            lines += [f"- {p}" for p in self.provenance_required]
        return "\n".join(lines) + "\n"


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


def job_from_request(
    request: GenerationRequest,
    *,
    job_id: str,
    production: str,
    line: str,
    shot_id: str | None = None,
    manifest_path: str = "",
    provenance_class: str = "interpretive",
    negative: tuple[str, ...] = (),
    references: tuple[JobReference, ...] = (),
    continuity_constraints: tuple[str, ...] = (),
    forbidden: tuple[str, ...] = (),
    hard_stops: tuple[str, ...] = (),
    acceptance_checklist: tuple[str, ...] = (),
    notes: str = "",
) -> GenerationJob:
    """Build a job from a rendered request plus the context the renderer does not hold.

    The renderer knows the prompt. It does not know the shot, the manifest, or the
    forbidden list — those live in records it never reads. The caller supplies them,
    which is why `pipeline.generate` assembles the job rather than `promptlib`.
    """
    return GenerationJob(
        job_id=job_id,
        prompt_card_id=request.prompt_card_id,
        production=production,
        line=line,
        shot_id=shot_id,
        modality=request.modality,
        prompt=request.rendered_prompt,
        negative=negative,
        parameters=dict(request.parameters),
        references=references,
        model_requirements=_model_requirements(request),
        continuity_constraints=continuity_constraints,
        forbidden=forbidden,
        hard_stops=hard_stops,
        acceptance_checklist=acceptance_checklist,
        output_path=request.output_path or "",
        manifest_path=manifest_path,
        provenance_class=provenance_class,
        provenance_required=PROVENANCE_REQUIRED,
        notes=notes,
    )


def _model_requirements(request: GenerationRequest) -> dict[str, Any]:
    """What the operator's surface has to be, for the result to be comparable.

    Vendor and model are recorded even when unset, because *which* surface produced a
    frame is provenance, not preference. Two shots made on different surfaces are not
    a continuity test, and a job that did not ask cannot detect it afterwards.
    """
    requirements: dict[str, Any] = {
        "vendor": request.vendor or "TBD — must be fixed before the diagnostic run",
        "model": request.model or "TBD",
        "seed": request.seed if request.seed is not None else "record whatever is used",
    }
    if request.parameters:
        requirements["parameters"] = "as listed above; report any that were changed"
    return requirements


# Demanded back with the file. Every one maps to a field the manifest requires, so an
# operator who reports all of these has supplied a complete provenance record and the
# ingest cannot fail for want of information.
PROVENANCE_REQUIRED: tuple[str, ...] = (
    "vendor — the surface that actually produced it",
    "model and exact version identifier",
    "seed, if the surface exposes one; say so plainly if it does not",
    "any parameter that differed from those specified above",
    "whether the file was edited, cropped, or re-encoded after generation",
)
