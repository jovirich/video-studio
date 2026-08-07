---
title: TBD — shooting script for the production
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [story-producer, visual-director]
episode: S00E00
line: xx-line-code
stage: 02_script
gate_blocking: script_lock
---

# Shooting script — TBD — production working title

> Copy this file to `shooting_script_v01.md`; do not fill it in place.

Narration against picture, sequence by sequence. This is the document the shot list
in [../03_storyboard/](../03_storyboard/) is derived from, and the one the edit is
conformed against.

## Conventions

| | |
|---|---|
| Two columns | Picture left, sound right. What a reader can check is whether the two halves are about the same thing. |
| Claim references | Carried through from the narration, unchanged. Never re-typed — copy them, so a claim ID cannot drift between two documents. |
| Provenance class | Stated on every picture cell. It determines whether a label is required and what may be said about the shot in the description. |
| Shot IDs | Allocated at storyboard, then written back here. Absent at first pass; that is expected. |
| Timecode | Approximate until picture lock. Do not tidy it; a precise-looking estimate invites planning against it. |

Provenance classes, and what each commits the production to:

| Class | Means | Consequence |
|---|---|---|
| `archival` | A genuine historical item, reproduced | May never be generated. May never have its content altered. |
| `contemporary` | Shot in the present day | Must not be cut to read as period material |
| `artefact` | An object photographed in a collection | Needs a credit line in the exact words the holder requires |
| `reconstruction` | A depiction built from evidence | Requires an evidence basis and an in-frame label |
| `interpretive` | A visual figure for something not directly depictable | Requires an in-frame label |
| `graphic` | Map, chart, timeline | Asserts, therefore carries claim IDs |
| `text_on_screen` | Quotation or title | Asserts, therefore carries claim IDs |

---

## SEQ-XX-S00E00-001 — TBD — sequence handle

**Runtime:** TBD **Function in the argument:** TBD — the move this sequence makes

| # | Picture | Sound |
|---|---|---|
| TBD — `SHT-XX-S00E00-0000` | TBD — what the viewer sees, written so an editor who has not read the script understands it.<br>*Class:* TBD *Label:* TBD — required / not required | **VO:** TBD — narration text. {{CLM-XX-0000}}<br>**Ambience:** TBD — note that ambience asserts what a place sounded like, and is therefore reconstruction<br>**Music:** TBD — cue handle, or `none` |
| TBD | TBD | TBD |

**Sequence notes:** TBD — anything the editor needs that the table cannot carry:
intended pace, a deliberate silence, a hold on a frame.

---

## SEQ-XX-S00E00-002 — TBD — sequence handle

**Runtime:** TBD **Function in the argument:** TBD

| # | Picture | Sound |
|---|---|---|
| TBD | TBD | TBD |

---

## Cross-cutting requirements

**Reconstruction explainer card.** The first reconstruction or interpretive shot in
the production is preceded by an explainer card. Its position: TBD — sequence and
shot. Its wording: [../10_publish/credits_ai_statement.md](../10_publish/credits_ai_statement.md)
carries the reusable block.

**Safe zones.** Every shot with critical information is checked against the 9:16 and
1:1 centre crops at storyboard, not at delivery.
[../../../standards/delivery_specs.md](../../../standards/delivery_specs.md) has the
percentages. A shot that fails here becomes a re-generation; a shot that fails at
delivery becomes a re-generation plus a missed date.

**On-screen text legibility.** Minimum 1/20 frame height, contrast measured rather
than eyeballed, held for twice the reading time. Text layers stay separate in the
NLE so a textless master is a render and not a rebuild.

**Language and orthography.** Diacritics are correct in the content and absent from
the filename. The font set must cover every diacritic used across the production —
checked once, at this stage, because discovering a missing glyph during the grade is
a re-render of every title in the episode.
