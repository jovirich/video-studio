---
title: 06_edit — assembly to picture lock
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [editor, visual-director]
---

# 06_edit

Where the assets become a cut. The stage the whole gate structure exists to protect,
because it is the stage at which everything that went wrong upstream becomes
expensive.

## What goes here

| Path | What it is | In git? |
|---|---|---|
| `project/` | NLE project files, one per cut version | Yes — they are small and their history matters |
| `edl/` | EDL / AAF / XML conform exports | Yes |
| `cuts/cut_v<NN>_notes.md` | What changed in each cut and why | Yes |
| `renders/` | Review renders and proxies | **No** — gitignored; they are derivable |
| `cache/` | NLE cache and rendered previews | **No** |

Cut versions are numeric: `cut_v01`, `cut_v02`. The version in the project filename,
the version in the render filename, and the version in the notes are the same
number, always. When they diverge, a note that says "fixed in v3" stops meaning
anything, and the fix stops being findable.

## Before this stage starts

- **Every asset on the timeline has a manifest entry.** `studio_ops pipeline conform`
  refuses a clip without one. This is not a warning to be dismissed: an asset with
  no manifest entry has no provenance, no rights status, and no label state, and it
  will be discovered at technical QC when the fix is a re-conform.
- **Generated clips are conformed to the delivery frame rate**, with the conform
  method recorded on the asset record. Tools output at their own native rates;
  `optical-flow` retiming leaves artefacts that survive grading and are checked for
  at picture lock. [../../../standards/delivery_specs.md](../../../standards/delivery_specs.md)
  § Picture.
- **Text layers are separate**, so a textless master is a render and not a rebuild.

## Before this stage can be left

The **picture lock** gate is signed by the Visual Director, certifying:

1. **The cut is final.** Not "final pending notes".
2. **Every generated shot passed the QC pass**: anatomy, anachronism, light
   consistency across cuts, skin-tone rendering, and temporal stability. These are
   checked shot by shot, not by watching the cut — a hand with the wrong number of
   fingers is invisible at speed and permanent at 4K.
3. **Every `reconstruction` and `interpretive` shot carries its in-frame label**,
   persistent for the full duration of the shot, inside title safe, contrast ≥ 3:1,
   legible at 360p, never obscured by a caption.
4. **The explainer card is placed** at the first labelled shot.
5. **Vertical and square safe zones hold** for every shot with critical content.
6. **No shot asserts anything the script does not.** A graphic, a map, or a
   juxtaposition can assert a claim the narration never made — adjacency reads as
   causation, and the viewer will not know which of the two the studio meant.

## Re-opening picture lock

Signed, then something changes. It happens; it is recorded rather than absorbed.

The gate returns to `pending`, the prior signature is retained in history, and
**every downstream gate signed on the basis of it returns to `pending` too** — audio
lock and technical QC among them. The cascade is the mechanism that makes a late
change feel like what it is, rather than like a small edit.
[../../../core/04_review_gate_framework.md](../../../core/04_review_gate_framework.md) §4.
