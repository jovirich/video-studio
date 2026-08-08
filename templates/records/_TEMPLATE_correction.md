---
# ---------------------------------------------------------------------------
# CORRECTION — a published error, what was done about it, and when.
# Copy to <line>/corrections/COR-XX-0000_<slug>.md with a toolkit-allocated ID.
# Do not fill this template in place.
#
# Front matter follows standards/schemas/correction.schema.json. That schema is
# authoritative; if the two disagree, `studio_ops validate --templates` fails.
# ---------------------------------------------------------------------------
id: COR-XX-0000
type: correction
line: xx-line-code
title: TBD — what was wrong, in one line
status: draft
version: "0.1.0"
updated: "2026-01-01"
owners: [editorial-lead]

# episode: S00E00
# published_version: TBD — the cut that carried the error

# Anyone may report an error. May be 'viewer' or anonymised.
reported_by: TBD
reported_on: "2026-01-01"
# triaged_on: within 5 working days of the report.

# material | minor
#
# MATERIAL changes a viewer's understanding and forces a re-cut or an on-screen
# correction card. MINOR is description and log only. The distinction is the
# whole record — grading a material error as minor is how a correction policy
# quietly becomes decorative.
severity: minor

what_was_wrong: >
  TBD — the error as published, stated plainly and without minimising it.

what_is_correct: >
  TBD — and on what evidence.

affected_claims: []

# re-cut | correction-card | description-note | claim-retracted | no-action
action: no-action

# Required whenever action is no-action. An unexplained no-action is
# indistinguishable from an error that was quietly ignored.
no_action_reason: >
  TBD

# corrected_on: "2026-01-01"

# signature:
#   role: editorial-lead
#   person: TBD
#   date: "2026-01-01"
---

# Correction — TBD

> Copy this file; do not fill it in place.

## What was published

TBD — the statement exactly as it went out, with its locator: file, anchor, timecode,
or the line of the description.

Quoted verbatim, not paraphrased. A paraphrased error is a second error, and it
reads as an attempt to soften the first.

## What it should have said

TBD — the corrected statement, at the register the evidence actually supports.

## What went wrong

TBD — the cause, specifically.

Useful causes are mechanical: *source misread*; *claim reference pointed at the wrong
record*; *register overstated between the claim and the narration*; *graphic implied
a relation nobody asserted*; *description written without a fact-check*; *source
retracted upstream after publication*.

"Human error" is not a cause. It is a category containing every cause, and naming it
guarantees the same thing happens again.

## Why the gates did not catch it

TBD — which gate should have caught this, and why it did not.

This is the section with real value and real discomfort. Possible honest answers: the
checklist did not cover this surface; the gate was signed without the checklist
committed; the same person effectively did the work and the review; the finding was
raised and dismissed; the surface was out of scope for every gate, which is a design
gap rather than a personal one.

## What was done

| | |
|---|---|
| Records amended | TBD — with their new versions |
| Claim retracted | TBD — `CLM-XX-0000` with its `retraction_reason`, or `n/a` |
| Dependents re-examined | TBD — every claim, beat, and shot that rested on it |
| Published work annotated | TBD — how and where |
| Re-cut shipped | TBD — version, or `no` |
| Corrections log updated | TBD — date |
| Reporter informed | TBD — date |

**Records are never deleted.** A retracted claim keeps its ID as a tombstone with a
retraction reason. `retracted` is how a studio remembers it was wrong about
something, which is worth considerably more than a registry that looks clean.

## What changed so it does not recur

TBD — the checklist item added, the validator rule written, the process changed, or —
honestly — nothing, because this one was genuinely a one-off.

A corrections log where nothing ever changes as a result is a log of apologies. The
value is in this section.

## Time to correction

| | |
|---|---|
| Reported to acknowledged | TBD |
| Acknowledged to published | TBD |

Recorded including when it was bad. A log that only shows fast responses is a log
with entries missing.
