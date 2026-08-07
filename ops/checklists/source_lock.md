---
title: Source lock gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# Source lock — checklist

| | |
|---|---|
| **Gate key** | `source_lock` |
| **Owner** | `research-lead` |
| **Stage** | `01_research` |
| **Blocks** | `02_script` |
| **Packs** | documentary-history |
| **Completed copy** | `01_research/checklists/source_lock.md` in the production folder |

After this signature the research pack is fixed for scripting. New evidence arriving
later requires a re-open, and a re-opened source lock cascades to every gate
downstream — it costs the production, not a rewrite
([../workflow_states.md](../workflow_states.md) §6). Slowness here is the cheapest
slowness available.

## What this signature certifies

> Every claim the outline requires exists at its required tier, independence has been
> checked on every `established` claim, contested claims carry named positions, T4
> sources have consent records, and open questions are registered.

## Checks

### Coverage

- [ ] Every claim the outline requires exists as a claim record with an ID
- [ ] Every claim record cites at least one source record. No claim ID exists without one
- [ ] Every source record has a tier (T1–T5) assigned deliberately, not by default
- [ ] No claim rests on a T5 source. **Model output is T5 and is never citable** — it may locate a lead; it never supports a claim
- [ ] No claim was reached by finding a T3 that repeats a T4 account. Circular sourcing through repetition is the most common failure in popular history

### Corroboration and independence

- [ ] Every `established` claim has ≥2 sources, at least one at T1 or T2
- [ ] **Independence checked explicitly on every `established` claim** — the sources are not derived from a common upstream source. This is a check performed, not an assumption recorded
- [ ] Every `probable` claim has ≥1 T1/T2, or ≥2 demonstrably independent T3
- [ ] Every `contested` claim carries sources for **each** position, at required tier, with the positions **named** rather than described as "some historians"
- [ ] Every `inferred` claim records the adjacent evidence and a written inference chain
- [ ] Every `traditional` claim has ≥1 T4 recorded under the oral history protocol, with the holder and the context of transmission named
- [ ] Every `unknown` records what was searched and where, so the next researcher does not repeat it

### Interrogation, not just citation

Every source record's `critique` block answers all five
([../../packs/documentary-history/02_evidence_and_sourcing.md](../../packs/documentary-history/02_evidence_and_sourcing.md) §4):

- [ ] Who made this, when, and for whom
- [ ] What they were in a position to know
- [ ] What interest they had
- [ ] What has happened to it since — translation, transcription, restoration, selective preservation, archival rearrangement
- [ ] What its silence means
- [ ] Recurring patterns are recorded in the bias register rather than re-derived per source

### Testimony and consent

- [ ] Every T4 source has a consent record stating scope, media, territory, duration, AI-processing permission, review rights, and withdrawal terms
- [ ] Oral testimony was recorded under the protocol in [../../packs/documentary-history/methodology/oral_history_protocol.md](../../packs/documentary-history/methodology/oral_history_protocol.md)
- [ ] Anonymised contributors' identities are held outside the repository, by the Research Lead and Showrunner only
- [ ] Full unedited recordings are retained under the source ID

### Entities and numbers

- [ ] Every person, place, polity, and organisation that will appear on screen has an entity record
- [ ] Each entity record carries the on-screen name form **and the reason it was chosen**, plus alternative and historical forms
- [ ] Every figure is marked `attested`, `estimated`, or `modelled`; modelled figures name the model and its author
- [ ] Every range is recorded as a range. A point date where the sources give a range is a false statement
- [ ] Currency, distance, area, and calendar conversions record their basis and its own source

### Gaps

- [ ] Every gap is registered as an open question with an ID, not left as a silence in the pack
- [ ] Where evidence ran out, the register was moved **down**, not the claim up
- [ ] Any sequence that cannot survive its honest register has been flagged to the Story Producer for cutting rather than softening

## Do not sign if

- **Independence was assumed rather than checked** on any `established` claim. Two
  sources sharing an upstream origin are one source, and the whole corroboration
  requirement collapses on this single check.
- **Any claim is at a register the evidence does not support.** Overclaiming is
  indistinguishable from a false statement to a viewer who cannot check, and it is
  the failure this gate exists to catch while it is still cheap.
- **A T4 account has been laundered into `established`** by finding a T3 that repeats
  it.
- **A gap is being carried as "we'll find it during scripting".** It will not be
  found; it will be filled. Register it as an open question and move the register down.
- **Any consent record is missing AI-processing scope.** Consent obtained without it
  is not valid for this platform's use, however willingly it was given.
- **You signed, or will sign, another gate on this production.** Note that
  documentary-history assigns `source_lock` and `fact_check` to this same role — see
  [../roles.md](../roles.md) §5.1. Until that conflict is resolved, two people are
  needed.

## Signature

| Field | Value |
|---|---|
| Role | `research-lead` |
| Person | |
| Date | |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
