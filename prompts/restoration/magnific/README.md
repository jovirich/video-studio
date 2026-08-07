---
title: Magnific
modality: restoration
vendor: magnific
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Magnific

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Creative upscaling with detail synthesis.

## Weak at

Explicitly hallucinates detail — that is the feature.

## Control surface

- Creativity and HDR sliders
- Resemblance control
- Prompt-guided upscaling

## Gotchas

- **Never on archival material.** This tool adds detail that was never present. On generated reconstruction it is acceptable and logged; on evidence it is fabrication.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: magnific
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
