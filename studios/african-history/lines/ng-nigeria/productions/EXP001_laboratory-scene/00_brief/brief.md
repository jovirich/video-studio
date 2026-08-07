---
title: EXP-001 brief
status: draft
maturity: NOT STARTED
version: 0.1.0
updated: "2026-08-07"
owners: [showrunner, research-lead]
---

# EXP-001 — brief

## What kind of production this is

A **laboratory production**. It runs the full pipeline on a small piece to find out
what breaks. It is never published. Its deliverable is
[`../08_review/findings.md`](../08_review/findings.md).

Unlike a broadcast production, its question is a *pipeline* question rather than a
historical one — but the history in it must still be real, because a pipeline tested
on invented content tests nothing about the research method.

## The pipeline question

> `TBD` — suggested form: *"Can this pipeline take twelve researched claims to twenty
> conformed shots with continuity intact — and what does it cost in money and hours?"*

## The subject

`TBD — Showrunner and Research Lead.`

Constraints the choice must satisfy, from [`../README.md`](../README.md) § Subject:

- [ ] Supportable at 8–12 real claims, researchable in a bounded time
- [ ] One location, one time of day
- [ ] One or two recurring characters, unnamed
- [ ] No named historical individual
- [ ] Nothing sacred, funerary, or restricted
- [ ] Inside the line's advisory coverage

> **Nothing in this repository may author the claims.** They are human research
> against real sources. A subject chosen because a model could describe it fluently
> is precisely the wrong subject.

## Scope

| | |
|---|---|
| Runtime | ~2 minutes |
| Claims | 8–12 |
| Locations | 1 (one continuity record) |
| Characters | 1–2 (one continuity record each) |
| Shots | ~20 |
| Sequences | 1–2 |

Two characters is better than one: it tests whether the continuity mechanism holds
them **separately** or collapses them toward a single face. One character passing
proves less than most people assume.

## Hypotheses under test

Each is falsifiable and each maps to a question in the findings report.

| # | Hypothesis | Falsified if |
|---|---|---|
| H2 | A continuity record holds a character across ~20 shots | Drift is visible in a cut |
| H3 | The prompt card's overhead is repaid by consistency and reviewability | `raw_override` dominates |
| H4 | The gate set can be staffed by the people actually available | Someone signs work they produced |
| H5 | Nothing reaches the edit without provenance | Any asset lacks a manifest entry |
| H6 | Cost per finished second is predictable within 2× | The estimate misses by more |
| H7 | A card renders to more than one vendor from one record | Only the vendor it was written for works |

**H1 is deliberately absent, and its absence is the most important thing on this page.**

H1 was: *facts can be researched into claim records before the script, at production
pace.* EXP-001 makes no historical claims, so it cannot test that — and H1 is the
load-bearing assumption of the entire architecture.
[ADR 0002](../../../../../../../docs/decisions/0002-claims-as-records.md) remains
**untested** after EXP-001 passes.

A green EXP-001 proves the *mechanics* work. It says nothing about whether the
evidence discipline survives a schedule. That needs its own experiment, with real
research, before episode one — and it is now the largest untested assumption in the
repository.

## Explicitly out of scope

Named so they are decisions rather than omissions:

- Narrative quality. This is not a pitch or a proof of taste.
- Publication, in any form, including as a behind-the-scenes clip.
- Archival material. Nothing third-party, so the rights surface stays small and the
  test stays focused on generation.
- Music beyond a utility bed. The AI-music policy is undecided and this is not the
  place to decide it.
- Any depiction requiring an advisory ruling.

## Conflicts of interest

`TBD` — an empty answer must still be an answer. Declaring none asserts the question
was asked.

## Approval

Greenlight is **blocked**. See [`../README.md`](../README.md) § Blockers — the line is
`candidate`, there is no Research Lead, no advisory contact, and no archive survey.

Those are the same conditions episode one would face. Clearing them is part of the
experiment.
