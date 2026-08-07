---
title: Meshy
modality: scene3d
vendor: meshy
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Meshy

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Image and text to 3D with usable textures.

## Weak at

Precision.

## Control surface

- Image to 3D
- Text to 3D
- PBR texture generation
- Remesh

## Gotchas

- Same caution as Tripo: background props yes, subject artefacts no.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: meshy
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
