---
# ---------------------------------------------------------------------------
# CLAIM — one factual statement, its confidence, and its evidence.
# Schema: ../../standards/schemas/claim.schema.json
# Copy to <line>/sources/claims/CLM-XX-0000_<slug>.md with a toolkit-allocated
# ID. Do not fill this template in place.
#
# Scripts reference claims. They do not contain facts. This record is the thing
# a `{{CLM-XX-0000}}` reference in a narration resolves to, and it is the unit
# the fact-check gate is signed against.
# ---------------------------------------------------------------------------
id: CLM-XX-0000
type: claim
line: xx-line-code
title: TBD — short handle for indexes, not the claim itself
status: draft
version: "0.1.0"
updated: "2026-08-07"
owners: [research-lead]
sensitivity: review-required

# The claim, as ONE declarative sentence, written at the confidence level the
# evidence supports. This exact text is what must survive fact-check, and it is
# what the script is permitted to say — not a paraphrase of it, and not a
# stronger version of it that reads better in a narration.
statement: TBD — one declarative sentence

# established | probable | contested | inferred | traditional | unknown
#
# The register is a property of the EVIDENCE, not of how sure the writer feels.
# Getting it wrong in the confident direction is the most common way an
# individually defensible research pack becomes an indefensible film.
#
#   established  independent sources agree; not seriously disputed
#   probable     the weight of evidence points one way; a specialist could differ
#   contested    specialists actively disagree, and both positions have standing
#   inferred     not attested; reasoned from adjacent evidence
#   traditional  held in a tradition, transmitted as such, presented as such
#   unknown      the honest answer, and a perfectly publishable one
confidence: TBD

# At least one entry is required by the schema. Corroboration requirements for
# each register come from the pack, and are checked by studio_ops rather than
# here.
evidence:
  - source: SRC-XX-0000
    locator: TBD — page, folio, timecode, catalogue number
    quotation: TBD — the supporting text, in the original language where relevant
    translation: TBD — and who translated it
    # fully | partially | by-inference
    # `partially` and `by-inference` are the honest answers far more often than
    # they are used. A source recorded as supporting `fully` what it merely
    # touches on is how a claim acquires strength nobody granted it.
    supports: TBD
    # Sources this one is demonstrably NOT derived from.
    #
    # Two sources sharing an upstream origin are ONE source. Independence must
    # be asserted deliberately, with a reason you could defend — it is never
    # inferred from two different titles. This field is checked at source lock
    # on every claim at the `established` register, because that register is
    # exactly the claim of independent agreement.
    independent_of: []

# Sources that contradict or complicate the claim. REQUIRED by the pack when
# confidence is `contested`, and worth recording whenever it exists — a claim
# whose counter-evidence is only in the researcher's head is a claim that will
# be defended badly by whoever inherits it.
counter_evidence:
  - source: SRC-XX-0000
    locator: TBD
    position: TBD — what this source holds instead

# REQUIRED by the schema when confidence is `contested`. At least two positions.
# Delete the block for any other register.
#
# contested_positions:
#   - position: TBD — stated fairly, in terms its holders would accept
#     held_by: TBD — NAMED scholars, schools, or traditions. Never "some
#              # historians" — an unattributed disagreement cannot be checked,
#              # and it usually means nobody looked.
#     sources: [SRC-XX-0000]
#   - position: TBD
#     held_by: TBD
#     sources: [SRC-XX-0000]

# REQUIRED by the schema when confidence is `inferred`. Delete otherwise.
#
# The reasoning from the adjacent evidence to the claim, written so a reviewer
# can ATTACK it. An inference chain that cannot be attacked has not been
# written down properly — it has been asserted in longer form.
#
# inference_chain: TBD — what is attested, what is reasoned, and where the step is weakest

# For claims involving a number. Numbers are quoted back more often than
# sentences and are almost never re-checked by whoever quotes them.
#
# quantity:
#   value: TBD
#   unit: TBD
#   range_low: 0                # a range is usually the honest form
#   range_high: 0
#   basis: TBD                  # attested | estimated | modelled
#   model: TBD                  # whose model, published where — required for `modelled`
#   conversion: TBD             # if converted from historical units: the
#                               # conversion factor and its source. An
#                               # unconverted historical unit silently becomes a
#                               # modern one in the reader's head.

# Historical dating. Always a range, because point dates are usually false
# precision — and a point date on screen asserts a precision the source did not.
dating:
  earliest: TBD
  latest: TBD
  display: TBD — how this is spoken on screen
  calendar: TBD — Gregorian, Hijri, regnal, relative
  basis: TBD — how the dating was arrived at
  confidence: TBD — register for the DATING, which is often weaker than for the event
  claims: []

# Records this claim is about: CHR-, LOC-, ORG-, OBJ-, EVT- IDs.
entities: []

open_questions: []              # TBD — QST-XX-0000

# Populated by the toolkit. Where this claim appears on screen — narration,
# on_screen_text, graphic, map, caption, description. Hand-maintaining it
# produces a list that is wrong within a week and is then believed.
used_in: []

fact_check:
  # not-required | pending | in-review | signed | blocked
  status: pending
  report: TBD — FCK record ID
  notes: TBD
  # `signature` is added by the person signing, with their own name and the real
  # date.

notes: TBD — anything a reviewer needs that the fields above cannot carry
---

# TBD — claim handle

> Copy this file; do not fill it in place.

## What this claim does and does not say

TBD — the boundary of the claim. The adjacent, stronger statement it is likely to be
mistaken for, and why the evidence does not reach it.

This section is short and does more work than its length suggests. A claim is
paraphrased every time it is used, and each paraphrase drifts slightly outward.
Writing the boundary down gives the fact-check something specific to check the
script against.

## Why this register

TBD — the reasoning for the confidence register, specifically: what agreement exists
between which sources, and what would have to be true for the register to move up or
down.

## History

| Version | Date | Change | Cause |
|---|---|---|---|
| 0.1.0 | TBD | Created | TBD |

A claim whose register changed after the script was written is the most important
row in this table, and the one most likely to go unrecorded.
