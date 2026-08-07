---
title: Claude
modality: text
vendor: claude
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Claude

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Long-context document work, structural critique, careful drafting assistance.

## Weak at

Not a source. Never a source.

## Control surface

- Long context for whole-document review
- Structured output for record extraction
- Explicit instruction to refuse fabrication
- Tool use for repository work

## Gotchas

- Best used adversarially: 'what would a hostile expert attack first?'
- Ask it to mark uncertainty explicitly rather than smoothing it.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: claude
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
