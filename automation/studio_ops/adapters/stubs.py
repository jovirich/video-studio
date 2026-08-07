"""Per-modality adapter stubs.

Each names the specific precondition that is missing, so the gap is legible rather
than a generic "not implemented". See base.py for why these refuse by design.

Registered under their modality names, so `get_adapter("video")` returns the stub and
its refusal, rather than a KeyError that says nothing about why. A caller asking for
video by name deserves the reason.

`local.LocalImageAdapter` is registered as "local" and is the one backend that runs.
It does not replace `ImageAdapter`: this stub stands for a *vendor* image backend,
whose preconditions are still unmet.
"""

from __future__ import annotations

from .base import StubAdapter, register


@register("image")
class ImageAdapter(StubAdapter):
    modality = "image"
    vendor = "generic-image"
    reason = (
        "Requires: a per-vendor renderer in promptlib, the manifest write path, and "
        "the vendor's commercial terms verified for the studio's plan tier."
    )


@register("video")
class VideoAdapter(StubAdapter):
    modality = "video"
    vendor = "generic-video"
    reason = (
        "Requires the image adapter first — the still-to-motion chain conditions "
        "motion on an approved still, and generating motion from an unreviewed frame "
        "inverts the cost curve."
    )


@register("audio_voice")
class VoiceAdapter(StubAdapter):
    modality = "audio_voice"
    vendor = "generic-voice"
    reason = (
        "Requires a pronunciation lexicon for the production line and a voice licence "
        "whose consent covers synthetic reproduction. Neither exists yet."
    )


@register("audio_music")
class MusicAdapter(StubAdapter):
    modality = "audio_music"
    vendor = "generic-music"
    reason = (
        "Blocked on the studio's AI-music policy decision. The default pending that "
        "decision is: abstract texture permitted, pastiche of a living tradition "
        "prohibited."
    )


@register("text")
class TextAdapter(StubAdapter):
    modality = "text"
    vendor = "generic-text"
    reason = (
        "Research assistance only. Model output is never a source, and no adapter may "
        "write to a claim record."
    )


REGISTRY: dict[str, type[StubAdapter]] = {
    "image": ImageAdapter,
    "video": VideoAdapter,
    "audio_voice": VoiceAdapter,
    "audio_music": MusicAdapter,
    "text": TextAdapter,
}
