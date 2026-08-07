---
title: sources — the source and claim registry
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# sources

The evidence layer. Everything the line asserts, and everything it asserts it from.

```
sources/
├── records/    SRC-* — one per item of evidence
└── claims/     CLM-* — one per factual statement, with its evidence and confidence
```

Templates: [../../records/_TEMPLATE_source_record.md](../../records/_TEMPLATE_source_record.md),
[../../records/_TEMPLATE_claim.md](../../records/_TEMPLATE_claim.md).
Tiering, corroboration, and independence rules are the pack's:
[../../../packs/documentary-history/02_evidence_and_sourcing.md](../../../packs/documentary-history/02_evidence_and_sourcing.md).

## The separation that makes this work

**A source is a thing. A claim is a statement. They are different records, and the
relationship between them is the evidence.**

Collapsing them — a "source note" that also asserts what the source shows — is the
default way research gets organised, and it removes the only place where the
question "does this actually support that?" can be asked. Keeping them apart means:

- One source supports many claims, at different strengths (`fully`, `partially`,
  `by-inference`) — recorded per claim, not assumed.
- One claim draws on many sources, and their **independence** is asserted
  deliberately rather than inferred from two different titles on a shelf.
- Withdrawing a source is a query, not an archaeology project:
  `studio_ops report dependents` names every claim and every line of narration that
  dies with it.

## Independence is the field that gets waved through

Two sources that share an upstream origin are **one source**. A chronicle and a
19th-century summary of that chronicle corroborate nothing; the second lends the
first a weight it never earned, and the resulting "established" claim rests on a
single testimony wearing two coats.

The `independent_of` field on a claim's evidence exists to make that assertion
explicit and attackable. It is never populated by default, and it is checked at
source lock on every claim at the `established` register.

## Critique is not optional

Every source record carries a `critique` block, and the schema requires three of its
fields: who made this and for whom, what they were in a position to observe, and
what interest shaped what was recorded.

**A citation without a critique is an unfinished record.** A citation tells you where
something is. It does not tell you whether the person who wrote it was there, what
they wanted, what they would never have written down, or what happened to the text
between then and now. Those are the questions that decide what the source can carry —
and they are asked once, in the record, rather than re-litigated in every meeting
where the source comes up.

The `silences` field is the one most often left thin, and the most consequential: an
absence in a source proves something only if the source would have recorded the
thing had it happened. Working that out is research; assuming it is an argument from
silence wearing a footnote.

## Tiers

| | |
|---|---|
| T1 | Primary / archival |
| T2 | Peer-reviewed secondary |
| T3 | Reputable general |
| T4 | Oral testimony — requires the oral protocol block and a consent record |
| T5 | **Never citable.** May exist as a lead only. Model output is T5. |

The schema enforces the T5 rule structurally: a T5 record's `supports_claims` list
must be empty. It cannot support anything, so it cannot be made to.
