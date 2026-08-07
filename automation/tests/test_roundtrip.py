"""The platform's acceptance test.

One question, asserted end to end:

    continuity record + shot record
        → prompt card
        → render
        → adapter
        → asset file on disk
        → manifest entry whose sha256 matches those bytes

If this passes, traceability is a property of the system. If it fails, every claim
about provenance elsewhere in this repository is aspiration.

These tests use the `local` adapter deliberately. It is deterministic, offline, and
free, which is what makes the round trip assertable at all — a vendor backend cannot
be asserted byte-for-byte, and this is the harness a vendor backend will be swapped
into.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import yaml

from studio_ops.adapters.base import BudgetExceededError, get_adapter
from studio_ops.config import Config
from studio_ops.paths import Layout, find_repo_root
from studio_ops.pipeline import generate, manifest, store

SCHEMAS = find_repo_root() / "standards" / "schemas"
LINE = "ng-nigeria"
PRODUCTION = "EXP001"


@pytest.fixture
def cfg(tmp_path: Path) -> Config:
    """A repository whose asset store is outside the working tree, as in production."""
    root = tmp_path / "repo"
    (root / "core").mkdir(parents=True)
    (root / "packs").mkdir()
    assets = tmp_path / "assets"
    assets.mkdir()
    import os

    os.environ["ASSET_STORE_LOCAL_PATH"] = str(assets)
    os.environ["ASSET_STORE_DRIVER"] = "local"
    return Config(root=root, layout=Layout(root=root))


def write_yaml(path: Path, data: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return path


# --------------------------------------------------------------------- fixtures
# Explicitly invented content. EXP-001 makes no historical claims, so neither does
# its test fixture: no period, no people, no place.


def continuity_location(root: Path) -> Path:
    return write_yaml(
        root / "continuity" / "CNL-NG-0001_workshop.yaml",
        {
            "id": "CNL-NG-0001",
            "type": "continuity_location",
            "line": LINE,
            "title": "Invented workshop interior",
            "status": "draft",
            "version": "0.1.0",
            "updated": "2026-08-07",
            "owners": ["visual-director"],
            "canonical_name": "Invented workshop interior",
            "era": {"display": "no period claimed — invented setting"},
            "lighting_language": {
                "time_of_day": "mid-morning",
                "primary_source": "a single high window",
                "direction": "raking from frame left",
                "quality": "hard-edged, dust in the beam",
            },
            "camera_language": {
                "movement_rules": "locked frames; movement only when a hand leads it",
            },
            "forbidden_objects": [
                {
                    "forbidden": "plastic",
                    "why": "invented pre-industrial setting",
                    "severity": "anachronism",
                },
                {"forbidden": "machine stitching", "why": "as above", "severity": "anachronism"},
            ],
        },
    )


def shot_record(root: Path, *, provenance_class: str = "interpretive") -> Path:
    return write_yaml(
        root / "03_storyboard" / "shots" / "SHT-NG-EXP001-0001.yaml",
        {
            "id": "SHT-NG-EXP001-0001",
            "type": "shot",
            "line": LINE,
            "title": "Hands at the bench",
            "status": "draft",
            "version": "0.1.0",
            "updated": "2026-08-07",
            "owners": ["visual-director"],
            "episode": "S01E01",  # schema field; the production code lives in the ID
            "sequence": "SEQ-NG-EXP001-001",
            "order": 1,
            "description": "Two hands working a length of cord at a bench.",
            "provenance_class": provenance_class,
        },
    )


def prompt_card(root: Path) -> Path:
    return write_yaml(
        root / "04_prompts" / "PC-NG-EXP001-0001_hands.prompt.yaml",
        {
            "id": "PC-NG-EXP001-0001",
            "type": "prompt_card",
            "line": LINE,
            "title": "Hands at the bench",
            "status": "draft",
            "version": "0.1.0",
            "updated": "2026-08-07",
            "owners": ["visual-director"],
            "modality": "image",
            "tool": {"vendor": "local", "model": "local-deterministic"},
            "target": {
                "provenance_class": "interpretive",
                "intent": "Establish that the work is close, manual, and unhurried.",
            },
            "prompt": {
                "subject": "two hands working a length of twisted cord",
                "setting": "a plank bench under a high window",
                "period_markers": ["hand-twisted cord", "unplaned timber", "iron tool"],
            },
        },
    )


def build_production(cfg: Config) -> dict[str, Path]:
    root = cfg.root / "productions" / "EXP001"
    paths = {
        "continuity": continuity_location(root),
        "shot": shot_record(root),
        "card": prompt_card(root),
        "manifest": root / "manifest.yaml",
        "work": root / "05_assets" / "stills",
    }
    manifest.save(
        paths["manifest"],
        manifest.create(line=LINE, episode=PRODUCTION, updated="2026-08-07"),
        schema_dir=SCHEMAS,
    )
    return paths


def run(cfg: Config, paths: dict[str, Path], **kwargs: Any) -> generate.RoundTrip:
    return generate.generate_shot(
        cfg,
        shot_path=paths["shot"],
        card_path=paths["card"],
        manifest_path=paths["manifest"],
        work_dir=paths["work"],
        continuity_paths=[paths["continuity"]],
        adapter_name="local",
        seed=20260807,
        dry_run=False,
        schema_dir=SCHEMAS,
        **kwargs,
    )


# ---------------------------------------------------------------- the acceptance


def test_the_round_trip_closes(cfg: Config) -> None:
    """THE acceptance criterion. Everything else in this file is a detail of it."""
    paths = build_production(cfg)

    trip = run(cfg, paths)

    # A real file, with real bytes.
    stored = store.resolve(store.root(cfg), trip.entry["store_path"])
    assert stored.is_file()
    assert stored.stat().st_size > 0
    assert stored.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"

    # The record and the bytes agree. This is the whole guarantee.
    assert trip.hash_matches_disk(store.root(cfg))
    assert trip.entry["sha256"] == store.sha256_file(stored)

    # The lineage is complete and points back at real records.
    gen = trip.entry["generation"]
    assert gen["prompt_card"] == "PC-NG-EXP001-0001"
    assert gen["seed"] == 20260807
    assert gen["tool"]["vendor"] == "local"
    assert gen["generated_at"] and gen["generated_by"]
    assert trip.entry["used_in_shots"] == ["SHT-NG-EXP001-0001"]
    assert trip.entry["origin"] == "generated"


def test_the_manifest_on_disk_validates(cfg: Config) -> None:
    """A round trip must leave the manifest schema-valid, not merely written."""
    paths = build_production(cfg)
    run(cfg, paths)

    loaded = manifest.load(paths["manifest"])
    assert manifest.validate(loaded, schema_dir=SCHEMAS) == []
    assert len(loaded["assets"]) == 1


def test_continuity_reaches_the_prompt(cfg: Config) -> None:
    """The continuity record must actually condition the render.

    If it does not, the registry is decoration and drift is unmanaged — which is the
    single failure the whole continuity system exists to prevent.
    """
    paths = build_production(cfg)

    trip = run(cfg, paths)

    assert "raking from frame left" in trip.rendered.prompt
    # forbidden_objects become negatives, minus anything culturally prohibited.
    assert "plastic" in trip.rendered.negative
    assert "machine stitching" in trip.rendered.negative
    # period markers survive; they do the most work against generic output.
    assert "hand-twisted cord" in trip.rendered.prompt


def test_the_same_shot_twice_is_byte_identical(cfg: Config) -> None:
    """Determinism is what makes the round trip assertable and the fixture reusable."""
    a = build_production(cfg)
    first = run(cfg, a)

    # A second production, same inputs, same seed.
    import os

    second_cfg = Config(root=cfg.root, layout=cfg.layout)
    b = a | {"manifest": cfg.root / "productions" / "EXP001" / "manifest2.yaml"}
    manifest.save(
        b["manifest"],
        manifest.create(line=LINE, episode=PRODUCTION, updated="2026-08-07"),
        schema_dir=SCHEMAS,
    )
    os.environ["ASSET_STORE_LOCAL_PATH"] = str(store.root(cfg))
    second = run(second_cfg, b)

    assert first.result.sha256 == second.result.sha256


# ------------------------------------------------------------------- refusals


def test_dry_run_is_the_default(cfg: Config) -> None:
    """A missing argument must yield the refusing state, never the spending one."""
    paths = build_production(cfg)

    with pytest.raises(Exception) as exc:
        generate.generate_shot(
            cfg,
            shot_path=paths["shot"],
            card_path=paths["card"],
            manifest_path=paths["manifest"],
            work_dir=paths["work"],
            continuity_paths=[paths["continuity"]],
            adapter_name="local",
            schema_dir=SCHEMAS,
        )
    assert "dry" in str(exc.value).lower() or "DRY" in str(exc.value)


def test_no_style_block_refuses(cfg: Config) -> None:
    """Rendering with nothing inherited yields a plausible image with no lineage."""
    paths = build_production(cfg)

    with pytest.raises(generate.RoundTripError, match="no style block"):
        generate.generate_shot(
            cfg,
            shot_path=paths["shot"],
            card_path=paths["card"],
            manifest_path=paths["manifest"],
            work_dir=paths["work"],
            adapter_name="local",
            dry_run=False,
            schema_dir=SCHEMAS,
        )


def test_reconstruction_without_evidence_refuses(cfg: Config) -> None:
    """A reconstruction asserts something. Without an evidence basis it may not exist.

    Note what this proves for EXP-001: because the fixture carries no claims, a shot
    classed `reconstruction` cannot be generated at all. The refusal is what keeps a
    no-claims laboratory production honest.
    """
    paths = build_production(cfg)
    shot_record(cfg.root / "productions" / "EXP001", provenance_class="reconstruction")

    with pytest.raises(Exception) as exc:
        run(cfg, paths)
    assert "evidence" in str(exc.value).lower()


def test_a_generated_asset_can_never_be_archival(cfg: Config) -> None:
    """The prohibition that matters most, enforced in code and not only in schema."""
    paths = build_production(cfg)
    shot_record(cfg.root / "productions" / "EXP001", provenance_class="archival")

    with pytest.raises(manifest.ProvenanceError, match="archival"):
        run(cfg, paths)


def test_nothing_is_stored_when_the_record_is_refused(cfg: Config) -> None:
    """The ordering guarantee: no bytes land unless the entry describing them is valid.

    This is the property that makes 'an asset without a manifest entry cannot be
    conformed' true rather than merely intended.
    """
    paths = build_production(cfg)
    shot_record(cfg.root / "productions" / "EXP001", provenance_class="archival")

    with pytest.raises(manifest.ProvenanceError):
        run(cfg, paths)

    store_root = store.root(cfg)
    stored_files = [p for p in store_root.rglob("*") if p.is_file()]
    assert stored_files == [], f"bytes landed despite a refused record: {stored_files}"
    assert manifest.load(paths["manifest"])["assets"] == []


def test_budget_guard_still_refuses_a_priced_run(cfg: Config) -> None:
    """A free backend must not have widened the guard for paid ones."""
    adapter_cls = get_adapter("local")
    adapter = adapter_cls(dry_run=False, budget_usd=0.0)

    request = generate.request_from_render(
        __import__("studio_ops.promptlib.registry", fromlist=["RenderedPrompt"]).RenderedPrompt(
            card_id="PC-NG-EXP001-0001",
            modality="image",
            vendor="local",
            model="local-deterministic",
            prompt="anything",
            parameters={},
        ),
        output_path=cfg.root / "out.png",
        seed=1,
        estimated_cost_usd=5.0,
    )

    with pytest.raises(BudgetExceededError):
        adapter.generate(request)


def test_schemas_are_the_real_ones() -> None:
    """Guard against the test suite quietly validating against a stale copy."""
    assert (SCHEMAS / "asset_manifest.schema.json").is_file()
    schema = json.loads((SCHEMAS / "asset_manifest.schema.json").read_text(encoding="utf-8"))
    assert schema["properties"]["type"]["const"] == "asset_manifest"
