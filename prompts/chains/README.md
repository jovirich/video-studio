---
title: Chains
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, pipeline-engineer]
---

# Chains

A **chain** is a multi-tool recipe: a sequence of generation and processing steps that
together produce one finished asset. Chains are named, versioned records so that a
shot's full lineage is reproducible, not just its final prompt.

## Why name them

Most finished shots are not one generation. A typical reconstruction shot is:

```
storyboard frame → structure conditioning → still generation → selection
    → upscale → motion → conform → grade
```

Seven steps, four tools. Without a named chain, that lineage lives in someone's head
and the shot cannot be rebuilt or explained. With one, the shot record says
`chain: still_to_motion@1.2.0` and the manifest carries each step.

## Available chains

| Chain | For |
|---|---|
| [still_to_motion.md](still_to_motion.md) | The default path for any moving reconstruction shot |
| [geometry_conditioned.md](geometry_conditioned.md) | Where spatial continuity or camera control matters |
| [archival_restoration.md](archival_restoration.md) | Genuine archival material — deliberately non-generative |
| [map_and_graphic.md](map_and_graphic.md) | Maps, timelines, data graphics |
| [voice_and_mix.md](voice_and_mix.md) | Narration through to stems |

## Chain record

```yaml
chain: still_to_motion
version: "1.2.0"
steps:
  - { id: 1, tool: blender,     action: render_depth_pass,  optional: true }
  - { id: 2, tool: flux,        action: generate_still,     card: PC-... }
  - { id: 3, tool: human,       action: select_and_assess,  rubric: evaluation_rubric }
  - { id: 4, tool: topaz,       action: upscale }
  - { id: 5, tool: kling,       action: image_to_video,     card: PC-... }
  - { id: 6, tool: studio_ops,  action: conform,            target_fps: 24 }
  - { id: 7, tool: resolve,     action: grade,              lut: show_lut_v3 }
```

Every step writes a `post_process` entry on the asset. The manifest ends up holding
the full lineage without anyone assembling it by hand.

## Rules

1. **A human assessment step is mandatory** in every chain that ends in a
   deliverable. There is no fully automatic path from prompt to timeline.
2. **Assess before you spend.** Put selection before the expensive steps — upscaling
   and animating an image you then reject is the most common waste in the pipeline.
3. **Chains are versioned.** Changing a step bumps the version. Shots record which
   version made them, because a chain change is a look change.
4. **Cost accumulates per chain**, and is recorded per step, so cost per finished
   second is knowable rather than guessed.
5. **A chain never crosses the archival boundary.** Generative steps do not appear in
   [archival_restoration.md](archival_restoration.md), and that chain is separate
   precisely so the boundary is structural rather than remembered.

## Authoring a chain

Start from an existing one. A new chain is justified when the *step sequence* differs
— not when the tools do. Swapping the image model inside `still_to_motion` is a
parameter, not a new chain.
