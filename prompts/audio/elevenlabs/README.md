---
title: ElevenLabs
modality: audio
vendor: elevenlabs
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# ElevenLabs

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Narration quality, multilingual coverage, voice cloning, dubbing.

## Weak at

Cost at long-form scale; expressive range against a trained human read.

## Control surface

- Voice ID and model version — both recorded, both change the output
- Stability, similarity, style exaggeration, speaker boost
- Pronunciation dictionaries and phoneme tags — mandatory for proper nouns
- Dubbing with timing preservation

## Gotchas

- Pronunciation dictionaries are the difference between a series a region respects and one it mocks. Build one per production line and version it.
- A model version change alters the voice audibly mid-season. Pin the version and record it.
- Cloning requires documented consent covering synthetic reproduction specifically.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: elevenlabs
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
