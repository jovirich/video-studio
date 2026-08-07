---
title: Runway Act
modality: performance
vendor: runway-act
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Runway Act

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Performance transfer from a driving video to a generated character.

## Weak at

Likeness constraints.

## Control surface

- Driving performance video
- Character target
- Expression fidelity

## Gotchas

- The driving performer is a contributor: credited and compensated, with consent covering this use.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: runway-act
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
