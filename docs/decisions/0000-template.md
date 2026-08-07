---
adr: 0000
title: ADR template
status: template
date: YYYY-MM-DD
deciders: [role-slug]
supersedes: none
superseded_by: none
---

# ADR NNNN — <short imperative title>

> Copy this file to `NNNN-kebab-title.md`. Do not edit an accepted ADR — supersede
> it with a new one and set `superseded_by` on the old.

## Context

What situation forces a decision? Include the constraint that makes the obvious
answer wrong. If there is no such constraint, this probably does not need an ADR.

State what was tried or considered informally before this, and why it was not enough.

## Decision

What is being decided, stated in the present tense as a fact about the system:
"Prompts are versioned records", not "we should version prompts".

Be specific enough that someone can tell whether a given change complies.

## Consequences

**Positive** — what this buys, concretely.

**Negative** — what this costs. An ADR with no negative consequences is not an
architectural decision; it is a preference. Name the real cost, including the one
that will tempt someone to abandon this later.

**Neutral** — what changes without being better or worse.

## Options rejected

Each with the reason. The rejected options are frequently more useful to a future
reader than the chosen one, because they are what that reader is about to propose.

## Validation

**How will we know this was wrong?** Name a concrete, observable signal — a metric,
a pattern in the git history, a class of bug, a piece of friction. An ADR without a
falsification condition can only be defended on taste.

## Links

- Evolution log entry: `docs/architecture/evolution.md#ae-nnn`
- Related ADRs:
- Bible sections affected:
- Schemas affected:
