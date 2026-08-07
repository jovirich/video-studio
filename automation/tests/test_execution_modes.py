"""Execution modes behind the adapter interface.

The claim under test: mode is an implementation detail, not a tier. A production says
"make me an image"; it does not know whether the pixels came from a container here, a
vendor API, or an operator at an interactive surface.

The one place the abstraction genuinely leaks is synchrony — interactive is two-phase
and cannot return a result from `generate()`. These tests pin that leak rather than
hide it, because an adapter that faked a result for work that had not happened would
defeat every provenance guarantee in the package.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from studio_ops.adapters import registered_adapters
from studio_ops.adapters.base import (
    AdapterNotBuiltError,
    AwaitingFulfilmentError,
    ExecutionMode,
    GenerationRequest,
    UnsupportedRequestError,
    get_adapter,
)
from studio_ops.adapters.interactive import InteractiveAdapter
from studio_ops.adapters.job import GenerationJob, JobReference, job_from_request


def make_request(tmp_path: Path, **kwargs: object) -> GenerationRequest:
    defaults: dict[str, object] = {
        "prompt_card_id": "PC-NG-EXP001-0001",
        "modality": "image",
        "vendor": "interactive",
        "model": "operator",
        "rendered_prompt": "a plain test subject",
        "seed": 7,
        "output_path": str(tmp_path / "out.png"),
    }
    defaults.update(kwargs)
    return GenerationRequest(**defaults)  # type: ignore[arg-type]


# ------------------------------------------------------------------ the modes


def test_every_backend_declares_a_mode() -> None:
    """An undeclared mode would default to the loosest reading of what is happening."""
    for name, cls in registered_adapters().items():
        assert isinstance(cls.capabilities().execution_mode, ExecutionMode), name


def test_local_declares_local_and_costs_nothing() -> None:
    caps = get_adapter("local").capabilities()
    assert caps.execution_mode is ExecutionMode.LOCAL
    assert caps.spends_money is False
    assert caps.two_phase is False


def test_interactive_declares_two_phase_and_does_not_claim_to_be_free() -> None:
    """Whether the operator's surface costs anything is outside this process's view.

    Declaring `spends_money=False` would be a claim about somebody else's account.
    """
    caps = get_adapter("interactive").capabilities()
    assert caps.execution_mode is ExecutionMode.INTERACTIVE
    assert caps.two_phase is True
    assert caps.spends_money is True


def test_unwired_vendor_adapters_default_to_api() -> None:
    """The conservative reading: an adapter that forgets to say is treated as paid."""
    assert get_adapter("image").capabilities().execution_mode is ExecutionMode.API


# --------------------------------------------------- interactive is two-phase


def test_interactive_generate_refuses_under_dry_run(tmp_path: Path) -> None:
    """The dry-run default guards interactive work exactly as it guards a vendor call.

    A job must not be written for a request that would have been refused.
    """
    adapter = InteractiveAdapter(job_dir=tmp_path / "jobs")
    with pytest.raises(AdapterNotBuiltError):
        adapter.generate(make_request(tmp_path))
    assert not (tmp_path / "jobs").exists()


def test_interactive_generate_never_returns_a_result(tmp_path: Path) -> None:
    """THE property. No result may exist for work that has not happened."""
    adapter = InteractiveAdapter(dry_run=False, budget_usd=1.0, job_dir=tmp_path / "jobs")

    with pytest.raises(AwaitingFulfilmentError) as exc:
        adapter.generate(make_request(tmp_path))

    assert exc.value.job_path is not None
    assert exc.value.job_path.is_file()


def test_a_bare_request_job_says_it_is_under_specified(tmp_path: Path) -> None:
    """A job assembled without records carries the prompt but none of the constraints.

    It must say so, loudly, rather than shipping a brief that looks complete.
    """
    adapter = InteractiveAdapter(dry_run=False, budget_usd=1.0, job_dir=tmp_path / "jobs")
    with pytest.raises(AwaitingFulfilmentError) as exc:
        adapter.generate(make_request(tmp_path))

    assert exc.value.job_path is not None
    data = yaml.safe_load(exc.value.job_path.read_text(encoding="utf-8"))
    assert "ASSEMBLED FROM A BARE REQUEST" in data["notes"]


# -------------------------------------------------------------- fulfilment


def test_fulfil_hashes_the_bytes_and_does_not_take_a_reported_hash(tmp_path: Path) -> None:
    """The single thing that makes an out-of-band mode as accountable as an in-process one."""
    import hashlib

    delivered = tmp_path / "delivered.png"
    delivered.write_bytes(b"\x89PNG\r\n\x1a\n" + b"payload")
    expected = hashlib.sha256(delivered.read_bytes()).hexdigest()

    adapter = InteractiveAdapter(dry_run=False, budget_usd=1.0)
    result = adapter.fulfil(
        make_request(tmp_path),
        delivered,
        vendor="some-surface",
        model="some-model",
        model_version="2026-08",
    )

    assert result.sha256 == expected
    assert result.request.prompt_card_id == "PC-NG-EXP001-0001"


def test_fulfil_refuses_a_missing_file(tmp_path: Path) -> None:
    """A report that generation happened is not an asset."""
    adapter = InteractiveAdapter(dry_run=False, budget_usd=1.0)
    with pytest.raises(UnsupportedRequestError, match="nothing delivered"):
        adapter.fulfil(
            make_request(tmp_path),
            tmp_path / "absent.png",
            vendor="v",
            model="m",
            model_version="1",
        )


def test_fulfil_demands_what_actually_made_it(tmp_path: Path) -> None:
    """'interactive' is how it arrived, not what made it."""
    delivered = tmp_path / "d.png"
    delivered.write_bytes(b"x")
    adapter = InteractiveAdapter(dry_run=False, budget_usd=1.0)

    with pytest.raises(UnsupportedRequestError, match="vendor and model"):
        adapter.fulfil(make_request(tmp_path), delivered, vendor="", model="", model_version="1")


def test_fulfilment_records_its_own_limits(tmp_path: Path) -> None:
    """A later reader of the manifest must see what was verified and what was reported."""
    delivered = tmp_path / "d.png"
    delivered.write_bytes(b"x")
    adapter = InteractiveAdapter(dry_run=False, budget_usd=1.0)

    result = adapter.fulfil(
        make_request(tmp_path), delivered, vendor="v", model="m", model_version="1"
    )

    verification = result.raw_response["verification"]
    assert "computed from the delivered bytes" in verification
    assert "not independently verifiable" in verification
    assert result.raw_response["execution_mode"] == "interactive"


# ------------------------------------------------------------ the job format


def test_a_job_carries_obligations_not_just_a_prompt(tmp_path: Path) -> None:
    """An operator reading only the job cannot bypass a rule in a file they never opened."""
    job = job_from_request(
        make_request(tmp_path),
        job_id="SHT-NG-EXP001-0001",
        production_id="EXP001",
        line="ng-nigeria",
        shot_id="SHT-NG-EXP001-0001",
        negative=("plastic", "machine stitching"),
        hard_stops=("regalia — requires an advisory ruling",),
        continuity_constraints=("A — scar through the right eyebrow",),
        acceptance_checklist=("scar on the RIGHT side",),
        character_references=(JobReference(kind="continuity_record", ref="CNC-NG-0001"),),
    )

    brief = job.to_operator_brief()
    assert "plastic" in brief
    assert "Hard stops" in brief
    assert "right eyebrow" in brief
    assert "CNC-NG-0001" in brief
    # The provenance demanded back is in the brief, not only in the YAML.
    assert "exact version identifier" in brief


def test_hard_stops_are_separated_from_negative_prompt_terms(tmp_path: Path) -> None:
    """A negative prompt is a nudge. Treating it as a safeguard is a category error."""
    job = job_from_request(
        make_request(tmp_path),
        job_id="j",
        production_id="EXP001",
        line="ng-nigeria",
        negative=("plastic",),
        hard_stops=("sacred material",),
    )
    brief = job.to_operator_brief()

    assert "not adjust the frame and keep it" in brief
    assert brief.index("### Negative prompt") < brief.index("Hard stops")


def test_a_job_carries_no_credentials(tmp_path: Path) -> None:
    """A job is a specification handed to a person. It is not an authorisation."""
    job = job_from_request(
        make_request(tmp_path, parameters={"width": 512}),
        job_id="j",
        production_id="EXP001",
        line="ng-nigeria",
    )
    text = job.to_yaml().lower()

    for secret in ("api_key", "apikey", "token", "secret", "password", "credential"):
        assert secret not in text


def test_a_job_round_trips_through_yaml(tmp_path: Path) -> None:
    job = job_from_request(
        make_request(tmp_path), job_id="j", production_id="EXP001", line="ng-nigeria"
    )
    path = job.write(tmp_path / "j.job.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert data["format"] == "studio_ops/generation_job"
    assert data["prompt_card_id"] == "PC-NG-EXP001-0001"
    assert data["output_filename"] or data["prompt"]


def test_the_job_is_not_a_record() -> None:
    """It has no ID in the reference graph and no schema. Deleting it loses nothing.

    Pinned because the freeze turns on this distinction: a record type would be a new
    abstraction; a work order derived from existing records is not.
    """
    from studio_ops.paths import find_repo_root

    schemas = find_repo_root() / "standards" / "schemas"
    assert not (schemas / "generation_job.schema.json").exists()
    assert "job_id" in GenerationJob.__dataclass_fields__
    assert "id" not in GenerationJob.__dataclass_fields__


# ------------------------------------------- the interactive round trip, closed


def test_the_interactive_round_trip_closes(tmp_path: Path) -> None:
    """prepare → (operator) → fulfil → manifest, with the hash matching the bytes.

    The same acceptance criterion as the one-phase round trip, across a two-phase
    boundary. The `local` adapter stands in for the operator: it is the only backend
    that can produce a real file offline, which is exactly why it exists.

    What this proves is not that an operator behaves — it is that an operator does not
    have to. The pipeline hashes what it is given and records what it verified.
    """
    import os

    import yaml as _yaml

    from studio_ops.adapters.base import get_adapter
    from studio_ops.config import Config
    from studio_ops.paths import Layout
    from studio_ops.pipeline import generate as gen
    from studio_ops.pipeline import manifest, store

    root = tmp_path / "repo"
    (root / "core").mkdir(parents=True)
    (root / "packs").mkdir()
    os.environ["ASSET_STORE_LOCAL_PATH"] = str(tmp_path / "assets")
    os.environ["ASSET_STORE_DRIVER"] = "local"
    cfg = Config(root=root, layout=Layout(root=root))

    schemas = Path(__file__).resolve().parents[2] / "standards" / "schemas"
    manifest_path = root / "manifest.yaml"
    manifest.save(
        manifest_path,
        manifest.create(line="ng-nigeria", episode="EXP001", updated="2026-08-07"),
        schema_dir=schemas,
    )

    # Phase one — a job, written without any adapter running.
    job_path = tmp_path / "jobs" / "SHT-NG-EXP001-0001.job.yaml"
    GenerationJob(
        job_id="SHT-NG-EXP001-0001",
        prompt_card_id="PC-NG-EXP001-0001",
        production_id="EXP001",
        line="ng-nigeria",
        shot_id="SHT-NG-EXP001-0001",
        prompt="a plain test subject",
        manifest_path=str(manifest_path),
        provenance_class="interpretive",
        output_filename="delivered.png",
        incoming_dir=str(tmp_path),
    ).write(job_path)

    # Out of band — the operator generates. Stood in for by the local backend.
    delivered = tmp_path / "delivered.png"
    local = get_adapter("local")(dry_run=False, budget_usd=1.0)
    local.generate(
        GenerationRequest(
            prompt_card_id="PC-NG-EXP001-0001",
            modality="image",
            vendor="local",
            model="local-deterministic",
            rendered_prompt="a plain test subject",
            seed=99,
            output_path=str(delivered),
        )
    )
    assert delivered.is_file()

    # Phase two — ingest.
    trip = gen.fulfil_job(
        cfg,
        job_path=job_path,
        delivered=delivered,
        vendor="stand-in-surface",
        model="stand-in-model",
        model_version="2026-08",
        seed=99,
        schema_dir=schemas,
    )

    # The guarantee: the record and the bytes agree.
    stored = store.resolve(store.root(cfg), trip.entry["store_path"])
    assert stored.is_file()
    assert trip.hash_matches_disk(store.root(cfg))
    assert trip.entry["sha256"] == store.sha256_file(stored)

    # The manifest is valid afterwards, not merely written.
    assert manifest.validate(manifest.load(manifest_path), schema_dir=schemas) == []

    # Provenance names what MADE it, not how it arrived.
    gen_block = trip.entry["generation"]
    assert gen_block["tool"]["vendor"] == "stand-in-surface"
    assert gen_block["prompt_card"] == "PC-NG-EXP001-0001"
    assert trip.entry["used_in_shots"] == ["SHT-NG-EXP001-0001"]

    # And the record carries its own limits, so a later reader is not misled.
    assert "not independently verifiable" in trip.result.raw_response["verification"]

    _ = _yaml


def test_fulfilment_refuses_a_job_with_no_manifest(tmp_path: Path) -> None:
    """An asset with nowhere to be recorded would exist with no provenance."""
    from studio_ops.config import Config
    from studio_ops.paths import Layout
    from studio_ops.pipeline import generate as gen

    root = tmp_path / "repo"
    (root / "core").mkdir(parents=True)
    (root / "packs").mkdir()
    cfg = Config(root=root, layout=Layout(root=root))

    delivered = tmp_path / "d.png"
    delivered.write_bytes(b"x")
    job_path = tmp_path / "j.job.yaml"
    GenerationJob(
        job_id="j",
        prompt_card_id="PC-NG-EXP001-0001",
        production_id="EXP001",
        line="ng-nigeria",
        manifest_path=str(tmp_path / "absent.yaml"),
    ).write(job_path)

    with pytest.raises(gen.RoundTripError, match="manifest_path"):
        gen.fulfil_job(
            cfg,
            job_path=job_path,
            delivered=delivered,
            vendor="v",
            model="m",
            model_version="1",
        )


# ------------------------------------------------- the handoff packet, v2 fields


def full_job(**over: object) -> GenerationJob:
    from studio_ops.adapters.job import VideoBrief

    fields: dict[str, object] = {
        "job_id": "SHT-NG-EXP001-0010",
        "production_id": "EXP001",
        "line": "ng-nigeria",
        "scene_id": "SEQ-NG-EXP001-001",
        "shot_id": "SHT-NG-EXP001-0010",
        "prompt_card_id": "PC-NG-EXP001-0001",
        "modality": "video",
        "creative_purpose": "Establish that the work is unhurried.",
        "continuity_records": ("CNC-NG-0001", "CNL-NG-0001"),
        "prompt": "a plain test subject",
        "negative": ("plastic",),
        "hard_stops": ("regalia — requires a ruling",),
        "continuity_constraints": ("A — scar through the right eyebrow",),
        "evidence_constraints": ("CLM-NG-0001",),
        "framing": "ms, three-quarter, eye",
        "lens_look": "50mm equivalent",
        "lighting": "raking\nfrom frame left",
        "duration_seconds": 4,
        "aspect_ratio": "16:9",
        "output_filename": "EXP001_SEQ001_SHT0010_interp_v01.mp4",
        "incoming_dir": "/prod/05_assets/video/incoming",
        "acceptance_checklist": ("scar on the RIGHT side",),
        "video": VideoBrief(
            source_still="AST-NG-EXP001-0003",
            first_frame_continuity="must BE the source still",
            end_state_intent="A reaches the door",
            camera_movement="track — follows A",
            subject_movement="A rises and walks",
            prohibited_motion=("identity drift",),
            identity_preservation=("A is the same person throughout",),
        ),
    }
    fields.update(over)
    return GenerationJob(**fields)  # type: ignore[arg-type]


def test_the_packet_carries_every_field_an_operator_needs() -> None:
    """One artefact, start to finish. Reconstructing context from four files is where
    the forbidden list gets dropped."""
    brief = full_job().to_operator_brief()

    for expected in (
        "EXP001",  # production
        "SEQ-NG-EXP001-001",  # scene
        "SHT-NG-EXP001-0010",  # shot
        "video",  # modality
        "Establish that the work is unhurried",  # creative purpose
        "scar through the right eyebrow",  # continuity constraint
        "CLM-NG-0001",  # evidence constraint
        "a plain test subject",  # prompt
        "plastic",  # negative
        "ms, three-quarter, eye",  # framing
        "50mm equivalent",  # lens
        "16:9",  # aspect
        "4s",  # duration
        "EXP001_SEQ001_SHT0010_interp_v01.mp4",  # output filename
        "/prod/05_assets/video/incoming",  # incoming folder
        "scar on the RIGHT side",  # acceptance checklist
    ):
        assert expected in brief, expected


def test_the_video_brief_appears_for_video_jobs() -> None:
    brief = full_job().to_operator_brief()
    for expected in (
        "AST-NG-EXP001-0003",
        "must BE the source still",
        "A reaches the door",
        "track — follows A",
        "identity drift",
        "A is the same person throughout",
    ):
        assert expected in brief, expected


def test_no_motion_brief_on_an_image_job() -> None:
    brief = full_job(modality="image", video=None).to_operator_brief()
    assert "Motion brief" not in brief


def test_multiline_record_fields_do_not_break_the_settings_table() -> None:
    """A newline inside a cell silently breaks the table — a defect that survives
    review because the file still renders, just wrongly."""
    brief = full_job().to_operator_brief()
    row = next(ln for ln in brief.splitlines() if ln.startswith("| Lighting"))
    assert row.count("|") == 3
    assert "raking from frame left" in row


def test_an_unauthorised_job_says_so_before_anything_else() -> None:
    """Preparation is free, so it is not blocked — but nobody may fulfil an
    unauthorised job without seeing that they are."""
    brief = full_job(authorised=False, authorisation_note="phase A only").to_operator_brief()
    head = brief.splitlines()[:6]
    assert any("NOT AUTHORISED" in ln for ln in head)
    assert "phase A only" in brief


def test_the_prompt_is_one_copyable_block() -> None:
    """A brief that makes an operator assemble the prompt from fragments is a brief
    that will be assembled wrongly."""
    brief = full_job(prompt="line one and line two").to_operator_brief()
    fences = [i for i, ln in enumerate(brief.splitlines()) if ln.startswith("```")]
    assert len(fences) >= 2
    body = brief.splitlines()[fences[0] + 1 : fences[1]]
    assert body == ["line one and line two"]
