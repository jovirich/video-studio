---
title: Blender
modality: scene3d
vendor: blender
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Blender

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Full 3D control: geometry, camera, light, physics. Free and scriptable.

## Weak at

Time cost; requires 3D skill.

## Control surface

- Python scripting for procedural generation
- Camera and lens matching to the production's lens set
- Physical light units
- Geometry nodes
- Render passes for compositing

## Gotchas

- The reliable answer to spatial and camera continuity: build the geometry once, render every angle from it.
- Also the honest tool for architectural reconstruction — you can model only what is evidenced and frame around what is not.
- Renders are still generated assets and carry manifest entries.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: blender
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
