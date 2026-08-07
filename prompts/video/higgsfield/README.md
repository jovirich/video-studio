---
title: Higgsfield
modality: video
vendor: higgsfield
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Higgsfield

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Camera-move presets — crash zooms, orbits, whip pans — as first-class controls.

## Weak at

General-purpose fidelity.

## Control surface

- Named camera-move presets
- Image-to-video
- Motion intensity

## Gotchas

- Preset moves are stylised by design. In documentary work most of them read as promotional; use sparingly and with a stated motivation.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: higgsfield
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
