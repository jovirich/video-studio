---
id: FCK-XX-S00E00-0000
type: fact_check
line: xx-line-code
title: TBD — fact-check report for the production
status: draft
version: "0.1.0"
updated: "2026-08-07"
owners: [research-lead]
episode: S00E00
stage: 08_review
gate_blocking: fact_check
---

# Fact-check report — TBD — production working title

> Copy this file to `FCK-XX-S00E00-0000_fact-check.md` with a toolkit-allocated ID.
> Do not fill this template in place.

## 1. What was checked

| | |
|---|---|
| Script version checked | TBD — the exact file, e.g. `narration_v04.md`, and its commit |
| Cut version checked | TBD |
| Manifest version checked | TBD |
| Checked by | TBD — named person, in the Research Lead role |
| Started / completed | TBD — ISO dates |

*Why the version matters more than the date:* a report against "the script" is
unauditable. A report against a named file at a named commit can be re-run, and if
the script moves afterwards the report visibly no longer applies.

## 2. Scope

Fact-check covers **everything that asserts**, not only narration:

| Surface | Checked? | Notes |
|---|---|---|
| Narration | TBD | |
| On-screen text and titles | TBD | |
| Quotations, and their translations | TBD | Translator and edition recorded? |
| Maps | TBD | An extent is a claim. So is a border drawn with a hard edge. |
| Charts and data graphics | TBD | Including the axis, the baseline, and the units |
| Timelines | TBD | Adjacency reads as causation; check the relations are asserted |
| Captions and subtitles | TBD | |
| Episode description and metadata | TBD | The text most likely to be quoted back |
| Thumbnail and artwork text | TBD | |
| Credits and AI-use statement | TBD | |

*Why the description is on this list:* it is written last, quickly, by whoever is
available, and it travels further than the episode.

## 3. Claim-by-claim result

| Claim | Register asserted in script | Register the evidence supports | Tier met? | Independence checked? | Result |
|---|---|---|---|---|---|
| TBD — `CLM-XX-0000` | TBD | TBD | TBD | TBD | TBD — pass / amend / fail |

**Independence** is the column most often waved through. Two sources that share an
upstream origin are one source, and the second one lends the first a corroboration
it never earned. Independence is asserted deliberately on the claim record; it is
never inferred from two different titles.

## 4. Findings

One row per finding. A finding is a specific defect at a specific locator, not an
impression.

| # | Locator | Finding | Severity | Required action | Owner | Status |
|---|---|---|---|---|---|---|
| 1 | TBD — file, anchor, timecode | TBD | TBD — blocking / amend / note | TBD | TBD — role | TBD — open / resolved / accepted |

Severity meanings:

| | |
|---|---|
| **blocking** | The gate cannot be signed. The statement is unsupported, mis-registered, or contradicted. |
| **amend** | The statement is defensible but the wording overstates. Fix the wording. |
| **note** | Correct as it stands; recorded because it will be queried. |

## 5. Statements without a claim reference

| Locator | Statement | Disposition |
|---|---|---|
| TBD | TBD | TBD — claim created `CLM-XX-0000` / rewritten as framing / cut |

Every entry here is either a fact that needs a record, or a sentence that was
asserting on the script's own authority. There is no such authority. This table
exists because that is the single most common way an unsourced statement reaches
air: not by anyone deciding to, but by nobody noticing the reference was missing.

## 6. Accepted limitations

Things known to be imperfect and shipped anyway, with a reason and a correction
path. Recording them here is what makes a later correction a follow-through rather
than an embarrassment.

| Limitation | Why accepted | Who accepted | Correction path |
|---|---|---|---|
| TBD | TBD | TBD — role and person | TBD — `COR-XX-0000` if raised |

## 7. Result

**Recommendation:** TBD — sign / sign with amendments listed above / do not sign.

**Blocking findings outstanding:** TBD — count, or `none`.

The signature goes on [../production.yaml](../production.yaml) alongside the
committed checklist. A signature without a committed checklist is treated as
`pending` by the validator — deliberately, because the checklist is the evidence and
the signature is only the claim about it.
