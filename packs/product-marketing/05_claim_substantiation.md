---
doc: packs/product-marketing/05
title: Claim substantiation
status: active
version: 0.1.0
updated: 2026-08-07
owners: [rights-and-clearances]
---

# 05 — Claim substantiation

This is the load-bearing document of the pack. Everything else here is craft.

Documentary's evidence chain exists because a viewer cannot check whether a walled
city enclosed forty hectares. This pack's exists for the opposite reason: a viewer
**can** check whether the product does the thing, will do it within a week of buying
it, and costs what the film said. A false product claim is not a slow credibility
leak. It is a refund request, a contract dispute, and in several categories a
regulatory matter.

## 1. The rule

> **Nothing on screen may assert a capability, performance level, price,
> availability, or comparison that is not recorded as a `product_claim` with a
> named evidence reference and an approver's signature.**

Scripts do not contain product facts. Scripts contain *references to claims*, on the
same principle as [documentary-history](../documentary-history/02_evidence_and_sourcing.md) §1
and for a different reason.

```
   evidence artefact (test run, ticket, price list, screen recording)
                          ▲
                          │ cited by
   product_claim record   PCL-<SCOPE>-<NNNN>   ← the assertion + status + approver
                          ▲
                          │ referenced by
   02_script/vo.md        "... {{PCL-GT-0014}} exports in under a minute ..."
```

The claim record holds the assertion, its evidence, the version of the product it was
true of, its approver, and its expiry. The script holds a pointer. This is what makes
it possible to answer "was that true when we shipped it?" a year later, and to find
every asset that needs pulling when it stops being true.

**Claims about the world, not the product** — market size, industry history,
regulatory background, social trends — are out of this pack's scope and are not
covered by a `product_claim`. If a piece needs them, it needs
[documentary-history](../documentary-history/)'s chain, not this one. See
[README.md](README.md) § What this pack deliberately does not cover.

## 2. What counts as a product claim

The test is not "does it sound like a claim". It is: **could a customer point at
this frame and say the product did not do that?**

| Kind | Shape on screen | Claim? |
|---|---|---|
| Capability | "Exports to PDF", "works offline" | **Yes** |
| Performance | "In under a minute", "handles 10,000 rows" | **Yes**, and needs a measured basis |
| Availability | "Available today", "on iOS and Android" | **Yes**, per territory and platform |
| Price | Any figure, any "free" | **Yes**, and expires fastest |
| Comparison | "Faster than", "unlike other tools" | **Yes** — and see §8 |
| Outcome | "Teams ship twice as often" | **Yes**, and it is a claim about *customers*, not the product |
| Compatibility | Named third-party integrations | **Yes**, including the right to name them |
| Security and compliance | Certifications, standards, data handling | **Yes**, and always §10 |
| Aspiration | "Built for people who care about their craft" | No |
| Mood, tone, atmosphere | Landscapes, hands, light, music | No |
| Naming the category | "A design tool" | No |

The right-hand column is why this pack is small. Roughly ten percent of a marketing
film's frames carry claims. Gating the other ninety percent produces theatre.

**The implicit claim rule.** A shot asserts what it shows. A screen recording of a
feature is a capability claim even if narration says nothing, and an interface shown
alongside a spoken price implies the price applies to that tier. Implicit claims are
recorded like spoken ones; the checklist at the substantiation gate walks the picture
track, not only the script.

## 3. Claim approval authority

`studio_must_decide: claim_approval_authority` — [pack.yaml](pack.yaml).

A studio adopting this pack names, before its first brief, who holds each of the
following. `studio_ops` refuses greenlight while any is unresolved.

| Authority | What it decides | Default if the studio does not decide |
|---|---|---|
| **Claim owner** | Proposes the claim and supplies the evidence. Normally the product owner for the surface concerned. | TBD — the studio names a role per product area |
| **Claim approver** | Signs that the evidence supports the assertion at the stated strength. | TBD — must not be the same person as the claim owner |
| **Legal reviewer** | Signs claims in the categories at §10. May be external counsel. | TBD — the studio names a person or firm, or declares that no legal review is available and therefore that §10 categories are out of scope |
| **Gate owner** | Signs the `claim_substantiation` gate for the production as a whole. Fixed by [gates.yaml](gates.yaml) as `rights-and-clearances`. | Fixed; not a studio decision |

Four rules on that table, none of them negotiable downward:

1. **Owner and approver are different people.** The person who wants the claim in the
   film is the worst available judge of whether it is supported. This is the same
   principle as core's separation of duties
   ([../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §5),
   applied one layer below the gate.
2. **Approval is on a version of the product**, recorded on the claim. "Approved" with
   no build, release, or date attached is not approval; it is a memory.
3. **The gate owner may refuse a claim an approver signed.** The approver certifies
   the evidence; the gate owner certifies that the *film* does not overstate it. A
   supported claim can still be misleading in the cut — see §6.
4. **Silence is refusal.** An unanswered approval request is not tacit approval, and
   a claim without a signature does not go in on the grounds that the deadline moved.

**Escalation.** Where owner and approver disagree, the Showrunner decides whether the
claim is cut or the evidence is strengthened. The Showrunner cannot overrule a legal
reviewer's refusal in a §10 category; that path is: change the claim, or do not ship
the piece.

## 4. Evidence types

Every `product_claim` carries at least one evidence reference. What counts:

| Type | Code | What it is | Sufficient alone? |
|---|---|---|---|
| **Direct observation** | `E-OBS` | A screen recording, session capture, or device capture of the product doing the thing, on a stated build. | Yes, for capability claims. |
| **Measurement** | `E-MSR` | A recorded run with stated hardware, dataset, configuration, and repetitions. | Yes, for performance claims — with the conditions on screen or in the description. |
| **System of record** | `E-SYS` | Price list, entitlement matrix, release plan, store listing, feature flag state, support matrix. | Yes, for price, availability, and compatibility. |
| **Customer attestation** | `E-CUS` | A named customer's own statement, given knowingly, with a signed release covering this use. | Yes, for outcome claims — attributed to them, never generalised. |
| **Third-party assessment** | `E-3P` | An audit, certification, or assessment by a body outside the studio. | Yes, within its own scope and term. |
| **Internal assertion** | `E-INT` | "Engineering says it does." | **Never sufficient.** A lead, not evidence. |

`E-INT` is this pack's T5. It is how a claim that nobody has actually watched the
product make good on reaches a finished film, and it is the most common real failure
in this genre — not malice, just a slot in the edit and a Slack message that sounded
confident.

**Evidence has a shelf life.** Every evidence reference records the date and the
product version observed. A claim whose evidence predates the current release is
`stale` and must be re-observed before the gate signs, because the most dangerous
claim is one that used to be true.

## 5. Roadmap language policy

`studio_must_decide: roadmap_language_policy` — [pack.yaml](pack.yaml).

"Coming soon" is a commitment someone has to keep, made by a video team, on behalf of
an engineering team, to an audience that will remember. It is also the single easiest
way for a marketing film to make a claim nobody intended: the shipped-versus-planned
boundary is invisible in a cut unless something puts it there.

The studio decides, once, and records it in `studio.yaml`:

| Decision | Options | Default pending a decision |
|---|---|---|
| May unreleased functionality appear on screen at all? | never / with a qualifier / freely | **Never.** The safe default is that the film shows what ships today. |
| If permitted, what qualifier, and where? | persistent on-screen mark / a card at first appearance / narration only | **Persistent on-screen mark for the duration of the shot**, on the same reasoning that governs the reconstruction mark in documentary — narration is missed, mute autoplay is common, and clips get re-cut |
| Who may commit to a date? | named role only | TBD — the studio names the role. Not the video team. |
| What happens when the date slips? | the asset is pulled, re-cut, or annotated | TBD — decide the mechanism before the first dated claim exists |

Rules that hold whatever the studio decides:

- **A date is a claim.** "Coming in Q3" is a `product_claim` with an approver and an
  expiry, not a piece of copy. Approval comes from the role that can actually move
  the date.
- **"Coming soon" without a date still expires.** It carries a review date on the
  claim record. An asset in market that still says "coming soon" about a feature that
  shipped eighteen months ago is a different kind of false, and no less false.
- **A qualifier is not a licence to show the thing working.** A demo of unreleased
  functionality is still a capability claim; the qualifier tells the viewer *when*,
  not *whether*. The functionality must exist and be captured under §6 of
  [06_product_depiction.md](06_product_depiction.md) — you may not render a screen
  for a feature that has not been built. That is the pack's non-negotiable and it
  applies with more force to roadmap material, not less, because there is nothing to
  capture and therefore maximum temptation.
- **Beta, preview, and limited availability are availability claims**, and the
  conditions (who can get it, where, at what price) are on the claim record.

## 6. Metrics and figures

A number on screen is an assertion with a decimal point, and it is read as more
precise than the prose around it.

- **State the basis.** Every figure records what was measured, on what, when, and how
  many times. A performance figure without its conditions is unsubstantiated
  regardless of how carefully it was measured.
- **Distinguish measured, modelled, and reported.** Measured is a run the studio can
  reproduce. Modelled is a projection with assumptions. Reported is what a customer
  told you. They are labelled differently on screen and are never averaged together.
- **Best case is labelled as best case.** A figure from the fastest run on the best
  hardware is not the figure; showing it as the figure is the misleading-true-statement
  failure from [documentary-history](../documentary-history/01_editorial_standards.md) §1,
  which is as fatal here as it is there.
- **Aggregates need their denominator.** "Most users", "teams typically", and "up to"
  each hide a distribution. Record the population and the period on the claim.
- **No figure is invented to fill a slot in the edit.** If the graphic needs a number
  and no number is substantiated, the graphic changes. This is the point at which
  generative tooling is most dangerous in this genre: a model will happily produce a
  plausible chart, and a plausible chart is a fabricated evidentiary artefact under
  [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 item 1.
- Data graphics follow [../../standards/data_graphics.md](../../standards/data_graphics.md):
  no truncated axes, uncertainty shown, source and date in frame.

## 7. Pricing and availability

The fastest-expiring claims on the platform, and the ones most likely to outlive
their evidence because the film is still running when the price changes.

| Claim | Must record | Expires when |
|---|---|---|
| A price | Currency, tier, billing period, tax treatment, territory | The price list changes |
| "Free" | What is free, for how long, what it converts to, whether a card is required | The entitlement changes |
| "Available now" | Platforms, territories, account types, rollout state | Rollout state changes |
| A discount or offer | Start, end, eligibility, code | The end date passes |

Two structural requirements:

1. **Every price and availability claim carries an expiry** on its record, and the
   assets referencing it are listed there. When the claim expires, the list is what
   tells you which files to pull. Assembling that list after the fact, from memory,
   across a year of cutdowns, is the avoidable emergency this rule exists to prevent.
2. **Tax, currency, and consumer-pricing display rules are jurisdiction-specific.**
   Whether a price may be shown exclusive of tax, what currency conversion may be
   implied, and what must accompany a headline price differ by territory and change.
   This pack does not state a rule. **Escalate to the legal reviewer named under §3
   for every territory in the distribution footprint**, and record the ruling on the
   claim.

## 8. Comparisons

Any assertion that positions the product against something else — named competitor,
unnamed competitor, "the old way", the studio's own previous version — is a
comparison claim.

- **Comparisons against a named third party are out of scope for this pack.**
  Comparative advertising is governed by jurisdiction-specific rules that differ on
  what may be named, what must be substantiated, how the comparison must be
  constructed, and what the remedy is when it is wrong.
  **Escalate.** See [07_brand_and_message.md](07_brand_and_message.md) §4.
- **Unnamed comparisons are still comparisons.** "Other tools make you wait" is an
  assertion about other tools. It carries the same evidence obligation as naming one,
  and frequently less legal cover, because it may be read as covering every
  competitor at once.
- **Self-comparison is the safe form and still needs evidence.** "Twice as fast as
  our previous release" requires both measurements, under the same conditions,
  recorded.
- **A comparison must be like-for-like.** Comparing your best configuration to a
  competitor's default, or your current version to their year-old one, is the
  misleading-true-statement failure again and is refused at the gate.

## 9. The `product_claim` record

Declared in [pack.yaml](pack.yaml) `required_record_types`. ID grammar follows
[../../standards/id_system.md](../../standards/id_system.md); this pack allocates the
`PCL` type at line scope. Records live under the line's registry and are never
deleted — a withdrawn claim is `retracted` with a reason, which is how the studio
remembers what it stopped saying and why.

```yaml
id: PCL-<SCOPE>-0014
type: product_claim
status: draft | review | locked | superseded | retracted
kind: capability | performance | availability | price | comparison | outcome | compatibility | compliance
assertion: >
  The exact words or the exact thing shown. Written as it will be understood, not
  as it is technically defensible.
strength: ships-today | limited-availability | roadmap
product_version: <build or release the claim was verified against>
territories: [<territory codes>]        # where the claim is true
platforms: [<platforms>]                # where the claim is true
evidence:
  - { type: E-OBS, ref: <artefact id or path>, observed_at: <iso8601>, observed_by: <person> }
conditions: >
  What must be true for the assertion to hold. Hardware, plan tier, dataset,
  configuration. Empty is a decision, not an omission.
owner: <role or person proposing>
approver: { role: <role>, person: <person>, signed_at: <iso8601> }
legal_review: { required: true|false, category: <§10 category>, ref: <ruling>, signed_at: <iso8601> }
expires_at: <iso8601 or review date>
used_in: [<asset or production ids>]     # what to pull when this stops being true
supersedes: <claim id>
retraction_reason: <required when retracted>
```

`used_in` is the field teams skip and later wish they had not. It is the difference
between "the price changed" being a ten-minute task and a two-day archaeology
exercise across every cutdown, thumbnail, and paid variant derived from the master.

## 10. What requires legal review, by category

Reviewed by the legal reviewer named under §3, in addition to the ordinary approver.
This list is a floor. It is not jurisdiction-specific advice and does not attempt to
be, because the rules differ by territory and change; the discipline it encodes is
*route these to someone qualified in the relevant jurisdictions before the shoot,
not before the delivery*.

| Category | Why | Disposition |
|---|---|---|
| Health, medical, wellbeing, or safety outcomes | Regulated in most territories; substantiation standards are set externally, not by the studio | Escalate. Out of this pack's scope — see [README.md](README.md) |
| Financial products, returns, savings, or credit | As above | Escalate |
| Content aimed at, or likely to reach, children | Separate advertising regimes | Escalate |
| Environmental and sustainability claims | Substantiation standards are specific and tightening in several territories | Escalate |
| Security certifications, compliance standards, data residency | The claim is about a third party's assessment, with a scope and a term the film will flatten | Legal review, plus the certificate itself as `E-3P` |
| Comparative claims naming a third party | §8 | Escalate |
| Third-party names, marks, or logos on screen | Permission to name is separate from permission to depict, and separate again from implying endorsement | Legal review; see [07_brand_and_message.md](07_brand_and_message.md) §4 |
| Any customer's name, likeness, or premises | Consent scope, including whether it covers AI processing — [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §7 | Legal review of the release, before the shoot |
| Prize draws, offers, and eligibility terms | Territory-specific rules on what accompanies the offer | Escalate |
| Any claim the studio intends to run as paid media | Platform ad policies apply on top of everything here | Escalate to distribution |

Where a studio has no legal reviewer, the categories above are not "approved by
default". They are **out of scope**: the piece does not make the claim.

## 11. Inheritance and enforcement

This document adds to core and tightens nothing away from it. Specifically, it
inherits without modification:

- [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 —
  no fabricated evidence, no unconsented likeness or voice, no autonomous
  publication, nothing generated presented as found material. A fabricated metric,
  chart, screen, or testimonial is prohibited here by that section, not by this one.
- [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) — clearance on every asset.
- [../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) — what a gate is, and separation of duties.

| Standard | Gate | Mechanism |
|---|---|---|
| §1, §2 | `claim_substantiation` | Every `{{PCL-…}}` reference resolves to a locked record; picture track walked for implicit claims |
| §3 | Greenlight | Studio cannot greenlight with `claim_approval_authority` unresolved |
| §5 | `claim_substantiation` | Roadmap-strength claims listed separately and approved separately |
| §7 | `technical_qc` | No claim past its expiry in a delivered package |
| §10 | `stakeholder_approval` | Legal signature present where the category requires it |

Checklists: [../../ops/checklists/](../../ops/checklists/). Gate definitions: [gates.yaml](gates.yaml).
