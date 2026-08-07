---
title: Story bible lock gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [story-producer]
---

# Story bible lock — checklist

| | |
|---|---|
| **Gate key** | `story_bible_lock` |
| **Owner** | `story-producer` |
| **Stage** | `01_research` |
| **Blocks** | `02_script` |
| **Packs** | narrative |
| **Completed copy** | `01_research/checklists/story_bible_lock.md` in the production folder |

Documentary's failure mode is inventing history. Narrative's is the opposite: it is
*supposed* to invent, so nothing internal stops it drifting into incoherence. The
story bible is what stops it, and this gate is where the bible stops being a working
document and becomes the thing the script is checked against.

It sits at `01_research` and blocks `02_script` for the same reason source lock does
in documentary: the layer that holds the facts is fixed before the layer that uses
them.

## What this signature certifies

> World rules, character canon, timeline, and geography are fixed and internally
> consistent. Every recurring character and location has a record. Contradictions
> between source variants are resolved deliberately, and the resolution is recorded
> rather than left to whichever version a writer remembered.

## Checks

### World rules

- [ ] The rules of the world are written down, including the ones that feel obvious
- [ ] Each rule is stated as a constraint, not a description — a rule that cannot be violated is not a rule, it is a mood
- [ ] Rules are internally consistent; where two imply a contradiction in an edge case, the resolution is recorded
- [ ] Where the world has a magic, technology, or authority system, its **limits** are specified. Unspecified limits are where narrative coherence dies

### Character canon

- [ ] Every recurring character has a record with an ID
- [ ] Each record carries physical description at the level of detail a generation prompt needs — not a novelist's description, a specification
- [ ] Age, appearance, and costume are specified **per point in the timeline** where the character changes across it
- [ ] Relationships, allegiances, and knowledge state per act are recorded. Who knows what, when, is the most common continuity failure in a script and the hardest to spot in a cut
- [ ] Names are fixed, including spelling and any variant forms, and match across bible, script, and captions

### Timeline and geography

- [ ] The timeline is explicit, with events in order and intervals stated
- [ ] Every scene's position on the timeline is fixed, including flashbacks and parallel action
- [ ] Every recurring location has a record with an ID
- [ ] Location records specify layout, scale, and relative position to other locations. "A great hall" is not a location record; a great hall with a known number of doors and a known relationship to the courtyard is
- [ ] Travel times and distances are consistent with the geography as recorded

### Adaptation and source variants

- [ ] Where the work adapts a source text, epic, scripture, or living tradition, the interpretive stance declared at greenlight is carried into the bible
- [ ] **Every contradiction between source variants is resolved deliberately, and the resolution is recorded with its reason.** Not resolved by whichever version a writer happened to remember
- [ ] Where a variant is not followed, the bible says which and why — audiences who hold the text read every choice as a claim about it
- [ ] What the production is **not** claiming about the tradition is stated
- [ ] Departures from the source that are intentional are listed, so script lock can check that no unintentional ones crept in

### Real settings

- [ ] Where the work is set in a real time and place, the **setting** claims are identified and evidenced. The plot is invention; the setting is an assertion about the world
- [ ] Those setting claims carry the same evidence discipline as documentary's, for the setting alone
- [ ] Depiction of real peoples and places has been routed to the sensitivity gate

### Handoff to generation

- [ ] Every record is written at a level of specificity a prompt card can inherit. A bible that reads well and cannot be prompted from will be silently replaced by whatever the model defaults to
- [ ] The bible names which characters and locations will need anchor sets at continuity lock

## Do not sign if

- **A recurring character or location has no record.** It will be re-described from
  memory every time it appears, and the model will produce a different one each time.
- **A source-variant contradiction is unresolved** because "we'll decide when we get
  to that scene". You will decide it twice, differently, in two scenes.
- **Character appearance is described evocatively rather than specifically.** The
  bible has to survive translation into a prompt; adjectives do not survive that.
- **The world's rules have no limits.** A system without limits generates no stakes
  and no continuity constraints, so nothing downstream can be checked against it.
- **The bible is still being written.** This gate blocks `02_script` precisely so
  that the script is not what fixes the bible.
- **You intend to also sign `script_lock` on this production.** Both are owned by
  `story-producer` — see [../roles.md](../roles.md) §5.1.

## Signature

| Field | Value |
|---|---|
| Role | `story-producer` |
| Person | |
| Date | |
| Character records | |
| Location records | |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
