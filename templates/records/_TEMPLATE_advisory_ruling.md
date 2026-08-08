---
# ---------------------------------------------------------------------------
# ADVISORY RULING — the record of a cultural or ethical hold and its outcome.
# Copy to <line>/rights/advisories/ADV-XX-0000_<slug>.md with a toolkit-allocated
# ID. Do not fill this template in place.
#
# Front matter follows standards/schemas/advisory_ruling.schema.json. That schema
# is authoritative; if the two disagree, `studio_ops validate --templates` fails.
# ---------------------------------------------------------------------------
id: ADV-XX-0000
type: advisory_ruling
line: xx-line-code
title: TBD — the question, in one line
status: draft
version: "0.1.0"
updated: "2026-01-01"
owners: [cultural-lead]
sensitivity: review-required

# ANY contributor may raise a hold, without standing or seniority, and is never
# penalised for it. A hold that turns out to be unnecessary cost an afternoon; a
# hold that was never raised can cost a community's trust permanently.
raised_by: TBD — named person or role
raised_on: "2026-01-01"

# What is actually under hold: an asset, shot, sequence, prompt card, or record.
target: TBD — the ID or path under hold

# sacred-or-restricted | human-remains-or-burial | violence-or-atrocity |
# living-community-claim | likeness-or-voice | language-or-naming |
# stereotype-or-framing | regalia-or-masquerade | other
category: other

concern: >
  TBD — what specifically might be wrong, harmful, or presumptuous. Written so
  someone who was not in the room can see the problem.

# Standing is the basis on which this person is competent to rule on THIS
# question. "An elder from the village" is not standing.
#
# Consultation is labour. An unpaid advisor is a favour being taken advantage of,
# and will eventually and rightly stop answering.
consulted: []
#  - advisor: TBD
#    standing: TBD
#    paid: true

# permitted | permitted-with-conditions | refused | deferred
ruling: deferred

# Required in substance whenever the ruling is permitted-with-conditions.
# conditions: >
#   TBD — exactly what must be true for the permission to hold.

reasoning: >
  TBD — why. Written so a future production facing the same question can apply
  this without re-litigating it.

# The hold stays closed until someone states otherwise. Absence is not release.
hold_released: false

# A human sign-off. Absence of a signature is never inferred from anything else.
# signature:
#   role: cultural-lead
#   person: TBD
#   date: "2026-01-01"
---

# Advisory ruling — TBD

> Copy this file; do not fill it in place.

## The question

TBD — what was asked, stated neutrally enough that someone who disagrees with the
outcome would accept the framing.

## The material at issue

TBD — specifically what was proposed: the shot, the prompt card, the sequence, the
line of narration, the entity depiction, the sound.

## The ruling

TBD — permitted / permitted with conditions / not permitted / deferred.

## Conditions

TBD — where permission is conditional, the conditions in full, and who verifies each
before publication.

A condition with no named verifier is a condition that gets checked by whoever
remembers it, which is a way of saying it does not get checked.

## Reasoning

TBD — why. Written for someone who will face a similar question in two years and
should not have to start over.

This is the section that earns the record its cost. A studio that resolves the same
category of question three times from scratch has an advisor doing avoidable work,
and is paying for it. It is also the section that lets a later ruling *depart* from
this one deliberately, rather than by having forgotten it.

## Who was consulted

| Person or community | Standing | How they were reached | Fee |
|---|---|---|---|
| TBD | TBD — their relationship to the material | TBD | TBD |

Consultation is a relationship, not a lookup. It carries a fee, a credit, and a copy
of the finished work.

## Scope of this ruling

TBD — what this ruling does **not** cover.

Rulings get generalised in retelling: "the advisor said the regalia was fine"
becomes permission for a category nobody ruled on. Bounding it here is what stops
that, and the bound is written by the person who made the ruling rather than
inferred later by the person who wants the shot.

## Release of the hold

| | |
|---|---|
| Hold raised on | TBD — ISO |
| Raised by | TBD |
| Released on | TBD — ISO, or `still in force` |
| Released by | TBD — the Cultural Advisor, in writing. No other role may release it. |

A hold takes effect immediately, is released only in writing by the designated
authority, and **the person who raised it is never penalised**. That last clause is
not a courtesy: if it is not visibly true, nobody raises the second hold, and the
mechanism is gone while still appearing in the documentation.

## Review

TBD — the date or event at which this ruling should be revisited, if any. Community
positions change, new material surfaces, and a ruling made under one set of facts
should not silently outlive them.
