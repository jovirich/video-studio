---
title: Training
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [showrunner, platform-owner]
---

# Training

**Status: NOT STARTED.** This file is the structure only. No training material exists.

Shared onboarding for everyone is [../onboarding/](../onboarding/) and is written. What
belongs here is **role-specific** material — the part of the job that the shared first
week deliberately does not cover.

## Why this is separate from onboarding

Onboarding teaches the shape of the repository and the four or five rules that will
bite anyone. Training teaches a role how to do its work well, and it is a different
kind of document: longer, exercise-based, and built around **worked examples with
known-wrong answers**. A researcher does not learn independence-checking from a
definition; they learn it from three pairs of sources where one pair is dependent and
looks independent.

That format is why none of this exists yet. It requires real material to work from, and
this repository deliberately contains none. Most of the modules below are genuinely
blocked on episode one, and building them from invented examples would violate the one
rule everything else rests on.

## Planned modules

### Researchers

| Module | Covers | Status | Blocked on |
|---|---|---|---|
| Source records and the critique block | Writing a critique that establishes what a source is reliable *about*; recognising the five questions as work rather than fields | **NOT STARTED** | Real source records |
| Tiers in practice | Placing borderline material; why T4 is not "lower"; never laundering T4 into `established` via a T3 that repeats it | **NOT STARTED** | Worked examples |
| Independence and corroboration | Two sources sharing an upstream origin are one source. Exercise-based; the failure is invisible without practice. | **NOT STARTED** | Worked examples |
| Registers and open questions | Choosing the honest register; `unknown` as a first-class state; writing a `QST-*` that saves the next researcher the search | **NOT STARTED** | — |
| Oral history protocol | Approach, consent, restricted knowledge, transcription order, recording standing and context of transmission | **NOT STARTED** | Cultural Advisor to author |
| Using AI in research | The T5 rule; the two prompting habits; what never goes near a hosted endpoint | **NOT STARTED** | [`methodology/using_ai_in_research.md`](../../packs/documentary-history/methodology/using_ai_in_research.md) is written and is the reading; the exercises are not |

### Prompt writers and visual leads

| Module | Covers | Status | Blocked on |
|---|---|---|---|
| Prompt cards as records | Why a card rather than a string; the required blocks; `evidence_basis` on reconstructions | **NOT STARTED** | — |
| Style inheritance and anchors | Style block, anchor IDs and checksums, when an override is legitimate and why a rising override rate is a failure signal | **NOT STARTED** | An anchor set to demonstrate |
| Period specificity | Countering the models' strong prior toward generic pan-historical imagery; `period_markers` as the lever | **NOT STARTED** | Real generations to compare |
| Provenance classes and labelling | `archival` / `reconstruction` / `interpretive` and what each obliges on screen | **NOT STARTED** | — |
| Reading a vendor sheet critically | The sheets are DESIGNED and unverified; how to check one and stamp it | **NOT STARTED** | Verification pass on the critical-path vendors |

### Reviewers and gate owners

| Module | Covers | Status | Blocked on |
|---|---|---|---|
| What a gate is | Named owner, written checklist, recorded signature, blocking. Why a review missing any of these is feedback, not a gate. | **NOT STARTED** | — |
| Signing honestly | What a signature asserts; refusing to sign; why "it looked fine" signs nothing | **NOT STARTED** | — |
| Re-opening and the cascade | Requesting, deciding, and living with downstream gates returning to `pending` | **NOT STARTED** | — |
| Separation of duties | Why no person signs two gates, and what to do when the staffing does not allow it — the honest answers, not the workaround | **NOT STARTED** | The staffing decision itself: [../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md) item 5 |
| Fact-check in practice | Walking script → claim → source; checking on-screen text, graphics, and maps to the same standard as narration | **NOT STARTED** | A real script |

### Advisors

| Module | Covers | Status | Blocked on |
|---|---|---|---|
| The advisory hold | How to raise one, that it takes effect immediately, that the Showrunner cannot release it, that nobody is penalised for raising one | **NOT STARTED** | — |
| Reviewing prompts before generation | Reviewing a specification rather than an image, and why that timing is the whole point | **NOT STARTED** | Real prompt cards |
| Scope of competence | Ruling within standing; recording what an advisor is *not* competent to rule on; escalation to a community body | **NOT STARTED** | Advisory board to exist |
| Working with communities | Recognised channels; consent scope; providing the finished work; the corrective trap | **NOT STARTED** | Cultural Advisor to author |

### Everyone

| Module | Covers | Status |
|---|---|---|
| The four maturity labels | Using DESIGNED / IMPLEMENTED / TESTED / NOT BUILT in documents, commits, and conversation | **NOT STARTED** |
| `TBD` over plausible | Why a placeholder that reads well is the most dangerous thing you can write | **NOT STARTED** |
| Restricted material | What it is, that it never enters git in any form, local-model-only processing | **NOT STARTED** |

## Format, when these are written

- **Reading, then exercise, then a worked answer.** No module is complete without an
  exercise whose answer is not obvious.
- **Every exercise uses real material** from a shipped production, with the
  contributor's or custodian's permission where relevant. Invented examples teach the
  invented case.
- **Known-wrong answers are included and discussed.** The failure modes are the
  curriculum; the correct answer is usually the least interesting part.
- Each module names its owner and states its own maturity in its front matter, like
  everything else here.

## Sequencing

Do not write these before episode one. They would be built from imagination and would
teach the imagined job. The right moment is the episode-one retrospective, when there
is a real corrections log, a real set of prompt-card `runs` notes, and a real record of
which gates caught what — which is exactly the material a training module needs and
cannot be written without.
</content>
