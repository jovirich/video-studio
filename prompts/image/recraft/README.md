---
title: Recraft
modality: image
vendor: recraft
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Recraft

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Vector output, brand-consistent graphics, icon and illustration systems.

## Weak at

Photoreal scenes.

## Control surface

- Style sets trained on your references
- True vector (SVG) export
- Brand palette locking

## Gotchas

- The right tool for maps, diagrams, lower thirds, and title systems — output is editable rather than baked.
- Vector output drops cleanly into the graphics layer, which keeps textless masters cheap.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: recraft
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
