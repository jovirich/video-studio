---
title: Advisory register — Nigeria line
status: template
version: 0.1.0
updated: 2026-08-07
owners: [cultural-advisor, showrunner]
---

# Advisory register

Who advises this line, on what, on what terms, and where the gaps are.

> **Status: NOT STARTED.** No advisor has been approached, engaged, or contracted.
> This register is empty.
>
> **This blocks the line from opening.** Condition 2 of the three in
> [bible/00_charter.md](../../../bible/00_charter.md) §2 — *at least one advisory
> contact with standing in the region has agreed to review* — is false in
> [../line.yaml](../line.yaml), and the
> [production_line schema](../../../../../standards/schemas/production_line.schema.json)
> refuses `line_status: open` while it is.
>
> It is the condition most likely to be skipped under enthusiasm, and it is the one
> that cannot be repaired after publication.

## 1. Why this register has teeth rather than good intentions

A studio depicting histories that belong to living communities, using tools that can
manufacture any image on request, has an unusual capacity to do harm quickly and at
scale. Good intentions do not scale; process does
([pack 07 §1](../../../../../packs/documentary-history/07_cultural_sensitivity.md)).

This register is the instrument. It is not a courtesy list and it is not a credit
block. It is the record that determines **what this line is permitted to make**, and
it is consulted at greenlight, before generation, and at picture lock.

## 2. What the register records, per advisor

All `TBD`. No entry exists.

| Field | Content | Why it is not optional |
|---|---|---|
| Name and contact | `TBD` | — |
| **Standing** | `TBD` — the basis on which they hold this competence: lineage, office, training, institutional position, community recognition | *"An elder from the village"* is not standing ([oral history protocol §3](../../../../../packs/documentary-history/methodology/oral_history_protocol.md)). Standing is what makes a ruling defensible when it is challenged, and it is what a viewer is entitled to know when the advisor is credited. |
| **Competent to rule on** | `TBD` — the specific traditions, communities, periods, practices, and languages | An advisor asked to rule outside their competence will usually try to help. That is the failure: a courteous answer becomes a studio decision, and neither party intended it to be one. |
| **NOT competent to rule on** | `TBD` — written explicitly, agreed with the advisor | The most-skipped field and the most load-bearing. Without it, one advisor silently becomes "the advisor" for a continent's worth of material, which is exactly the flattening [pack 07 §6](../../../../../packs/documentary-history/07_cultural_sensitivity.md) prohibits — *"African" is not a culture. Nor is "Nigerian".* |
| Communities and traditions covered | `TBD` | Defines the line's coverage envelope. See §3. |
| Languages | `TBD` | Feeds the [language register](../languages/README.md) and pronunciation verification ([voice_policy.md](../languages/voice_policy.md)) |
| Conflicts of interest | `TBD` | Declared, not concealed. Declaration does not disqualify; concealment does ([pack 01 §5](../../../../../packs/documentary-history/01_editorial_standards.md)). |
| **Terms** | `TBD` — see §4 | — |

## 3. Coverage and gaps

The register records the communities and traditions covered **and the gaps not yet
covered**, and the gaps are recorded as prominently as the coverage.

> **A line does not begin production on material outside its advisory coverage.** If
> the register has no one competent on a tradition a production needs, the production
> waits.
> — [pack 07 §5](../../../../../packs/documentary-history/07_cultural_sensitivity.md)

This is checked at **greenlight**, which is where it is cheap. A production greenlit
outside coverage will reach the sensitivity gate having already spent its research and
generation budget, and at that point every incentive in the room argues for finding
someone quickly rather than finding the right person.

The coverage envelope is therefore a **scheduling input**, not a compliance check. The
slate is built from what the register covers, or the register is extended first — and
extending it takes months, because it means approaching people through recognised
channels, agreeing terms, and paying them.

An honest gaps section is uncomfortable to write and is the most useful part of this
document. A register that claims complete coverage of a region's traditions is either
wrong or is describing an advisor who has been asked to overreach.

## 4. Terms

Recorded per advisor, agreed in writing before any work, `TBD` for all.

| Term | Position |
|---|---|
| **Fee** | Agreed and budgeted **before the approach**, and paid promptly — on the advisor's terms, not the studio's payment cycle. *"Advisors are paid. An advisor who is not paid is not an advisor; they are a favour being taken advantage of, and they will eventually and rightly stop answering"* ([pack 07 §5](../../../../../packs/documentary-history/07_cultural_sensitivity.md)). Consultation is labour, not a favour ([bible/00_charter.md](../../../bible/00_charter.md) §7). |
| **Credit** | By name, in the form they choose, including the option not to be credited |
| **Review rights** | What they see, when, and how long they have. Material they informed is shown to them before it airs. |
| **Right to withdraw** | Explicit, with an honest statement of what withdrawal can and cannot undo after release |
| **Scope of use** | What their contribution may be used for. Consent for a production is not consent for a trailer, a thumbnail, or a training set ([pack 07 §7](../../../../../packs/documentary-history/07_cultural_sensitivity.md)). |
| **AI processing** | Stated explicitly. Consent obtained without stating the AI processing scope is not valid for this studio's purposes ([pack 07 §8](../../../../../packs/documentary-history/07_cultural_sensitivity.md)). |
| **Finished work** | Provided to them, and to the community where relevant, in a form they can actually access |

## 5. Hold authority

**Any contributor may file a `[sensitivity]` issue, which places an advisory hold on
the affected asset, shot, sequence, or record. The hold takes effect immediately.**

Under hold: no further generation on the held item; the item cannot enter an edit or
pass any gate; the hold is released **only by a written ruling from the Cultural
Advisor**, recorded in this register as an `ADV-NG-*` ruling.

> **The Showrunner cannot unilaterally release a hold.**

That is the single structural check on the Showrunner's editorial authority in this
studio ([pack 07 §4](../../../../../packs/documentary-history/07_cultural_sensitivity.md),
[bible/00_charter.md](../../../bible/00_charter.md) §6). It exists because the cost of
being wrong here is borne by people outside the studio, who have no other lever.

Four properties are core requirements
([core/04 §6](../../../../../core/04_review_gate_framework.md)) and no layer may
weaken them:

1. **Any contributor may raise a hold**, without needing standing or seniority. A
   junior editor, a freelance translator, and an advisor have identical authority to
   raise one.
2. **It takes effect immediately** — before anyone assesses whether it is justified.
   The assessment is the ruling; the hold is not conditional on it.
3. **It is released only in writing**, by the Cultural Advisor, and the ruling is
   recorded here permanently.
4. **The person who raised it is never penalised. Ever.** The first time that rule is
   bent, holds stop being raised — and the problems do not stop, they merely stop
   being visible from inside the studio.

Disagreement escalates to a documented ruling with the advisory contact for the
relevant community. It does not escalate to a meeting where the deadline is mentioned.

### Rulings

`ADV-NG-NNNN`, permanent, never reused
([standards/id_system.md](../../../../../standards/id_system.md)). Each records: what
was held, who raised it, when, the question, who ruled, the reasoning, the outcome, and
what changed as a result.

**None exist.** Rulings accumulate into the line's actual working knowledge of where
the boundaries are, and a ruling reversed later is superseded rather than deleted.

## 6. Review points

The sensitivity gate runs three times per production
([pack 07 §9](../../../../../packs/documentary-history/07_cultural_sensitivity.md)):

| Point | Question |
|---|---|
| Greenlight | Does the premise clear, and is it inside advisory coverage? |
| **Before generation** | Do these prompts clear? |
| Picture lock | Does the cut clear? |

The middle one is the one that matters and the one that gets moved. Review happens
**before generation, not before publication** — because once a striking image exists,
the argument about whether it should exist becomes much harder to win, and the person
arguing against it is arguing against something everyone in the room can already see.

## 7. Approaching an advisor

Before the first approach, and in this order:

- [ ] The Cultural Advisor role is filled at studio level (`TBD` in [studio.yaml](../../../studio.yaml))
- [ ] The **recognised channel** is identified. An unannounced approach to a knowledge
      holder can itself be a breach.
- [ ] The fee is agreed and budgeted
- [ ] What the work is, where it will be shown, in what media, and for how long is
      stated plainly — including the AI processing scope
- [ ] The boundary around **restricted knowledge** is established *before* the
      conversation, not during it

## 8. What is missing right now

Everything. No Cultural Advisor at studio level, no advisory contact for this line, no
terms, no coverage, no gaps documented, no rulings.

Until at least one advisor is engaged on recorded terms, this line cannot open, no
production can be greenlit, and no generation may occur — and no amount of documenting
the process substitutes for a person who has agreed to do it.
