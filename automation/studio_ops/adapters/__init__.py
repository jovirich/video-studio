"""Generation adapters.

One backend runs: `local.LocalImageAdapter`, an offline deterministic image
generator with no key, no network, and no cost. Every vendor backend is still a
deliberate stub — see `base` for the three preconditions that gate wiring one, and
for why generation refuses by default even when it is free.

    from studio_ops.adapters import GenerationRequest, get_adapter

    adapter = get_adapter("local").from_config(cfg, dry_run=False)
    result = adapter.generate(request)
    entry = result.to_generation_block()   # → asset_manifest.schema.json

Importing this package registers every backend, so `get_adapter` is always populated.

Maturity: local adapter IMPLEMENTED and TESTED; all vendor adapters NOT BUILT.
"""

from __future__ import annotations

from .base import (
    Adapter,
    AdapterError,
    AdapterNotBuiltError,
    BudgetExceededError,
    Capabilities,
    GenerationRequest,
    GenerationResult,
    IncompleteProvenanceError,
    StubAdapter,
    UnsupportedRequestError,
    default_operator,
    get_adapter,
    register,
    registered_adapters,
    sha256_file,
)
from .local import LocalImageAdapter
from .stubs import (
    ImageAdapter,
    MusicAdapter,
    TextAdapter,
    VideoAdapter,
    VoiceAdapter,
)

__all__ = [
    "Adapter",
    "AdapterError",
    "AdapterNotBuiltError",
    "BudgetExceededError",
    "Capabilities",
    "GenerationRequest",
    "GenerationResult",
    "ImageAdapter",
    "IncompleteProvenanceError",
    "LocalImageAdapter",
    "MusicAdapter",
    "StubAdapter",
    "TextAdapter",
    "UnsupportedRequestError",
    "VideoAdapter",
    "VoiceAdapter",
    "default_operator",
    "get_adapter",
    "register",
    "registered_adapters",
    "sha256_file",
]

from . import interactive  # noqa: F401  (registers the backend)
