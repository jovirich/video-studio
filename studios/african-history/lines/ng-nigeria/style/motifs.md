---
title: Motif register — Nigeria line
status: template
version: 0.1.0
updated: 2026-08-07
owners: [visual-director, story-producer]
---

# Motif register

The record of recurring visual and narrative motifs in this line, so that they are
**deliberate rather than accidental**.

Maturity: **NOT STARTED**. This register is empty. No production exists, so no motif
has recurred.

## 1. What a motif is here, and why it needs a register

A motif is any element that repeats and accumulates meaning by repeating: a recurring
image, a compositional device, a transition, a colour use, a sonic gesture, a
structural move, a phrase in narration, a way of showing uncertainty.

Motifs form whether or not anyone decides to form them. Three shots that rhyme across
an episode teach the viewer that the rhyme means something — and if it means nothing,
the viewer has been taught something false and will apply it to the next occurrence.
On a documentary that is not merely untidy: **a visual rhyme is an argument.** Cutting
from one people to another on a matched composition asserts a connection; opening every
sequence about a particular kind of subject with the same device asserts a category.
Neither assertion has a claim ID, neither passed fact-check, and neither was noticed by
anyone who could have objected.

Two further pressures make the register load-bearing on *this* line specifically:

- **Generation produces accidental motifs at volume.** A prompt phrase that stays in a
  style block, a style anchor reused because it worked, a generator's own compositional
  preference — each recurs across dozens of shots and reads as authorial intent. Some
  of these are worth keeping. They are kept by being written down here and chosen, not
  by surviving unexamined.
- **Pan-regional pastiche is the model's default.** A motif that is really a generator
  habit will flatten distinct peoples, places, and periods into a single look while
  every individual shot passes review
  ([pack 07 §6](../../../../../packs/documentary-history/07_cultural_sensitivity.md)).
  The register is where that is caught, because it is the only artefact that looks
  across shots.

## 2. What is recorded, per motif

All fields required. A motif with an empty `means` field is not a motif; it is a habit.

| Field | Content |
|---|---|
| `id` | Short stable key, referenced from prompt cards and beat sheets |
| `kind` | visual / structural / sonic / verbal |
| `description` | What it is, concretely enough that someone else can execute it |
| `means` | **What it asserts to a viewer.** If this cannot be written, the motif is dropped or made deliberate first. |
| `origin` | Whose decision it was, and when — or, honestly, that it emerged and was adopted afterwards |
| `first_use` | Production and sequence |
| `applies_to` | Where it is used, and where it is explicitly **not** used |
| `evidence_dependency` | Whether it implies anything factual, and the claim IDs if so |
| `sensitivity` | Whether it touches an advisory category, and the ruling reference |
| `status` | proposed / adopted / retired |

Retired motifs stay in the register with the reason. A motif dropped after two seasons
is a decision a later producer will otherwise re-make, and the register is the only
place that memory survives a staffing change.

## 3. Rules

1. **A motif that implies a factual connection needs a claim behind it.** A recurring
   device linking two things asserts the link. Either the link is a claim with sources
   and a confidence register, or the device does not connect those two things.
2. **A motif that touches an advisory category is ruled on before it is adopted**, not
   after it has appeared in three productions
   ([pack 07 §2](../../../../../packs/documentary-history/07_cultural_sensitivity.md)).
   Repetition of a sensitive depiction is not less sensitive for being stylised.
3. **A motif is not a shortcut around the evidence.** Reaching for the established
   device because the sequence is thin is the visual form of proceeding on thinner
   evidence at the same confidence level.
4. **Register a motif before its third use.** By the third use it is established with
   the audience regardless of whether it is established with the production.
5. **Audit at the close of each production.** Ask what repeated, whether it was
   intended, and what it now means. What emerged unintentionally is either adopted
   deliberately or removed — leaving it unexamined is choosing it without saying so.
6. **Motifs are line-scoped.** A second line does not inherit this register. Reusing
   this line's visual grammar elsewhere would assert a continental sameness that no
   evidence supports and that [README.md](README.md) §1 exists to prevent.

## 4. Relationship to the rest of the style system

| | |
|---|---|
| [visual_identity.md](visual_identity.md) | The look: what everything is made of. Constant. |
| This register | What repeats *within* that look, and what the repetition means. Accumulates. |
| Style anchors | The concrete reference files a prompt card inherits |
| [pack 03 §10](../../../../../packs/documentary-history/03_narrative_doctrine.md) | Series-level continuity, which is what a motif register serves |

## 5. Series-level continuity in narration

Structural and verbal motifs sit with the Story Producer and are registered here too —
how uncertainty is voiced, how a contested position is introduced, how a production
returns to its hook, how the studio says "we do not know".

That last one is worth registering early rather than late. It will recur in every
production, it will become the studio's most recognisable verbal gesture, and a
formula that sounds apologetic will teach the audience to hear honest uncertainty as a
failure of the work rather than a property of the record
([pack 03 §5](../../../../../packs/documentary-history/03_narrative_doctrine.md)).

---

# Register

<!-- Empty. No production exists. Entries are added before a motif's third use. -->
