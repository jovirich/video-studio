---
title: Gemini
modality: text
vendor: gemini
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Gemini

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Very long context; multimodal document and video review.

## Weak at

Not a source.

## Control surface

- Long context
- Multimodal input including PDF and video
- Structured output

## Gotchas

- Useful for a first pass over a large scanned collection to locate what is worth reading properly. The reading is still yours.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: gemini
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
