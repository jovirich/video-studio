---
title: HeyGen
modality: performance
vendor: heygen
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# HeyGen

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Presenter video and multilingual dubbing with lip sync.

## Weak at

Likeness constraints.

## Control surface

- Avatar from consented capture
- Translation with lip sync
- Voice cloning

## Gotchas

- Legitimate for a consenting presenter across languages. The consent must explicitly cover synthetic reproduction and each target language.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: heygen
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
