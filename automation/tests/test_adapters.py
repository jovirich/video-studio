"""Tests for the generation adapters.

Two things are under test and they pull in opposite directions.

The first is that the guards actually refuse. A safety default that has never been
observed refusing is a comment. These assert that a missing environment variable
yields the refusing state, that a priced backend with no ceiling is stopped before it
spends, and that the stubs still say *why* they are stubs.

The second is that the local backend actually works, end to end, deterministically —
a real file, a real PNG, a real hash of the bytes on disk, and a provenance record the
manifest schema would accept. The PNG is parsed here rather than sniffed: the magic
bytes plus a chunk walk with CRC verification, because "starts with 0x89PNG" is true
of a truncated file too.
"""

from __future__ import annotations

import struct
import zlib
from dataclasses import replace
from pathlib import Path
from typing import Any

import pytest

from studio_ops.adapters import stubs
from studio_ops.adapters.base import (
    Adapter,
    AdapterNotBuiltError,
    BudgetExceededError,
    Capabilities,
    GenerationRequest,
    GenerationResult,
    IncompleteProvenanceError,
    UnsupportedRequestError,
    get_adapter,
    registered_adapters,
    sha256_file,
)
from studio_ops.adapters.local import LocalImageAdapter, resolve_seed
from studio_ops.config import Config

CARD = "PC-NG-S01E01-0037"
PROMPT = "Kano city walls at dawn, wide, dust haze"

# Small on purpose: these tests generate a lot of images and none of them is looked at.
SMALL: dict[str, Any] = {"width": 48, "height": 32}


def make_request(tmp_path: Path, name: str = "shot.png", **overrides: Any) -> GenerationRequest:
    request = GenerationRequest(
        prompt_card_id=CARD,
        modality="image",
        vendor="local",
        model="local-deterministic",
        rendered_prompt=PROMPT,
        parameters=dict(SMALL),
        seed=42,
        output_path=str(tmp_path / name),
    )
    return replace(request, **overrides) if overrides else request


def run_local(request: GenerationRequest) -> GenerationResult:
    """The local backend, deliberately enabled. Zero budget, because it is free."""
    return LocalImageAdapter(dry_run=False, operator="test-runner").generate(request)


# --------------------------------------------------------------- PNG inspection


def parse_png(data: bytes) -> dict[str, Any]:
    """Walk the file as a PNG, verifying every chunk CRC. Raises if it is not one."""
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "PNG signature missing"

    offset = 8
    chunks: list[str] = []
    header: dict[str, Any] = {}
    while offset < len(data):
        (length,) = struct.unpack(">I", data[offset : offset + 4])
        kind = data[offset + 4 : offset + 8]
        body = data[offset + 8 : offset + 8 + length]
        (crc,) = struct.unpack(">I", data[offset + 8 + length : offset + 12 + length])
        assert crc == zlib.crc32(kind + body), f"bad CRC on {kind!r} chunk"
        chunks.append(kind.decode("ascii"))

        if kind == b"IHDR":
            width, height, depth, colour, comp, filt, interlace = struct.unpack(">IIBBBBB", body)
            header = {
                "width": width,
                "height": height,
                "bit_depth": depth,
                "colour_type": colour,
                "compression": comp,
                "filter": filt,
                "interlace": interlace,
            }
        offset += 12 + length

    assert chunks[0] == "IHDR", "IHDR must come first"
    assert chunks[-1] == "IEND", "IEND must come last"
    assert "IDAT" in chunks, "no image data"
    return {"chunks": chunks, **header}


# ------------------------------------------------------------------- the guards


def test_dry_run_is_the_default(tmp_path: Path) -> None:
    """A backend built with no arguments must refuse. Free is not a reason to run."""
    adapter = LocalImageAdapter()

    with pytest.raises(AdapterNotBuiltError) as excinfo:
        adapter.generate(make_request(tmp_path))

    assert "GENERATION_DRY_RUN" in str(excinfo.value)
    assert not (tmp_path / "shot.png").exists()


def test_missing_env_var_yields_the_refusing_state(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The point of the default: an unset variable must not be the spending state."""
    monkeypatch.delenv("GENERATION_DRY_RUN", raising=False)
    monkeypatch.delenv("GENERATION_BUDGET_USD_PER_EPISODE", raising=False)
    (tmp_path / "core").mkdir()
    (tmp_path / "packs").mkdir()

    cfg = Config.load(tmp_path)
    assert cfg.generation_dry_run is True

    with pytest.raises(AdapterNotBuiltError):
        LocalImageAdapter.from_config(cfg).generate(make_request(tmp_path))


class PricedAdapter(Adapter):
    """A stand-in for a vendor backend: costs money, never actually called."""

    vendor = "priced-test-double"
    modality = "image"

    @classmethod
    def capabilities(cls) -> Capabilities:
        return Capabilities(modalities=frozenset({"image"}), spends_money=True)

    def estimate_cost(self, request: GenerationRequest) -> float:
        return 5.0

    def _generate(self, request: GenerationRequest) -> GenerationResult:  # pragma: no cover
        raise AssertionError("the budget guard should have refused before this ran")


def test_budget_guard_refuses_a_priced_backend_with_no_ceiling(tmp_path: Path) -> None:
    """No ceiling plus a price is unaccountable, not merely cheap."""
    adapter = PricedAdapter(dry_run=False, budget_usd=0.0)

    with pytest.raises(BudgetExceededError) as excinfo:
        adapter.generate(make_request(tmp_path, vendor="priced-test-double"))

    assert "no generation budget set" in str(excinfo.value)


def test_budget_guard_refuses_a_run_over_the_ceiling(tmp_path: Path) -> None:
    adapter = PricedAdapter(dry_run=False, budget_usd=2.0)

    with pytest.raises(BudgetExceededError) as excinfo:
        adapter.generate(make_request(tmp_path, vendor="priced-test-double"))

    assert "ceiling" in str(excinfo.value)


def test_the_ceiling_uses_the_higher_of_the_two_estimates(tmp_path: Path) -> None:
    """Neither the adapter's quote nor the caller's declaration can lower the bar alone."""
    adapter = LocalImageAdapter(dry_run=False, budget_usd=1.0)
    request = make_request(tmp_path, estimated_cost_usd=99.0)

    with pytest.raises(BudgetExceededError):
        adapter.generate(request)


def test_a_genuinely_free_run_needs_no_ceiling(tmp_path: Path) -> None:
    """The zero-cost case is arithmetic, not an exemption: 0.00 fits under any ceiling.

    This is what makes the local backend usable in CI without any budget being set,
    while the identical guard still stops `PricedAdapter` above.
    """
    adapter = LocalImageAdapter(dry_run=False, budget_usd=0.0)

    result = adapter.generate(make_request(tmp_path))

    assert result.cost_usd == 0.0
    assert adapter.spent_usd == 0.0


class LyingFreeAdapter(LocalImageAdapter):
    """Declares itself free, then charges. The declaration is a safety claim."""

    def _generate(self, request: GenerationRequest) -> GenerationResult:
        return replace(super()._generate(request), cost_usd=7.5)


def test_a_backend_that_declares_itself_free_may_not_charge(tmp_path: Path) -> None:
    with pytest.raises(IncompleteProvenanceError) as excinfo:
        LyingFreeAdapter(dry_run=False).generate(make_request(tmp_path))

    assert "spends_money=False" in str(excinfo.value)


def test_stub_adapters_still_refuse_and_still_say_why() -> None:
    """Enabled, funded, and still refusing — because they are not built.

    A generic "not implemented" would be useless here. Each stub names the specific
    precondition that is missing, and this asserts the reason survives to the caller.
    """
    for modality, cls in stubs.REGISTRY.items():
        adapter = cls(dry_run=False, budget_usd=100.0)
        request = GenerationRequest(
            prompt_card_id=CARD,
            modality=modality,
            vendor=adapter.vendor,
            model="whatever",
            rendered_prompt=PROMPT,
        )

        with pytest.raises(AdapterNotBuiltError) as excinfo:
            adapter.generate(request)

        message = str(excinfo.value)
        assert "NOT BUILT" in message
        assert cls.reason in message
        assert "docs/status.md" in message


def test_unsupported_modality_is_refused_with_the_alternatives(tmp_path: Path) -> None:
    adapter = LocalImageAdapter(dry_run=False)

    with pytest.raises(UnsupportedRequestError) as excinfo:
        adapter.generate(make_request(tmp_path, modality="video"))

    assert "image" in str(excinfo.value)


# ------------------------------------------------------------------- the registry


def test_registry_resolves_names_to_backends() -> None:
    assert get_adapter("local") is LocalImageAdapter
    assert get_adapter("video") is stubs.VideoAdapter
    assert "local" in registered_adapters()


def test_unknown_adapter_name_lists_what_exists() -> None:
    with pytest.raises(AdapterNotBuiltError) as excinfo:
        get_adapter("midjourney")

    assert "local" in str(excinfo.value)


def test_only_the_local_backend_declares_itself_free() -> None:
    """Conservative default: an undeclared backend is treated as a paid one."""
    free = {
        name for name, cls in registered_adapters().items() if not cls.capabilities().spends_money
    }

    assert free == {"local"}


# ------------------------------------------------------------- the local backend


def test_local_writes_a_file_that_parses_as_a_png(tmp_path: Path) -> None:
    result = run_local(make_request(tmp_path))
    path = Path(result.asset_path)

    assert path.is_file()
    png = parse_png(path.read_bytes())

    assert png["width"] == SMALL["width"]
    assert png["height"] == SMALL["height"]
    assert png["bit_depth"] == 8
    assert png["colour_type"] == 2  # truecolour RGB
    assert png["interlace"] == 0


def test_local_embeds_its_provenance_in_the_file(tmp_path: Path) -> None:
    """The file says what made it even after it is copied out of the repository."""
    result = run_local(make_request(tmp_path))
    raw = Path(result.asset_path).read_bytes()

    assert b"tEXt" in raw
    assert CARD.encode() in raw
    assert b"local-deterministic" in raw


def test_sha256_is_the_hash_of_the_bytes_on_disk(tmp_path: Path) -> None:
    """Not the hash of the buffer we meant to write. That claim must survive a read."""
    result = run_local(make_request(tmp_path))

    assert result.sha256 == sha256_file(Path(result.asset_path))
    assert len(result.sha256) == 64


def test_same_seed_and_prompt_produce_identical_bytes(tmp_path: Path) -> None:
    """The property that makes this a fixture rather than a toy."""
    first = run_local(make_request(tmp_path, "a.png"))
    second = run_local(make_request(tmp_path, "b.png"))

    assert first.sha256 == second.sha256
    assert first.raw_response["pixel_sha256"] == second.raw_response["pixel_sha256"]
    assert (tmp_path / "a.png").read_bytes() == (tmp_path / "b.png").read_bytes()


def test_a_different_seed_produces_a_different_image(tmp_path: Path) -> None:
    first = run_local(make_request(tmp_path, "a.png", seed=42))
    second = run_local(make_request(tmp_path, "b.png", seed=43))

    assert first.sha256 != second.sha256
    assert first.raw_response["pixel_sha256"] != second.raw_response["pixel_sha256"]


def test_a_different_prompt_produces_a_different_image(tmp_path: Path) -> None:
    first = run_local(make_request(tmp_path, "a.png"))
    second = run_local(make_request(tmp_path, "b.png", rendered_prompt=PROMPT + ", night"))

    assert first.sha256 != second.sha256
    assert first.raw_response["pixel_sha256"] != second.raw_response["pixel_sha256"]


def test_a_missing_seed_is_derived_and_recorded(tmp_path: Path) -> None:
    """A generation nobody can repeat is not traceable, and the manifest requires a seed."""
    request = make_request(tmp_path, seed=None)

    result = run_local(request)

    assert result.seed == resolve_seed(request)
    assert str(result.seed).strip()
    # Derived from the prompt, so it is reproducible rather than merely present.
    assert result.seed == resolve_seed(replace(request, output_path="elsewhere.png"))


def test_local_refuses_without_an_output_path(tmp_path: Path) -> None:
    """The asset store owns placement; this backend does not go looking for a home."""
    with pytest.raises(UnsupportedRequestError):
        run_local(make_request(tmp_path, output_path=None))


def test_local_refuses_a_path_whose_extension_lies(tmp_path: Path) -> None:
    with pytest.raises(UnsupportedRequestError):
        run_local(make_request(tmp_path, output_path=str(tmp_path / "shot.jpg")))


def test_local_creates_missing_parent_directories(tmp_path: Path) -> None:
    target = tmp_path / "05_assets" / "stills" / "shot.png"

    result = run_local(make_request(tmp_path, output_path=str(target)))

    assert Path(result.asset_path).is_file()


# ------------------------------------------------------------ provenance contract


MANIFEST_REQUIRED = ("tool", "prompt_card", "seed", "generated_at", "generated_by")


def test_result_carries_every_field_the_manifest_requires(tmp_path: Path) -> None:
    """asset_manifest.schema.json $defs.asset.generation, with nothing empty."""
    result = run_local(make_request(tmp_path))
    block = result.to_generation_block()

    for key in MANIFEST_REQUIRED:
        assert key in block, f"missing {key}"
        assert block[key] not in (None, "", {}, []), f"empty {key}"

    assert block["tool"] == {
        "vendor": "local",
        "model": "local-deterministic",
        "version": "1.0.0",
    }
    assert block["prompt_card"] == CARD
    assert block["cost_usd"] == 0.0
    assert block["generated_by"] == "test-runner"
    assert block["generated_at"].endswith("Z")

    # No key outside the schema's closed object.
    assert set(block) <= {*MANIFEST_REQUIRED, "parameters", "inputs", "cost_usd"}


def test_result_records_the_backend_that_actually_ran(tmp_path: Path) -> None:
    """A caller's declared vendor does not get to be the provenance record."""
    result = run_local(make_request(tmp_path, vendor="midjourney", model="v7"))

    assert result.to_generation_block()["tool"]["vendor"] == "local"
    assert result.to_generation_block()["tool"]["model"] == "local-deterministic"


class ForgetfulAdapter(LocalImageAdapter):
    """Produces the file, then loses the hash. The failure this contract exists for."""

    def _generate(self, request: GenerationRequest) -> GenerationResult:
        return replace(super()._generate(request), sha256="")


def test_a_backend_cannot_return_an_asset_without_its_provenance(tmp_path: Path) -> None:
    with pytest.raises(IncompleteProvenanceError) as excinfo:
        ForgetfulAdapter(dry_run=False).generate(make_request(tmp_path))

    assert "sha256" in str(excinfo.value)


class MisattributingAdapter(LocalImageAdapter):
    def _generate(self, request: GenerationRequest) -> GenerationResult:
        result = super()._generate(request)
        return replace(result, request=replace(result.request, vendor="somebody-else"))


def test_a_backend_cannot_misattribute_the_work(tmp_path: Path) -> None:
    with pytest.raises(IncompleteProvenanceError) as excinfo:
        MisattributingAdapter(dry_run=False).generate(make_request(tmp_path))

    assert "actually produced" in str(excinfo.value)
