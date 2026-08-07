---
title: Review templates — see ops/checklists
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer]
---

# Review templates

**The canonical gate checklists live in [../../ops/checklists/](../../ops/checklists/).
Not here.**

There is no checklist template in this directory, and that absence is deliberate.

## Why a checklist is not a template

A gate is a named human certifying a specific claim **against a written checklist**,
and recording a signature
([../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §1).
The checklist is fixed **in advance**, is the same for every production, and is the
evidence the signature refers to.

A per-production template would make each checklist a document that can be edited by
the person about to sign it. That is not a checklist; it is a form. The whole
mechanism depends on the list being written by someone other than the person working
against it, at a time other than the moment of signing.

## Where each part lives

| Thing | Where | Why there |
|---|---|---|
| What a gate **is**, its states, holds, separation of duties, re-opening | [../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) | True of every production, whatever the genre |
| **Which** gates exist, their owners, and what each certifies | the pack's `gates.yaml` — e.g. [../../packs/documentary-history/gates.yaml](../../packs/documentary-history/gates.yaml) | A brand film has no fact-check gate and should not be forced to fake one |
| The **checklist content** for each gate | [../../ops/checklists/](../../ops/checklists/) and the pack's [checklists/](../../packs/documentary-history/checklists/) | Fixed in advance, identical across productions |
| The **completed** checklist for one gate on one production | that production's stage folder, at the path named in its `production.yaml` | It is evidence, and evidence belongs with the thing it is evidence of |
| The **signature** | that production's `production.yaml` | One record holds the production's true state |

Both checklist directories currently exist and are empty. That is an honest **NOT
BUILT** — see [../../docs/status.md](../../docs/status.md). Until they have content,
no gate can be signed, because there is nothing to sign against and a signature
without a committed checklist is treated as `pending` by the validator.

## What review-shaped templates do exist

They are production artefacts rather than gate checklists, and they live with the
production:

| Template | For |
|---|---|
| [../production/08_review/_TEMPLATE_fact_check_report.md](../production/08_review/_TEMPLATE_fact_check_report.md) | The fact-check findings on one production |
| [../production/08_review/_TEMPLATE_cut_notes.md](../production/08_review/_TEMPLATE_cut_notes.md) | Notes from one screening, including the generated-shot QC pass |
| [../records/_TEMPLATE_fact_check.md](../records/_TEMPLATE_fact_check.md) | The registry-side record of a fact-check |
| [../records/_TEMPLATE_advisory_ruling.md](../records/_TEMPLATE_advisory_ruling.md) | A written ruling by the Cultural Advisor |
