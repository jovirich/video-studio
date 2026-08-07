---
title: Unreal Engine
modality: scene3d
vendor: unreal
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Unreal Engine

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Real-time rendering, virtual camera, large environments, previs.

## Weak at

Project weight and setup cost.

## Control surface

- Sequencer for camera work
- Nanite and Lumen
- Virtual camera
- Environment assembly
- Movie Render Queue for final frames

## Gotchas

- Strong for previs: block a sequence in 3D, then use the frames as structure references for generation.
- Marketplace asset licences must permit film use — check per asset, not per store.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: unreal
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
