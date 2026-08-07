---
title: Gaussian splatting
modality: scene3d
vendor: gaussian-splatting
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Gaussian splatting

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Photoreal capture of real places from photography; free camera movement through a captured space.

## Weak at

Requires good capture; struggles with reflective and transparent surfaces.

## Control surface

- Capture from photo or video sets
- Free camera path through the scene
- Export to standard pipelines

## Gotchas

- The strongest option for present-day site footage: capture a real location once, then move a virtual camera through it as the edit requires.
- Provenance class is `contemporary`, not `reconstruction` — it is a capture of a real place.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: gaussian-splatting
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
