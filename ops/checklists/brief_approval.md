---
title: Brief approval gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [showrunner]
---

# Brief approval — checklist

| | |
|---|---|
| **Gate key** | `brief_approval` |
| **Owner** | `showrunner` |
| **Stage** | `00_brief` |
| **Blocks** | `02_script` |
| **Packs** | product-marketing, fashion-film |
| **Completed copy** | `00_brief/checklists/brief_approval.md` in the production folder |

The lighter analogue of documentary's greenlight. These packs move faster and their
risk sits elsewhere — in product claims and in representation — so this gate checks
that the piece has **one job** and that the obligations which are expensive to
retrofit are scoped now.

## What this signature certifies

> *product-marketing:* Audience, single core message, call to action, and success
> measure are agreed. The piece has one job, stated in one sentence.
>
> *fashion-film:* Collection, season, audience, and the single idea the film carries
> are agreed. Deliverable set and aspect variants are specified up front.

## Checks

### One job

- [ ] The piece's job is stated in **one sentence**. Not a list of objectives
- [ ] Audience is named specifically enough to exclude someone
- [ ] The single core message is one message. A brief with three core messages has none
- [ ] Success measure is stated and is something that can actually be observed after release
- [ ] *(product-marketing)* Call to action is stated, singular, and matches what the destination actually offers

### Scope of deliverables

- [ ] The full deliverable set is specified: durations, aspect variants, platform variants, language variants
- [ ] Aspect variants are declared **now**, so 9:16 and 1:1 safe zones can be marked in the storyboard. A vertical cut decided after picture lock is a re-generation, not a crop
- [ ] Caption languages named
- [ ] *(fashion-film)* Collection and season identified; every garment intended to appear is listed

### Obligations that are expensive to retrofit

- [ ] *(product-marketing)* Every intended product claim is listed in the brief, with a named owner for its evidence. Claims discovered in the edit have no evidence and no time to get any
- [ ] *(product-marketing)* Any regulated category — financial, health, children's advertising, comparative claims against a named competitor — is identified and escalated. This pack does not cover them
- [ ] *(product-marketing)* Roadmap language is identified up front: anything describing what the product will do rather than what it does today
- [ ] *(fashion-film)* Whether synthetic humans will appear is decided **here**, at studio policy level, not shot by shot in the edit
- [ ] *(fashion-film)* Any cultural textile, motif, or garment form the film draws on is named, so attribution and agreement can be sought before generation rather than after publication
- [ ] Music approach is decided: original, commissioned, licensed, or library — with a budget line, because music is what fashion film routinely gets wrong

### Record and budget

- [ ] Stakeholders who will sign at `stakeholder_approval` are named now. Discovering an additional approver at `08_review` is a schedule event, not an administrative one
- [ ] Budget carries lines for music licensing, translation, and consultation where the piece needs them
- [ ] `budget.generation_ceiling_usd` is set
- [ ] The distinct-signatory count meets the pack's `minimum_distinct_signatories`, and no person is slated to sign two gates — see [../roles.md](../roles.md) §5.1

## Do not sign if

- **The brief has more than one core message.** Every downstream compromise will be
  resolved by keeping all of them, and the piece will do none of them.
- **The aspect variants are "we'll decide later".** Later is after the storyboard,
  which means after the safe zones were not marked, which means the vertical cut is a
  regeneration at full cost.
- **A product claim is intended but its evidence owner is unnamed** *(product-marketing)*.
  `claim_substantiation` blocks delivery and cannot be satisfied retroactively by
  someone who was not asked in time.
- **The synthetic-human question is being deferred** *(fashion-film)*. It is a
  studio-level decision with a disclosure obligation attached; deferring it means it
  gets made implicitly by whoever writes the first prompt.
- **A regulated category is in scope and legal review is not.**
- **You intend to also sign `stakeholder_approval` on this production.** Both are
  owned by `showrunner` in these packs, which conflicts with
  [../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §5 —
  see [../roles.md](../roles.md) §5.1. Until that is resolved, name two people.

## Signature

| Field | Value |
|---|---|
| Role | `showrunner` |
| Person | |
| Date | |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
