"""Tests for the provenance manifest and the local asset store.

These assert the refusals, not the happy path alone. A manifest module that can
record an asset has proved very little; the guarantee is in what it declines to
write — a duplicate ID, a reconstruction with no evidence, a generated asset
dressed as archival, an invalid file.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

import pytest

from studio_ops.adapters.base import GenerationRequest, GenerationResult
from studio_ops.config import Config
from studio_ops.paths import Layout
from studio_ops.pipeline import manifest as mf
from studio_ops.pipeline import store

REPO = Path(__file__).resolve().parents[2]
SCHEMAS = REPO / "standards" / "schemas"

LINE = "ng-nigeria"
EPISODE = "S01E01"
SHOT = "SHT-NG-S01E01-0001"
CARD = "PC-NG-S01E01-0037"

PAYLOAD = b"not really a PNG, but it hashes like one"
PAYLOAD_SHA = hashlib.sha256(PAYLOAD).hexdigest()


# ------------------------------------------------------------------- fixtures


@pytest.fixture
def cfg(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Config:
    """A repository and a store root that is a sibling of it, never a child."""
    root = tmp_path / "repo"
    (root / "core").mkdir(parents=True)
    (root / "packs").mkdir()
    monkeypatch.setenv("ASSET_STORE_DRIVER", "local")
    monkeypatch.setenv("ASSET_STORE_LOCAL_PATH", str(tmp_path / "assets"))
    return Config(root=root, layout=Layout(root=root))


def make_result(asset_path: Path, *, sha256: str = PAYLOAD_SHA) -> GenerationResult:
    return GenerationResult(
        request=GenerationRequest(
            prompt_card_id=CARD,
            modality="image",
            vendor="flux",
            model="flux-pro",
            rendered_prompt="a walled city at dawn",
            parameters={"aspect_ratio": "16:9"},
            inputs=["STA-NG-0004"],
            seed=99,
            estimated_cost_usd=0.04,
        ),
        asset_path=str(asset_path),
        sha256=sha256,
        seed=99,
        model_version="1.1",
        generated_at="2026-08-07T10:15:00Z",
        generated_by="e.ekakitie",
        cost_usd=0.04,
    )


def new_manifest() -> dict[str, Any]:
    return mf.create(line=LINE, episode=EPISODE, updated="2026-08-07")


def generated_entry(**kwargs: Any) -> dict[str, Any]:
    defaults: dict[str, Any] = {
        "provenance_class": "reconstruction",
        "used_in_shots": [SHOT],
        "evidence_basis": ["CLM-NG-0117", "SRC-NG-0042"],
    }
    defaults.update(kwargs)
    return mf.entry_from_generation(make_result(Path("out/shot.png")), **defaults)


# ------------------------------------------------------------------ round trip


def test_round_trip_preserves_the_manifest(tmp_path: Path) -> None:
    m = new_manifest()
    entry = generated_entry()
    entry["asset_id"] = mf.next_asset_id(m)
    mf.add(m, entry)

    path = tmp_path / "manifest.yaml"
    mf.save(path, m, schema_dir=SCHEMAS)

    assert mf.load(path) == m


def test_created_manifest_is_valid_and_empty() -> None:
    """A new production needs a manifest before it has assets, not after."""
    m = new_manifest()

    assert mf.validate(m, schema_dir=SCHEMAS) == []
    assert m["assets"] == []


def test_next_asset_id_allocates_in_sequence() -> None:
    m = new_manifest()
    first = mf.next_asset_id(m)
    entry = generated_entry()
    entry["asset_id"] = first
    mf.add(m, entry)

    assert first == "AST-NG-S01E01-0001"
    assert mf.next_asset_id(m) == "AST-NG-S01E01-0002"


# ---------------------------------------------------------- the adapter seam


def test_entry_from_generation_is_schema_valid() -> None:
    """Validated against the real schema, not a paraphrase of it."""
    m = new_manifest()
    mf.add(m, generated_entry())

    assert mf.validate(m, schema_dir=SCHEMAS) == []


def test_entry_from_generation_carries_the_provenance() -> None:
    entry = generated_entry()

    assert entry["origin"] == "generated"
    assert entry["generation"]["tool"] == {
        "vendor": "flux",
        "model": "flux-pro",
        "version": "1.1",
    }
    assert entry["generation"]["prompt_card"] == CARD
    assert entry["generation"]["seed"] == 99
    assert entry["sha256"] == PAYLOAD_SHA
    # reconstruction always carries an in-frame mark; it is recorded, not inferred.
    assert entry["label"] == {"required": True, "applied": False}


def test_entry_omits_store_path_until_the_bytes_land() -> None:
    """The adapter knows where it wrote a file; it does not know the store."""
    entry = generated_entry()

    assert "store_path" not in entry
    assert "bytes" not in entry


def test_reconstruction_without_evidence_basis_raises() -> None:
    with pytest.raises(mf.ProvenanceError, match="evidence_basis"):
        generated_entry(evidence_basis=None)


def test_generated_archival_raises() -> None:
    """The one combination with no reviewer and no deadline that permits it."""
    with pytest.raises(mf.ProvenanceError, match="archival"):
        generated_entry(provenance_class="archival", evidence_basis=None)


def test_add_also_refuses_generated_archival() -> None:
    """Enforced twice: the schema is only checked on demand."""
    entry = generated_entry(provenance_class="interpretive", evidence_basis=None)
    entry["provenance_class"] = "archival"

    with pytest.raises(mf.ProvenanceError, match="archival"):
        mf.add(new_manifest(), entry)


def test_add_refuses_generated_asset_with_no_generation_block() -> None:
    entry = generated_entry()
    del entry["generation"]

    with pytest.raises(mf.ProvenanceError, match="generation"):
        mf.add(new_manifest(), entry)


def test_add_refuses_acquired_asset_with_no_acquisition_block() -> None:
    entry = generated_entry(provenance_class="artefact", evidence_basis=None)
    del entry["generation"]
    entry["origin"] = "licensed"

    with pytest.raises(mf.ProvenanceError, match="acquisition"):
        mf.add(new_manifest(), entry)


def test_duplicate_asset_id_raises() -> None:
    m = new_manifest()
    entry = generated_entry()
    mf.add(m, entry)

    with pytest.raises(mf.ProvenanceError, match="already in this manifest"):
        mf.add(m, entry)


def test_add_refuses_a_frozen_manifest() -> None:
    m = new_manifest()
    entry = generated_entry()
    entry["store_path"] = "x/y.png"
    mf.add(m, entry)
    mf.freeze(m)

    second = generated_entry()
    second["asset_id"] = "AST-NG-S01E01-0002"
    with pytest.raises(mf.ProvenanceError, match="frozen"):
        mf.add(m, second)


def test_unmapped_modality_raises() -> None:
    result = make_result(Path("out/notes.txt"))
    text = GenerationResult(
        request=GenerationRequest(
            prompt_card_id=CARD,
            modality="text",
            vendor="anthropic",
            model="claude",
            rendered_prompt="summarise",
        ),
        asset_path=result.asset_path,
        sha256=PAYLOAD_SHA,
        seed=1,
        model_version="1",
        generated_at="2026-08-07T10:15:00Z",
        generated_by="e.ekakitie",
        cost_usd=0.0,
    )

    with pytest.raises(mf.ProvenanceError, match="media_type"):
        mf.entry_from_generation(text, provenance_class="graphic", used_in_shots=[SHOT])


# ------------------------------------------------------------------- writing


def test_invalid_manifest_is_not_written(tmp_path: Path) -> None:
    m = new_manifest()
    m["version"] = "one"  # not semver
    path = tmp_path / "manifest.yaml"

    with pytest.raises(mf.ManifestInvalidError):
        mf.save(path, m, schema_dir=SCHEMAS)

    assert not path.exists()


def test_save_does_not_truncate_a_good_manifest_with_a_bad_one(tmp_path: Path) -> None:
    path = tmp_path / "manifest.yaml"
    good = new_manifest()
    mf.save(path, good, schema_dir=SCHEMAS)

    bad = new_manifest()
    bad["episode"] = "nonsense"
    with pytest.raises(mf.ManifestInvalidError):
        mf.save(path, bad, schema_dir=SCHEMAS)

    assert mf.load(path) == good


def test_a_laboratory_production_can_hold_a_manifest(tmp_path: Path) -> None:
    """EXP-001 needs a manifest before it has a single frame.

    Regression: `episode` was typed as the strict `episodeCode` (`S\\d{2}E\\d{2}`)
    while `assetId`, `shotId`, and `promptCardId` all admitted `EXP\\d{3}`, so a
    laboratory manifest could hold valid asset IDs inside a production code that
    was not — and every save was refused.
    """
    path = tmp_path / "manifest.yaml"
    m = mf.create(line=LINE, episode="EXP001", updated="2026-08-07")

    entry = mf.entry_from_generation(
        make_result(Path("out/shot.png")),
        provenance_class="interpretive",
        used_in_shots=["SHT-NG-EXP001-0001"],
    )
    entry["asset_id"] = mf.next_asset_id(m)
    mf.add(m, entry)
    mf.save(path, m, schema_dir=SCHEMAS)

    assert entry["asset_id"] == "AST-NG-EXP001-0001"
    assert mf.load(path) == m


# --------------------------------------------------------------------- store


def test_put_then_verify_passes(cfg: Config) -> None:
    stored = store.put(cfg, PAYLOAD, relative_path=f"{LINE}/productions/{EPISODE}/generated/a.png")

    assert stored.sha256 == PAYLOAD_SHA
    assert stored.bytes == len(PAYLOAD)
    assert stored.created
    assert store.verify(cfg, {"asset_id": "AST-NG-S01E01-0001", **_ref(stored)})


def test_verify_fails_on_a_corrupted_file(cfg: Config) -> None:
    stored = store.put(cfg, PAYLOAD, relative_path="a/b.png")
    stored.path.write_bytes(PAYLOAD + b"corruption")

    entry = {"asset_id": "AST-NG-S01E01-0001", **_ref(stored)}
    assert not store.verify(cfg, entry)

    finding = store.check(store.root(cfg), entry)
    assert finding is not None
    assert "INTEGRITY FAILURE" in finding


def test_verify_fails_when_the_file_is_gone(cfg: Config) -> None:
    stored = store.put(cfg, PAYLOAD, relative_path="a/b.png")
    stored.path.unlink()

    assert not store.verify(cfg, {"asset_id": "AST-NG-S01E01-0001", **_ref(stored)})


def test_put_is_idempotent_for_identical_bytes(cfg: Config) -> None:
    first = store.put(cfg, PAYLOAD, relative_path="a/b.png")
    second = store.put(cfg, PAYLOAD, relative_path="a/b.png")

    assert first.sha256 == second.sha256
    assert not second.created


def test_put_refuses_to_overwrite_different_bytes(cfg: Config) -> None:
    store.put(cfg, PAYLOAD, relative_path="a/b.png")

    with pytest.raises(store.StoreCollisionError):
        store.put(cfg, PAYLOAD + b"v2", relative_path="a/b.png")


def test_put_refuses_a_path_escaping_the_store(cfg: Config) -> None:
    with pytest.raises(store.StoreConfigError):
        store.put(cfg, PAYLOAD, relative_path="../outside.png")


def test_unbuilt_driver_refuses(cfg: Config, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ASSET_STORE_DRIVER", "s3")

    with pytest.raises(store.StoreDriverNotBuiltError):
        store.root(cfg)


def test_store_root_refuses_to_sit_inside_the_git_worktree(
    cfg: Config, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Media inside the working tree gets committed by accident exactly once."""
    (cfg.root / ".git").mkdir()
    monkeypatch.setenv("ASSET_STORE_LOCAL_PATH", "assets")

    with pytest.raises(store.StoreConfigError, match="working tree"):
        store.root(cfg)


def _ref(stored: store.StoredAsset) -> dict[str, Any]:
    return {"store_path": stored.store_path, "sha256": stored.sha256}


# -------------------------------------------------------------------- ingest


def test_ingest_stores_the_bytes_and_records_them(cfg: Config, tmp_path: Path) -> None:
    src = tmp_path / "shot.png"
    src.write_bytes(PAYLOAD)
    path = cfg.root / "manifest.yaml"
    mf.save(path, new_manifest(), schema_dir=SCHEMAS)

    entry = mf.ingest_generation(
        cfg,
        path,
        make_result(src),
        provenance_class="reconstruction",
        used_in_shots=[SHOT],
        evidence_basis=["CLM-NG-0117"],
        schema_dir=SCHEMAS,
    )

    saved = mf.load(path)
    assert saved["assets"][0]["asset_id"] == "AST-NG-S01E01-0001"
    assert entry["bytes"] == len(PAYLOAD)
    assert mf.verify(saved, store.root(cfg)) == []


def test_ingest_refuses_when_the_bytes_contradict_the_result(cfg: Config, tmp_path: Path) -> None:
    """The record and the bytes disagree before either is stored. Store neither."""
    src = tmp_path / "shot.png"
    src.write_bytes(b"different bytes entirely")
    path = cfg.root / "manifest.yaml"
    mf.save(path, new_manifest(), schema_dir=SCHEMAS)

    with pytest.raises(mf.ProvenanceError, match="hashes to"):
        mf.ingest_generation(
            cfg,
            path,
            make_result(src),
            provenance_class="interpretive",
            used_in_shots=[SHOT],
            schema_dir=SCHEMAS,
        )

    assert mf.load(path)["assets"] == []
    assert not list(store.root(cfg).rglob("*.png"))


# ------------------------------------------------------------ verify / freeze


def test_verify_reports_every_broken_reference(cfg: Config, tmp_path: Path) -> None:
    src = tmp_path / "shot.png"
    src.write_bytes(PAYLOAD)
    path = cfg.root / "manifest.yaml"
    mf.save(path, new_manifest(), schema_dir=SCHEMAS)
    mf.ingest_generation(
        cfg,
        path,
        make_result(src),
        provenance_class="interpretive",
        used_in_shots=[SHOT],
        schema_dir=SCHEMAS,
    )

    saved = mf.load(path)
    stored_path = store.root(cfg) / saved["assets"][0]["store_path"]
    stored_path.write_bytes(b"silently corrupted by a sync tool")

    findings = mf.verify(saved, store.root(cfg))

    assert len(findings) == 1
    assert "INTEGRITY FAILURE" in findings[0]
    assert "incident_response" in findings[0]


def test_freeze_marks_and_returns_a_stable_hash() -> None:
    m = new_manifest()
    entry = generated_entry()
    entry["store_path"] = f"{LINE}/productions/{EPISODE}/generated/shot.png"
    mf.add(m, entry)

    digest = mf.freeze(m)

    assert m["frozen"] is True
    assert len(digest) == 64
    assert digest == mf.freeze(m)  # idempotent
    # The hash is over what the manifest says, not how it was written out.
    assert digest == mf.manifest_hash(dict(reversed(list(m.items()))))


def test_freeze_refuses_an_asset_still_pending_rights() -> None:
    m = new_manifest()
    entry = generated_entry(rights_status="pending")
    entry["store_path"] = "a/b.png"
    mf.add(m, entry)

    with pytest.raises(mf.ProvenanceError, match="pending"):
        mf.freeze(m)

    assert not m.get("frozen")


def test_freeze_refuses_an_entry_with_no_hash() -> None:
    m = new_manifest()
    entry = generated_entry()
    entry["store_path"] = "a/b.png"
    del entry["sha256"]
    mf.add(m, entry)

    with pytest.raises(mf.ProvenanceError, match="nothing to freeze"):
        mf.freeze(m)
