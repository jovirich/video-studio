---
title: Representation review gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [cultural-advisor]
---

# Representation review — checklist

| | |
|---|---|
| **Gate key** | `representation_review` |
| **Owner** | `cultural-advisor` |
| **Stage** | `04_prompts`, then `08_review` |
| **Blocks** | `05_assets`, `09_delivery` |
| **Hold authority** | Yes |
| **Packs** | fashion-film |
| **Completed copy** | `04_prompts/checklists/representation_review.md`, re-signed at `08_review` |

Fashion film's characteristic failure is not factual; it is representational and
attributive. Generative models carry strong, narrow priors about bodies. Left
unmanaged they produce a single body type, a narrow skin-tone range, and impossible
proportions — and the output reads as a deliberate editorial position, because it is
one. Nobody decided it; that does not make it not a decision.

Like documentary's sensitivity gate, this one carries **hold authority** and runs
before generation as well as after. Reviewing casting range after 400 images exist is
reviewing a fait accompli.

## What this signature certifies

> Casting range is deliberate rather than a model default. No impossible body
> proportions. Skin-tone rendering is correct across the full range shown. Any cultural
> textile, motif, or garment form drawn on is attributed and, where required, agreed
> with its custodians. Synthetic-human disclosure is applied per studio policy.

## Pass 1 — prompt set, at `04_prompts`

**Before generation.**

- [ ] The intended casting range is written down before it is generated — body types, ages, skin tones, and any other axis the brief takes a position on
- [ ] Prompts specify that range rather than relying on the model to produce it. A prompt that does not specify produces the model's prior, which is narrow
- [ ] No prompt requests body proportions that a human body does not have
- [ ] No prompt generates a body presented as a specific real model
- [ ] No prompt generates in the style of a living artist or a named cultural custodian's work
- [ ] Every cultural textile, motif, or garment form the film draws on is identified **by name** at prompt stage — which tradition, which form. "Ethnic print" is not an identification
- [ ] Where attribution or agreement is required for a cultural source, it is in hand before the prompt runs, not sought afterwards
- [ ] The synthetic-human decision from brief approval is reflected in the prompt set, and the disclosure it triggers is planned into the edit

## Pass 2 — the cut, at `08_review`

- [ ] The delivered casting range matches what was written down at pass 1. Where it does not, the gap is explained rather than absorbed
- [ ] No impossible body proportions survive in any deliverable, including crops and thumbnails
- [ ] **Skin-tone rendering is correct across the full range shown**, under the show LUT, on a calibrated display. This is the check most often skipped and most visible to the people it fails
- [ ] The show LUT does not crush, desaturate, or shift any skin tone in the range
- [ ] Retouching that changes body shape is logged as a post-process step on the asset and complies with studio disclosure policy
- [ ] No generated body is presented as a specific real model
- [ ] No real model's likeness has been generated beyond their contract's scope — confirm with [stakeholder_approval.md](stakeholder_approval.md), do not assume
- [ ] Cultural sources are attributed on screen or in credits, in the form agreed with their custodians
- [ ] Where agreement was required and obtained, the terms are honoured in the cut — including any restriction on how the form may be shown or combined
- [ ] Synthetic-human disclosure is present **on screen** where synthetic humans appear, not only in metadata
- [ ] Thumbnails and crops carry the same standards as the film. They are seen more often than it is

## Holds

- [ ] Every open hold on this production is resolved by a **written** ruling
- [ ] No held item was generated, edited, or advanced while under hold
- [ ] No hold was released by anyone other than this role
- [ ] Nobody who raised a hold has been penalised or worked around

## Do not sign if

- **The casting range was never written down before generation.** What you are
  reviewing then is the model's prior, and the only available finding is that it looks
  like every other generated campaign.
- **A cultural source is identified only generically.** "Inspired by traditional
  patterns" is the phrasing of an attribution that was never made, and it is the
  field's most reliable source of justified anger.
- **Attribution is being planned for the credits when agreement was required before
  use.** Credit is not consent.
- **Skin-tone rendering was checked on an uncalibrated display**, or on the 16:9
  master only.
- **A body-shape retouch is unlogged** because it was "just a clean-up".
- **The synthetic-human disclosure is in metadata only** where studio policy requires
  it on screen.
- **You are told the campaign date makes a regeneration impossible.** The date is why
  pass 1 exists; if pass 1 did not happen, that is the finding.

## Signature

| Field | Value |
|---|---|
| Role | `cultural-advisor` |
| Pass | 1 of 2 / 2 of 2 |
| Person | |
| Date | |
| Gate status | `signed` / `blocked` (gate reaches `signed` only at pass 2) |
| Rulings referenced | |
| Blockers, if blocked | |
| Note | |
