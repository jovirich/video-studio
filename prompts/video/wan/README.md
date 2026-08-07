---
title: Wan
modality: video
vendor: wan
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Wan

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Open weights — local execution, customisation, no data leaving the building.

## Weak at

Requires infrastructure; slower iteration.

## Control surface

- Local deployment
- Fine-tuning and LoRA
- Full parameter access
- Image-to-video

## Gotchas

- The correct choice when source material is restricted or community-controlled and cannot go to a third-party endpoint.
- Record model hash and full environment — reproducibility depends on more than the seed.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: wan
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
