"""Tests for the prompt renderer.

The claim under test is ADR 0003's: that a prompt is better held as a record than as
a string, because the record can inherit a style, be reviewed field by field, and be
re-pointed at another vendor. Each of those is asserted here rather than assumed —
in particular that one card really does render differently for two vendors, which is
the entire justification for the abstraction.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import yaml

from studio_ops.paths import Layout, find_repo_root
from studio_ops.promptlib import registry, render

SCHEMAS = Layout(root=find_repo_root(Path(__file__))).schemas


def make_card(**overrides: Any) -> dict[str, Any]:
    """A minimal card that validates. `interpretive` avoids the evidence_basis rule."""
    card: dict[str, Any] = {
        "id": "PC-NG-S01E01-0037",
        "type": "prompt_card",
        "line": "ng-metalwork",
        "title": "Shaft furnace at first light",
        "status": "draft",
        "version": "0.1.0",
        "updated": "2026-08-07",
        "owners": ["visual-director"],
        "modality": "image",
        "tool": {"vendor": "midjourney", "model": "v6"},
        "target": {
            "provenance_class": "interpretive",
            "intent": "Establish that the works are larger than the viewer expects.",
        },
        "prompt": {
            "subject": "Three metalworkers at a shaft furnace",
            "action": "Working charcoal into the tuyère",
            "setting": "A walled compound on laterite ground",
            "period_markers": ["mud-brick coursing", "indigo-dyed cotton wrapper"],
            "camera": "35mm, chest height, static",
            "light": "Low side light, first hour after sunrise",
        },
        "parameters": {},
    }
    card.update(overrides)
    return card


STYLE_BLOCK: dict[str, Any] = {
    "id": "STY-NG-0001",
    "palette": "Ochre, charcoal, unbleached cotton",
    "texture": "16mm grain, no digital sharpening",
    "camera": "50mm, eye height, static",
    "negative": ["oversaturated", "lens flare"],
}


# ------------------------------------------------------------- style inheritance


def test_style_block_fills_fields_the_card_omits() -> None:
    resolved = render.resolve(make_card(), STYLE_BLOCK)

    assert resolved["prompt"]["palette"] == "Ochre, charcoal, unbleached cotton"
    assert resolved["prompt"]["texture"] == "16mm grain, no digital sharpening"


def test_card_field_beats_inherited_field() -> None:
    resolved = render.resolve(make_card(), STYLE_BLOCK)

    assert resolved["prompt"]["camera"] == "35mm, chest height, static"


def test_style_block_may_nest_its_prompt_fields() -> None:
    resolved = render.resolve(make_card(), {"id": "STY-NG-0001", "prompt": {"mood": "Unhurried"}})

    assert resolved["prompt"]["mood"] == "Unhurried"


def test_style_block_identity_keys_are_not_treated_as_prompt_fields() -> None:
    resolved = render.resolve(make_card(), STYLE_BLOCK)

    assert "id" not in resolved["prompt"]


def test_negatives_merge_line_then_shot() -> None:
    """negative_library.md § Inheritance: line → sequence → card, not replacement."""
    card = make_card()
    card["prompt"]["negative"] = ["corrugated metal roofing", "oversaturated"]

    resolved = render.resolve(card, STYLE_BLOCK)

    # Inherited first, shot-specific appended, duplicates collapsed.
    assert resolved["prompt"]["negative"] == [
        "oversaturated",
        "lens flare",
        "corrugated metal roofing",
    ]


def test_the_card_itself_is_not_mutated() -> None:
    card = make_card()
    render.resolve(card, STYLE_BLOCK)

    assert "palette" not in card["prompt"]


# -------------------------------------------------------------------- overrides


def test_override_without_a_reason_is_rejected() -> None:
    card = make_card()
    card["inheritance"] = {"overrides": [{"field": "palette", "value": "Cool blue"}]}

    with pytest.raises(render.OverrideWithoutReasonError):
        render.resolve(card, STYLE_BLOCK)


def test_override_with_a_blank_reason_is_rejected() -> None:
    card = make_card()
    card["inheritance"] = {"overrides": [{"field": "palette", "value": "Cool blue", "reason": " "}]}

    with pytest.raises(render.OverrideWithoutReasonError):
        render.resolve(card, STYLE_BLOCK)


def test_override_with_a_reason_beats_both_style_and_card() -> None:
    card = make_card()
    card["prompt"]["palette"] = "Ochre and charcoal"
    card["inheritance"] = {
        "overrides": [
            {
                "field": "palette",
                "value": "Cold blue, desaturated",
                "reason": "Night interior; the ochre block reads as firelight here.",
            }
        ]
    }

    resolved = render.resolve(card, STYLE_BLOCK)

    assert resolved["prompt"]["palette"] == "Cold blue, desaturated"


def test_override_may_target_a_vendor_parameter() -> None:
    card = make_card()
    card["inheritance"] = {
        "overrides": [
            {"field": "parameters.stylize", "value": "50", "reason": "House look off for QC."}
        ]
    }

    assert render.resolve(card, {})["parameters"]["stylize"] == "50"


def test_override_naming_an_unappliable_field_is_rejected() -> None:
    """An override nobody applies is invisible drift — the failure it exists to stop."""
    card = make_card()
    card["inheritance"] = {
        "overrides": [{"field": "wardrobe", "value": "Plain wrapper", "reason": "Continuity."}]
    }

    with pytest.raises(render.UnknownOverrideFieldError):
        render.resolve(card, {})


def test_render_checks_overrides_even_with_no_style_block() -> None:
    card = make_card()
    card["inheritance"] = {"overrides": [{"field": "mood", "value": "Tense"}]}

    with pytest.raises(render.OverrideWithoutReasonError):
        render.render(card)


# -------------------------------------------------------------------- rendering


def test_period_markers_appear_in_the_rendered_string_for_every_vendor() -> None:
    """The field that does the most work against generic pan-historical output."""
    card = make_card()

    for vendor in ("midjourney", "flux"):
        rendered = render.render(card, vendor)
        assert "mud-brick coursing" in rendered.prompt
        assert "indigo-dyed cotton wrapper" in rendered.prompt


def test_generic_renderer_labels_the_technical_fields() -> None:
    rendered = render.render(make_card(), "flux", style_block=STYLE_BLOCK)

    assert rendered.renderer == registry.GENERIC
    assert rendered.prompt.startswith("Three metalworkers at a shaft furnace.")
    assert "Camera: 35mm, chest height, static" in rendered.prompt
    assert "Period detail: mud-brick coursing, indigo-dyed cotton wrapper" in rendered.prompt


def test_negatives_render_as_an_avoid_clause_for_the_generic_target() -> None:
    card = make_card()
    card["prompt"]["negative"] = ["corrugated metal roofing", "wristwatch"]

    rendered = render.render(card, "flux")

    assert "Avoid: corrugated metal roofing, wristwatch." in rendered.prompt
    assert "--no" not in rendered.prompt
    assert rendered.negative == ("corrugated metal roofing", "wristwatch")


def test_negatives_render_as_a_no_flag_for_midjourney() -> None:
    card = make_card()
    card["prompt"]["negative"] = ["corrugated metal roofing", "wristwatch"]

    rendered = render.render(card, "midjourney")

    assert "--no corrugated metal roofing, wristwatch" in rendered.prompt
    assert "Avoid:" not in rendered.prompt


def test_parameters_are_returned_as_a_dict_not_only_as_syntax() -> None:
    """The manifest records what was sent; a string is not a record."""
    card = make_card()
    card["parameters"] = {"ar": "16:9", "tile": False, "seed_lock": True}

    rendered = render.render(card, "midjourney")

    assert rendered.parameters == {"ar": "16:9", "tile": False, "seed_lock": True}
    assert "--ar 16:9" in rendered.prompt
    assert "--seed_lock" in rendered.prompt  # a true flag needs no value
    assert "--tile" not in rendered.prompt  # a false one is not sent


def test_the_same_card_renders_differently_for_two_vendors() -> None:
    """The whole point of the abstraction. If this ever passes trivially, it is dead."""
    card = make_card()
    card["prompt"]["negative"] = ["oversaturated"]

    mj = render.render(card, "midjourney")
    generic = render.render(card, "flux")

    assert mj.prompt != generic.prompt
    # Order is a property of the vendor, not of the card.
    assert mj.order != generic.order
    assert mj.order[1] == "period_markers"  # midjourney drops the tail; markers lead
    assert generic.order[1] == "action"
    # Negatives land in the vendor's own channel.
    assert "--no oversaturated" in mj.prompt
    assert "Avoid: oversaturated" in generic.prompt
    assert mj.renderer == "midjourney"
    assert generic.renderer == registry.GENERIC


def test_targeting_another_vendor_drops_the_cards_model() -> None:
    """`midjourney/v6` travelling into a Flux request would be a provenance lie."""
    card = make_card()

    assert render.render(card, "midjourney").model == "v6"
    assert render.render(card, "flux").model == ""


def test_vendor_defaults_to_the_cards_own_tool() -> None:
    assert render.render(make_card()).vendor == "midjourney"


def test_unregistered_vendor_falls_back_to_generic_rather_than_refusing() -> None:
    rendered = render.render(make_card(), "some-vendor-nobody-has-written-yet")

    assert rendered.renderer == registry.GENERIC
    assert rendered.vendor == "some-vendor-nobody-has-written-yet"
    assert rendered.prompt


def test_empty_prompt_fields_are_omitted_not_rendered_blank() -> None:
    card = make_card()
    card["prompt"]["mood"] = ""

    assert "mood" not in render.render(card, "flux").order


# ----------------------------------------------------------------- raw override


def test_raw_override_bypasses_assembly_and_is_flagged() -> None:
    card = make_card()
    card["prompt"]["raw_override"] = "verbatim string the renderer cannot express"
    card["parameters"] = {"ar": "16:9"}
    card["notes"] = "Vendor syntax not expressible structurally."

    rendered = render.render(card, "midjourney")

    assert rendered.raw_override is True
    assert rendered.prompt == "verbatim string the renderer cannot express"
    # Nothing from the structured fields leaked in.
    assert "mud-brick coursing" not in rendered.prompt
    assert "--ar" not in rendered.prompt
    assert rendered.order == ()
    # The record still travels: the escape hatch is about syntax, not about the card.
    assert rendered.parameters == {"ar": "16:9"}


def test_raw_override_bypasses_every_vendor_identically() -> None:
    card = make_card()
    card["prompt"]["raw_override"] = "verbatim"

    assert render.render(card, "midjourney").prompt == render.render(card, "flux").prompt


# --------------------------------------------------- the ADR 0003 failure signal


def test_override_rate_counts_only_raw_overrides() -> None:
    plain = make_card()
    raw = make_card()
    raw["prompt"]["raw_override"] = "verbatim"

    assert render.override_rate([plain, plain, plain, raw]) == 0.25
    assert render.override_rate([raw]) == 1.0
    assert render.override_rate([plain]) == 0.0


def test_override_rate_of_no_cards_is_zero_not_an_error() -> None:
    assert render.override_rate([]) == 0.0


def test_override_rate_ignores_a_blank_raw_override() -> None:
    card = make_card()
    card["prompt"]["raw_override"] = "   "

    assert render.override_rate([card]) == 0.0


def test_style_overrides_are_not_the_failure_signal() -> None:
    """An `inheritance.overrides` entry is normal practice; `raw_override` is not."""
    card = make_card()
    card["inheritance"] = {
        "overrides": [{"field": "palette", "value": "Cold blue", "reason": "Night interior."}]
    }

    assert render.override_rate([card]) == 0.0


# ------------------------------------------------------------ loading from disk


def write_card(tmp_path: Path, card: dict[str, Any]) -> Path:
    path = tmp_path / "PC-NG-S01E01-0037_furnace.prompt.yaml"
    path.write_text(yaml.safe_dump(card, sort_keys=False), encoding="utf-8")
    return path


def test_a_valid_card_loads_and_renders(tmp_path: Path) -> None:
    path = write_card(tmp_path, make_card())

    rendered = render.render_file(path, schemas=SCHEMAS)

    assert rendered.card_id == "PC-NG-S01E01-0037"
    assert "shaft furnace" in rendered.prompt


def test_an_invalid_card_raises_rather_than_rendering(tmp_path: Path) -> None:
    card = make_card()
    card["status"] = "final"  # not in the recordStatus enum
    path = write_card(tmp_path, card)

    with pytest.raises(render.CardValidationError) as caught:
        render.render_file(path, schemas=SCHEMAS)

    assert any("status" in error for error in caught.value.errors)


def test_a_reconstruction_without_an_evidence_basis_does_not_render(tmp_path: Path) -> None:
    """The schema's own conditional rule. A picture asserting a past needs its record."""
    card = make_card()
    card["target"]["provenance_class"] = "reconstruction"
    path = write_card(tmp_path, card)

    with pytest.raises(render.CardValidationError):
        render.render_file(path, schemas=SCHEMAS)


def test_malformed_yaml_raises_a_card_error_not_a_traceback(tmp_path: Path) -> None:
    path = tmp_path / "broken.prompt.yaml"
    path.write_text("id: PC-NG-S01E01-0037\n  bad: [\n", encoding="utf-8")

    with pytest.raises(render.CardValidationError):
        render.load_card(path, schemas=SCHEMAS)


def test_schema_validation_alone_does_not_catch_an_unfilled_template() -> None:
    """A finding, pinned here so it is not rediscovered.

    The shipped template VALIDATES. Every placeholder is a free-form string and the
    schema has no way to reject `TBD`, so a card can be well-formed and still say
    nothing. Schema validation is necessary and not sufficient; catching placeholder
    text belongs to the prompts gate, not to the renderer.

    What the renderer does catch is the template's placeholder override, which names
    a field that cannot be applied — and refusing that is the renderer's own job.
    """
    template = find_repo_root(Path(__file__)) / (
        "templates/production/04_prompts/_TEMPLATE_card.prompt.yaml"
    )
    if not template.is_file():  # pragma: no cover - a moved template is another gate's job
        pytest.skip("template not present")

    card = render.load_card(template, schemas=SCHEMAS)  # does not raise — that is the finding

    with pytest.raises(render.UnknownOverrideFieldError):
        render.render(card)


# -------------------------------------------------------------------- registry


def test_registry_lists_what_it_can_target() -> None:
    pairs = registry.registered()

    assert (registry.ANY_MODALITY, registry.GENERIC) in pairs
    assert ("image", "midjourney") in pairs


def test_registering_over_an_existing_pair_is_refused() -> None:
    with pytest.raises(registry.DuplicateRendererError):
        registry.register_renderer("image", "midjourney", registry.render_generic)
