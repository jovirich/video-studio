---
title: FLUX
modality: image
vendor: flux
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# FLUX

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Prompt adherence, anatomy (notably hands), legible in-image text, natural-language prompting.

## Weak at

Plainer default aesthetic — it will not flatter a weak prompt.

## Control surface

- Guidance scale — mid-range beats maximum
- Steps — find the plateau once per model and record it
- LoRA adapters for trained style or character consistency
- ControlNet-style structure conditioning where the deployment supports it
- Available open-weight and hosted; deployment choice affects terms

## Gotchas

- Responds well to full sentences rather than comma-separated tags.
- Open-weight deployment changes the rights position — record which you used.
- Different distributions (dev / pro / schnell) have different licences. Check per variant.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: flux
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
