---
title: Imagen
modality: image
vendor: imagen
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Imagen

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Photorealism and prompt adherence; strong on people and natural scenes.

## Weak at

Tied to the Google stack; availability and terms vary by surface.

## Control surface

- Aspect ratio, person generation controls
- Negative prompting
- Safety filter levels

## Gotchas

- Terms differ between the consumer surface and the Cloud API. Record which was used.
- Person-generation restrictions vary by region and tier.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: imagen
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
