"""promptlib — a prompt card is a record; a vendor string is a projection of it.

Two modules:

- `registry` — renderers keyed by `(modality, vendor)`, plus the `generic` fallback.
  Field order per vendor lives here.
- `render` — load and validate a card, resolve style inheritance and overrides,
  render, and compute the `raw_override` rate that ADR 0003 names as its own
  falsification condition.

The `render` FUNCTION is deliberately not re-exported here. A function of that name
in this namespace would shadow the module of that name, so `promptlib.render.load_card`
would resolve or fail depending on import order. Call it as:

    from studio_ops.promptlib import render
    rendered = render.render(card, vendor="midjourney")

Offline. Nothing here calls a vendor; running a rendered prompt is the adapter's job
and is gated by a cost ceiling. See `studio_ops.adapters.base`.
"""

from __future__ import annotations

from . import registry, render
from .registry import (
    GENERIC,
    PROMPT_FIELDS,
    RenderedPrompt,
    register,
    register_renderer,
    registered,
)
from .render import (
    CardValidationError,
    OverrideWithoutReasonError,
    PromptCardError,
    UnknownOverrideFieldError,
    load_card,
    override_rate,
    render_file,
    resolve,
    uses_raw_override,
    validate_card,
)

__all__ = [
    "GENERIC",
    "PROMPT_FIELDS",
    "CardValidationError",
    "OverrideWithoutReasonError",
    "PromptCardError",
    "RenderedPrompt",
    "UnknownOverrideFieldError",
    "load_card",
    "override_rate",
    "register",
    "register_renderer",
    "registered",
    "registry",
    "render",
    "render_file",
    "resolve",
    "uses_raw_override",
    "validate_card",
]
