---
title: Ideogram
modality: image
vendor: ideogram
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Ideogram

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Text rendering inside images — signage, titles, lettering — by a wide margin.

## Weak at

Photoreal texture and atmospheric subtlety.

## Control surface

- Text-focused prompting with quoted strings
- Magic prompt expansion — disable for controlled work
- Style presets, aspect ratio

## Gotchas

- For historical work, in-image text is a factual claim: script, language, and orthography must be verified before generation, not after.
- Prefer a graphics layer in post for anything that must be exactly right.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: ideogram
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
