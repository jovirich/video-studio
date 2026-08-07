---
title: 03_storyboard — shot list and shot records
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# 03_storyboard

Where the shooting script becomes an enumerated, individually addressable set of
shots. Nothing is generated until each shot exists as a record here, because a shot
that has not been specified cannot be reviewed, and an unreviewed generated shot is
how a production acquires an image it then has to argue about.

## What goes here

| File | Template | What it is |
|---|---|---|
| `shotlist.csv` | [_TEMPLATE_shotlist.csv](_TEMPLATE_shotlist.csv) | The whole production, one row per shot. The working view. |
| `shots/SHT-XX-S00E00-0000.yaml` | [_TEMPLATE_shot.yaml](_TEMPLATE_shot.yaml) | One record per shot. The authoritative form. |
| `boards/` | — | Board frames, safe-zone overlays. Images: asset store, not git. |

The CSV and the YAML records hold the same fields — the CSV header is generated from
[../../../standards/schemas/shot.schema.json](../../../standards/schemas/shot.schema.json).
The CSV exists because a shot list is read across, and the YAML exists because a
shot is validated, referenced, and signed individually. When they disagree, the YAML
is right; `studio_ops` regenerates the CSV from the records rather than the reverse.

## Reading the CSV

The header row is the flattened field set of the shot schema: nested objects become
dotted columns (`camera.size`, `review.picture_lock`), and list-valued columns
(`owners`, `claims`, `entities.*`, `audio.sfx`, `generation.prompt_cards`) hold
`|`-separated values. Empty means absent, not `none` — the two are different, and a
column that conflates them cannot be validated.

The template ships with one placeholder row using obviously-fake IDs
(`XX`, `S00E00`, `0000`). Delete it before the first real shot.

## Before this stage starts

- **Script lock is signed.** Boarding an unlocked script produces shots for lines
  that will not survive the pass, and those shots get generated anyway because they
  exist.
- Sequence anchors in the narration are stable. A shot's `narration_ref` points at
  one; renaming anchors afterwards breaks the join silently.

## Before this stage can be left

There is no gate of its own — this stage feeds picture lock — but the following must
be true before [04_prompts](../04_prompts/) begins:

1. **Every shot has an ID and a record.** IDs are allocated by the toolkit.
2. **Every shot has a provenance class**, and it is honest. The class decides
   whether a label is required and what may be said about the shot in public.
3. **Every `graphic` and `text_on_screen` shot carries claim IDs.** A map asserts an
   extent; a timeline asserts a sequence and, by adjacency, a causal relation; a
   chart asserts a quantity. The schema requires claims on these classes for that
   reason. See [../../../standards/data_graphics.md](../../../standards/data_graphics.md).
4. **Every `reconstruction` and `interpretive` shot has `label_required: true`.**
   The schema enforces it; the point of enforcing it here is that the label is
   designed into the frame rather than pasted over it later.
5. **Every non-static camera movement has a stated motivation.** Unmotivated drift
   is the signature tell of generated video, and it accumulates one shot at a time
   because each individual instance looks fine.
6. **Safe zones are marked.** 9:16 and 1:1 centre crops, per
   [../../../standards/delivery_specs.md](../../../standards/delivery_specs.md).
   A shot whose critical content sits outside the vertical crop is a re-generation,
   and finding that out at delivery costs a date.

## Sequences

Sequence IDs use a three-digit serial (`SEQ-XX-S00E00-001`); shots use four
(`SHT-XX-S00E00-0000`). The difference is deliberate — it makes a mistyped ID fail
the pattern check rather than resolve to the wrong record.
