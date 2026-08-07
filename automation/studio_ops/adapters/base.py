"""Generation adapter interface — DELIBERATE STUBS.

These are not unfinished. Nothing here calls a vendor, and that is the design.

Wiring an adapter is a separate, budgeted decision with three preconditions, because
the moment a real adapter exists the repository can spend money and produce
untraceable files:

1. The vendor's terms are current in rights/permissions/model_terms_register.md,
   verified for the plan tier the studio actually holds.
2. A cost ceiling is set for the production, and the adapter refuses past it.
3. The manifest write path exists, so no generated file can exist without a
   provenance record.

Until all three hold, every adapter refuses. `GENERATION_DRY_RUN` defaults to true
so that the refusing state is what you get from a missing environment variable
rather than the spending state.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


class AdapterNotBuiltError(RuntimeError):
    """Raised by every adapter. Carries the reason, not just the failure."""


class BudgetExceededError(RuntimeError):
    """Raised when a run would exceed the production's generation ceiling."""


@dataclass(frozen=True)
class GenerationRequest:
    """One generation, fully specified.

    Built from a prompt card by `promptlib.render`. Never assembled by hand — the
    card is the reviewable artefact and the request is derived from it.
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


@dataclass(frozen=True)
class GenerationResult:
    """One generation's output plus everything the manifest needs.

    Every field here is required by asset_manifest.schema.json. The type exists so
    that an adapter physically cannot return an asset without its provenance.
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


class Adapter(ABC):
    """Base for every vendor adapter.

    Subclasses implement `_generate`. `generate` enforces the preconditions, so no
    adapter can bypass the budget or the dry-run default by forgetting to check.
    """

    vendor: str = "unknown"
    modality: str = "unknown"

    def __init__(self, *, dry_run: bool = True, budget_usd: float = 0.0) -> None:
        self.dry_run = dry_run
        self.budget_usd = budget_usd
        self.spent_usd = 0.0

    def generate(self, request: GenerationRequest) -> GenerationResult:
        if self.dry_run:
            raise AdapterNotBuiltError(
                f"{self.vendor}: GENERATION_DRY_RUN is set. Generation is disabled by "
                "default; enabling it is a deliberate act with a cost ceiling."
            )
        if self.budget_usd <= 0:
            raise BudgetExceededError(
                f"{self.vendor}: no generation budget set for this production. "
                "Set budget.generation_ceiling_usd on the production record."
            )
        if self.spent_usd + request.estimated_cost_usd > self.budget_usd:
            raise BudgetExceededError(
                f"{self.vendor}: run would exceed the production ceiling "
                f"(${self.spent_usd:.2f} spent of ${self.budget_usd:.2f})."
            )
        result = self._generate(request)
        self.spent_usd += result.cost_usd
        return result

    @abstractmethod
    def _generate(self, request: GenerationRequest) -> GenerationResult:
        """Vendor call. Every subclass currently raises AdapterNotBuiltError."""

    @abstractmethod
    def estimate_cost(self, request: GenerationRequest) -> float:
        """Cost before spending it, so the ceiling can be enforced in advance."""


class StubAdapter(Adapter):
    """Base for the per-modality stubs. Refuses, and says why."""

    reason: str = "not implemented"

    def _generate(self, request: GenerationRequest) -> GenerationResult:
        raise AdapterNotBuiltError(
            f"{self.vendor} ({self.modality}) adapter is NOT BUILT. {self.reason} "
            "See automation/README.md maturity table and docs/status.md."
        )

    def estimate_cost(self, request: GenerationRequest) -> float:
        return 0.0
