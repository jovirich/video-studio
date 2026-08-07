---
title: Perplexity
modality: text
vendor: perplexity
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Perplexity

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Search with citations.

## Weak at

Citations are pointers, not verification.

## Control surface

- Search with source links
- Focus modes
- Follow-up refinement

## Gotchas

- **Follow every citation to the actual document.** The tool can cite a real source that does not say what the summary claims.
- Excellent for finding where to look. Never for what is true.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: perplexity
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
