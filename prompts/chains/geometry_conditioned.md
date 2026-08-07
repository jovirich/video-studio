---
chain: geometry_conditioned
version: 1.0.0
status: active
updated: 2026-08-07
owners: [visual-director]
---

# Chain — geometry-conditioned generation

For shots where **spatial continuity or camera control matters more than speed**: a
location seen from several angles, a camera move that must match a storyboard, an
architectural reconstruction whose limits must be visible.

## Why

Generative models have no spatial memory. The same courtyard prompted three times is
three different courtyards. For a recurring location that is fatal, and no amount of
prompt discipline fixes it.

Building the geometry once solves it rather than mitigating it — and, for
reconstruction work, it does something a prompt cannot: **it makes you build only
what is evidenced.** If the roof form is unattested you do not model a roof; you frame
below the roofline. A model will always invent one, confidently.

## Steps

| # | Step | Tool | Notes |
|---|---|---|---|
| 1 | Assemble evidence | human | Excavation reports, standing structures, contemporary descriptions. Unattested elements listed explicitly on the location record. |
| 2 | Block geometry | [blender](../scene3d/blender/) / [unreal](../scene3d/unreal/) | Only what is evidenced. Grey blocking is enough. |
| 3 | Set camera | same | From the production's defined lens set. This is the shot's real camera. |
| 4 | Render conditioning passes | same | Depth, normal, edge. Also a grey render for reference. |
| 5 | Condition generation | [stable-diffusion](../image/stable-diffusion/) ControlNet, or [flux](../image/flux/) | Structure locked; surface, light quality, and texture free |
| 6 | Assess and select | human | [evaluation_rubric.md](../_framework/evaluation_rubric.md) |
| 7 | Motion | [luma](../video/luma/) start/end frames, or render the camera move in 3D | Either path; record which |
| 8 | Conform and grade | `studio_ops`, [resolve](../post/resolve/) | |

## What each layer contributes

| Layer | Supplies |
|---|---|
| Geometry | Space, scale, camera, occlusion, spatial continuity, evidential honesty |
| Generation | Surface, material, light quality, atmosphere, texture |

Neither does the other's job well. The value of the chain is the division of labour.

## When it is worth the cost

- A location appears in more than three shots
- A camera move must match an approved storyboard exactly
- Architectural accuracy is load-bearing for the shot's claim
- Repeated attempts at a prompted version keep failing on geometry

## When it is not

A single atmospheric wide shot. Blocking geometry for one shot rarely pays back.

## Provenance

The scene file is an asset, archived with the production. Renders carry the scene
file's ID and version. The location record lists the unattested elements that were
deliberately not modelled — which is the durable output of step 1, and useful to
every future production that touches the same place.
