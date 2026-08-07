---
title: Adobe Firefly
modality: image
vendor: firefly
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Adobe Firefly

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Commercially-licensed training data and enterprise indemnity; Adobe ecosystem integration.

## Weak at

Conservative outputs; content filters can block legitimate historical subject matter.

## Control surface

- Structure and style reference
- Generative fill and expand inside Photoshop
- Content Credentials applied automatically
- Style presets

## Gotchas

- The indemnity position is a genuine differentiator for commercial delivery — but it is tier-dependent. Record which tier the studio holds.
- Filters may refuse violence, weapons, or human remains that a documentary legitimately needs. Plan an alternative.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: firefly
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
