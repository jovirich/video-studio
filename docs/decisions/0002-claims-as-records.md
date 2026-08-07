---
adr: 0002
title: Facts live in claim records, not in scripts
status: accepted
date: 2026-08-07
deciders: [showrunner, research-lead, pipeline-engineer]
supersedes: none
superseded_by: none
---

# ADR 0002 — Facts live in claim records, not in scripts

## Context

The characteristic failure of AI-assisted documentary is that generation is fast and
verification is slow. Once imagery exists, narrative pressure runs toward the
imagery, and unsourced assertions slip through because checking them is the only
part of the process that has not been accelerated.

Conventional approaches and why they fail here:

| Approach | Failure |
|---|---|
| Footnotes in the script | Do not survive re-cuts, re-orderings, or cutdowns. No mechanical check. |
| A separate bibliography document | Lists what was consulted, not what supports which sentence. |
| Trusting the researcher | Works until deadline, staff turnover, or a public challenge eighteen months later. |
| A fact-check pass at the end | Finds errors after the imagery that depends on them has been generated and paid for. |

## Decision

Facts are **records**, not prose.

- A **source record** (`SRC-*`) describes one item of evidence, its tier, its
  custody, and — mandatorily — a critique block interrogating who made it and what
  they were in a position to know.
- A **claim record** (`CLM-*`) holds one factual statement, its confidence register,
  and an evidence array of sources with locators.
- **Scripts contain references**, written `{{CLM-NG-0117}}` inline. They contain no
  bare facts.
- CI walks script → claim → source for every reference. A broken link fails the
  build.

Confidence registers (`established`, `probable`, `contested`, `inferred`,
`traditional`, `unknown`) are part of the claim, so a script's certainty is a
property of the evidence rather than of the writer's mood on the day.

## Consequences

**Positive**

- "Where did that come from?" is answerable for any frame, permanently, without the
  original researcher.
- Cutdowns, trailers, and translations inherit the evidence chain automatically —
  the validator runs on them too.
- The bibliography, sources page, and citation appendix are generated, not written.
- Contested history becomes cheap to handle correctly: `confidence: contested`
  requires named positions, so the honest treatment is the path of least resistance.
- `unknown` becomes a first-class, recordable state rather than a gap someone is
  tempted to fill.

**Negative**

- Substantially more upfront research overhead per screen minute. This is the real
  cost and it is not small.
- Writers draft against a registry rather than freely. Some find this constricting.
- Risk of the discipline inverting: claims created retroactively to satisfy the
  validator. Watched for in [../architecture/evolution.md](../architecture/evolution.md) AE-002.

**Neutral**

- Requires ID allocation tooling from day one. Hand-allocated IDs collide.

## The T5 rule

Language-model output is tier T5 and is **never citable**. A model may help locate,
summarise, translate, or structure — its assertions are leads. This is stated in the
schema (a T5 source may support zero claims) as well as in the Bible, because it is
the single rule most likely to erode under time pressure.

## Validation

Failure signal: claim records appearing in git history *after* the script drafts that
reference them. That inversion means the validator is being farmed rather than
served, and the system is producing an appearance of rigour instead of rigour.
