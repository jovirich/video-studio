---
title: Hailuo
modality: video
vendor: hailuo
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Hailuo

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Subject consistency and strong image-to-video adherence to the source frame.

## Weak at

Camera control depth.

## Control surface

- Image-to-video
- Subject reference
- Motion prompt
- Duration

## Gotchas

- Holds the input frame's identity well, which makes it a good default for the still-to-motion chain.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: hailuo
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
