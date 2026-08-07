---
title: GPT
modality: text
vendor: gpt
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# GPT

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

General assistance, structured extraction, broad task coverage.

## Weak at

Not a source.

## Control surface

- Structured output / JSON mode
- Function calling
- Long context

## Gotchas

- Structured output mode is the useful one here — extracting a document you have read into a record schema.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: gpt
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
