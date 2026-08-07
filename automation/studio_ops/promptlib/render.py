"""Prompt card → vendor string. NOT BUILT.

The main practical payoff of treating a prompt as a record rather than a string is
that the same card can target a different vendor by changing one field. That payoff
lives entirely in this module, and it is currently unproven.

Canon: prompts/README.md, prompts/_framework/prompt_anatomy.md
Schema: standards/schemas/prompt_card.schema.json
Decision: docs/decisions/0003-prompt-cards.md
Status: docs/status.md

Design, when it is built:

- One renderer per vendor, registered by `(modality, vendor)`.
- Each renderer receives the resolved card — style block inherited from the line and
  sequence, overrides applied — and emits the vendor's expected string plus its
  parameter dict.
- Field ORDER is per-vendor, because most image models weight earlier tokens more
  heavily. The order lives in the renderer, never in the card, so that changing it
  improves every card at once. Reordering fields by hand in a card is a smell.
- `prompt.raw_override` bypasses the renderer entirely and must be counted. A rising
  override rate is the documented failure signal for ADR 0003: it means the
  abstraction does not fit the tools actually in use.

Deliberately absent: any network call. Rendering is offline; running is
`promptlib.run`, which goes through an adapter with a cost ceiling.
"""

from __future__ import annotations

from typing import Any

NOT_BUILT = "promptlib.render is NOT BUILT. See docs/status.md."


class RendererNotBuiltError(NotImplementedError):
    """Raised by every function here."""


def resolve(card: dict[str, Any], style_block: dict[str, Any]) -> dict[str, Any]:
    """Apply style inheritance and overrides to a card. NOT BUILT."""
    raise RendererNotBuiltError(NOT_BUILT)


def render(card: dict[str, Any], vendor: str | None = None) -> tuple[str, dict[str, Any]]:
    """Render a resolved card to (prompt_string, parameters) for a vendor. NOT BUILT."""
    raise RendererNotBuiltError(NOT_BUILT)


def override_rate(cards: list[dict[str, Any]]) -> float:
    """Fraction of cards using raw_override — the ADR 0003 failure signal. NOT BUILT."""
    raise RendererNotBuiltError(NOT_BUILT)
