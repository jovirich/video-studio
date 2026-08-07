---
title: After Effects
modality: post
vendor: after-effects
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# After Effects

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Motion graphics, maps, timelines, data graphics, the reconstruction label.

## Weak at

—

## Control surface

- Expression-driven data graphics
- Map animation
- Title and lower-third systems
- The persistent label overlay
- Essential Graphics export

## Gotchas

- Data graphics built here must follow standards/data_graphics.md — no truncated axes, uncertainty shown, sources in frame.
- Build the label overlay once as a template so it is identical across every production.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: after-effects
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
