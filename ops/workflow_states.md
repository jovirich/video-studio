---
title: Workflow states
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner]
---

# Workflow states

The production lifecycle: what enters each stage, what leaves it, which gate closes
it, and what it costs to re-open one.

**This document describes the framework, not a fixed gate set.** Core defines what a
gate is and how re-opening cascades
([../core/04_review_gate_framework.md](../core/04_review_gate_framework.md)); the
*set* of gates comes from the canon pack a studio has adopted. A brand film has no
fact-check gate and a narrative piece has no source lock, and neither is an exemption
— they are different gate sets, declared as data.

The worked example throughout is
[documentary-history](../packs/documentary-history/gates.yaml)'s nine gates, because
it is the largest set and therefore shows every mechanism. Where the other three
packs behave differently, §8 says how.

## 1. Two state machines, not one

Confusing these is how a production ends up recorded as further along than it is.

| | **Lifecycle state** | **Gate state** |
|---|---|---|
| What it describes | Where the production has got to | Whether one specific certification exists |
| Where it lives | `stage:` on the production record | `gates.<key>.status` on the production record |
| Values | `concept` … `published`, plus `shelved` | `not-required`, `pending`, `in-review`, `signed`, `blocked` |
| Who moves it | Advances when the gate that closes the previous stage is `signed` | Only the gate owner |
| Defined in | [../standards/schemas/episode.schema.json](../standards/schemas/episode.schema.json) | [../core/04_review_gate_framework.md](../core/04_review_gate_framework.md) §2 |

The lifecycle state is a **consequence**, never an input. Nobody sets `stage:
picture-locked`; it becomes true because `gates.picture_lock.status` became `signed`.
A production record where the two disagree has been hand-edited, and the gate state is
the one to believe — it is the one carrying a signature.

## 2. The lifecycle

```
LIFECYCLE STATE     STAGE FOLDER      GATE THAT CLOSES THE STAGE      OWNER
─────────────────────────────────────────────────────────────────────────────────
   concept
      │             00_brief          GREENLIGHT                      showrunner
      │                               SENSITIVITY  (1 of 3)           cultural-advisor
      ▼
   greenlit
      │             01_research       SOURCE LOCK                     research-lead
      ▼
   source-locked
      │             02_script         SCRIPT LOCK                     story-producer
      ▼
   script-locked  ◄── generation may not begin before this line ──────────────────
      │
      │             03_storyboard     (no gate — safe zones marked)
      ▼
   storyboard
      │             04_prompts        SENSITIVITY  (2 of 3)           cultural-advisor
      ▼
   generation
      │             05_assets         (no gate — blocked in by script lock,
      │                                        blocked out by picture lock)
      ▼
   edit                                                    ┌───────────────────────┐
      │             06_edit           PICTURE LOCK         │  08_review runs       │
      ▼                               visual-director      │  ALONGSIDE 06 and 07, │
   picture-locked                                          │  not after them:      │
      │             07_audio_post     AUDIO LOCK           │                       │
      ▼                               audio-lead           │   FACT-CHECK          │
   audio-locked                                            │     research-lead     │
      │                                                    │   SENSITIVITY (3/3)   │
      │             09_delivery       RIGHTS                │     cultural-advisor  │
      │                               rights-and-clearances│   RIGHTS (1st pass)   │
      │                               TECHNICAL QC          │     rights-and-clear. │
      ▼                               pipeline-engineer    └───────────────────────┘
   delivery
      │             10_publish        (no gate — publication is the
      ▼                                consequence of technical QC)
   published

   shelved  ◄── reachable from any state, by the showrunner, at any time.
                Signed gates are retained. Nothing is deleted.
```

## 3. Stage by stage

| Stage | Enters when | Leaves when | Closing gate(s) |
|---|---|---|---|
| `00_brief` | A slate slot exists and someone writes a question with stakes | The question, advisory coverage, research lead, budget, and declared conflicts are all present and the premise clears cultural review | greenlight; sensitivity 1 of 3 |
| `01_research` | Greenlight is `signed` | Every claim the outline requires exists at its required tier, independence is checked on every `established` claim, contested claims carry named positions, T4 sources have consent records, and remaining gaps are registered as open questions | source lock |
| `02_script` | Source lock is `signed` | Narration and shooting script are final, every factual statement carries a claim ID, the certainty register matches the evidence, and no prohibited language pattern survives | script lock |
| `03_storyboard` | Script lock is `signed` | Every shot has a frame, a provenance class, and a 9:16 and 1:1 safe zone marked | none |
| `04_prompts` | Storyboard exists | Every generated shot has a versioned prompt card inheriting its style block, and the prompt set has cleared cultural review | sensitivity 2 of 3 |
| `05_assets` | Script lock **and** sensitivity 2 of 3 are `signed` | Every asset has a manifest entry with tool, model, version, prompt card, seed, parameters, and evidence basis where the class requires it | none |
| `06_edit` | Assets exist in the manifest | The cut is final, every generated shot has passed the shot QC list, labels are applied, safe zones hold — and fact-check and sensitivity 3 of 3 are already `signed`, because both block this gate | picture lock |
| `07_audio_post` | Picture lock is `signed` | Loudness and true-peak targets met, all stems rendered including M&E, every proper noun verified against the VO record sheet by a speaker of the language | audio lock |
| `08_review` | Runs from `06_edit` onward — **not a sequential stage**, see §4 | Fact-check, sensitivity 3 of 3, and the first rights pass are all `signed` | fact-check; sensitivity 3 of 3; rights |
| `09_delivery` | Picture lock and audio lock are `signed` | Specs met, captions validate, manifest complete and frozen, model terms re-checked at delivery, cue sheet complete, chain of title assembles, package built | rights (delivery re-check); technical QC |
| `10_publish` | Technical QC is `signed` | The package is published with its evidence layer — sources page, provenance summary, corrections log | none |

Two entries above are load-bearing and easy to skim past:

**`05_assets` has no gate of its own and is the most expensive stage.** It is fenced
on both sides instead: nothing generates before script lock and sensitivity 2, and
nothing leaves without a manifest entry. Generating for an unlocked script is how a
production ends up writing toward the footage it happens to have, which is the single
most common way AI-assisted work loses its spine.

**`10_publish` has no gate because publication is not a decision.** It is the
consequence of technical QC being signed. There is deliberately no separate "approve
for release" step, because such a step is where a production that failed a gate gets
released anyway.

## 4. The numbering is a folder layout, not a sequence

`08_review` is numbered after `06_edit` and `07_audio_post` and runs *concurrently
with them*. Fact-check is declared at stage `08_review` and its `blocks:` list
contains `picture_lock`, which is at `06_edit`. So the fact-check must be complete
before the cut can lock.

Read the `blocks:` graph, not the folder numbers. A schedule built on the numbers is
wrong by a full review cycle, and it will be wrong in the direction that hurts: the
review that was supposed to happen before lock gets planned for after it.

The documentary-history blocking graph, in full:

| Gate | Blocks |
|---|---|
| greenlight | `01_research` |
| source lock | `02_script` |
| script lock | `03_storyboard`, `04_prompts`, `05_assets` |
| sensitivity | `05_assets`, `09_delivery` |
| fact-check | picture lock, `09_delivery` |
| rights | `09_delivery` |
| picture lock | `07_audio_post`, `09_delivery` |
| audio lock | `09_delivery` |
| technical QC | `10_publish` |

## 5. Gate states

```
                    ┌──────────────┐
                    │ not-required │  pack does not include this gate, or it
                    └──────────────┘  does not apply here. Requires a reason.

   ┌──────────┐   submitted   ┌───────────┐   certified   ┌────────┐
   │ pending  │ ────────────► │ in-review │ ────────────► │ signed │
   └──────────┘               └───────────┘               └────────┘
        ▲                           │                          │
        │                           │ failed / held            │ re-opened by
        │                           ▼                          │ the gate owner
        │                     ┌──────────┐                     │
        └──────────────────── │ blocked  │ ◄───────────────────┘
          blockers cleared    └──────────┘   (prior signature retained
                                              in history, never erased)
```

`signed` is the only state that permits downstream work. A signature without a
completed checklist committed in git is not a signed gate, and the validator treats
it as `pending` ([../core/04_review_gate_framework.md](../core/04_review_gate_framework.md)
§7).

`not-required` is a real state with a real cost: it demands a written reason. A gate
marked `not-required` without one is indistinguishable from a gate that was skipped.

## 6. Re-opening, and what it costs

Re-opening is sometimes necessary and is always recorded. The procedure is core's
([§4](../core/04_review_gate_framework.md)):

1. Anyone may request a re-open, with a stated reason.
2. The **gate owner** decides — not the person who wants the change, and not the
   Showrunner.
3. On re-open the gate returns to `pending`, the prior signature is **retained in
   history**, and **every downstream gate signed on the basis of it returns to
   `pending` too**.

That third clause is the whole mechanism. Its purpose is to make late changes
*visible* rather than quiet. A change to a locked script after picture lock is not a
small edit, and the cascade makes it feel like what it is — which is the point at
which someone asks whether the change is worth it, instead of discovering the answer
during delivery.

| Gate re-opened | Gates returning to `pending` | Work that has to be redone |
|---|---|---|
| greenlight | All eight others | Everything. In practice this is not a re-open, it is a new production with a retained ID |
| source lock | script lock, fact-check, sensitivity, picture lock, audio lock, rights, technical QC | Re-script from the affected claims outward; every shot illustrating a changed claim is re-prompted and regenerated; VO re-recorded for the changed passages; mix and captions re-timed |
| script lock | fact-check, sensitivity, picture lock, audio lock, rights, technical QC | Regeneration of every affected shot at whatever the manifest records those shots cost; a new VO session or a punch-in; re-cut; caption re-timing |
| sensitivity | picture lock, technical QC, and generation on the held item | Held items cannot be re-generated until the ruling releases them. If the ruling stands, the sequence is re-conceived or cut — not softened |
| fact-check | picture lock, technical QC | Claim records corrected or retracted; every shot and graphic resting on a changed claim re-checked; on-screen text and the episode description re-checked to the same standard |
| rights | technical QC | Asset replaced or cleared; cue sheet and chain of title reassembled; if an asset is replaced, picture lock is re-opened too, and the cascade continues from there |
| picture lock | audio lock, technical QC | Re-cut; audio conform to the new picture; stems re-rendered; captions re-timed against new picture |
| audio lock | technical QC | Re-mix, re-render all six stems including M&E, re-check loudness and true peak |
| technical QC | none — but `10_publish` is blocked | Re-package and re-validate |

The asymmetry in that table is the useful part: **cost falls off steeply the later the
gate.** A re-opened audio lock costs a re-mix. A re-opened source lock costs the
production. This is why the front gates are the ones worth being slow about, and why
`source_lock` and `script_lock` are the two gates most often signed under pressure and
most expensive to have signed wrongly.

### The cascade is not a punishment

Nothing is deleted on a re-open. Prior signatures stay in history, so the record shows
that a gate was signed, on what date, by whom, and then re-opened for a stated reason.
That history is the evidence that the process was followed *and* that the studio found
its own error — which is a stronger claim than a record that was clean because nobody
looked again.

## 7. Holds are not failed gates

A **hold** is a different mechanism from a `blocked` gate, and the difference matters
under time pressure.

| | Failed gate | Hold |
|---|---|---|
| Scope | The whole gate | One named item: an asset, a shot, a sequence, a record |
| Who raises it | The gate owner | **Any contributor**, without standing or seniority |
| Effect | Downstream stages cannot proceed | Work on that item freezes immediately |
| Released by | The gate owner, when blockers clear | Only the authority the pack designates, **in writing** |
| Retaliation | n/a | The person who raised it is not penalised, ever |

In documentary-history and narrative the releasing authority is the Cultural Advisor,
and it is the one authority the Showrunner cannot unilaterally override. A hold that
required standing to raise would be a suggestion with extra steps.

## 8. The other three packs

Same framework, different shape. What changes is the gate set, never the state
machine.

| Pack | Gates | What is different |
|---|---|---|
| [documentary-history](../packs/documentary-history/gates.yaml) | 9 | The worked example above. Heaviest front end: two gates close before a single frame is generated |
| [product-marketing](../packs/product-marketing/gates.yaml) | 5 | No source lock, no fact-check. Picture and audio lock are one gate. The load is at `08_review`, where claim substantiation and stakeholder approval both sit — the exposure is in product claims, not in history |
| [narrative](../packs/narrative/gates.yaml) | 7 | Adds story bible lock at `01_research` and **continuity lock at `04_prompts`**, which blocks `05_assets`. Retrofitting continuity across a generated sequence costs more than regenerating it, so the anchors are gated before generation rather than checked after |
| [fashion-film](../packs/fashion-film/gates.yaml) | 6 | Adds garment verification and representation review, both at `08_review`; representation review carries hold authority and blocks `05_assets` as well as `09_delivery` |

Every pack includes technical QC at `09_delivery`, blocking `10_publish`. Core
requires it, and no pack may drop it — it is where the platform's own guarantees are
verified rather than assumed.

## 9. Maturity

| Capability | Status |
|---|---|
| Lifecycle and gate state definitions | **DESIGNED** |
| `stage` enum in the episode schema | **DESIGNED** — never validated against a real record |
| Cascade on re-open | **DESIGNED** — no gate has been signed, so none has been re-opened |
| `studio_ops status` (would report every production's gate states) | **NOT BUILT** |
| Automatic cascade on re-open | **NOT BUILT** — today this is a human editing a record, which is the least reliable part of the design |

The first thing that could move any of these past DESIGNED is the dry-run production
in [../ROADMAP.md](../ROADMAP.md) Phase 3. Ledger:
[../docs/status.md](../docs/status.md).
