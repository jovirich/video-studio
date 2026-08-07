"""Interactive execution — the operator generates, the pipeline accounts for it.

## The shape

`local` and `api` are one-phase: call, get bytes. Interactive is two-phase, because
the generating happens somewhere this process cannot reach — a person at a chat
surface, an agent in an editor, a design tool.

    prepare   →   (out of band)   →   fulfil
    job file      operator works      file ingested, hashed, recorded

`generate()` therefore cannot return a `GenerationResult`. It runs every guard, writes
the job, and raises `AwaitingFulfilmentError`. It does **not** fabricate a result for
work that has not happened — doing so would defeat every provenance guarantee in this
package, and would be trivially easy to do accidentally.

## Why this is a mode and not a vendor

The pipeline must not depend on any particular product or subscription. Interactive
mode describes a *shape of work* — a human-in-the-loop surface producing a file — and
is deliberately agnostic about which surface that is. A job prepared here can be
fulfilled from a chat client, an image tool, a colleague's workstation, or a vendor
console, and the ingest path is identical in every case.

**No claim is made that any particular assistant, subscription, or editor exposes an
image-generation API.** This mode exists precisely because some do not: it routes
around the absence of an API rather than assuming one.

## What the operator is trusted with, and what they are not

Trusted: producing pixels that satisfy a written specification.

Not trusted, because the pipeline checks rather than believes:

- the hash — recomputed from the delivered bytes, never taken on report
- the destination — the file is ingested into the store by the pipeline
- the manifest entry — written from the fulfilment record, not from a claim
- acceptance — the checklist is a human gate and stays one

An operator can hand back the wrong file. They cannot hand back a file with a hash
that does not match its bytes, because nobody is asked for the hash.
"""

from __future__ import annotations

import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .base import (
    Adapter,
    AwaitingFulfilmentError,
    Capabilities,
    ExecutionMode,
    GenerationRequest,
    GenerationResult,
    UnsupportedRequestError,
    default_operator,
    register,
    sha256_file,
)
from .job import GenerationJob

MODEL = "interactive-operator"
VERSION = "1.0.0"


@register("interactive")
class InteractiveAdapter(Adapter):
    """Prepares a job; ingests what comes back. Generates nothing itself."""

    vendor = "interactive"
    modality = "image"

    def __init__(self, *, job_dir: Path | None = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.job_dir = job_dir

    @classmethod
    def capabilities(cls) -> Capabilities:
        return Capabilities(
            modalities=frozenset({"image", "video", "audio_voice", "audio_music", "text"}),
            # Whether the OPERATOR's surface costs anything is outside this process's
            # knowledge and outside its control. Declaring False would be a claim
            # about someone else's account; the conservative reading is kept, and the
            # ceiling is enforced against the cost the operator reports at fulfilment.
            spends_money=True,
            deterministic=False,
            accepts_seed=True,
            execution_mode=ExecutionMode.INTERACTIVE,
            notes=(
                "Two-phase. Vendor-agnostic by design: any surface capable of "
                "producing a file can fulfil a job. Asserts nothing about whether a "
                "given assistant or subscription exposes a generation API."
            ),
        )

    def estimate_cost(self, request: GenerationRequest) -> float:
        """Zero to this process.

        Whatever the operator's surface costs is charged to their account, not to a
        ceiling this process can see or enforce. The honest quote is zero, and the
        real figure is captured at fulfilment where it is actually known.
        """
        return 0.0

    # --- phase one ---------------------------------------------------------

    def _generate(self, request: GenerationRequest) -> GenerationResult:
        """Write the job and stop. Never returns a result.

        Reached only after `generate()`'s pre-flight has run, so the dry-run default
        and the budget guard apply to interactive work exactly as they do to a vendor
        call. A job is not written for a request that would have been refused.
        """
        job_path = self._write_job(request)
        raise AwaitingFulfilmentError(
            f"interactive: job prepared at {job_path}. Generation happens out of band; "
            "no asset exists yet. Hand the job to the operator, then ingest the "
            "returned file with `studio_ops ingest`.",
            job_path=job_path,
        )

    def prepare(self, request: GenerationRequest, job: GenerationJob) -> Path:
        """Write a fully-assembled job. The caller supplies the context this adapter lacks.

        `pipeline.generate` builds the job because the constraints live in continuity
        and shot records that an adapter has no business reading.
        """
        target = self._job_path(job.job_id)
        job.write(target)
        (target.with_suffix(".md")).write_text(job.to_operator_brief(), encoding="utf-8")
        return target

    def _write_job(self, request: GenerationRequest) -> Path:
        """Fallback for a bare request with no assembled job.

        Deliberately minimal — a job written from a request alone carries the prompt
        but none of the continuity constraints, so it is marked as such rather than
        quietly shipping an under-specified brief to an operator.
        """
        from .job import job_from_request

        job = job_from_request(
            request,
            job_id=request.prompt_card_id or "job",
            production="unknown",
            line="unknown",
            notes=(
                "ASSEMBLED FROM A BARE REQUEST. Continuity constraints, forbidden "
                "objects, and the acceptance checklist are ABSENT because no records "
                "were supplied. Do not fulfil this without them — use "
                "`studio_ops generate --mode interactive`, which assembles the full job."
            ),
        )
        return self.prepare(request, job)

    def _job_path(self, job_id: str) -> Path:
        base = self.job_dir or Path(os.environ.get("STUDIO_JOB_DIR", "")) or Path("jobs")
        return Path(base) / f"{job_id}.job.yaml"

    # --- phase two ---------------------------------------------------------

    def fulfil(
        self,
        request: GenerationRequest,
        delivered: Path,
        *,
        vendor: str,
        model: str,
        model_version: str,
        seed: int | str | None = None,
        cost_usd: float = 0.0,
        operator: str | None = None,
        notes: str = "",
    ) -> GenerationResult:
        """Turn a delivered file into a provenance record.

        The hash is computed from the bytes on disk. It is never accepted on report,
        which is the one thing that makes an out-of-band mode as accountable as an
        in-process one: an operator can hand back the wrong file, but cannot hand back
        a file whose hash disagrees with its contents, because nobody asks them for it.

        `vendor` and `model` are what ACTUALLY produced the file, reported by the
        operator. They are recorded as given — this process cannot verify them — and
        that limit is stated plainly rather than papered over. It is the same trust
        placed in any human-reported provenance, and it is why the acceptance
        checklist stays a human gate.
        """
        if not delivered.is_file():
            raise UnsupportedRequestError(
                f"interactive: nothing delivered at {delivered}. Fulfilment needs the "
                "file itself; a report that generation happened is not an asset."
            )
        if not vendor or not model:
            raise UnsupportedRequestError(
                "interactive: fulfilment must name the vendor and model that actually "
                "produced the file. 'interactive' is how it arrived, not what made it, "
                "and a manifest entry that cannot say what made an asset is not a "
                "provenance record."
            )

        digest = sha256_file(delivered)
        return GenerationResult(
            request=request,
            asset_path=str(delivered),
            sha256=digest,
            seed=seed if seed is not None else "not-exposed-by-surface",
            model_version=model_version or VERSION,
            generated_at=datetime.now(UTC).isoformat(),
            generated_by=operator or default_operator(),
            cost_usd=cost_usd,
            raw_response={
                "execution_mode": str(ExecutionMode.INTERACTIVE),
                "reported_vendor": vendor,
                "reported_model": model,
                "reported_model_version": model_version,
                "operator_notes": notes,
                # Stated on the record itself, so a later reader of the manifest sees
                # the limit without having to know how the asset arrived.
                "verification": (
                    "sha256 computed from the delivered bytes by the pipeline. "
                    "vendor, model, version, and seed are as reported by the operator "
                    "and are not independently verifiable by this process."
                ),
            },
        )
