---
chain: voice_and_mix
version: 1.0.0
status: active
updated: 2026-08-07
owners: [audio-lead]
---

# Chain — voice through to stems

Narration from locked script to delivered stems.

## Steps

| # | Step | Tool | Notes |
|---|---|---|---|
| 1 | Script lock | human | No VO before the script is locked. Re-recording is cheap; re-cutting around new VO is not. |
| 2 | Extract proper nouns | `studio_ops report pronunciation` | Every name in the script, automatically, into the VO record sheet **[NOT BUILT]** |
| 3 | IPA and reference recordings | human, speaker of the language | **Mandatory.** A tonal language mispronounced by tone is a different word — a factual error, not a stylistic one. |
| 4 | Build pronunciation lexicon | [elevenlabs](../audio/elevenlabs/) or equivalent | Versioned per production line, reused across the season |
| 5 | Record or synthesise | human VO, or licensed synthetic voice | If synthetic: voice ID, model, and version all pinned and recorded |
| 6 | Pronunciation check | human, speaker of the language | Against the reference recordings. A named person on the gate, not a general responsibility. |
| 7 | Edit and time to picture | [resolve](../post/resolve/) / [premiere](../post/premiere/) | |
| 8 | Ambience and SFX | library, foley, generated | Ambience is a claim about a place — period and species checked |
| 9 | Music | commissioned / licensed / generated per pack policy | Cue sheet entry for every cue, from production one |
| 10 | Mix | [resolve](../post/resolve/) Fairlight | Targets in [delivery_specs](../../standards/delivery_specs.md) |
| 11 | Render stems | same | VO, testimony, music, ambience, SFX, **M&E** |
| 12 | Captions | [descript](../post/descript/) draft → human correction | Corrected against the script and the VO record sheet |

## Steps 2–4 and 6 are the ones that get skipped

They are also the difference between a series a region respects and one it mocks.
Mispronounced names are read — correctly — as evidence that nobody from the place was
in the room, and no amount of production value recovers from that in the first thirty
seconds.

Budget the time. It is not large, and it is not optional.

## The M&E stem

Rendered from production one, even with no localisation deal in sight. Retrofitting it
later costs more than producing it correctly the first time, and the retrofit always
lands under deadline.

## Model version pinning

A synthetic voice changes audibly when the vendor updates the model. Pin the version,
record it on every card, and re-check before any pickup session. A season where
episode 6 sounds like a different narrator is a real and avoidable failure.

## Prohibited

- Synthesising a real or historical person's voice ([core/01 §2](../../core/01_provenance_and_ai_disclosure.md))
- Voice-synthesis editing applied to a contributor's testimony
- Shipping uncorrected auto-captions
- Sacred or ceremonial music as underscore

## Provenance

Every generated audio asset — narration, ambience, SFX, music — carries a manifest
entry with tool, model, version, seed or generation ID, and prompt card. The
pronunciation lexicon is archived with the production line, not the production, since
it is reused.
