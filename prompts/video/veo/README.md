---
title: Veo
modality: video
vendor: veo
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Veo

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Prompt adherence, physical plausibility, and native synchronised audio.

## Weak at

Google stack dependency; availability varies by surface.

## Control surface

- Text-to-video and image-to-video
- Native audio generation
- Camera and style direction
- Resolution and duration

## Gotchas

- Native audio is convenient and a provenance complication — generated ambience is a claim about a place. Log it as a separate audio asset.
- Disable native audio when the mix is being built properly.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: veo
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
