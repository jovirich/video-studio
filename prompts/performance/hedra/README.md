---
title: Hedra
modality: performance
vendor: hedra
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Hedra

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Character performance from a still and an audio track.

## Weak at

Subject to core's likeness prohibitions.

## Control surface

- Image plus audio to performance
- Expression and motion intensity
- Duration

## Gotchas

- Only for figures whose depiction and voice are both cleared. A historical figure fails this test in every pack — synthesising their speech is fabricated evidence.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: hedra
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
