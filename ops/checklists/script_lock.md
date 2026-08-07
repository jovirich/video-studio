---
title: Script lock gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [story-producer]
---

# Script lock — checklist

| | |
|---|---|
| **Gate key** | `script_lock` |
| **Owner** | `story-producer` |
| **Stage** | `02_script` |
| **Blocks** | `03_storyboard`, `04_prompts`, `05_assets` |
| **Packs** | documentary-history, narrative |
| **Completed copy** | `02_script/checklists/script_lock.md` in the production folder |

**Generation does not begin before this gate.** That is the whole reason it blocks
three stages instead of one. Generating imagery for an unlocked script is how a
production ends up writing toward the footage it happens to have — the single most
common way AI-assisted work loses its spine, and the most expensive to reverse,
because by then the striking image already exists and the argument about whether it
should is much harder to win.

## What this signature certifies

> *documentary-history:* The narration and shooting script are final, every factual
> statement carries a claim ID, the certainty register matches the evidence, and no
> prohibited language pattern remains.
>
> *narrative:* The script is final and consistent with the story bible. Any departure
> from the source text is intentional and recorded.

## Checks

### Artefacts complete

- [ ] Narration draft final
- [ ] Shooting script final
- [ ] Outline and beat sheet locked earlier and not diverged from
- [ ] VO record sheet generated from the script, with every proper noun extracted

### Claims — *(documentary-history)*

- [ ] **Every factual statement carries a claim ID.** Dates, names, figures, places, quantities, sequences of events
- [ ] Every referenced claim ID resolves to a claim record that exists and is at the required tier
- [ ] Every superlative — "the largest", "the first", "the only" — carries a claim ID. Superlatives are factual assertions
- [ ] Every bare figure has its basis in the narration, not only on the record: "an estimated N, on the basis of X"
- [ ] The certainty register in the narration matches the register on the claim, sentence by sentence. A `probable` claim spoken as plain assertion is an overclaim
- [ ] `unknown` appears somewhere in the script. A full episode that never says "we do not know" is not a careful script; it is an incurious one

### Attribution and language — *(documentary-history)*

- [ ] No passive attribution: "it is believed", "some say", "historians think" without a named referent
- [ ] Where a position belongs to a named scholar or tradition, it is named
- [ ] Where a colonial-era record is the only source, the script says so and says what its author was in a position to know
- [ ] No prohibited language pattern remains — checked against [../../standards/prohibited_language.md](../../standards/prohibited_language.md)
- [ ] Adjectives are earned. "Vast", "mighty", "legendary", "mysterious" are load-bearing when they should be decorative; they smuggle in claims the evidence has not made
- [ ] Colonial-era categories are interrogated rather than inherited

### Story bible consistency — *(narrative)*

- [ ] The script is consistent with the locked story bible: world rules, character canon, timeline, geography
- [ ] Every departure from the source text is **intentional and recorded**, with the reason
- [ ] Where variants of the source tradition conflict, the script follows the resolution recorded at story bible lock rather than whichever version a writer remembered
- [ ] No recurring character or location appears that has no record

### Structure and craft

- [ ] The question raised in the opening is addressed by the close, even if the answer is "we do not know, and here is why that matters"
- [ ] No movement is a list — no section can be reordered without loss
- [ ] Cold open contains a concrete image, a stated question, and one piece of evidence; it contains no branding, no presenter introduction, and no "in this episode we will explore"
- [ ] Information density holds: no more than one new named entity per 20 seconds in the ground movement
- [ ] Narration reads at 145–165 wpm; dense passages are marked for slower delivery

### Representation and depiction

- [ ] Historical subjects act; they are not framed as acted upon. Passive framing is checked for at this gate specifically
- [ ] Every depiction names the people, place, and period it depicts — "African" is not a culture, and neither is a nationality
- [ ] Societies are depicted with internal complexity, not as uniform, including when the tone is admiring
- [ ] No named figure is scripted speaking invented words. Documented words are attributed on screen to the document
- [ ] Sequences involving atrocity, human remains, or graphic injury carry warnings and have been routed to the sensitivity gate before generation

### Naming and language

- [ ] Every name form matches its entity record exactly
- [ ] Exonyms and colonial names are not the primary form; where given for orientation, they are marked as such
- [ ] Contested names give both forms and name the dispute
- [ ] Titles and honorifics are rendered accurately, not translated into approximate European equivalents

## Do not sign if

- **Any factual statement lacks a claim ID.** Not "the claim exists, we'll link it
  later". The link is the mechanism; without it the claim chain is decorative.
- **The register in the narration is stronger than the register on the claim
  record.** This is the specific overclaim this gate catches, and it is invisible to
  everyone downstream — the shot looks the same either way.
- **A sequence survives only because its evidence is stated loosely.** If it cannot
  survive its honest register, it is cut. Softening the language is how the register
  system gets defeated while continuing to appear intact.
- **You are locking under pressure to start generation.** That pressure is the
  entire reason this gate blocks `05_assets`. Mark it `blocked` and record the
  pressure in the note field.
- **Any prohibited language pattern remains** because it "reads better". It reads
  better because it is claiming more.
- **You signed another gate on this production.** Note that narrative assigns
  `story_bible_lock` and `script_lock` to this same role — see
  [../roles.md](../roles.md) §5.1.

## Signature

| Field | Value |
|---|---|
| Role | `story-producer` |
| Person | |
| Date | |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
