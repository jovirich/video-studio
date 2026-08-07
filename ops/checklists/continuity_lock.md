---
title: Continuity lock gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# Continuity lock — checklist

| | |
|---|---|
| **Gate key** | `continuity_lock` |
| **Owner** | `visual-director` |
| **Stage** | `04_prompts` |
| **Blocks** | `05_assets` |
| **Packs** | narrative |
| **Completed copy** | `04_prompts/checklists/continuity_lock.md` in the production folder |

**Generation may not begin before this gate**, and the reason is arithmetic rather
than principle: retrofitting continuity across a generated sequence costs more than
regenerating it. A face that drifts across 300 shots is not fixed by grading; it is
fixed by generating the sequence again, with anchors that should have existed first.

Generative tools have no memory. Coherence is held externally or it is not held at
all. This gate certifies that the external thing exists before it is needed.

## What this signature certifies

> Every recurring character has a character anchor set; every recurring location has a
> location anchor set; the style block is fixed.

## Checks

### Character anchors

- [ ] Every recurring character named in the locked story bible has an anchor set
- [ ] Each anchor set is **specific files with checksums**, referenced by ID — not "a vibe", not a folder someone will curate later
- [ ] Anchors cover the angles the script actually requires: front, profile, three-quarter, and any distinctive rear or full-body view the cut needs
- [ ] Where a character changes across the timeline — age, injury, costume state — there is an anchor set **per state**, and the script's scenes are mapped to states
- [ ] Anchor sets are versioned. A replaced anchor is a new version, not an overwritten file, so a shot generated last month can still be explained
- [ ] Each anchor set is referenced by ID from every prompt card that uses it

### Location anchors

- [ ] Every recurring location in the bible has an anchor set
- [ ] Anchors establish layout, scale, and the relationships between spaces — not just a mood image of the place
- [ ] Coverage includes the angles and lighting states the script requires, including any night or weather variant
- [ ] Where the geography of a location constrains action, the anchor set makes that geography legible to a prompt

### Style block

- [ ] The style block is fixed and versioned
- [ ] Every prompt card inherits it from its sequence, which inherits from the production
- [ ] Any prompt card that overrides the style block **states why** on the card
- [ ] The lens set, light behaviour, palette, and texture are specified as language a prompt can inherit, not as reference images alone
- [ ] Aspect discipline and safe zones are in the style block, so vertical variants remain crops

### Prompt cards

- [ ] Every generated shot has a versioned prompt card
- [ ] Prompt cards are versioned rather than overwritten, and each version records what changed and why
- [ ] Each card records the vendor and **model version** it targets. See [../risk_register.md](../risk_register.md) `RSK-PLAT-0006` — a version change mid-production is a sequence-level regeneration decision, not a shot-level one
- [ ] Seeds are recorded, and the seed-reproduces-output assumption has been tested at least once on this production
- [ ] Prompts name people, places, and periods specifically rather than relying on the model's defaults

### Prerequisites

- [ ] Story bible lock is `signed`
- [ ] Script lock is `signed`
- [ ] Sensitivity has reviewed the prompt set, where the pack's sensitivity gate applies to this stage

## Do not sign if

- **An anchor set is "the images we've been using".** An anchor is a file with a
  checksum and an ID. Anything else cannot be referenced from a prompt card and cannot
  be checked at picture lock.
- **A character changes across the timeline and has one anchor set.** The drift will
  be generated deliberately, by you, and discovered accidentally, later.
- **Generation has already started.** If it has, the sequences already produced are
  outside this certification and must be listed as such in the note field — and
  expected to be regenerated.
- **The style block exists only as reference images.** A prompt inherits language;
  images alone cannot be inherited by a text prompt and will be paraphrased
  differently every time.
- **Model versions are unpinned.** An unpinned version means a shot regenerated next
  month may not match the sequence around it, and the fix surfaces at picture lock
  when it is a re-cut rather than a re-prompt.
- **You intend to also sign `picture_audio_lock` on this production.** Both are owned
  by `visual-director` — see [../roles.md](../roles.md) §5.1.

## Signature

| Field | Value |
|---|---|
| Role | `visual-director` |
| Person | |
| Date | |
| Character anchor sets | |
| Location anchor sets | |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
