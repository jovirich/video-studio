---
title: Houdini
modality: scene3d
vendor: houdini
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Houdini

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Procedural systems: crowds, destruction, water, particles, scattering.

## Weak at

Steep learning curve.

## Control surface

- Procedural node graphs
- Crowd simulation
- Fluid and pyro
- Scattering for vegetation and settlements

## Gotchas

- Where a generated video model fails — water, fire, crowds — this is the alternative that holds up under scrutiny.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: houdini
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
