---
title: Tripo
modality: scene3d
vendor: tripo
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Tripo

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Fast image-to-3D for props and objects.

## Weak at

Topology and fine detail.

## Control surface

- Image to mesh
- Text to mesh
- Texture generation

## Gotchas

- Useful for background props. For an artefact that is the subject of a shot, photogrammetry of the real object is better and more honest.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: tripo
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
