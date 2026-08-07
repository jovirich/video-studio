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
**It is the platform's acceptance test.**

It exists to run the production mechanics for real, on a small piece, and find out what
breaks — before anything is at stake. Its deliverable is not a film. Its deliverable
is [`08_review/findings.md`](08_review/findings.md).

| | |
|---|---|
| Kind | `laboratory` |
| Role | **Acceptance test for the platform** |
| Target | ~20 shots, one location, one or two recurring characters |
| Historical claims | **none — see below** |
| Published | never |
| Success | a long findings list |

## It makes no historical claims

EXP-001 depicts **explicitly fictional** subjects. No period, no people, no place is
claimed. Its location and characters are invented, and are labelled as such on their
records.

This is a deliberate change from an earlier design in which EXP-001 would have carried
8–12 researched claims. Two consequences follow, and both matter:

**It unblocks the experiment.** With no historical claims there is nothing to be wrong
about, so EXP-001 may exercise production mechanics **before the Nigeria line is
formally opened** — no Research Lead, no archive survey, no advisory coverage on a
historical subject. That relaxation is recorded in
[the studio amendment log](../../../../bible/amendment_log.md) and applies to laboratory
productions making no historical claims. It does not extend to anything else.

**It narrows what the test proves.** EXP-001 now tests the *mechanics*: continuity,
prompt rendering, generation, provenance, conform, and whether the gates can be
staffed. It does **not** test the claim chain — whether research survives contact with
a production schedule. That hypothesis is untested and remains untested after EXP-001
passes.

> **The claim chain is the load-bearing assumption of the whole architecture, and
> EXP-001 no longer exercises it.** A separate, later experiment must, before episode
> one. Do not read a green EXP-001 as evidence that
> [ADR 0002](../../../../../../docs/decisions/0002-claims-as-records.md) works.

## Why fictional subjects still test what matters

Continuity, drift, prompt rendering, manifest completeness, and cost per finished
second are all indifferent to whether the subject is real. A model drifts a fictional
face exactly as readily as a historical one.

What is lost is only the research half — and buying that back would have cost weeks
before the first generated shot, which is the wrong trade at this point.

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
| 1 | **Does the round trip close?** Continuity + shot record → card → render → adapter → asset → manifest entry whose hash matches the file. | Any link needs a manual step, or the hash does not match |
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

An **invented** interior or exterior with one or two **invented** figures. Not a
depiction of any real time, place, or people.

Constraints on the choice:

- **Explicitly fictional.** No period, no culture, no place is claimed. The location
  and character records carry no `entity` link, because there is no historical entity
  to answer to.
- **One location, one time of day.** The continuity test needs a place seen from
  several angles, not several places.
- **One or two recurring characters.** Two is better — it tests whether the mechanism
  holds *per character* or collapses them into one face.
- **Visually demanding, not visually easy.** Pick a subject with hands doing
  something, a material with texture, and a light source with a direction. A subject
  chosen because it generates cleanly proves nothing.
- **Nothing that reads as a real culture.** Avoid regalia, ceremony, script, and
  dress that a viewer would place. The advisory board does not exist yet and this
  experiment must not become the reason to skip a ruling.

> **No claim, name, date, or real place may be entered anywhere in this production.**
> Nothing in this repository — including its tooling — may author historical content.
> That rule is why the repository exists.

## Blockers

Most of the original blocker list fell away when EXP-001 stopped making historical
claims. What remains is tooling.

| Blocker | Status | Owner |
|---|---|---|
| `new-record` — ID allocator | in progress | Pipeline Engineer |
| Prompt renderer | in progress | Pipeline Engineer |
| One generation adapter | in progress | Pipeline Engineer |
| Manifest + asset store | in progress | Pipeline Engineer |
| Visual identity for the line | **not required** — EXP-001 defines a throwaway style block, since it depicts nothing real | Visual Director |

**No longer blocking**, by the relaxation above: line status, Research Lead, advisory
contact, archive survey. Each is still required before *episode one*, and before any
production that makes a historical claim.

**A relaxation for laboratory productions:** the gate set may run with fewer distinct
signatories than the pack requires, *provided* the shortfall is recorded in the
findings as a breakage. That is a finding about staffing, not permission to sign your
own work.

**The sensitivity gate is not relaxed.** Generated imagery of people is still imagery
of people, and it is the one gate whose failure harms someone outside the studio.

## Stages

Standard eleven, with two differences: `10_publish` stays empty, and `08_review`
gains the findings report, which is the actual output.

| Stage | Note |
|---|---|
| [`00_brief/`](00_brief/) | Subject, question, the hypotheses this tests |
| [`01_research/`](01_research/) | **Empty by design.** No claims — see § It makes no historical claims. |
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
