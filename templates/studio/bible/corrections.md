---
title: TBD — studio corrections log
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [showrunner, research-lead]
---

# Corrections

> Skeleton. Copied to `studios/<code>/bible/corrections.md` and **published**.
> It starts empty. An empty corrections log on a studio that has published
> nothing is honest; an empty one on a studio with a back catalogue is a claim
> nobody believes.

This is a public document. It is linked from every production's description and from
the studio's methodology page, and it is published **from the start** rather than
created after the first error.

## What goes here

Every factual error in published work, and what was done about it. Individual
corrections are records ([../../records/_TEMPLATE_correction.md](../../records/_TEMPLATE_correction.md),
IDs `COR-*`); this log is the public index over them.

| | |
|---|---|
| **Correction** | A statement was wrong. The record is amended, the log entry is published, and the affected material is annotated or re-cut. |
| **Clarification** | A statement was defensible but read as more than the evidence supports. The wording is fixed; the substance stood. |
| **Retraction** | A claim is withdrawn. The claim record moves to `retracted` with a reason, and everything that depended on it is re-examined. |

The distinction matters because collapsing all three into "corrections" makes a
studio look either sloppier or more careless than it is, and neither reading is
useful to a viewer trying to calibrate trust.

## Rules

1. **Records are never deleted.** A retracted claim keeps its ID as a tombstone,
   with `retraction_reason`. `retracted` is how a studio remembers it was wrong
   about something, which is worth more than a registry that looks clean.
2. **The published work is annotated, not silently re-cut.** If a re-cut ships, the
   version number changes and this log says what changed between them.
3. **A correction is published whether or not anyone noticed the error.** The
   internal-audit correction is the one that establishes the log means anything.
4. **The person who reported it is credited if they wish**, and never named without
   asking.
5. **Response time is recorded**, including when it was bad. A log that only shows
   fast responses is a log with entries missing.

## Log

| Date | Production | Type | What was wrong | What it should say | Cause | Action taken | Record |
|---|---|---|---|---|---|---|---|
| TBD — ISO | TBD — `S00E00` | TBD — correction / clarification / retraction | TBD — the statement as published | TBD — the corrected statement | TBD — see below | TBD — record amended, annotation added, re-cut shipped as `v<NN>` | TBD — `COR-XX-0000` |

**Cause** is the column that earns the log its keep. Useful values are specific:
*source misread*, *claim reference pointed at the wrong record*, *register
overstated*, *graphic implied a relation nobody asserted*, *description written
without a fact-check*, *source later retracted upstream*.

"Human error" is not a cause. It is a category that contains every cause and
therefore prevents any of them being fixed.

## Reporting an error

**TBD — the studio's public intake address.**

**TBD — what a reporter can expect**: an acknowledgement within a stated period, an
assessment, and a published outcome whichever way it goes — including when the
studio concludes the original was right, which is also an outcome worth publishing.
