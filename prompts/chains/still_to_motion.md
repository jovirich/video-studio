---
chain: still_to_motion
version: 1.0.0
status: active
updated: 2026-08-07
owners: [visual-director]
---

# Chain — still to motion

The default path for any moving generated shot. Use this unless there is a reason not
to.

## Why not text-to-video directly

Text-to-video hands composition, light, palette, subject, period detail, and motion to
the model in a single request. Every one of those is a place it can go wrong, and you
find out only after paying for a clip.

Image-to-video hands it a frame that has already been **reviewed, corrected, and
approved**, and asks for one thing: motion.

Three consequences, all good:

1. **Review happens on a still**, which is far easier to assess than a clip — and it
   happens before the expensive step.
2. **Iteration is cheap.** Fixing a composition problem costs one still, not one clip.
3. **The sensitivity and anachronism gates get something concrete** to look at before
   generation of the moving asset.

## Steps

| # | Step | Tool | Notes |
|---|---|---|---|
| 1 | Storyboard frame | human / [after-effects](../post/after-effects/) | Composition decided by a person, in the production's aspect ratio, with safe zones marked |
| 2 | *(optional)* Structure conditioning | [blender](../scene3d/blender/) or ControlNet | Where the frame must match precisely. See [geometry_conditioned.md](geometry_conditioned.md). |
| 3 | Generate still | [flux](../image/flux/) / [midjourney](../image/midjourney/) / [stable-diffusion](../image/stable-diffusion/) | Batch. Prompt card required. |
| 4 | **Assess and select** | human | [evaluation_rubric.md](../_framework/evaluation_rubric.md), in order. Record every run including rejections. |
| 5 | *(optional)* Correct | [adobe](../restoration/adobe/) | Inpaint a local failure rather than regenerating the whole frame |
| 6 | Upscale | [topaz](../restoration/topaz/) | Only after selection. Logged. |
| 7 | Generate motion | [kling](../video/kling/) / [runway](../video/runway/) / [hailuo](../video/hailuo/) | Image-to-video from the approved still. One action. |
| 8 | Assess clip | human | Temporal stability across the whole clip, not frame one |
| 9 | Conform | `studio_ops` | To delivery frame rate; method recorded |
| 10 | Grade | [resolve](../post/resolve/) | Under the show LUT, never around it |

## Where it goes wrong

| Symptom | Cause | Fix |
|---|---|---|
| Clip drifts from the still | Motion strength too high, or duration too long | Lower motion; shorten; cut around it |
| Identity changes mid-clip | Model duration limit exceeded | Plan the cut shorter. Do not extend. |
| Beautiful still, unusable clip | Composition too dependent on fine detail | Reframe wider at step 1 |
| Cost overrun | Upscaling and animating before selection | Move assessment earlier — this is step 4 for a reason |
| Sequence looks incoherent | Style anchor not applied at step 3 | Anchors are not optional |

## Cost shape

Steps 6 and 7 dominate. Everything before step 4 should be cheap and disposable;
everything after should run only on approved material. If your spend is concentrated
before step 4, the chain is being run backwards.

## Provenance

Two prompt cards (still and motion) and one asset record with a `post_process` array
covering upscale, conform, and grade. The still is retained as its own asset — it is
frequently reusable, and it is the evidence of what was approved.
