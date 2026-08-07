---
title: Pika
modality: video
vendor: pika
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Pika

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Stylised motion, effects, quick turnaround.

## Weak at

Photoreal human motion.

## Control surface

- Image-to-video
- Region-specific modification
- Effects presets
- Lip sync

## Gotchas

- Useful for graphic and interpretive shots rather than depictive reconstruction.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: pika
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
