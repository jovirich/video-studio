---
# ---------------------------------------------------------------------------
# FACT-CHECK RECORD — the registry-side record of one fact-check.
# Copy to <line>/research/fact_checks/FCK-XX-S00E00-0000_<slug>.md with a
# toolkit-allocated ID. Do not fill this template in place.
#
# This is the LINE-level record. The production-side report, which carries the
# findings in full, is
# ../production/08_review/_TEMPLATE_fact_check_report.md — the two are the same
# check seen from the registry and from the production.
#
# No schema exists for this record type yet; front matter follows the minimum in
# ../../standards/metadata_spec.md plus the ID system.
# ---------------------------------------------------------------------------
id: FCK-XX-S00E00-0000
type: fact_check
line: xx-line-code
episode: S00E00
title: TBD — what was checked
status: draft
version: "0.1.0"
updated: "2026-08-07"
owners: [research-lead]

# The exact artefacts checked. A report against "the script" is unauditable; a
# report against a named file at a named commit can be re-run, and if the script
# moves afterwards the report visibly no longer applies.
checked:
  script: TBD — filename and commit
  cut: TBD — cut version
  manifest: TBD — manifest version
  description: TBD — filename and commit

checked_by: TBD — named person, in the Research Lead role
started: "2026-08-07"
completed: TBD — ISO date

# not-required | pending | in-review | signed | blocked
gate_status: pending

claims_checked: 0
findings_blocking: 0
findings_amend: 0
findings_note: 0
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
