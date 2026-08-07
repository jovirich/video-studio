---
title: Corrections log
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead, showrunner]
---

# Corrections — African History Studio

Public. Append-only. Nothing here is ever deleted, quietly edited, or reordered.

> **This log is currently empty, and that is a statement of fact rather than a
> formatting placeholder.** No production has been published, so nothing exists to
> correct. The first entry will appear the first time this studio is wrong in public.
> A studio that has published work and has an empty correction log has either found
> nothing or is not looking.

Maturity: **DESIGNED**. The procedure below is written; it has never been run, no
correction has been triaged, and the intake address does not yet exist.

## 1. Why this document is prominent rather than buried

**A visible correction log is the strongest available evidence that the rest of the
work is honest.**

Every claim this studio makes is unverifiable by most of its audience — that is the
nature of history documentary, and it is doubly true of a studio whose imagery is
generated. A viewer cannot check the archive. What a viewer *can* check is whether
the studio behaves like an organisation that expects to be checked. A dated, specific,
publicly reachable record of the studio's own errors is the only cheap signal that
survives contact with a sceptical audience.

Corrections are therefore **not embarrassments to be minimised**. They are not
softened, not batched into an annual round-up, not phrased so the error is hard to
locate, and not written to make the studio sound as though it was nearly right. The
entry names what was said, what is true instead, and how it got through. A correction
that does not identify the failure in the process is a half-correction, because it
guarantees the same failure recurs.

The inverse is also studio policy: **a correction is never treated as a performance
problem for the person who made or reported the error.** The moment it is, reporting
stops and the errors remain — they simply stop being visible from inside.

## 2. Intake

| Route | Use when | Where it goes |
|---|---|---|
| Public correction address | Anyone outside the studio, including a viewer or a community member | `TBD — Showrunner.` Recorded in [studio.yaml](../studio.yaml) as `correction_intake`. **Blocks first publication** — an episode may not ship without a working intake address in its description. |
| `[source]` issue | A contributor disputing evidence, a figure, a date, a name form, or an attribution | Research Lead |
| `[sensitivity]` issue | A contributor or advisor disputing a depiction, a naming choice, or a use of restricted material | Cultural Advisor, and it carries an **advisory hold** under [pack 07 §4](../../../packs/documentary-history/07_cultural_sensitivity.md) — the item freezes immediately |
| Takedown contact | A rights holder or a community body | `TBD — Showrunner.` Recorded in [studio.yaml](../studio.yaml) as `takedown_contact`. |

A report is never rejected for arriving by the wrong route or from someone without
standing. It is re-routed. Requiring a reporter to know the studio's internal
taxonomy is a way of receiving fewer reports.

## 3. Triage

The procedure is the pack's — see
[01_editorial_standards.md §4](../../../packs/documentary-history/01_editorial_standards.md).
It is not restated here. What this studio binds itself to on top of it:

- **The Research Lead triages within 5 working days of receipt**, and the clock starts
  at receipt, not at the point someone gets to it. The reporter is told the outcome
  even when the outcome is "not an error" — with the reasoning.
- Where the report touches a sensitivity category, the Cultural Advisor triages in
  parallel, and the advisory hold stands until they rule in writing. The Research
  Lead's finding does not release it.
- **A report that cannot be resolved inside the SLA is logged as open**, with what is
  being checked and by when. Silence is not a triage outcome.

### Material and minor

The distinction determines the remedy, and it is drawn on the effect on the viewer,
never on the effort required to fix it.

| | **Material** | **Minor** |
|---|---|---|
| Test | A viewer who believed the original would understand something different from a viewer who believed the correction | The viewer's understanding is unchanged |
| Typically | A wrong claim; an overclaimed certainty register; a misattributed source; a caption implying a different time, place, or people; a name form the people concerned reject | A spelling; a diacritic; a credit omission; a date restated within the range the sources already gave |
| Remedy | Re-cut, or an on-screen correction card if a re-cut is impractical, **and** the correction at the top of the description, **and** an entry here | Corrected in the description **and** an entry here |
| Version | Increments the published version; the superseded master is retained | No version increment |

Two judgements are made deliberately and recorded, because the temptation runs one
way in each:

- **Register errors are material.** Stating as `established` something the evidence
  supports only as `probable` changes what a viewer takes away, even when every word
  is defensible. It is not a wording nit.
- **Name-form errors are material where the form was rejected by the people
  concerned**, per [pack 09 §3](../../../packs/documentary-history/09_localization.md).
  Treating an imposed exonym as a spelling matter is itself the error.

Silent replacement of a published file is prohibited under
[core/03 §6](../../../core/03_distribution_and_formats.md). If the file changed, the
version changed, and this log says so.

## 4. Entry format

Corrections carry a permanent, never-reused ID in the affected line's scope —
`COR-<SCOPE>-<NNNN>`, per [standards/id_system.md](../../../standards/id_system.md).
A correction spanning lines uses the `STUDIO` scope.

```
## COR-<SCOPE>-<NNNN> — <YYYY-MM-DD> — <one-line summary>

**Production:** <line> / <production code> / <published version>
**Severity:** material | minor
**Reported:** <YYYY-MM-DD> by <name, or "a viewer", or "anonymous at the reporter's request">
**Triaged by:** <role: name> on <YYYY-MM-DD>
**Claim(s) affected:** <CLM-* ids, or "none — on-screen text only">

**What we said**
<The original wording or depiction, quoted, with its timecode.>

**What is correct**
<The corrected statement, at the certainty register the evidence actually supports,
with the claim ID and source records that carry it.>

**How it happened**
<The process failure. "A transcription error survived fact-check because the figure
was checked against the script rather than the source record." Not "human error".>

**What was done**
<Re-cut / correction card / description note. The new published version. The date it
went live.>

**What changed in the process**
<The checklist item, validator rule, or record field added so this class of error is
caught next time. "None" is permitted and is a signal worth noticing if it recurs.>
```

Per-production correction logs are published alongside each episode's sources page and
provenance summary ([core/03 §5](../../../core/03_distribution_and_formats.md)); this
document is the studio-wide record and is authoritative where the two differ.

## 5. Retraction

Where a claim cannot be corrected because it should never have been made, the claim
record is marked `retracted`, keeps its ID, and records what replaced it — never
deleted, per [standards/id_system.md](../../../standards/id_system.md) § Lifecycle
states. The correction entry links the retracted claim.

A registry that looks clean because its mistakes were removed has destroyed the audit
trail that justified keeping it.

---

# Log

<!-- No corrections. Nothing has been published. -->
<!-- New entries are appended below this line, newest last. Nothing above is edited. -->
