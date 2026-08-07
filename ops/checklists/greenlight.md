---
title: Greenlight gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [showrunner]
---

# Greenlight — checklist

| | |
|---|---|
| **Gate key** | `greenlight` |
| **Owner** | `showrunner` |
| **Stage** | `00_brief` |
| **Blocks** | `01_research` (documentary-history), `02_script` (narrative) |
| **Packs** | documentary-history, narrative |
| **Completed copy** | `00_brief/checklists/greenlight.md` in the production folder |

Greenlight is the cheapest gate to fail and the most expensive to have passed
wrongly. Re-opening it is not a re-open; it is a new production with a retained ID
([../workflow_states.md](../workflow_states.md) §6). Everything downstream is
conditional on the judgements made here.

## What this signature certifies

> *documentary-history:* The production has a question with stakes, falls inside the
> line's advisory coverage, has a research lead assigned, has consultation fees
> budgeted, and has declared conflicts of interest.
>
> *narrative:* The story has a reason to exist in this form, and where it adapts a
> source text or a living tradition, the interpretive stance is declared in writing.

## Checks

### The question

- [ ] The brief states the question in **one sentence**. If it cannot, the production is not ready
- [ ] It is a question, not a topic. "The kingdom of X" is a topic; "why did X's authority survive three successions and then collapse in one?" is a question
- [ ] The question has stakes — an answer would change how a viewer understands something
- [ ] The thesis and logline are present and are not restatements of the question
- [ ] Runtime target is set and is a value the line actually holds to

### Advisory coverage — *(documentary-history)*

- [ ] `advisory_coverage.covered` is `true` on the production record
- [ ] Named advisors are listed, and each is competent on the traditions this specific production touches — not on the region in general
- [ ] `advisory_coverage.gaps` is empty. **A gap is not a caveat; it is a stop.** A line does not begin production on material outside its advisory coverage
- [ ] The advisory register records each advisor's fee, credit, review rights, and right to withdraw

### Interpretive stance — *(narrative)*

- [ ] Where the work adapts a source text, epic, scripture, or living tradition, the stance is declared **in writing** and states all four: which tradition, which variant, whose reading, and **what the production is not claiming**
- [ ] The stance is a document in `00_brief/`, not a paragraph in a conversation
- [ ] Where the setting is a real time and place, the setting-fidelity obligation is acknowledged and scoped

### People

- [ ] A research lead is assigned by name *(documentary-history)*
- [ ] A story producer is assigned
- [ ] The distinct-signatory count for this production meets the pack's `minimum_distinct_signatories`, and no person is slated to sign two gates
- [ ] Where a role is doubled, two people are named for it — see [../roles.md](../roles.md) §5.1

### Budget

- [ ] `budget.consultation_fees_budgeted` is `true`. **This is the named red flag at greenlight**
- [ ] `budget.generation_ceiling_usd` is set, and set above the expected spend rather than equal to it
- [ ] Translation, archive access, travel, music licensing, and voice licensing lines are present or explicitly `TBD` with what is needed to resolve them
- [ ] Contingency is non-zero
- [ ] The category breakdown exists, not only a total. See [../budget_template.md](../budget_template.md) §6

### Conflicts and sensitivity

- [ ] `conflicts_of_interest` is present on the record. An **empty array asserts the question was asked**; an absent field asserts nothing
- [ ] Every declared conflict names the person, the nature, and the mitigation. Declaration does not disqualify; concealment does
- [ ] The premise has been submitted to the sensitivity gate (pass 1 of 3) and has cleared — see [sensitivity_review.md](sensitivity_review.md)

## Do not sign if

- **The question is a topic.** This is the most common failure at this gate and the
  most consequential, because a production without a question will discover its shape
  during the edit, which is the most expensive place to discover it.
- **`advisory_coverage.gaps` is non-empty.** The pressure to sign anyway is entirely
  schedule-shaped, and the cost of being wrong falls on people outside the studio who
  have no other route to a veto. The episode waits.
- **`consultation_fees_budgeted` is `false`.** An advisor who is not paid is not an
  advisor. A production that has not budgeted consultation has decided to work without
  advisors and has not said so out loud.
- **The `conflicts_of_interest` field is absent** rather than empty. Absent means
  nobody asked.
- **No research lead is assigned** *(documentary-history)*. Assigning one later means
  the research pack is built by whoever is free, which is how a claim chain acquires
  authors who cannot be identified.
- **You intend to sign a second gate on this production.**

## Signature

| Field | Value |
|---|---|
| Role | `showrunner` |
| Person | |
| Date | |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
