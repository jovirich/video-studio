---
title: DaVinci Resolve
modality: post
vendor: resolve
status: active
checked: 2026-08-07
owners: [pipeline-engineer]
---

# DaVinci Resolve

> Cheat sheet. Vendors change models, parameters, and terms frequently and without
> notice. `checked` above is the last verification date; `studio_ops validate
> --prompts` flags a sheet older than 90 days as stale.

## Good at

Grade, conform, edit, finish, deliver. Colour management for the whole pipeline.

## Weak at

—

## Control surface

- Show LUT / colour management for the production
- Node-based grading
- Fusion for compositing and labelling
- Fairlight for mix and stems
- Deliver presets matched to standards/delivery_specs.md
- Scripting API

## Gotchas

- The show LUT lives in library/luts/ and is versioned. Shot grading works UNDER it, never around it.
- Keep on-screen text in separate layers so a textless master is a render, not a rebuild.
- Build delivery presets from the spec once, and use them — hand-set exports drift.

## Before generating with this tool

- [ ] Terms current in [model terms register](../../../rights/permissions/model_terms_register.md)
- [ ] Commercial use permitted at the plan tier the studio holds
- [ ] Training-on-inputs position known, and acceptable for this material
- [ ] Prompt card exists and has passed its pack's pre-generation review
- [ ] Cost ceiling for the production not exceeded

## Prompt card target

```yaml
tool:
  vendor: resolve
  model: TBD
  version: TBD
  terms_checked: TBD
```

Craft guidance for this modality: [../README.md](../README.md).
Card structure: [../../_framework/prompt_anatomy.md](../../_framework/prompt_anatomy.md).
