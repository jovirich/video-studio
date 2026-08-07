---
title: 00_brief — the case for making this
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [showrunner, story-producer]
---

# 00_brief

The stage where a production earns the right to exist. Everything downstream
inherits the decisions made here, and none of it can repair a bad one.

## What goes here

| File | What it is |
|---|---|
| `brief.md` | The commissioning case: question, stakes, audience, scope, risks, advisory position |
| `thesis.md` | The answer the evidence currently supports, at its current confidence, with what would falsify it |
| `greenlight.md` | The completed greenlight checklist, committed at the path named in [../production.yaml](../production.yaml) |
| `sensitivity_pass_01.md` | The Cultural Advisor's first-pass findings on the premise |

Templates: [_TEMPLATE_brief.md](_TEMPLATE_brief.md), [_TEMPLATE_thesis.md](_TEMPLATE_thesis.md).

Naming: lowercase, underscores between fields, no dates in the filename unless the
artefact is genuinely dated — then ISO, per
[../../../standards/naming_conventions.md](../../../standards/naming_conventions.md).

## Before this stage starts

- The line is `open` — all three opening conditions in its `line.yaml` are true.
  A production greenlit against a `candidate` line has no research lead, no advisory
  contact, and no idea what archives exist. See [../../line/line.yaml](../../line/line.yaml).
- The production has a slate slot and a `production.yaml` allocated by the scaffolder.

## Before this stage can be left

The **greenlight** gate is signed by the Showrunner, certifying:

1. There is a **question with stakes**, not a topic. The distinction is not
   pedantry: a topic produces a cut with no spine, and the absence is not visible
   until the assembly, by which point the money is spent.
2. The subject falls inside the line's **advisory coverage**, and the advisor has
   accepted it. `advisory_coverage.covered: true` on the production record.
3. A **Research Lead is named** — a person, not a plan to find one.
4. **Consultation fees are budgeted.** `consultation_fees_budgeted: false` at
   greenlight is a red flag, not a detail to settle later; settling it later means
   asking people to work unpaid because the budget was already allocated.
5. **Conflicts of interest are declared.** An empty array asserts the question was
   asked.

The **sensitivity** gate runs its first of three passes here, on the premise. A hold
raised at the brief costs a conversation. The same hold raised at picture lock costs
the sequence.

## What this stage does not do

It does not decide what is true. The thesis written here is provisional by
construction, and [01_research](../01_research/) exists to attack it. A brief that
cannot survive its own research was worth writing; a brief that research is not
permitted to overturn was not a brief.
