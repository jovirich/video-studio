"""Renderer registry — one renderer per `(modality, vendor)`.

A prompt card is a record; a vendor string is a disposable projection of it. This
module holds the projections, keyed by the two card fields that decide which one
applies: `modality` and `tool.vendor`.

Field ORDER lives here, never in the card. Most image models weight earlier tokens
more heavily, so the order is a property of the tool, not of the shot. Keeping it in
the renderer means changing it improves every card at once; reordering fields by hand
inside a card improves one card and silently diverges from the rest.

Canon: prompts/_framework/prompt_anatomy.md § Order matters, per model
Schema: standards/schemas/prompt_card.schema.json

## What is registered here, and what is deliberately not

- `generic` — modality-agnostic, the fallback for every `(modality, vendor)` with no
  specific renderer. This is the one that has to work: it is what the local adapter
  uses, and it is the reason an unregistered vendor degrades to a readable prompt
  instead of an exception.
- `("image", "midjourney")` — one named vendor, to prove the seam is real rather
  than theoretical.

The Midjourney renderer implements two things this repository can actually verify:
the **field order** (its cheat sheet states that earlier tokens dominate and that
literal adherence is weak, so the fields that must survive go first), and the `--no`
negative flag (`prompts/image/midjourney/README.md` § Control surface,
`prompts/_framework/negative_library.md` § Per-vendor syntax).

It deliberately does **not** invent spellings for aspect ratio, stylisation, chaos,
`--sref`, or `--cref`. Those are named as concepts in the cheat sheet but the sheet
records no syntax, and a fabricated flag would fail silently at generation time —
the worst possible failure, because the run still costs money and the output still
looks plausible. Instead, entries in the card's `parameters` block are emitted with
the author's own key spelling. `parameters` is `additionalProperties: true` by
design and the vendor cheat sheet is the documented authority on valid keys; the
renderer passes them through rather than pretending to know them.

Adding a vendor is one function and one decorator. See `render_midjourney` below.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any

GENERIC = "generic"

# Registry key for a renderer that applies to every modality.
ANY_MODALITY = "*"

# The structured prompt fields, in the order the schema declares them. Every renderer
# starts from this list and reorders for its own vendor; nothing outside a renderer
# may reorder it.
PROMPT_FIELDS: tuple[str, ...] = (
    "subject",
    "action",
    "setting",
    "period_markers",
    "composition",
    "camera",
    "light",
    "palette",
    "texture",
    "mood",
)

# Prompt fields that are lists. They merge on inheritance rather than replace, per
# negative_library.md § Inheritance: line → sequence → card.
LIST_FIELDS: frozenset[str] = frozenset({"period_markers", "negative"})


@dataclass(frozen=True)
class RenderedPrompt:
    """One card projected onto one vendor.

    The parameter dict is returned alongside the string rather than folded into it,
    because the manifest records what was actually sent and a string is not a record.
    Some vendors carry parameters inline in the prompt (Midjourney's flags); the dict
    is still populated, so the provenance path does not depend on the vendor's syntax.
    """

    card_id: str
    modality: str
    vendor: str
    model: str
    prompt: str
    parameters: dict[str, Any] = field(default_factory=dict)
    negative: tuple[str, ...] = ()
    # The field order this renderer used, for review and for diffing two vendors.
    order: tuple[str, ...] = ()
    # True when `prompt.raw_override` bypassed field assembly. Counted by
    # `render.override_rate` — the documented failure signal for ADR 0003.
    raw_override: bool = False
    renderer: str = GENERIC

    def to_dict(self) -> dict[str, Any]:
        return {
            "card_id": self.card_id,
            "modality": self.modality,
            "vendor": self.vendor,
            "model": self.model,
            "prompt": self.prompt,
            "parameters": dict(self.parameters),
            "negative": list(self.negative),
            "order": list(self.order),
            "raw_override": self.raw_override,
            "renderer": self.renderer,
        }


# A renderer takes a RESOLVED card — style inherited, overrides applied — and the
# vendor being targeted, which may differ from the card's own `tool.vendor` when a
# card is being re-pointed at another tool.
Renderer = Callable[[Mapping[str, Any], str], RenderedPrompt]

_RENDERERS: dict[tuple[str, str], Renderer] = {}


class DuplicateRendererError(ValueError):
    """Two renderers claimed the same `(modality, vendor)`."""


def register_renderer(modality: str, vendor: str, renderer: Renderer) -> None:
    """Explicit registration, for renderers defined outside this module."""
    key = (modality, vendor)
    if key in _RENDERERS:
        raise DuplicateRendererError(f"a renderer is already registered for {key}")
    _RENDERERS[key] = renderer


def register(modality: str, vendor: str) -> Callable[[Renderer], Renderer]:
    """Decorator form of `register_renderer`."""

    def decorate(fn: Renderer) -> Renderer:
        register_renderer(modality, vendor, fn)
        return fn

    return decorate


def get(modality: str, vendor: str) -> Renderer:
    """Most specific renderer for `(modality, vendor)`, falling back to `generic`.

    The fallback is not a convenience. An unregistered vendor must still produce a
    reviewable string, because the alternative — refusing to render — makes the card
    unusable for exactly the tool nobody has written a renderer for yet.
    """
    for key in (
        (modality, vendor),
        (ANY_MODALITY, vendor),
        (modality, GENERIC),
        (ANY_MODALITY, GENERIC),
    ):
        found = _RENDERERS.get(key)
        if found is not None:
            return found
    raise LookupError(f"no renderer for {(modality, vendor)} and no generic fallback")


def has_renderer(modality: str, vendor: str) -> bool:
    """True when a renderer is registered for this pair specifically, not by fallback."""
    return (modality, vendor) in _RENDERERS or (ANY_MODALITY, vendor) in _RENDERERS


def registered() -> list[tuple[str, str]]:
    """Every registered `(modality, vendor)`, sorted. Used by the CLI to list targets."""
    return sorted(_RENDERERS)


# --- shared helpers ---------------------------------------------------------


def as_text(value: Any) -> str:
    """Flatten one prompt field to text. Lists join with commas; empties vanish."""
    if value is None or isinstance(value, bool):
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (list, tuple)):
        return ", ".join(part for part in (as_text(item) for item in value) if part)
    return str(value).strip()


def ordered_fields(prompt: Mapping[str, Any], order: Sequence[str]) -> list[tuple[str, str]]:
    """`(name, text)` for each non-empty field, in the renderer's order."""
    out: list[tuple[str, str]] = []
    for name in order:
        text = as_text(prompt.get(name))
        if text:
            out.append((name, text))
    return out


def negatives(prompt: Mapping[str, Any]) -> tuple[str, ...]:
    """De-duplicated negative terms, order preserved."""
    seen: dict[str, None] = {}
    raw = prompt.get("negative")
    if isinstance(raw, (list, tuple)):
        for item in raw:
            text = as_text(item)
            if text:
                seen[text] = None
    elif as_text(raw):
        seen[as_text(raw)] = None
    return tuple(seen)


def base_fields(card: Mapping[str, Any], vendor: str) -> tuple[str, str, str, str]:
    """`(card_id, modality, vendor, model)` for the RenderedPrompt header.

    `model` is dropped when the target vendor is not the card's own. A card names a
    model for one vendor; carrying `midjourney/v6` into a Flux request would be a
    provenance lie that the adapter has no way to detect.
    """
    tool = card.get("tool") or {}
    card_vendor = as_text(tool.get("vendor"))
    model = as_text(tool.get("model")) if vendor == card_vendor else ""
    return as_text(card.get("id")), as_text(card.get("modality")), vendor, model


# --- generic ----------------------------------------------------------------

# Fields that read as prose on their own get no label; the technical ones do, so a
# reviewer can find the camera line without reading the whole string.
GENERIC_LABELS: dict[str, str] = {
    "period_markers": "Period detail",
    "composition": "Composition",
    "camera": "Camera",
    "light": "Light",
    "palette": "Palette",
    "texture": "Texture",
    "mood": "Mood",
}


@register(ANY_MODALITY, GENERIC)
def render_generic(card: Mapping[str, Any], vendor: str) -> RenderedPrompt:
    """Readable, well-ordered prose. The fallback, and the one that must work.

    Order is the schema's own field order, which is already the sensible one: what is
    depicted, then where, then how it is photographed. Negatives are stated as an
    `Avoid:` clause because a generic target has no negative channel — several models
    honour a plain-language exclusion, and none is harmed by it.
    """
    prompt = card.get("prompt") or {}
    fields = ordered_fields(prompt, PROMPT_FIELDS)

    segments: list[str] = []
    for name, text in fields:
        label = GENERIC_LABELS.get(name)
        segments.append(f"{label}: {text}" if label else text)

    negs = negatives(prompt)
    if negs:
        segments.append("Avoid: " + ", ".join(negs))

    body = ". ".join(segment.rstrip(" .") for segment in segments)
    card_id, modality, target, model = base_fields(card, vendor)
    return RenderedPrompt(
        card_id=card_id,
        modality=modality,
        vendor=target,
        model=model,
        prompt=f"{body}." if body else "",
        parameters=dict(card.get("parameters") or {}),
        negative=negs,
        order=tuple(name for name, _ in fields),
        renderer=GENERIC,
    )


# --- midjourney -------------------------------------------------------------

# Subject and period markers lead. The cheat sheet records two facts that decide this
# order: earlier tokens dominate, and literal prompt adherence at detail level is
# weak. Period markers are the card's main defence against generic pan-historical
# output, so they must not sit in the tail where adherence falls off.
MIDJOURNEY_ORDER: tuple[str, ...] = (
    "subject",
    "period_markers",
    "setting",
    "action",
    "composition",
    "camera",
    "light",
    "palette",
    "texture",
    "mood",
)


@register("image", "midjourney")
def render_midjourney(card: Mapping[str, Any], vendor: str) -> RenderedPrompt:
    """Comma-separated phrases, negatives on `--no`, parameters as trailing flags.

    No labels: Midjourney reads descriptive phrases, and a label consumes weight that
    the phrase needs. Parameter keys are emitted exactly as the card author wrote
    them — see this module's docstring for why they are not translated.
    """
    prompt = card.get("prompt") or {}
    fields = ordered_fields(prompt, MIDJOURNEY_ORDER)
    body = ", ".join(text.rstrip(" .") for _, text in fields)

    negs = negatives(prompt)
    if negs:
        body = f"{body} --no {', '.join(negs)}".strip()

    parameters = dict(card.get("parameters") or {})
    flags = [flag for flag in (_flag(key, value) for key, value in parameters.items()) if flag]
    if flags:
        body = f"{body} {' '.join(flags)}".strip()

    card_id, modality, target, model = base_fields(card, vendor)
    return RenderedPrompt(
        card_id=card_id,
        modality=modality,
        vendor=target,
        model=model,
        prompt=body,
        parameters=parameters,
        negative=negs,
        order=tuple(name for name, _ in fields),
        renderer="midjourney",
    )


def _flag(key: str, value: Any) -> str | None:
    """One `parameters` entry as a command-line flag, or None if it is off."""
    if value is None or value is False:
        return None
    if value is True:
        return f"--{key}"
    text = as_text(value)
    return f"--{key} {text}" if text else None


__all__ = [
    "ANY_MODALITY",
    "GENERIC",
    "LIST_FIELDS",
    "MIDJOURNEY_ORDER",
    "PROMPT_FIELDS",
    "DuplicateRendererError",
    "RenderedPrompt",
    "Renderer",
    "as_text",
    "base_fields",
    "get",
    "has_renderer",
    "negatives",
    "ordered_fields",
    "register",
    "register_renderer",
    "registered",
    "render_generic",
    "render_midjourney",
]
