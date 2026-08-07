---
title: Resemble
modality: audio
vendor: resemble
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Resemble

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Voice cloning with consent-oriented tooling; real-time synthesis.

## Weak at

Ecosystem breadth.

## Control surface

- Voice cloning with consent capture
- Real-time API
- Emotion and style control
- Localisation

## Gotchas

- Consent workflow tooling is genuinely useful, but the studio's own consent record remains the authority.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: resemble
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
