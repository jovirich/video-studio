---
title: DALL·E
modality: image
vendor: dall-e
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# DALL·E

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Instruction following and conversational iteration; good at compositional instructions.

## Weak at

Fine aesthetic control; consistency across a series.

## Control surface

- Natural-language iteration
- Inpainting via mask
- Size and quality

## Gotchas

- Prompts are often silently rewritten before generation. Capture the actual submitted prompt, not what you typed.
- Weak continuity tooling — pair with a stronger reference mechanism for recurring subjects.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: dall-e
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
