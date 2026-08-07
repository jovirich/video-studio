"""Prompt card → vendor string.

The main practical payoff of treating a prompt as a record rather than a string is
that the same card can target a different vendor by changing one field. That payoff
lives entirely in this module.

Canon: prompts/README.md, prompts/_framework/prompt_anatomy.md
Schema: standards/schemas/prompt_card.schema.json
Decision: docs/decisions/0003-prompt-cards.md

The shape:

- `load_card` reads a card from disk and validates it against the schema. A card that
  does not validate does not render — rendering an invalid card produces a plausible
  string from an incomplete record, which is worse than an error because it costs
  money before anyone notices.
- `resolve` applies style inheritance, then the card's own fields, then its declared
  overrides. Every override carries a stated reason; one without a reason raises,
  because unexplained overrides accumulate — each defensible alone — and the look
  drifts with no single decision having caused it.
- `render` dispatches to a renderer registered by `(modality, vendor)` and returns
  the string AND the parameter dict. Field order is per-vendor and lives in the
  renderer, never in the card. See `registry`.
- `override_rate` counts `prompt.raw_override`. ADR 0003 names a rising rate as its
  own falsification condition, so the decision is only ever evaluated if someone can
  compute this.

`raw_override` bypasses field assembly entirely: the verbatim string is returned and
`RenderedPrompt.raw_override` records that it did. Vendor parameters still travel,
because the escape hatch is about prompt syntax, not about abandoning the record.

Deliberately absent: any network call. Rendering is offline; running is the
adapter's job, and the adapter has a cost ceiling.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from ..frontmatter import read_yaml
from ..paths import Layout, find_repo_root
from .registry import (
    GENERIC,
    LIST_FIELDS,
    PROMPT_FIELDS,
    RenderedPrompt,
    as_text,
    base_fields,
    get,
)

SCHEMA_NAME = "prompt_card.schema.json"

# Override targets. A bare name must be a prompt field; anything else must be an
# explicit path. Restricting the set is the point: an override naming a field nobody
# applies is invisible drift, which is the exact failure the reason requirement
# exists to prevent.
OVERRIDE_ROOTS: frozenset[str] = frozenset({"prompt", "parameters"})


class PromptCardError(Exception):
    """Base for everything this module refuses to do."""


class CardValidationError(PromptCardError):
    """The card does not satisfy prompt_card.schema.json, or would not parse."""

    def __init__(self, message: str, errors: Sequence[str] = ()) -> None:
        super().__init__(message)
        self.errors: tuple[str, ...] = tuple(errors)


class OverrideWithoutReasonError(PromptCardError):
    """An override carried no reason. Per the schema's intent, that fails review."""


class UnknownOverrideFieldError(PromptCardError):
    """An override named a field the renderer has no way to apply."""


# --- loading and validation -------------------------------------------------


def schema_dir(explicit: Path | None = None) -> Path:
    """Where the schemas live. Explicit path wins; otherwise the repository's."""
    if explicit is not None:
        return explicit
    return Layout(root=find_repo_root()).schemas


def validate_card(card: Mapping[str, Any], *, schemas: Path | None = None) -> list[str]:
    """Schema errors for one card, as `pointer: message` strings. Empty means valid."""
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012

    directory = schema_dir(schemas)
    if not directory.is_dir():
        raise CardValidationError(f"schema directory not found: {directory}")

    store: dict[str, dict[str, Any]] = {}
    for path in sorted(directory.glob("*.schema.json")):
        store[path.name] = json.loads(path.read_text(encoding="utf-8"))

    schema = store.get(SCHEMA_NAME)
    if schema is None:
        raise CardValidationError(f"{SCHEMA_NAME} is missing from {directory}")

    # Sibling schemas reference each other by bare filename (_common.schema.json#/...).
    registry: Registry = Registry()
    for name, doc in store.items():
        registry = registry.with_resource(
            name, Resource.from_contents(doc, default_specification=DRAFT202012)
        )

    validator = Draft202012Validator(schema, registry=registry)
    return [
        f"{'/'.join(str(part) for part in error.path) or '(root)'}: {error.message}"
        for error in sorted(validator.iter_errors(card), key=lambda e: list(e.path))
    ]


def load_card(path: Path, *, schemas: Path | None = None) -> dict[str, Any]:
    """Read and validate a `*.prompt.yaml`. Raises rather than returning a bad card."""
    data, error = read_yaml(path)
    if error is not None:
        raise CardValidationError(f"{path}: {error}")
    card = data or {}
    errors = validate_card(card, schemas=schemas)
    if errors:
        joined = "\n  ".join(errors)
        raise CardValidationError(f"{path} is not a valid prompt card:\n  {joined}", errors)
    return card


# --- resolution -------------------------------------------------------------


def resolve(card: Mapping[str, Any], style_block: Mapping[str, Any]) -> dict[str, Any]:
    """Apply style inheritance, then the card's fields, then its overrides.

    Precedence, weakest first:

    1. the inherited style block,
    2. the card's own `prompt` fields — a card field beats an inherited one,
    3. `inheritance.overrides`, each of which must state a reason.

    List fields merge rather than replace, per negative_library.md § Inheritance: the
    line's negatives still apply, and the card adds what is specific to this shot. An
    empty card value does not clear an inherited one — clearing is a deviation, so it
    goes through an override where it has to carry a reason.

    The style block may be a flat mapping of prompt field names, or a mapping with a
    `prompt` key holding them. Keys that are not prompt fields are ignored: a style
    block also carries its own identity, and that is not a prompt.
    """
    resolved = copy.deepcopy(dict(card))

    inherited = _style_prompt_fields(style_block)
    prompt: dict[str, Any] = dict(inherited)
    for name, value in (card.get("prompt") or {}).items():
        if name in LIST_FIELDS:
            merged = _merge_list(inherited.get(name), value)
            if merged:
                prompt[name] = merged
            continue
        if as_text(value):
            prompt[name] = value

    resolved["prompt"] = prompt
    _apply_overrides(resolved, (card.get("inheritance") or {}).get("overrides") or [])
    return resolved


def _style_prompt_fields(style_block: Mapping[str, Any]) -> dict[str, Any]:
    source = style_block.get("prompt") if isinstance(style_block.get("prompt"), Mapping) else None
    fields: Mapping[str, Any] = source if source is not None else style_block
    known = set(PROMPT_FIELDS) | {"negative"}
    return {name: value for name, value in fields.items() if name in known and as_text(value)}


def _merge_list(inherited: Any, own: Any) -> list[str]:
    """Inherited terms first, then this shot's, de-duplicated with order preserved."""
    merged: dict[str, None] = {}
    for source in (inherited, own):
        if isinstance(source, (list, tuple)):
            for item in source:
                text = as_text(item)
                if text:
                    merged[text] = None
        elif as_text(source):
            merged[as_text(source)] = None
    return list(merged)


def _apply_overrides(resolved: dict[str, Any], overrides: Any) -> None:
    if not isinstance(overrides, (list, tuple)):
        raise PromptCardError("inheritance.overrides must be a list")

    for position, override in enumerate(overrides, start=1):
        if not isinstance(override, Mapping):
            raise PromptCardError(f"override {position} is not a mapping")

        target = as_text(override.get("field"))
        if not target:
            raise PromptCardError(f"override {position} names no field")
        if "value" not in override:
            raise PromptCardError(f"override {position} ({target}) carries no value")
        if not as_text(override.get("reason")):
            raise OverrideWithoutReasonError(
                f"override {position} of `{target}` states no reason. Every deviation "
                "from the inherited style carries one, or the production's look drifts "
                "without any single decision having caused it."
            )

        _set_override(resolved, target, override["value"])


def _set_override(resolved: dict[str, Any], target: str, value: Any) -> None:
    if "." in target:
        root, _, leaf = target.partition(".")
    elif target in PROMPT_FIELDS or target == "negative":
        root, leaf = "prompt", target
    else:
        raise UnknownOverrideFieldError(
            f"override names `{target}`, which is not a prompt field. Use one of "
            f"{', '.join(sorted(set(PROMPT_FIELDS) | {'negative'}))}, or an explicit "
            "path such as `parameters.<key>`."
        )

    if root not in OVERRIDE_ROOTS or not leaf:
        raise UnknownOverrideFieldError(
            f"override names `{target}`; overrides may only target "
            f"{', '.join(sorted(OVERRIDE_ROOTS))}."
        )
    if root == "prompt" and leaf not in PROMPT_FIELDS and leaf != "negative":
        raise UnknownOverrideFieldError(
            f"override names `{target}`, which is not a field of the prompt block."
        )

    block = resolved.setdefault(root, {})
    if not isinstance(block, dict):
        raise PromptCardError(f"cannot apply override `{target}`: `{root}` is not a mapping")
    block[leaf] = value


# --- rendering --------------------------------------------------------------


def render(
    card: Mapping[str, Any],
    vendor: str | None = None,
    *,
    style_block: Mapping[str, Any] | None = None,
) -> RenderedPrompt:
    """Render a card for a vendor. Returns the string and the parameter dict.

    `vendor` defaults to the card's `tool.vendor`. Passing another one re-points the
    same record at another tool, which is the whole reason the record is structured.
    An unregistered vendor falls back to the generic renderer rather than refusing.

    Style inheritance and overrides are always applied first, even with no style
    block, so an override without a reason is caught on every path to a string.
    """
    resolved = resolve(card, style_block or {})

    tool = resolved.get("tool") or {}
    target = as_text(vendor) or as_text(tool.get("vendor")) or GENERIC
    modality = as_text(resolved.get("modality"))

    prompt = resolved.get("prompt") or {}
    raw = as_text(prompt.get("raw_override"))
    if raw:
        card_id, card_modality, target_vendor, model = base_fields(resolved, target)
        return RenderedPrompt(
            card_id=card_id,
            modality=card_modality,
            vendor=target_vendor,
            model=model,
            prompt=raw,
            parameters=dict(resolved.get("parameters") or {}),
            raw_override=True,
            renderer="raw_override",
        )

    return get(modality, target)(resolved, target)


def render_file(
    path: Path,
    vendor: str | None = None,
    *,
    style_block: Mapping[str, Any] | None = None,
    schemas: Path | None = None,
) -> RenderedPrompt:
    """Load, validate, and render a card from disk. Invalid cards raise."""
    return render(load_card(path, schemas=schemas), vendor, style_block=style_block)


# --- the ADR 0003 failure signal --------------------------------------------


def uses_raw_override(card: Mapping[str, Any]) -> bool:
    """True when this card bypasses field assembly."""
    return bool(as_text((card.get("prompt") or {}).get("raw_override")))


def override_rate(cards: Sequence[Mapping[str, Any]]) -> float:
    """Fraction of cards using `raw_override` — the ADR 0003 failure signal.

    Every override marks a place the abstraction did not fit. If most cards use one,
    the structure is wrong for the tools actually in use and should be revised rather
    than defended. Three lines, and the only way that decision is ever evaluated.
    """
    if not cards:
        return 0.0
    return sum(1 for card in cards if uses_raw_override(card)) / len(cards)


__all__ = [
    "OVERRIDE_ROOTS",
    "PROMPT_FIELDS",
    "SCHEMA_NAME",
    "CardValidationError",
    "OverrideWithoutReasonError",
    "PromptCardError",
    "RenderedPrompt",
    "UnknownOverrideFieldError",
    "load_card",
    "override_rate",
    "render",
    "render_file",
    "resolve",
    "schema_dir",
    "uses_raw_override",
    "validate_card",
]
