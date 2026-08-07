"""The preconditions on paid generation, and the phase gate.

Every test here asserts a REFUSAL. That is the point: nothing in this file can spend,
and these guards are what make that true rather than merely intended.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import yaml

from studio_ops.adapters.base import (
    AdapterNotBuiltError,
    BudgetExceededError,
    ExecutionMode,
    GenerationRequest,
    UnsupportedRequestError,
    get_adapter,
)
from studio_ops.adapters.openai_images import (
    FLOATING_ALIAS,
    PINNED_MODEL,
    OpenAIImageAdapter,
    PriceUnknownError,
    TermsNotVerifiedError,
)
from studio_ops.pipeline import phases


def req(tmp_path: Path) -> GenerationRequest:
    return GenerationRequest(
        prompt_card_id="PC-NG-EXP001-0001",
        modality="image",
        vendor="openai",
        model=PINNED_MODEL,
        rendered_prompt="a plain test subject",
        output_path=str(tmp_path / "out.png"),
    )


def enabled(**kwargs: Any) -> OpenAIImageAdapter:
    """An adapter with every precondition satisfied except the one under test."""
    defaults: dict[str, Any] = {
        "dry_run": False,
        "budget_usd": 10.0,
        "api_key": "test-key-not-real",
        "price_per_image_usd": 0.01,
        "terms_checked": "2026-08-07",
    }
    defaults.update(kwargs)
    return OpenAIImageAdapter(**defaults)


# ------------------------------------------------------- the four preconditions


def test_dry_run_default_refuses(tmp_path: Path) -> None:
    with pytest.raises(AdapterNotBuiltError, match="DRY_RUN"):
        OpenAIImageAdapter(api_key="k").generate(req(tmp_path))


def test_missing_api_key_refuses(tmp_path: Path) -> None:
    with pytest.raises(AdapterNotBuiltError, match="OPENAI_API_KEY"):
        enabled(api_key="").generate(req(tmp_path))


def test_unverified_terms_refuse(tmp_path: Path) -> None:
    """A studio generating before reading the terms has no answer when asked whether
    it may use what it generated."""
    with pytest.raises(TermsNotVerifiedError, match="terms have not been verified"):
        enabled(terms_checked="").generate(req(tmp_path))


def test_missing_price_refuses_and_will_not_guess(tmp_path: Path) -> None:
    """A guessed price yields a ceiling that bounds nothing while looking like one."""
    with pytest.raises(PriceUnknownError, match="will not guess"):
        enabled(price_per_image_usd=None).generate(req(tmp_path))


def test_no_ceiling_refuses_a_priced_run(tmp_path: Path) -> None:
    with pytest.raises(BudgetExceededError):
        enabled(budget_usd=0.0).generate(req(tmp_path))


def test_ceiling_is_enforced_before_any_call(tmp_path: Path) -> None:
    """Ten images at 0.05 against a 0.10 ceiling never reaches the wire."""
    adapter = enabled(budget_usd=0.10, price_per_image_usd=0.05)
    request = GenerationRequest(
        prompt_card_id="PC",
        modality="image",
        vendor="openai",
        model=PINNED_MODEL,
        rendered_prompt="x",
        parameters={"n": 10},
        output_path=str(tmp_path / "o.png"),
    )
    with pytest.raises(BudgetExceededError):
        adapter.generate(request)


# ------------------------------------------------------------- the pinned model


def test_floating_alias_is_refused(tmp_path: Path) -> None:
    """A continuity run needs the model to hold still.

    A floating alias can change underneath the experiment, and then every drift
    measurement becomes uninterpretable.
    """
    with pytest.raises(UnsupportedRequestError, match="floating alias"):
        enabled(model=FLOATING_ALIAS).generate(req(tmp_path))


def test_the_pinned_snapshot_is_not_the_alias() -> None:
    assert PINNED_MODEL != FLOATING_ALIAS
    assert PINNED_MODEL.startswith(FLOATING_ALIAS)


def test_wire_format_is_marked_unverified(tmp_path: Path) -> None:
    """The last guard. It refuses AFTER the others pass, so satisfying terms, price,
    key, and ceiling still does not produce a call from unverified code."""
    with pytest.raises(AdapterNotBuiltError, match="not been checked against current"):
        enabled().generate(req(tmp_path))


def test_openai_declares_api_mode_and_no_seed_determinism() -> None:
    caps = get_adapter("openai").capabilities()
    assert caps.execution_mode is ExecutionMode.API
    assert caps.spends_money is True
    # Recorded honestly: continuity here is held by reference images, not by seeds.
    assert caps.accepts_seed is False


# ------------------------------------------------------------------- the phases


def plan(tmp_path: Path, **over: Any) -> phases.RunPlan:
    data: dict[str, Any] = {
        "production": "EXP001",
        "active_phase": "A",
        "execution_mode": "api",
        "phases": [
            {
                "key": "A",
                "title": "Anchors",
                "approved": True,
                "allowed": [
                    "PC-NG-EXP001-0001",
                    "PC-NG-EXP001-0002",
                    "PC-NG-EXP001-0003",
                ],
            },
            {
                "key": "B",
                "title": "Diagnostics",
                "requires_approval_before": True,
                "approved": False,
                "allowed": ["SHT-NG-EXP001-0001"],
            },
        ],
    }
    data.update(over)
    path = tmp_path / "run_plan.yaml"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    return phases.load(path)


def test_phase_a_allows_only_the_three_anchors(tmp_path: Path) -> None:
    p = plan(tmp_path)
    p.check("PC-NG-EXP001-0001")
    with pytest.raises(phases.PhaseError, match="not authorised"):
        p.check("SHT-NG-EXP001-0002")


def test_budget_is_not_an_authorisation(tmp_path: Path) -> None:
    """The point of this module. A cheap unauthorised run is the likelier failure."""
    p = plan(tmp_path)
    with pytest.raises(phases.PhaseError, match="Remaining budget is not a reason"):
        p.check("SHT-NG-EXP001-0002")


def test_phase_b_is_blocked_until_approved(tmp_path: Path) -> None:
    p = plan(tmp_path, active_phase="B")
    with pytest.raises(phases.PhaseError, match="has not been approved"):
        p.check("SHT-NG-EXP001-0001")


def test_phase_b_runs_once_approved(tmp_path: Path) -> None:
    p = plan(
        tmp_path,
        active_phase="B",
        phases=[
            {
                "key": "B",
                "title": "Diagnostics",
                "requires_approval_before": True,
                "approved": True,
                "allowed": ["SHT-NG-EXP001-0001"],
            }
        ],
    )
    p.check("SHT-NG-EXP001-0001")


def test_modes_may_not_be_mixed_in_one_run(tmp_path: Path) -> None:
    """A difference between two shots could be the mechanism or the surface."""
    p = plan(tmp_path)
    with pytest.raises(phases.PhaseError, match="Mixing modes"):
        p.check("PC-NG-EXP001-0001", execution_mode="interactive")


def test_the_real_exp001_plan_authorises_only_phase_a() -> None:
    """Against the run plan actually committed to the repository."""
    from studio_ops.paths import find_repo_root

    root = find_repo_root()
    p = phases.load(
        root
        / "studios/african-history/lines/ng-nigeria/productions"
        / "EXP001_laboratory-scene/run_plan.yaml"
    )
    assert p.active_phase == "A"
    assert p.execution_mode == "api"
    assert p.model == PINNED_MODEL

    for card in ("PC-NG-EXP001-0001", "PC-NG-EXP001-0002", "PC-NG-EXP001-0003"):
        p.check(card)

    for blocked in ("SHT-NG-EXP001-0001", "SHT-NG-EXP001-0004", "SHT-NG-EXP001-0018"):
        with pytest.raises(phases.PhaseError):
            p.check(blocked)

    phase_c = p.phase("C")
    assert phase_c is not None
    # Phase C authorises nothing, and having budget left cannot reach it.
    assert phase_c.allowed == ()
    assert phase_c.approved is False
