---
title: TBD — narration for the production
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [story-producer, research-lead]
episode: S00E00
line: xx-line-code
stage: 02_script
gate_blocking: script_lock
---

# Narration — TBD — production working title

> Copy this file to `narration_v01.md`; do not fill it in place. Increment the
> version on every pass. Earlier versions are never overwritten, because "what did
> the script say when the fact-check ran" is a question that gets asked.

## 1. The claim-reference convention

This is the mechanism that makes every fact in a finished production traceable. It
is worth understanding precisely rather than approximately.

**A script references claims. It does not contain facts.**

Every factual statement carries an inline reference in double braces, immediately
after the clause it supports:

```
TBD — a clause asserting one fact. {{CLM-XX-0000}} TBD — a second clause,
resting on different evidence. {{CLM-XX-0001}}
```

| Rule | Reason |
|---|---|
| Double braces, uppercase ID, no spaces inside | `studio_ops validate --sources` parses this exact form; anything else is invisible to it |
| Stripped at render | The braces never reach a viewer, a caption, or a teleprompter |
| One reference per **clause**, not per paragraph | A paragraph-level reference cannot tell you which sentence the source actually supports, which is precisely what fact-check needs to know |
| Two facts from two sources get two references | Otherwise the second fact inherits the first's evidence and nobody notices |
| A reference may repeat | Repetition is normal and costs nothing; a missing reference costs a gate |

### What must carry a reference

Any **date, name, place, figure, quantity, causal statement, attribution, comparison,
or superlative**. Superlatives especially — "the largest", "the first", "the only" —
because they are the statements most likely to be repeated by someone else, out of
context, with the studio's name attached.

### What must not

Framing, transitions, questions posed to the viewer, and statements about the
production's own method ("what the record does not tell us is…"). These assert
nothing about the past and referencing them dilutes the signal until the check
becomes noise.

### Register discipline

The words around a reference must match the claim's confidence register. The
validator can check that a reference *resolves*; only a human can check that a
`probable` claim has not been spoken as an established one. That check is what
script lock is signed against.

| Register | Speak it as |
|---|---|
| `established` | Plainly. No hedge. Hedging established facts trains the viewer to ignore hedges. |
| `probable` | With the weight of evidence named, not with a vague "likely" |
| `contested` | With the positions attributed to named holders. Never "some historians". |
| `inferred` | With the inference visible: what is attested, and what is reasoned from it |
| `traditional` | Attributed to the tradition that holds it, as a tradition, without ironic distance |
| `unknown` | Said out loud. It is publishable, and it is usually more interesting than a hedge. |

### Unsourced material does not enter here

If the research does not know, the script does not get to decide, and neither does a
model. A sentence with no reference and no way to acquire one is an open question
([../../records/_TEMPLATE_open_question.md](../../records/_TEMPLATE_open_question.md)),
not a line of narration.

## 2. Pronunciation

Every proper noun appearing below is on
[_TEMPLATE_vo_record_sheet.md](_TEMPLATE_vo_record_sheet.md) with its IPA and a
reference recording from a speaker of the language, verified by a named person. A
proper noun in the narration and absent from that sheet blocks audio lock — because
the alternative is a VO session where the read is decided by whoever is in the booth.

## 3. Narration

Sequence anchors (`## SEQ-XX-S00E00-000`) are the join between this document and the
shot records; they are what a shot's `narration_ref` points at. Keep them stable
once shots exist.

---

### SEQ-XX-S00E00-001 — TBD — sequence handle

TBD — narration text. Each factual clause is followed by its reference in double
braces. {{CLM-XX-0000}}

TBD — a second paragraph. Where a clause rests on different evidence from the one
before it, it carries its own reference. {{CLM-XX-0001}}

TBD — a framing or transitional line carries no reference, because it asserts
nothing about the past.

> **Uncertainty, spoken:** TBD — where the record is silent, say so in the
> narration rather than composing around it. A stated silence is a fact about the
> archive and belongs to the viewer.

---

### SEQ-XX-S00E00-002 — TBD — sequence handle

TBD — narration text. {{CLM-XX-0002}}

---

## 4. On-screen text and quotations

On-screen text asserts exactly as much as narration does and carries claim
references on the same terms. A translated quotation additionally records the
translator and the edition translated from — an uncredited translation is an
editorial act presented as a transcription.

| Anchor | Text as it appears | Claim | Source | Translator |
|---|---|---|---|---|
| TBD | TBD | TBD — `CLM-XX-0000` | TBD — `SRC-XX-0000` | TBD — or `n/a` |

## 5. Word count and timing

| | |
|---|---|
| Word count | TBD |
| Words per minute assumed | TBD — measured from the narrator's own reference read, not a generic figure |
| Estimated VO runtime | TBD |
| Target runtime | TBD — from [../production.yaml](../production.yaml) |

An estimate built on an assumed pace is off by enough to matter over a full episode.
Measure it once, from the actual voice, and record the number here.
