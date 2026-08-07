---
title: Premiere Pro
modality: post
vendor: premiere
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Premiere Pro

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Editorial, Adobe ecosystem integration, caption workflows.

## Weak at

—

## Control surface

- Project structure conventions
- Caption creation and export
- Essential Graphics for text layers
- Media Encoder presets

## Gotchas

- Essential Graphics templates keep text layers separate and localisable — set this up before the first cut.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: premiere
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
