---
doc: bible/12
title: Amendment log
status: active
version: 0.1.0
owners: [showrunner]
---

# 12 — Amendment log

Append-only. Every change to any Bible document is recorded here before it takes
effect. An amendment absent from this log has no force, and the prior text stands.

## Format

```
## <YYYY-MM-DD> — <short title>

**Documents:** bible/NN, bible/NN
**Version:** <old> → <new>
**Signatures:** <role: name>, <role: name>
**Supersedes:** <link to the prior text, or "n/a — new section">

**Change**
<What is different, stated so a reader who has not seen the diff understands it.>

**Rationale**
<Why. What went wrong, or what was learned, that made the old text inadequate.>

**Migration**
<What existing records, scripts, or assets are invalidated, and the command or
procedure that brings them into compliance. "None" is an acceptable answer only if
it is true.>
```

## Required signatures

| Section changed | Signatures required |
|---|---|
| Any | Showrunner + Cultural Advisor |
| 02 Evidence and sourcing | + Research Lead |
| 08 Rights and licensing | + Rights & Clearances |
| 04, 05, 10 (technical specs) | + Pipeline Engineer |
| 07 Cultural sensitivity | + the relevant line's advisory contact |

## Standing rule

A Bible amendment is never bundled into an episode PR. It rides on a `studio/bible-*`
branch and is reviewed on its own merits, because a change to canon justified by one
episode's convenience is how a standard erodes.

---

# Log

## <YYYY-MM-DD> — Initial ratification

**Documents:** bible/00 through bible/12
**Version:** — → 0.1.0
**Signatures:** `TBD — the Bible is not yet ratified. It is a draft until the`
`Showrunner and Cultural Advisor sign, and no episode may be greenlit before that.`
**Supersedes:** n/a

**Change**
Establishes the Production Bible: charter, editorial standards, evidence and
sourcing, narrative doctrine, visual language, sound and score, AI disclosure and
ethics, cultural sensitivity, rights and licensing, localization, distribution,
glossary, and this log.

**Rationale**
The studio's method is unusual — heavy generative tooling applied to contested,
sparsely documented history belonging to living communities. That combination has
specific failure modes which informal judgement does not reliably catch under
deadline. The Bible converts judgement into process and gives the process
enforcement points.

**Migration**
None. No production work predates this document.

**Open items blocking ratification**
- `bible/00` §1 mission, §3 audience, §8 success conditions
- `bible/04` line visual identity for ng-nigeria
- `bible/05` §4 AI-generated music policy — the single decision most likely to be
  regretted if made casually
- `bible/09` §1 production language
- `bible/10` §1 target runtime and platform set

<!-- New entries are appended below this line, newest last. -->
