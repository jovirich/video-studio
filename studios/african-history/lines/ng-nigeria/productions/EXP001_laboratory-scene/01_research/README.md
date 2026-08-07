---
title: EXP-001 research
status: draft
maturity: NOT STARTED
version: 0.1.0
updated: "2026-08-07"
owners: [research-lead]
---

# EXP-001 — research

Empty. No source, claim, or open question exists.

> **Nothing in this repository may author these records** — not a template, not a
> validator, not a model. The 8–12 claims are human research against real documents,
> read by a person. That rule is the reason this repository exists, and a laboratory
> production that shortcut it would test the tooling while invalidating the thing the
> tooling is for.

## Target

| | |
|---|---|
| Claims | 8–12 |
| Sources | as many as the claims require, at their tiers |
| Open questions | as many as the research honestly produces |

**A high open-question count is a good outcome.** A two-minute piece that produced
twelve confident claims and no open questions was researched too shallowly or written
too confidently, and either way that is the finding.

## Method

[`packs/documentary-history/methodology/research_protocol.md`](../../../../../../../packs/documentary-history/methodology/research_protocol.md),
in full. The laboratory relaxation does not extend here — the research method is a
subject of the experiment, so running it loosely would mean testing nothing.

Two steps carry most of the value and are the two most likely to be skipped:

**The critique block.** A citation is a location, not a warrant. Every source record
answers who made it, for whom, with what interest, and what its silence means. See
[`bias_register.md`](../../../../../../../packs/documentary-history/methodology/bias_register.md)
before writing one.

**The independence check.** Two sources descending from a common upstream are one
source. Record `independent_of` explicitly on every `established` claim. Circular
sourcing through repetition is the most common failure in popular history, and it is
invisible unless someone traces each claim to its earliest attestation.

## Layout

| Path | Holds |
|---|---|
| [`sources/`](sources/) | `SRC-NG-*.yaml` |
| [`claims/`](claims/) | `CLM-NG-*.yaml` |
| [`open_questions/`](open_questions/) | `QST-NG-*.md` |

Records may equally live in the line registry at
[`../../../sources/`](../../../sources/) and be referenced from here — that is the
normal arrangement for a broadcast production, since sources outlive productions. For
EXP-001 either is acceptable; **which one feels natural is itself a finding** worth
recording.

## The measurement that matters

Record, per claim: **how long it took, and what it cost.**

The pipeline question this production exists to answer is whether the claim chain
survives contact with real research *at production pace*. That is answered by hours
per claim, not by whether the records eventually got written.

Also record every instance of the shape: *"I know this, but I cannot source it at the
required tier."* Each one is a place where the honest register is lower than a writer
would like, and how those get resolved under time pressure is the single most
informative thing this experiment can surface.

## Failure signal

At the end, check the git log: **do the claim records predate the script drafts that
reference them?**

If not, the discipline inverted — claims were created to satisfy the validator rather
than to establish what is true — and [ADR 0002](../../../../../../../docs/decisions/0002-claims-as-records.md)
needs revisiting before episode one. Check the log. Do not ask anyone.

## Blockers

- No Research Lead named
- No archive landscape survey — the claims have nowhere to come from
- `new-record` is NOT BUILT, so IDs would be hand-allocated, and a collision is silent
  and unrecoverable
