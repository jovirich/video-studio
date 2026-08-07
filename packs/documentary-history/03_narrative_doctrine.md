---
doc: bible/03
title: Narrative doctrine
status: active
version: 0.1.0
owners: [showrunner, story-producer]
---

# 03 — Narrative doctrine

How the studio tells a history. Structure, voice, and the handling of uncertainty
as a storytelling asset rather than an obstacle.

## 1. The governing idea

History is not a list of events; it is a set of questions about why things went one
way and not another. An episode is built around **a question with stakes**, not
around a period or a person. "The Kingdom of X" is a topic. "Why did X's authority
survive three successions and then collapse in one?" is an episode.

If the brief cannot state the question in one sentence, the episode is not ready.

## 2. Episode architecture

The default five-movement structure. Deviations are permitted and are argued for in
the brief.

| Movement | Function | Typical share |
|---|---|---|
| **I. The hook** | A concrete scene, object, or discrepancy that makes the question urgent. Never a summary of what the episode will cover. | 5–8% |
| **II. The ground** | What the viewer needs to hold: geography, actors, stakes, the state of things before the change. | 20–25% |
| **III. The turn** | The pressure and the events. The bulk of the narrative. | 35–40% |
| **IV. The reckoning** | Consequence. What it cost, who paid, what it set in motion. | 20–25% |
| **V. The residue** | What survives — in the ground, in the archive, in practice, in dispute. Returns to the hook. | 8–12% |

Two structural rules:
- **The hook is answered.** A question raised in movement I is addressed by
  movement V, even if the answer is "we do not know, and here is why that matters."
- **No movement is a list.** If a section can be reordered without loss, it is a
  list, and lists do not hold attention.

## 3. Cold open

Length target 45–90 seconds. Contains: a concrete image, a stated question, and one
piece of evidence. Contains no: series branding, presenter introduction, or
"in this episode we will explore."

## 4. Voice

- **Person.** Third person for the historical narrative. First person plural
  ("we do not know", "the record we have") only when speaking about the process of
  knowing — never to claim collective identity with historical subjects.
- **Tense.** Simple past for events. Present for surviving material and for
  scholarship ("the wall stands", "historians divide").
- **Sentence length.** Vary hard. Narration read aloud at 145–165 wpm; a paragraph
  of uniform 20-word sentences is unlistenable regardless of content.
- **Adjectives.** Earn them. "Vast", "mighty", "legendary", and "mysterious" are on
  the prohibited list in [../standards/prohibited_language.md](../standards/prohibited_language.md)
  not because they are wrong but because they are load-bearing when they should be
  decorative — they smuggle in claims the evidence has not made.
- **Superlatives require a claim ID.** "The largest", "the first", "the only" are
  factual assertions and are validated as such.

## 5. Uncertainty as content

The register table in [01_editorial_standards.md](01_editorial_standards.md) §2 is a
writing tool, not a compliance form. Used well, uncertainty is the most engaging
material available:

- **Name the disagreement.** "Two readings of this survive, and which you accept
  changes what the next fifty years mean."
- **Show the gap.** "The record stops here. It resumes eleven years later, and by
  then everything has changed. What happened in between is the question."
- **Interrogate the source on screen.** "This account was written by the man who
  won. That does not make it false. It makes it a particular kind of true."

This is also the honest solution to thin evidence: a sequence about *how we know*
can be gripping where a sequence pretending to know is merely fluent.

## 6. Reconstruction

Reconstructed scenes carry the story where no archival image exists — which, for
most of the periods this studio covers, is nearly everywhere.

**Permitted:** environments, material culture, crowds and daily life, geography,
processes, architecture, journeys, battles at a level of generality the evidence
supports.

**Constrained:**
- A named historical figure may be depicted only where the record supports the
  depiction's specifics, and the depiction is flagged `reconstruction` on the shot
  record with the evidence basis recorded.
- A named figure may not be shown *speaking* invented words. Documented words may be
  voiced, attributed on screen to the document.
- A reconstruction may not depict a specific documented event in a way that asserts
  contested details as settled. Where a detail is contested, shoot around it.

**Prohibited:** anything designed to be mistaken for archival material. See
[06_ai_disclosure_and_ethics.md](06_ai_disclosure_and_ethics.md) §3.

## 7. Handling violence and atrocity

- Depict consequence, not spectacle. The test: does the shot help the viewer
  understand what happened, or does it substitute affect for understanding?
- Never generate imagery of identifiable real victims.
- Warnings precede sequences involving atrocity, human remains, or graphic injury.
- Where a community's descendants are living, the sequence goes through the
  sensitivity gate before generation begins, not after.
- The default is restraint. A held wide shot and a plain sentence will usually carry
  more than a rendered close-up, and costs nothing in credibility.

## 8. Pacing

- **Breath.** After a heavy beat, hold. Silence and a static frame for 3–6 seconds
  is a legitimate and underused tool.
- **Information density.** No more than one new named entity per 20 seconds of
  narration in the ground movement. Viewers lose names faster than writers expect.
- **Recap.** A one-line orientation at each movement boundary. Not a summary — a
  compass bearing.

## 9. Script artefacts and their order

| Artefact | Location | Locked at |
|---|---|---|
| Brief | `00_brief/brief.md` | Greenlight |
| Question and thesis | `00_brief/thesis.md` | Greenlight |
| Research pack | `01_research/` | Source lock |
| Outline | `02_script/outline.md` | Outline approval |
| Beat sheet | `02_script/beat_sheet.md` | Outline approval |
| Narration draft | `02_script/narration.md` | Script lock |
| Shooting script | `02_script/shooting_script.md` | Script lock |
| VO record sheet | `02_script/vo_record_sheet.md` | Before VO session |

**Generation does not begin before script lock.** Generating imagery for an unlocked
script is how a studio ends up writing toward the footage it happens to have — the
single most common way AI-assisted documentary loses its spine.

## 10. Series-level continuity

- Names, dates, and characterisations are consistent across episodes because they
  are pulled from the same records, not because someone remembered.
- Where a later episode revises an earlier claim, the earlier episode gets a
  correction entry. Continuity is maintained forward *and* backward.
- Recurring motifs (a returning object, a recurring question) are registered in the
  line's `style/motifs.md` so they are deliberate rather than accidental.
