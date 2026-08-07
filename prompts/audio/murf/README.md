---
title: Murf
modality: audio
vendor: murf
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Murf

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Stock narration voices for temp tracks and utility work.

## Weak at

Distinctive or emotionally specific delivery.

## Control surface

- Voice library
- Pace and pitch
- Emphasis markers

## Gotchas

- Fine for temp narration during edit. A temp track that survives to delivery is a failure of process, not of the tool.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: murf
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
