---
title: CapCut
modality: post
vendor: capcut
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# CapCut

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Fast social cutdowns and vertical variants.

## Weak at

Colour accuracy and delivery control.

## Control surface

- Vertical reframe
- Auto-caption
- Templates

## Gotchas

- Cutdowns are DERIVED from a locked, gated master. A short-form piece making a claim absent from a gated production has bypassed the whole review system.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: capcut
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
