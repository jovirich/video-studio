---
title: Luma
modality: video
vendor: luma
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Luma

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Fast iteration and reliable start/end keyframe conditioning.

## Weak at

Peak fidelity.

## Control surface

- Start and end frame conditioning
- Loop
- Camera motion
- Extend

## Gotchas

- Start-and-end-frame conditioning is the most controllable path from an approved storyboard to motion — you specify both ends.
- Fast enough to iterate at the storyboard stage rather than after.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: luma
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
