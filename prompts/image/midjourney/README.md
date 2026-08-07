---
title: Midjourney
modality: image
vendor: midjourney
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# Midjourney

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Aesthetic coherence, light quality, texture, painterly and photographic surface.

## Weak at

Literal prompt adherence at detail level; legible text; precise composition control.

## Control surface

- Style reference (`--sref`) — the primary continuity lever; pin one per sequence
- Character reference (`--cref`) with a weight for identity strength
- Stylise — raise for beauty, lower for adherence. Documentary work wants low.
- Weird / chaos — exploration only; never on an approved shot
- Aspect ratio, quality, tile, no-parameter negatives

## Gotchas

- Strong house aesthetic. Left at defaults it imposes a look on everything, which is exactly what breaks a defined visual identity.
- Prompt order matters; earlier tokens dominate.
- Permalinks are not provenance. Record seed, version, and full parameters in the manifest.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: midjourney
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
