---
title: Runway
modality: video
vendor: runway
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Runway

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Breadth of control — motion brush, camera parameters, keyframes — and a mature surrounding toolset.

## Weak at

Long-duration coherence against specialist rivals.

## Control surface

- Image-to-video with start frame
- Motion brush for region-specific movement
- Explicit camera controls: pan, tilt, zoom, roll, dolly
- Keyframe start/end conditioning
- Act/performance transfer (see ../performance/runway-act)

## Gotchas

- Motion brush is the most precise regional motion control widely available — use it instead of hoping prose describes the intent.
- Generate longer than the cut needs; trim the stable middle.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: runway
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
