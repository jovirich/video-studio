---
title: Leonardo
modality: image
vendor: leonardo
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Leonardo

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Custom trained models for a locked house style; consistent series output.

## Weak at

Peak single-image fidelity against frontier models.

## Control surface

- Custom model training on your own references
- Elements / style adapters
- ControlNet-equivalent guidance
- Prompt magic

## Gotchas

- Training a model on your own approved stills is a strong continuity mechanism — and a rights question if any reference is third-party.
- A trained model is a production asset: version it and archive it with the season.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: leonardo
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
