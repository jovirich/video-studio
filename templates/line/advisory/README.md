---
title: advisory — advisors, rulings, holds
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [cultural-advisor, showrunner]
---

# advisory

The line's advisory register, its rulings, and the terms under which advisors work.

```
advisory/
├── register.md              who advises this line, on what, and the coverage gaps
├── rulings/                 ADV-XX-0000_<slug>.md
└── terms_of_engagement.md   fees, credit, review rights, right to withdraw
```

Template: [../../records/_TEMPLATE_advisory_ruling.md](../../records/_TEMPLATE_advisory_ruling.md).
Agreement: [../../legal/advisor_agreement.md](../../legal/advisor_agreement.md).
Procedure: [../../../packs/documentary-history/07_cultural_sensitivity.md](../../../packs/documentary-history/07_cultural_sensitivity.md).

## Coverage is checked at greenlight, not at review

A production is not greenlit outside its line's advisory coverage. The check is on
the production record (`advisory_coverage.covered`), and the `gaps` field is the
useful one: **naming what is not covered** is what stops a production drifting into
material nobody qualified has agreed to look at.

An empty `gaps` list asserts that the question was asked and the answer was none. It
is not a default.

## The advisory hold

The one authority the Showrunner cannot unilaterally override.

| | |
|---|---|
| Who may raise one | **Any contributor.** No standing, no seniority, no route through a manager. |
| When it takes effect | Immediately. Work on the item freezes before the discussion, not after it. |
| Who releases it | The Cultural Advisor, **in writing**, as a recorded ruling. |
| What happens to the person who raised it | Nothing. Ever. |

That last row is not a courtesy. If it is not visibly, demonstrably true, nobody
raises the second hold, and the mechanism is gone while still appearing in the
documentation.

[../../../core/04_review_gate_framework.md](../../../core/04_review_gate_framework.md) §6.

## Rulings are records, not conversations

A ruling records the question, the material at issue, the decision, the reasoning,
and the conditions attached. It is referenced by `advisory_ref` from every record it
governs, and a record at `sensitivity: held` cannot validate without one — the schema
requires it.

Writing the reasoning down is what makes the next, similar question cheaper. A studio
that resolves the same category of question three times from scratch has an advisor
doing avoidable work, and is paying for it.

## Advisors are paid, credited, and given a review

All three. Not a choice among them.

- **Paid.** `consultation_fees_budgeted: false` at greenlight is a red flag, because
  settling it later means asking someone to work unpaid after the budget is gone.
- **Credited by name**, or in the form they chose — named, anonymised, or withheld.
- **Given the opportunity to review** the material they informed, before it airs,
  with enough time to respond.

Consultation with a community is not sourcing; it is a relationship. It carries a
fee, a credit, and a copy of the finished work.
[../../../core/01_provenance_and_ai_disclosure.md](../../../core/01_provenance_and_ai_disclosure.md) §7.

An advisor may withdraw. The terms — what withdrawal removes from the credits, and
what it can and cannot undo after release — are on the agreement, agreed in advance,
because agreeing them during a disagreement is not agreeing them.
