---
title: TBD — cut notes
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [editor, visual-director]
episode: S00E00
line: xx-line-code
stage: 08_review
gate_blocking: picture_lock
---

# Cut notes — TBD — cut version

> Copy this file to `cut_notes_v<NN>.md`; do not fill it in place.

## Session

| | |
|---|---|
| Cut version | TBD — `cut_v01`; the same number as the project file and the render |
| Render viewed | TBD — filename and duration, so it is clear what was watched |
| Date | TBD — ISO |
| Present | TBD — names and roles |
| Viewing conditions | TBD — calibrated display / laptop / phone. It changes what people notice. |

*Why viewing conditions are recorded:* half the notes on a first assembly are about
things visible only on a large calibrated display, and half of the notes on the
label legibility are only correct on a phone. Knowing which room a note came from is
how you tell a real defect from a room artefact.

## How to write a note

A note names a **locator**, a **problem**, and — where the writer has one — a
**proposal**. It does not name a solution and leave the problem implicit.

> "Shot 042 loses the wall's scale because there's nothing human in frame" is a
> note. "Add a figure to 042" is an instruction that will be followed even if it is
> the wrong fix for the right problem.

Every note gets a disposition. A note with no disposition is a note somebody will
raise again at the next screening, and the second raising costs the same as the
first.

## Notes

| # | TC | Locator | Note | Type | Raised by | Disposition | Owner |
|---|---|---|---|---|---|---|---|
| 1 | TBD | TBD — `SHT-XX-S00E00-0000` | TBD | TBD | TBD | TBD — actioned / declined, with reason / deferred to `v<NN>` | TBD |

Types, because they route to different people and different gates:

| Type | Goes to | Blocks |
|---|---|---|
| `story` | Story Producer | picture lock |
| `picture` | Visual Director / editor | picture lock |
| `generated-shot QC` | Visual Director | picture lock |
| `label` | Visual Director | picture lock |
| `sound` | Audio Lead | audio lock |
| `pronunciation` | Audio Lead | audio lock |
| `fact` | Research Lead | fact-check |
| `sensitivity` | Cultural Advisor | sensitivity — **and freezes the item immediately** |
| `rights` | Rights & Clearances | rights |
| `technical` | Pipeline Engineer | technical QC |

A `fact` note found in a screening is a fact-check finding and belongs on the
fact-check report as well. It does not get resolved in a cut-notes table, because
the fact-check report is what the gate is signed against.

## Generated-shot QC pass

Run per shot, not by watching the cut. Defects at this level are invisible at
24 frames a second and permanent at delivery resolution.

| Shot | Anatomy | Anachronism | Light continuity | Skin tone | Temporal stability | Label present | Result |
|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

- **Anatomy** — hands, limb counts, eyelines, the geometry of objects being held.
- **Anachronism** — materials, textiles, tools, architecture, flora, script forms.
  The model supplies these confidently from the wrong century.
- **Light continuity** — direction and colour of the key across shots that cut
  together. This is what makes a generated sequence feel assembled rather than shot.
- **Skin tone** — rendering across the range present in the material, checked on a
  calibrated display. Many models render some tones with visible bias, and the
  failure is not subtle to the people it applies to.
- **Temporal stability** — flicker, texture crawl, and drift on generated motion.
- **Label** — present, persistent, inside title safe, legible at 360p.

## Holds raised in this session

| Item | Raised by | Category | Authority to release | Status |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD — Cultural Advisor for sensitivity | TBD |

Any contributor may raise a hold, without standing or seniority. It takes effect
immediately. It is released only in writing by the designated authority. The person
who raised it is not penalised, ever — and if that rule is not visibly true, nobody
raises the second one.

## Outcome

**Cut version status:** TBD — proceed to `v<NN>` / picture lock recommended / blocked.

**Blocking notes outstanding:** TBD — count, or `none`.
