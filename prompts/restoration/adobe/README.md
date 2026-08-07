---
title: Adobe (Photoshop / Camera Raw)
modality: restoration
vendor: adobe
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Adobe (Photoshop / Camera Raw)

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Precise, controllable, non-generative correction — plus generative fill when wanted.

## Weak at

Manual.

## Control surface

- Non-generative: levels, dust, scratch, colour, perspective
- Generative fill and expand — a separate, logged act
- Content Credentials

## Gotchas

- The right tool for archival restoration precisely because the non-generative operations are separable from the generative ones. Keep them separate in the log.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: adobe
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
