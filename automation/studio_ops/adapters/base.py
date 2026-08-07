"""Generation adapter interface — one working backend, every vendor still refusing.

Nothing here calls a vendor, and that is still the design.

Wiring a *vendor* adapter is a separate, budgeted decision with three preconditions,
because the moment a real adapter exists the repository can spend money and produce
untraceable files:

1. The vendor's terms are current in rights/permissions/model_terms_register.md,
   verified for the plan tier the studio actually holds.
2. A cost ceiling is set for the production, and the adapter refuses past it.
3. The manifest write path exists, so no generated file can exist without a
   provenance record.

Until all three hold, every vendor adapter refuses. `GENERATION_DRY_RUN` defaults to
true so that the refusing state is what you get from a missing environment variable
rather than the spending state.

## What changed, and what deliberately did not

`local.LocalImageAdapter` is the first backend that actually produces a file. It is
offline, deterministic, and genuinely free, so preconditions 1 and 2 do not apply to
it: there are no vendor terms to verify and no money to ceiling. Precondition 3 is
still outstanding for everybody — `pipeline.manifest` is NOT BUILT — which is exactly
why the local adapter is **not** exempt from the dry-run default. It must be enabled
deliberately, per call site, like anything else that writes a file this repository
will later have to account for.

The zero-cost case is expressed arithmetically rather than as an exemption flag. The
budget guard's real invariant is *spend must not exceed the ceiling*; a run priced at
exactly 0.00 satisfies that for every ceiling, including a ceiling of zero, without
any special case. The only thing the guard adds is that a run priced **above** zero
against **no** ceiling is refused outright, because a priced run with no ceiling is
unaccountable rather than merely cheap. Nothing about a free backend loosens the path
a priced one takes.

`Capabilities.spends_money` is therefore a declaration for humans and for the CLI —
"safe to run in CI" — not a key that unlocks the guard. It is cross-checked after the
fact: an adapter that declares itself free and then returns a non-zero cost raises.

## The other half of the guarantee

`generate` is not overridable plumbing. It runs the pre-flight checks, calls the
subclass, and then verifies what came back. A subclass therefore cannot:

- skip the dry-run default or the cost ceiling by forgetting to check them,
- return an asset with a missing seed, model version, timestamp, operator, or hash,
- return a hash that is not a SHA-256 digest,
- attribute the work to a vendor other than the one that actually ran.

Every one of those is a provenance record that would fail at the manifest, discovered
at the point of generation instead of three steps downstream.
"""

from __future__ import annotations

import getpass
import hashlib
import os
import re
from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any, Self, TypeVar

if TYPE_CHECKING:  # pragma: no cover - import cycle avoidance only
    from ..config import Config

SHA256_PATTERN = re.compile(r"^[a-f0-9]{64}$")

# Matches asset_manifest.schema.json $defs.asset.sha256.
_HASH_CONTRACT = "a lowercase 64-character SHA-256 hex digest of the bytes written"


class AdapterError(RuntimeError):
    """Base for every adapter failure. Each subclass carries the reason, not the failure alone."""


class AdapterNotBuiltError(AdapterError):
    """Raised by every unwired adapter, and by the dry-run guard."""


class BudgetExceededError(AdapterError):
    """Raised when a run would exceed — or has exceeded — the production's ceiling."""


class UnsupportedRequestError(AdapterError):
    """Raised when a request asks a backend for something it does not do."""


class IncompleteProvenanceError(AdapterError):
    """Raised when a backend returns an asset the manifest could not accept.

    This is a defect in the adapter, not in the request. It fires after the file has
    been written, on purpose: a file on disk with an unusable provenance record is
    precisely the state this module exists to make impossible to ignore.
    """


@dataclass(frozen=True)
class Capabilities:
    """What a backend can do, declared by the backend itself.

    Conservative by default. An adapter that forgets to declare anything is treated
    as a paid, non-deterministic backend supporting no modality — the safe reading.
    """

    modalities: frozenset[str] = frozenset()
    spends_money: bool = True
    deterministic: bool = False
    accepts_seed: bool = False
    max_pixels: int | None = None
    notes: str = ""

    def supports(self, modality: str) -> bool:
        return modality in self.modalities


@dataclass(frozen=True)
class GenerationRequest:
    """One generation, fully specified.

    Built from a prompt card by `promptlib.render`. Never assembled by hand — the
    card is the reviewable artefact and the request is derived from it.

    `output_path` is the exception: it is filled by the pipeline, not the renderer,
    because where an asset lands is a storage decision and the card knows nothing
    about it. An adapter writes there and nowhere else; the asset store owns the
    permanent location and is free to move the file afterwards.
    """

    prompt_card_id: str
    modality: str
    vendor: str
    model: str
    rendered_prompt: str
    parameters: dict[str, Any] = field(default_factory=dict)
    inputs: list[str] = field(default_factory=list)
    seed: int | str | None = None
    estimated_cost_usd: float = 0.0
    output_path: str | None = None


@dataclass(frozen=True)
class GenerationResult:
    """One generation's output plus everything the manifest needs.

    Every field here is required by asset_manifest.schema.json. The type exists so
    that an adapter physically cannot return an asset without its provenance.

    `request` is the request **as executed**, not necessarily as submitted: the base
    class requires that its `vendor` names the adapter that actually ran, so an
    adapter that normalises the tool attribution is doing the right thing.
    """

    request: GenerationRequest
    asset_path: str
    sha256: str
    seed: int | str
    model_version: str
    generated_at: str
    generated_by: str
    cost_usd: float
    raw_response: dict[str, Any] = field(default_factory=dict)

    def to_generation_block(self) -> dict[str, Any]:
        """The `generation` object of an asset manifest entry.

        Exactly the shape of asset_manifest.schema.json $defs.asset.generation — no
        more, since that object sets `additionalProperties: false`. The surrounding
        entry (asset_id, provenance_class, rights_status, label) is not an adapter's
        to decide; those are editorial and rights judgements made by a person.
        """
        return {
            "tool": {
                "vendor": self.request.vendor,
                "model": self.request.model,
                "version": self.model_version,
            },
            "prompt_card": self.request.prompt_card_id,
            "seed": self.seed,
            "parameters": dict(self.request.parameters),
            "inputs": list(self.request.inputs),
            "generated_at": self.generated_at,
            "generated_by": self.generated_by,
            "cost_usd": self.cost_usd,
        }


class Adapter(ABC):
    """Base for every backend.

    Subclasses implement `_generate` and `estimate_cost`. `generate` enforces the
    preconditions and audits the result, so no adapter can bypass the budget, the
    dry-run default, or the provenance contract by forgetting to check.
    """

    vendor: str = "unknown"
    modality: str = "unknown"

    def __init__(
        self,
        *,
        dry_run: bool = True,
        budget_usd: float = 0.0,
        operator: str | None = None,
    ) -> None:
        self.dry_run = dry_run
        self.budget_usd = budget_usd
        self.operator = operator or default_operator()
        self.spent_usd = 0.0

    # --- declaration ------------------------------------------------------

    @classmethod
    def capabilities(cls) -> Capabilities:
        """What this backend does. Conservative default: paid, non-deterministic."""
        return Capabilities()

    @classmethod
    def from_config(cls, cfg: Config, **kwargs: Any) -> Self:
        """Build from runtime configuration, so the dry-run default comes from env.

        The single place a caller should construct an adapter. Passing `dry_run`
        explicitly is possible and is meant to look deliberate when you read it.
        """
        kwargs.setdefault("dry_run", cfg.generation_dry_run)
        kwargs.setdefault("budget_usd", cfg.generation_budget_usd)
        return cls(**kwargs)

    # --- the guarded path -------------------------------------------------

    def generate(self, request: GenerationRequest) -> GenerationResult:
        self._preflight(request)
        result = self._generate(request)
        return self._postflight(result)

    def quoted_cost(self, request: GenerationRequest) -> float:
        """The price the ceiling is checked against.

        The higher of what the adapter quotes and what the caller declared, so that
        neither side can lower the bar alone. An adapter that under-quotes is caught
        after the fact by the post-flight overrun check.
        """
        quoted = self.estimate_cost(request)
        if quoted < 0:
            raise UnsupportedRequestError(
                f"{self.vendor}: estimate_cost returned a negative price ({quoted}). "
                "A refund is not a generation."
            )
        return max(quoted, request.estimated_cost_usd, 0.0)

    def _preflight(self, request: GenerationRequest) -> None:
        if self.dry_run:
            raise AdapterNotBuiltError(
                f"{self.vendor}: GENERATION_DRY_RUN is set. Generation is disabled by "
                "default; enabling it is a deliberate act with a cost ceiling."
            )

        caps = self.capabilities()
        if not caps.supports(request.modality):
            supported = ", ".join(sorted(caps.modalities)) or "nothing"
            raise UnsupportedRequestError(
                f"{self.vendor}: asked for {request.modality!r}; this backend supports {supported}."
            )

        cost = self.quoted_cost(request)
        if cost > 0 and self.budget_usd <= 0:
            raise BudgetExceededError(
                f"{self.vendor}: no generation budget set for this production, and this "
                f"run is priced at ${cost:.2f}. Set budget.generation_ceiling_usd on the "
                "production record."
            )
        if self.spent_usd + cost > self.budget_usd:
            raise BudgetExceededError(
                f"{self.vendor}: run would exceed the production ceiling "
                f"(${self.spent_usd:.2f} spent of ${self.budget_usd:.2f}, "
                f"${cost:.2f} requested)."
            )

    def _postflight(self, result: GenerationResult) -> GenerationResult:
        self._require_complete(result)

        if not self.capabilities().spends_money and result.cost_usd > 0:
            raise IncompleteProvenanceError(
                f"{self.vendor} declares spends_money=False but returned a cost of "
                f"${result.cost_usd:.4f}. The declaration is a safety claim other code "
                "reads; fix the declaration or fix the price."
            )

        self.spent_usd += result.cost_usd
        if result.cost_usd > 0 and self.spent_usd > self.budget_usd:
            raise BudgetExceededError(
                f"{self.vendor}: actual cost exceeded the quote and the run has overrun "
                f"the ceiling (${self.spent_usd:.2f} of ${self.budget_usd:.2f}). The "
                "spend has already happened; this is the ledger saying so."
            )
        return result

    def _require_complete(self, result: GenerationResult) -> None:
        """Refuse a result the manifest could not accept.

        Runs for every adapter, including future vendor ones, so the provenance
        contract is a property of the base class rather than a convention.
        """
        missing = [
            name
            for name, value in (
                ("asset_path", result.asset_path),
                ("sha256", result.sha256),
                ("model_version", result.model_version),
                ("generated_at", result.generated_at),
                ("generated_by", result.generated_by),
                ("seed", result.seed),
            )
            if value is None or not str(value).strip()
        ]
        if missing:
            raise IncompleteProvenanceError(
                f"{self.vendor}: returned an asset without {', '.join(missing)}. Every "
                "field is required by asset_manifest.schema.json; an asset that cannot "
                "be recorded cannot be conformed."
            )

        if not SHA256_PATTERN.match(result.sha256):
            raise IncompleteProvenanceError(
                f"{self.vendor}: sha256 must be {_HASH_CONTRACT}, got {result.sha256!r}."
            )

        if result.cost_usd < 0:
            raise IncompleteProvenanceError(
                f"{self.vendor}: cost_usd must be a non-negative number, got {result.cost_usd}."
            )

        if result.request.vendor != self.vendor:
            raise IncompleteProvenanceError(
                f"{self.vendor}: returned a result attributed to {result.request.vendor!r}. "
                "The manifest must name the backend that actually produced the file."
            )

    # --- subclass surface -------------------------------------------------

    @abstractmethod
    def _generate(self, request: GenerationRequest) -> GenerationResult:
        """Produce the asset. Called only after the pre-flight checks have passed."""

    @abstractmethod
    def estimate_cost(self, request: GenerationRequest) -> float:
        """Price this request in USD before spending it, so the ceiling binds in advance.

        Must be non-negative, must not perform a network call, and must not depend on
        anything the caller cannot see. Return 0.0 only if the run is genuinely free.
        """


class StubAdapter(Adapter):
    """Base for the per-modality stubs. Refuses, and says why."""

    reason: str = "not implemented"

    @classmethod
    def capabilities(cls) -> Capabilities:
        # Claims its modality so the refusal is about being unbuilt rather than about
        # the request shape — the reason a caller needs to read is `reason`.
        return Capabilities(modalities=frozenset({cls.modality}), notes=cls.reason)

    def _generate(self, request: GenerationRequest) -> GenerationResult:
        raise AdapterNotBuiltError(
            f"{self.vendor} ({self.modality}) adapter is NOT BUILT. {self.reason} "
            "See automation/README.md maturity table and docs/status.md."
        )

    def estimate_cost(self, request: GenerationRequest) -> float:
        return 0.0


# --- registry -------------------------------------------------------------
#
# Lookup by name, so a call site names a backend as data ("local") rather than by
# importing a class. That is what lets the CLI take `--adapter` and what will let a
# vendor backend be swapped in without touching the caller.

_REGISTRY: dict[str, type[Adapter]] = {}

AdapterT = TypeVar("AdapterT", bound=Adapter)


def register(name: str) -> Callable[[type[AdapterT]], type[AdapterT]]:
    """Class decorator. Registers a backend under a stable, user-facing name."""

    def decorate(cls: type[AdapterT]) -> type[AdapterT]:
        existing = _REGISTRY.get(name)
        if existing is not None and existing is not cls:
            raise ValueError(
                f"adapter name {name!r} is already registered to {existing.__name__}; "
                "two backends under one name makes a provenance record ambiguous."
            )
        _REGISTRY[name] = cls
        return cls

    return decorate


def get_adapter(name: str) -> type[Adapter]:
    """Look up a backend by name, or say what does exist."""
    try:
        return _REGISTRY[name]
    except KeyError:
        known = ", ".join(sorted(_REGISTRY)) or "none"
        raise AdapterNotBuiltError(
            f"no adapter registered as {name!r}. Registered: {known}."
        ) from None


def registered_adapters() -> dict[str, type[Adapter]]:
    """Every registered backend, name → class. A copy; mutating it changes nothing."""
    return dict(_REGISTRY)


# --- shared helpers -------------------------------------------------------


def sha256_file(path: Path) -> str:
    """Digest of what is actually on disk, read back after writing.

    Hashing the buffer you meant to write proves nothing about the file. This reads
    it, which is the claim the manifest makes.
    """
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def default_operator() -> str:
    """Who to record as `generated_by` when the caller does not say.

    `STUDIO_OPERATOR` first, because in CI the OS user is meaningless. Never empty:
    the manifest requires the field, and "unknown" is at least an honest answer.
    """
    named = os.environ.get("STUDIO_OPERATOR", "").strip()
    if named:
        return named
    try:
        return getpass.getuser() or "unknown"
    except Exception:  # pragma: no cover - platform dependent
        return "unknown"
