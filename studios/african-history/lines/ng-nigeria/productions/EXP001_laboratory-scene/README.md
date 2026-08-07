---
title: Experimental Production 001 — laboratory scene
status: draft
maturity: NOT STARTED
version: 0.1.0
updated: "2026-08-07"
owners: [showrunner, research-lead, visual-director]
---

# EXP-001 — laboratory scene

**This is not an episode. It will never be published.**

It exists to run the entire pipeline for real, on a small piece, and find out what
breaks — before anything is at stake. Its deliverable is not a film. Its deliverable
is [`08_review/findings.md`](08_review/findings.md).

| | |
|---|---|
| Kind | `laboratory` |
| Target | ~20 shots, one location, one or two recurring characters |
| Claims | 8–12, researched properly against real sources |
| Published | never |
| Success | a long findings list |

## Why a laboratory production

Everything in this repository is **DESIGNED**. The validators are IMPLEMENTED; almost
nothing is TESTED. A schema that has never seen a real record has proved nothing, and
a continuity mechanism that has never been drift-tested is an assumption.

The alternative to this production is discovering all of it during episode one, when
a slip costs a schedule and a reputation instead of a fortnight.

**A laboratory production that finds nothing has not been run honestly.** If the
findings report is short, the piece was made too carefully — go back and run it at
the pace a real production would.

## What it is testing, in priority order

| # | Question | Fails if |
|---|---|---|
| 1 | Does the claim chain survive contact with real research? | Claims get created after the script, to satisfy the validator |
| 2 | Does continuity hold across ~20 shots? | A character or location drifts and nobody can say what the correct version was |
| 3 | Is the prompt card worth its overhead? | `raw_override` is used on most cards |
| 4 | Can the gates be staffed? | One person signs work they produced |
| 5 | Does the manifest actually get filled? | An asset reaches the edit without a provenance entry |
| 6 | What does a finished second cost, in money and hours? | Nobody can answer afterwards |
| 7 | Which schema fields are dead weight? | Fields are filled `TBD` and never read |

Question 7 matters as much as the rest. This repository is over-built by design and
the experiment is the instrument for cutting it back. **Any field nobody used is a
candidate for deletion**, and that finding is as valuable as a bug.

## Subject

`TBD — Showrunner and Research Lead.`

Constraints on the choice:

- **Historically supportable at 8–12 claims.** Enough real evidence to research
  properly in a bounded time. A subject where the honest answer to everything is "we
  do not know" tests the pipeline but not the research method.
- **One location, one time of day.** The continuity test needs a place seen from
  several angles, not several places.
- **One or two recurring characters.** Two is better — it tests whether the
  mechanism holds *per character* or collapses into one face.
- **No named historical individual.** Depicting a specific documented person adds a
  clearance and depiction question that has nothing to do with what is being tested.
  Use unnamed figures.
- **Nothing sacred, funerary, or restricted.** The advisory board does not exist yet.
  A subject requiring a ruling cannot proceed, and the experiment must not become the
  reason to skip one.
- **Inside the line's advisory coverage** — which is currently empty. See below.

A working title of the shape *"A Morning in [place], c. [year]"* fits these
constraints well: a bounded scene, a single location, ordinary life rather than
documented events, and no named individuals.

> **No claim, name, date, or place has been entered anywhere in this production.**
> The 8–12 claims are human research work against real sources, and nothing in this
> repository — including its tooling — may author them. That rule is the reason the
> repository exists, and breaking it in the first production would be self-refuting.

## Blockers

EXP-001 cannot start until these are true. They are the same conditions episode one
would face, which is part of the test.

| Blocker | Why it blocks | Owner |
|---|---|---|
| Line is `candidate`, not `open` | No production may be greenlit on a closed line | Showrunner |
| No Research Lead named | Nobody can own the claims | Showrunner |
| No advisory contact | Even an ordinary-life scene depicts a people | Showrunner |
| No archive landscape survey | The claims have nowhere to come from | Research Lead |
| No visual identity | Every prompt card inherits from it | Visual Director |
| `new-record` NOT BUILT | IDs would be hand-allocated, and a collision is silent and unrecoverable | Pipeline Engineer |
| No image or video adapter | Nothing can be generated | Pipeline Engineer |

The last two are the smallest and should be built first. See
[ROADMAP](../../../../../../ROADMAP.md) Phase 3.

**A relaxation for this production only:** the gate set may run with fewer distinct
signatories than the pack requires, *provided* the shortfall is recorded in the
findings as a breakage. That is a laboratory finding about staffing, not permission
to sign your own work — and the sensitivity gate is not relaxed, because it is the
one gate whose failure harms people outside the studio.

## Stages

Standard eleven, with two differences: `10_publish` stays empty, and `08_review`
gains the findings report, which is the actual output.

| Stage | Note |
|---|---|
| [`00_brief/`](00_brief/) | Subject, question, the hypotheses this tests |
| [`01_research/`](01_research/) | 8–12 claims, their sources, open questions |
| [`02_script/`](02_script/) | Short. Enough narration to hang 20 shots on. |
| [`03_storyboard/`](03_storyboard/) | ~20 shot records |
| [`04_prompts/`](04_prompts/) | One card per shot |
| [`05_assets/`](05_assets/) | Generated media. Not in git; manifest is. |
| [`06_edit/`](06_edit/) | Assembly and conform |
| [`07_audio_post/`](07_audio_post/) | Includes an M&E stem — testing the workflow is the point |
| [`08_review/`](08_review/) | **`findings.md` — the deliverable** |
| [`09_delivery/`](09_delivery/) | Package assembled and QC'd, then shelved |
| `10_publish/` | Stays empty. Deliberately. |

## Method note

Run it **at production pace**, not carefully. The failures worth finding are the ones
that appear under time pressure, and a laboratory piece made with unlimited care
tests the design rather than the practice.

Record every breakage as it happens, in the moment. Reconstructing them afterwards
loses precisely the small frictions that compound into a schedule.
