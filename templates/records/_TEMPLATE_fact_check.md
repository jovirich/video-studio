---
# ---------------------------------------------------------------------------
# FACT CHECK — the gate record for one production's factual accuracy pass.
# Copy to <line>/productions/<PROD>/07_review/FCK-XX-S00E00-0000_<slug>.md with a
# toolkit-allocated ID. Do not fill this template in place.
#
# Front matter follows standards/schemas/fact_check.schema.json. That schema is
# authoritative; if the two disagree, `studio_ops validate --templates` fails.
# ---------------------------------------------------------------------------
id: FCK-XX-S00E00-0000
type: fact_check
line: xx-line-code
title: TBD — fact check, <production>
status: draft
version: "0.1.0"
updated: "2026-01-01"
owners: [fact-checker]

episode: S00E00

# What was checked: narration, on-screen text, graphics, maps, description. ALL
# of them — or the gate is partial and must say so here, in words, rather than
# being signed as though it were complete.
scope: >
  TBD

claims_checked: 0

# One entry per finding.
#   locator    — where in the cut (timecode, page, shot ID)
#   claim      — CLM-XX-0000, where the finding is against a specific claim
#   issue      — unsourced | tier-insufficient | register-overclaimed |
#                misleading-placement | independence-not-established |
#                name-form-wrong | figure-imprecise | prohibited-language
#   detail     — what is actually wrong
#   resolution — corrected | register-lowered | cut | accepted-with-note | open
findings: []
#  - locator: TBD
#    issue: unsourced
#    detail: TBD
#    resolution: open

# MUST BE 0 before the gate can be signed. This is the number that makes the
# signature mean something.
unresolved: 0

# signature:
#   role: fact-checker
#   person: TBD
#   date: "2026-01-01"
---

# Fact-check — TBD

> Copy this file; do not fill it in place.

## Result

TBD — signed / signed with amendments / not signed, and the date.

## What this record is for

The production's fact-check report is filed with the production. This record is the
**registry-side** entry: it is what makes "when was this claim last checked, and
against what" answerable from the claim, rather than only from whichever production
happened to check it.

The link runs both ways. Each claim's `fact_check.report` field names this record;
this record names the claims it touched. Without that, a claim used in three
productions has been checked three times and nobody can tell which check was the
most recent or the most thorough.

## Claims touched

| Claim | Register in script | Register the evidence supports | Result | Action |
|---|---|---|---|---|
| TBD — `CLM-XX-0000` | TBD | TBD | TBD — pass / amend / fail | TBD — record amended, register lowered, claim retracted |

Where a check changed a claim record, the claim's own version history records it.
A register lowered during a fact-check is the most important thing this table can
contain, and the thing most likely to be fixed in the script and forgotten in the
record.

## Sources re-examined

| Source | Why re-examined | Outcome |
|---|---|---|
| TBD — `SRC-XX-0000` | TBD — a claim leant harder on it than the critique supported | TBD |

## Findings referred onward

| Finding | Referred to | Reference |
|---|---|---|
| TBD | TBD — sensitivity / rights / open questions | TBD — `ADV-XX-0000`, `CLR-XX-0000`, `QST-XX-0000` |

## Accepted limitations

| Limitation | Why accepted | Who accepted | Correction path |
|---|---|---|---|
| TBD | TBD | TBD — role and person | TBD — `COR-XX-0000` if later raised |

Recording these is what makes a later correction a follow-through rather than a
surprise. A limitation that was known, accepted, and written down reads very
differently from the same limitation discovered by a viewer.
