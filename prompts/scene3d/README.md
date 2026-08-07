---
title: 3D and scene construction
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# 3D and scene construction

The underused half of the pipeline, and often the honest one.

## Why build geometry at all

Generative models have no spatial memory. Ask for the same courtyard from three
angles and you get three different courtyards. For any location that recurs across a
sequence — let alone across a season — that is fatal to continuity.

Building the geometry once and rendering every angle from it solves the problem
completely rather than mitigating it.

There is a second reason, specific to reconstruction work: **you can model only what
is evidenced.** If the roof form is unattested, you do not build a roof — you frame
below the roofline. A generative model will always invent one. Geometry makes the
limits of the evidence visible while you work, which is exactly when it is useful.

## Vendors

| Vendor | For |
|---|---|
| [blender](blender/) | General 3D: geometry, camera, light, physics. Free, scriptable. |
| [houdini](houdini/) | Procedural systems — crowds, water, fire, destruction, scattering |
| [gaussian-splatting](gaussian-splatting/) | Photoreal capture of real present-day places |
| [tripo](tripo/) · [meshy](meshy/) | Fast image-to-3D for background props |
| [unreal](unreal/) | Real-time previs, virtual camera, large environments |

## Where this beats generation

| Problem | Why geometry wins |
|---|---|
| Same location, many angles | One model, unlimited consistent views |
| Camera matching a storyboard | Set the camera; do not describe it and hope |
| Architecture from excavation | Build what is evidenced; frame around what is not |
| Water, fire, cloth, crowds | Simulation holds up; generated video does not |
| Maps and terrain | Real elevation data, correct projection |
| An object in a collection | Photogrammetry of the real object beats any generation |

## The hybrid pattern

The most productive use is not 3D *instead of* generation but 3D *conditioning*
generation:

```
build blocking geometry  ──►  render depth / normal / edge passes
                                        │
                                        ▼
                          structure-condition the image model
                                        │
                                        ▼
                        approved still  ──►  motion  ──►  grade
```

Geometry supplies spatial truth and camera control; the image model supplies surface,
light quality, and texture. Neither does the other's job well.

Recipe: [../chains/geometry_conditioned.md](../chains/geometry_conditioned.md).

## Provenance

A 3D render is a generated asset. It carries a manifest entry, a prompt-card-equivalent
record of the scene file and render settings, and — where it depicts a real place or
period — an evidence basis like any other reconstruction.

**A gaussian splat of a real present-day location is `contemporary`, not
`reconstruction`.** It is a capture, not a depiction. Classify it correctly; the
labelling obligation differs.

## Asset licensing

Marketplace models, HDRIs, textures, and scan libraries carry licences that vary by
item, not by store. Film and broadcast use is frequently excluded from the default
tier. Each asset used in a deliverable is recorded in the clearance log like any
third-party material.

Camera and lens settings come from the production's defined lens set — the same set
the prompt cards inherit. Matching them is what makes a 3D render and a generated
still read as the same production.
