"""Local deterministic image backend — the first adapter that actually produces a file.

This is not a mock. It writes a real PNG, with real bytes, a real SHA-256 of what
landed on disk, and a complete provenance record. What it does not do is call
anybody, spend anything, or need a key.

## Why this one first

The rule the repository is built on is that no second adapter exists until the first
can complete a traceable round trip: continuity record and shot record → prompt →
returned asset → provenance manifest. That round trip is the thing worth proving, and
none of it is vendor-specific. A vendor backend proves the same plumbing while also
requiring an account, a budget decision, current terms, and a network — four ways for
the test to fail that have nothing to do with the code under test.

So the plumbing is proved here, offline, and stays proved: this adapter is the CI
fixture forever. A vendor backend behind the same interface is then an isolated
change with a known-good baseline to compare against.

## Determinism, precisely

Identical inputs produce a byte-identical file. The pixels are derived from a
counter-mode SHA-256 stream — no `random`, no floats, no clock — so the *image
content* is identical on any platform and any Python build. Two hashes are recorded:

- `sha256` on the result is the file, which additionally depends on the zlib build
  that compressed it and on the deterministic metadata written into the PNG.
- `raw_response["pixel_sha256"]` is the uncompressed pixel data, which depends on
  nothing but the prompt, the seed, and the dimensions.

Assert against the first within an environment, the second across environments.

The file's inputs, in full: rendered prompt, seed, width, height, prompt card id,
model, and model version. Not the timestamp, not the operator, not the asset path —
those go in the provenance record where they belong, and would otherwise make the
same generation unreproducible on a Tuesday.

## What it is not

The images are colour fields. They are not meant to look like the shot; nothing
generated here is fit to appear in an episode. Its output is `provenance_class:
interpretive` at best and in practice belongs nowhere near a cut — it is a test
signal, and the fact that it is visibly a test signal is a feature.
"""

from __future__ import annotations

import hashlib
import struct
import zlib
from dataclasses import replace
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .base import (
    Adapter,
    Capabilities,
    GenerationRequest,
    GenerationResult,
    UnsupportedRequestError,
    register,
    sha256_file,
)

MODEL = "local-deterministic"
VERSION = "1.0.0"

DEFAULT_WIDTH = 512
DEFAULT_HEIGHT = 512
MAX_DIMENSION = 4096

# Side of the repeating noise tile. Big enough not to read as a pattern, small enough
# that the whole tile is one hash expansion.
_TILE = 64

# Peak deviation, per channel, that the noise adds to the gradient. Enough to give the
# field texture; not enough to swamp the colour that identifies the prompt.
_NOISE_AMPLITUDE = 28

_PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


@register("local")
class LocalImageAdapter(Adapter):
    """Deterministic offline image generation. Zero cost, no network, no key.

    Still refuses under `GENERATION_DRY_RUN`. Being free is a reason not to need a
    budget; it is not a reason to write files nobody asked for. See base.py.
    """

    vendor = "local"
    modality = "image"

    @classmethod
    def capabilities(cls) -> Capabilities:
        return Capabilities(
            modalities=frozenset({"image"}),
            spends_money=False,
            deterministic=True,
            accepts_seed=True,
            max_pixels=MAX_DIMENSION * MAX_DIMENSION,
            notes=(
                "Offline, zero cost, byte-identical for identical inputs. Safe to run "
                "in CI. Output is a colour field, not imagery."
            ),
        )

    def estimate_cost(self, request: GenerationRequest) -> float:
        """Genuinely zero. Nothing is billed, so nothing is estimated."""
        return 0.0

    def _generate(self, request: GenerationRequest) -> GenerationResult:
        path = _output_path(request)
        width, height = _dimensions(request)
        seed = resolve_seed(request)

        pixels = _pixel_field(request.rendered_prompt, seed, width, height)
        png = _encode_png(
            width,
            height,
            pixels,
            text={
                "Software": f"studio_ops {MODEL} {VERSION}",
                "Comment": (
                    "AI-generated. Never archival. See core/01_provenance_and_ai_disclosure.md."
                ),
                "prompt_card": request.prompt_card_id,
                "seed": str(seed),
                "prompt_sha256": hashlib.sha256(
                    request.rendered_prompt.encode("utf-8")
                ).hexdigest(),
            },
        )

        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(png)

        return GenerationResult(
            # Attribution is normalised to what actually ran, not to what the caller
            # declared. The base class enforces that this matches `self.vendor`.
            request=replace(request, vendor=self.vendor, model=MODEL),
            asset_path=str(path),
            sha256=sha256_file(path),
            seed=seed,
            model_version=VERSION,
            generated_at=datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
            generated_by=self.operator,
            cost_usd=0.0,
            raw_response={
                "backend": "local",
                "width": width,
                "height": height,
                "bytes": len(png),
                # Independent of zlib and of the metadata chunks: the same everywhere.
                "pixel_sha256": hashlib.sha256(b"".join(pixels)).hexdigest(),
            },
        )


# --- request interpretation ----------------------------------------------


def resolve_seed(request: GenerationRequest) -> int | str:
    """The seed as recorded. Never None.

    A generation with no seed is a generation nobody can repeat, and the manifest
    requires the field. With none supplied one is derived from the prompt, which is
    reproducible and, unlike a random seed, states where it came from.
    """
    if request.seed is None or (isinstance(request.seed, str) and not request.seed.strip()):
        digest = hashlib.sha256(request.rendered_prompt.encode("utf-8")).digest()
        return int.from_bytes(digest[:4], "big")
    return request.seed


def _output_path(request: GenerationRequest) -> Path:
    if not request.output_path:
        raise UnsupportedRequestError(
            "local: no output_path on the request. This backend writes where the "
            "caller says and nowhere else; the asset store owns the permanent location."
        )
    path = Path(request.output_path)
    if path.suffix.lower() != ".png":
        raise UnsupportedRequestError(
            f"local: output_path must end in .png, got {path.name!r}. This backend "
            "produces PNG, and a file whose extension lies about its contents will "
            "fail somewhere less obvious."
        )
    return path


def _dimensions(request: GenerationRequest) -> tuple[int, int]:
    width = _dimension(request.parameters.get("width", DEFAULT_WIDTH), "width")
    height = _dimension(request.parameters.get("height", DEFAULT_HEIGHT), "height")
    return width, height


def _dimension(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise UnsupportedRequestError(f"local: {name} must be an integer, got {value!r}.")
    if not 1 <= value <= MAX_DIMENSION:
        raise UnsupportedRequestError(
            f"local: {name} must be between 1 and {MAX_DIMENSION}, got {value}."
        )
    return value


# --- deterministic pixels -------------------------------------------------


def _expand(material: bytes, length: int) -> bytes:
    """Counter-mode SHA-256 keystream.

    Stable across platforms, Python versions, and time, which `random` is not
    guaranteed to be and which is the whole point of the exercise.
    """
    out = bytearray()
    counter = 0
    while len(out) < length:
        out += hashlib.sha256(material + counter.to_bytes(8, "big")).digest()
        counter += 1
    return bytes(out[:length])


def _pixel_field(prompt: str, seed: int | str, width: int, height: int) -> list[bytes]:
    """One RGB row of bytes per scanline.

    A bilinear blend between four hash-derived corner colours, textured with a tiled
    hash-derived noise field. All integer arithmetic — no floats, so no chance of a
    platform-dependent rounding difference in the last bit of a pixel.
    """
    material = hashlib.sha256(
        f"{MODEL}/{VERSION}|{seed}|{width}x{height}|{prompt}".encode()
    ).digest()

    corners = _expand(material + b"corners", 12)
    top_left, top_right = corners[0:3], corners[3:6]
    bottom_left, bottom_right = corners[6:9], corners[9:12]
    noise = _expand(material + b"noise", _TILE * _TILE)

    # Interpolation weights precomputed once; the inner loop is then three multiplies
    # per channel and nothing else.
    x_weights = [(x * 255) // (width - 1) if width > 1 else 0 for x in range(width)]

    rows: list[bytes] = []
    for y in range(height):
        ty = (y * 255) // (height - 1) if height > 1 else 0
        left = [(top_left[c] * (255 - ty) + bottom_left[c] * ty) // 255 for c in range(3)]
        right = [(top_right[c] * (255 - ty) + bottom_right[c] * ty) // 255 for c in range(3)]
        noise_row = noise[(y % _TILE) * _TILE : (y % _TILE) * _TILE + _TILE]

        row = bytearray()
        for x in range(width):
            tx = x_weights[x]
            grain = ((noise_row[x % _TILE] - 128) * _NOISE_AMPLITUDE) // 128
            for c in range(3):
                value = (left[c] * (255 - tx) + right[c] * tx) // 255 + grain
                row.append(0 if value < 0 else 255 if value > 255 else value)
        rows.append(bytes(row))
    return rows


# --- PNG encoding ---------------------------------------------------------
#
# Standard library only, per the dependency freeze. A PNG is a signature followed by
# length-prefixed, CRC-checked chunks; truecolour 8-bit with filter type 0 on every
# scanline is the simplest form that any decoder will read. Spec: RFC 2083 §4.


def _chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))


def _text_chunk(key: str, value: str) -> bytes:
    """A tEXt chunk. Latin-1 keyword and value, NUL-separated, per the spec.

    Only deterministic values go in here. A timestamp in the file would make the same
    generation produce a different hash every run, which would cost the adapter the
    one property that makes it useful.
    """
    keyword = key.encode("latin-1", "replace")[:79]
    text = value.replace("\x00", " ").encode("latin-1", "replace")
    return _chunk(b"tEXt", keyword + b"\x00" + text)


def _encode_png(
    width: int, height: int, rows: list[bytes], text: dict[str, str] | None = None
) -> bytes:
    header = struct.pack(
        ">IIBBBBB",
        width,
        height,
        8,  # bit depth
        2,  # colour type: truecolour RGB
        0,  # compression: deflate
        0,  # filter method: adaptive, and we use filter type 0 throughout
        0,  # interlace: none
    )
    # Filter type byte 0 (None) prefixes every scanline.
    raw = b"".join(b"\x00" + row for row in rows)

    # Compression parameters are pinned rather than defaulted so that the file bytes
    # depend on this call and not on whatever zlib happens to prefer.
    compressor = zlib.compressobj(6, zlib.DEFLATED, 15, 8, zlib.Z_DEFAULT_STRATEGY)
    compressed = compressor.compress(raw) + compressor.flush()

    parts = [_PNG_MAGIC, _chunk(b"IHDR", header)]
    for key, value in (text or {}).items():
        parts.append(_text_chunk(key, value))
    parts.append(_chunk(b"IDAT", compressed))
    parts.append(_chunk(b"IEND", b""))
    return b"".join(parts)
