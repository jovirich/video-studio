"""OpenAI image generation — the first vendor adapter. Refuses until a human acts.

## What is verified here, and what is not

Everything in this file that concerns *this repository* — the guards, the provenance
contract, the phase control, the retry discipline — is implemented and tested.

Everything that concerns *OpenAI* is not, and cannot be from inside this process:

- **The terms have not been read.** No claim is made here about ownership of outputs,
  commercial use, indemnity, training on inputs, or content restrictions. Those live
  in `rights/permissions/model_terms_register.md` and must be entered by a person who
  has opened the current terms page.
- **The price is unknown.** This adapter will not guess what an image costs. A guessed
  price would produce a ceiling that does not bound anything.
- **The model snapshot is unconfirmed.** `gpt-image-2-2026-04-21` is recorded because
  it was directed, not because this process checked that it resolves. A snapshot ID
  that does not exist fails loudly; worse, a snapshot ID that silently resolves to a
  floating alias would defeat the entire point of pinning it for a continuity run.
- **The request and response shape is asserted, not verified.** `_call_api` is written
  against the documented Images API shape as understood at authoring time and is
  marked accordingly. It must be checked against current API documentation before the
  first real call.

Four preconditions therefore gate every paid call, and each is a human act:

1. `terms_checked` recorded in the vendor register  → `OPENAI_TERMS_CHECKED`
2. a per-image price supplied                       → `OPENAI_IMAGE_PRICE_USD`
3. a ceiling set on the production                  → `budget_usd`
4. dry-run explicitly disabled                      → `GENERATION_DRY_RUN=false`

Miss any one and the adapter refuses with the reason. That is not friction for its own
sake: the first three are exactly the things a studio regrets not having decided when
the invoice arrives.

## Why the wire call is one small method

`_call_api` is the only part of this file that touches a network, and it is
deliberately short and isolated. When the API shape turns out to differ from what is
written here — and it will, eventually — the fix is confined to one method and no
guard, provenance rule, or phase check moves.
"""

from __future__ import annotations

import base64
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .base import (
    Adapter,
    AdapterNotBuiltError,
    Capabilities,
    ExecutionMode,
    GenerationRequest,
    GenerationResult,
    UnsupportedRequestError,
    default_operator,
    register,
    sha256_file,
)

VENDOR = "openai"

# Directed, not verified. See the module docstring: this process did not confirm that
# the snapshot resolves, and a snapshot that silently falls back to a floating alias
# would defeat the reason for pinning it.
PINNED_MODEL = "gpt-image-2-2026-04-21"
FLOATING_ALIAS = "gpt-image-2"

API_BASE = "https://api.openai.com/v1"
IMAGES_ENDPOINT = f"{API_BASE}/images/generations"

# Wire shape as understood at authoring time. UNVERIFIED — check against current API
# documentation before the first real call.
WIRE_FORMAT_VERIFIED = False


class TermsNotVerifiedError(AdapterNotBuiltError):
    """Raised when a paid call is attempted before anyone read the vendor's terms."""


class PriceUnknownError(AdapterNotBuiltError):
    """Raised when no per-image price has been supplied.

    Deliberately not a default. A guessed price yields a ceiling that bounds nothing,
    which is worse than no ceiling because it looks like a control.
    """


@register("openai")
class OpenAIImageAdapter(Adapter):
    """Pinned-snapshot image generation. Every guard from the base class still applies."""

    vendor = VENDOR
    modality = "image"

    def __init__(
        self,
        *,
        model: str = PINNED_MODEL,
        api_key: str | None = None,
        price_per_image_usd: float | None = None,
        terms_checked: str | None = None,
        allow_floating_alias: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.model = model
        self._api_key = api_key or os.environ.get("OPENAI_API_KEY") or ""
        self.price_per_image_usd = _price_from(price_per_image_usd)
        self.terms_checked = terms_checked or os.environ.get("OPENAI_TERMS_CHECKED") or ""
        self.allow_floating_alias = allow_floating_alias

    @classmethod
    def capabilities(cls) -> Capabilities:
        return Capabilities(
            modalities=frozenset({"image"}),
            spends_money=True,
            deterministic=False,
            accepts_seed=False,
            execution_mode=ExecutionMode.API,
            notes=(
                f"Pinned snapshot {PINNED_MODEL}. Terms, price, and wire format all "
                "require human verification before the first call — see the module "
                "docstring. Not seed-deterministic: identical inputs are not "
                "guaranteed to return identical bytes, which is why continuity is "
                "held by reference images rather than by seeds."
            ),
        )

    # --- pricing -----------------------------------------------------------

    def estimate_cost(self, request: GenerationRequest) -> float:
        """One image at the supplied price. Refuses to guess.

        The base class checks this against the ceiling before anything is called, so a
        missing price stops a run before it starts rather than after.
        """
        if self.price_per_image_usd is None:
            raise PriceUnknownError(
                "openai: no per-image price supplied, so no meaningful ceiling can be "
                "enforced. Set OPENAI_IMAGE_PRICE_USD from the vendor's current "
                "pricing page. This adapter will not guess: a guessed price produces "
                "a ceiling that bounds nothing while looking like a control."
            )
        return float(self.price_per_image_usd) * int(request.parameters.get("n", 1) or 1)

    # --- the guarded path --------------------------------------------------

    def _generate(self, request: GenerationRequest) -> GenerationResult:
        self._require_preconditions(request)
        output = Path(str(request.output_path))
        payload = self._call_api(request)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(payload["image_bytes"])

        return GenerationResult(
            request=request,
            asset_path=str(output),
            sha256=sha256_file(output),
            # This surface does not expose a reproducible seed. Recording a fabricated
            # one would be worse than recording its absence, because a later reader
            # would believe the render could be reproduced from it.
            seed=request.seed if request.seed is not None else "not-exposed-by-vendor",
            model_version=self.model,
            generated_at=datetime.now(UTC).isoformat(),
            generated_by=default_operator(),
            cost_usd=self.estimate_cost(request),
            raw_response={
                "execution_mode": str(ExecutionMode.API),
                "endpoint": IMAGES_ENDPOINT,
                "model": self.model,
                "pinned_snapshot": self.model != FLOATING_ALIAS,
                "terms_checked": self.terms_checked,
                "wire_format_verified": WIRE_FORMAT_VERIFIED,
                "response_id": payload.get("response_id", ""),
            },
        )

    def _require_preconditions(self, request: GenerationRequest) -> None:
        """The four human acts. Each is a thing a studio regrets not deciding."""
        if not self._api_key:
            raise AdapterNotBuiltError("openai: OPENAI_API_KEY is not set. Nothing has been spent.")
        if not self.terms_checked:
            raise TermsNotVerifiedError(
                "openai: terms have not been verified. Record the terms URL, effective "
                "date, ownership and output provisions, generation restrictions, and "
                "the date checked in rights/permissions/model_terms_register.md, then "
                "set OPENAI_TERMS_CHECKED to that date. A studio that generates before "
                "reading the terms has no answer when asked whether it may use what it "
                "generated."
            )
        if self.model == FLOATING_ALIAS and not self.allow_floating_alias:
            raise UnsupportedRequestError(
                f"openai: refusing the floating alias '{FLOATING_ALIAS}'. A continuity "
                "run needs a fixed snapshot, or the model can change underneath it "
                "mid-experiment and every drift measurement becomes uninterpretable. "
                f"Use a dated snapshot such as {PINNED_MODEL}."
            )
        if not WIRE_FORMAT_VERIFIED:
            raise AdapterNotBuiltError(
                "openai: the request and response shape in this adapter has not been "
                "checked against current API documentation. Verify it, set "
                "WIRE_FORMAT_VERIFIED = True, and run once against a throwaway prompt "
                "before any diagnostic shot. Nothing has been spent."
            )

    # --- the only method that touches a network ----------------------------

    def _call_api(self, request: GenerationRequest) -> dict[str, Any]:
        """The wire call. UNVERIFIED shape — see the module docstring.

        Isolated deliberately: when the API differs from what is written here, the fix
        is confined to this method and no guard, provenance rule, or phase check moves.

        Left unimplemented rather than written speculatively. Writing a plausible
        request body and a plausible response parse would produce code that looks
        ready and fails on first contact, having already been counted as done.
        """
        raise AdapterNotBuiltError(
            "openai: the wire call is not implemented. It is the last piece, and it is "
            "deliberately not written from memory — the request body, the response "
            "envelope, and the image encoding must be read from current API "
            "documentation. Everything around it is built and tested: guards, "
            "provenance, phase control, and retry discipline."
        )

    @staticmethod
    def _decode_image(data: str) -> bytes:
        """base64 payload to bytes. Kept separate so it is testable without a network."""
        return base64.b64decode(data)


def _price_from(explicit: float | None) -> float | None:
    if explicit is not None:
        return explicit
    raw = os.environ.get("OPENAI_IMAGE_PRICE_USD", "").strip()
    if not raw:
        return None
    try:
        return float(raw)
    except ValueError:
        return None
