---
doc: packs/narrative/09
title: Setting fidelity
status: active
version: 0.1.0
updated: 2026-08-07
owners: [story-producer]
---

# 09 — Setting fidelity

A story set in an invented world asserts nothing about the world. A story set in a
real time and place asserts a great deal, and none of it deliberately.

The audience knows the plot is invented. They do not extend that knowledge to the
buildings, the clothes, the crops, the tools, the languages, the streets, or the way
people addressed each other — and they are right not to, because for most of the
history of the medium those things were researched. A viewer's model of an unfamiliar
period or place is assembled substantially from fiction, and a generative pipeline
will produce a confident, coherent, entirely invented version of it on request.

This document says which parts of the frame carry an evidence obligation, which do
not, and where the boundary sits.

## 1. What is asserted and what is not

| The work says | Status |
|---|---|
| These people existed and did this | **Not asserted.** The plot is fiction and the audience knows it |
| This is what a house of that kind looked like | **Asserted.** Depiction of material reality |
| This is what people of this place wore | **Asserted** |
| This is what they ate, farmed, traded, carried, worshipped with | **Asserted** |
| This is what the city looked like from the hill | **Asserted** |
| This is how they addressed each other, what they called this place | **Asserted** |
| This is what this real named person actually did | **Asserted**, and outside this pack — see §6 |
| This document, photograph, or recording is a real record | **Asserted**, and prohibited — see §5 |
| This character felt this way | Not asserted |

The pattern: **the setting is evidenced; the plot is not.** Everything a documentary
would need a source record for, this pack needs a source record for — *except* the
events of the story, the people in it, and what they said and felt.

That split is not a compromise. It is the accurate description of what a period
fiction actually claims, and it is why this pack borrows a fragment of documentary's
chain rather than adopting the whole of it or none of it.

## 2. Setting evidence threshold

`studio_must_decide: setting_evidence_threshold` — [pack.yaml](pack.yaml). Decided at
studio level, before the first line opens, and recorded in `studio.yaml`.

**Recommended threshold, and the pack's default if the studio does not decide:
the setting is evidenced, the plot is not.** In practice that means the studio picks a
level from this table and applies it uniformly.

| Level | What carries a source record | Suited to |
|---|---|---|
| **L0 — none** | Nothing. The setting is invented, or so distant from any real referent that no viewer will read it as a claim. | Secondary-world fantasy, science fiction, allegory |
| **L1 — anchored** | Named real places and periods carry a source record. Everything else is production design. | Work set in a real place at a generalised or unspecified time |
| **L2 — material** *(recommended default where the setting is real)* | Architecture, dress, food, tools, transport, technology, flora and fauna, writing systems, and language forms carry source records at the tier below. The plot does not. | Historical and period fiction, adaptation set in a real world |
| **L3 — documentary-adjacent** | L2, plus any depicted real event, institution, or public figure carries a claim record at documentary's standard. | Work that dramatises documented events. **Consider whether this work should be on [documentary-history](../documentary-history/) instead** — see §6 |

**Rules on the threshold, whichever level is chosen:**

- **It is declared once and applies to the whole line.** A production that evidences
  its first act and improvises its third has an evidenced first act and a false
  reputation for rigour.
- **It is declared in the interpretive stance** where the work adapts a source
  ([06_adaptation.md](06_adaptation.md) §1), because "we did not research the
  costume" is exactly the sort of thing the stance's fourth question exists to say
  out loud.
- **It may be tightened per production, never loosened.** Same rule as the pack layer
  itself ([../../core/README.md](../../core/README.md) § Precedence).
- **A studio at L0 that starts naming real places has changed level**, whether or not
  anyone said so. The `story_bible_lock` checklist asks.

## 3. Borrowing documentary's evidence chain, and only the part that fits

Where the threshold is L2 or above, the setting uses
[documentary-history](../documentary-history/02_evidence_and_sourcing.md)'s machinery,
narrowed. Adopt these parts:

| Adopt | As-is? | Note |
|---|---|---|
| **Source records and source tiers** (that document's §2) | Yes | T1–T5 unchanged. **T5 includes any output of a language model**, which is the rule that matters most here: a model's confident description of what people wore is a lead, never a source |
| **Interrogating the source** (§4) | Yes | A citation is a location, not a warrant, in fiction as in documentary |
| **The anachronism pass** ([documentary-history](../documentary-history/04_visual_language.md) §6) | Yes | Materials, textiles, crops, weapons, writing, architecture, animals, imported goods, each checked against period. This is where generated imagery fails most often, because models default to a generic pan-historical vocabulary that belongs to no place and no century |
| **Named-entity records for real places** | Yes | Merged into the `story_location` record rather than duplicated |
| **Claim records with confidence registers** | **No** | A fiction does not narrate its confidence. The register machinery is for a narrator who is making assertions in their own voice |
| **The fact-check gate** | **No** | There is no fact to check in the plot, and forcing one produces theatre — [../README.md](../README.md) |
| **Corroboration thresholds for `established`** | Partially | Use them for load-bearing setting elements. Requiring two independent sources for the shape of a cooking pot will stop the production and protect nobody |

**The practical form.** Setting evidence attaches to the story bible, not to the
script:

```
source record (SRC-…)                    ← the evidence
        ▲
        │ cited by
story_location / world_rule record       ← "roofs in this region and period are X"
        ▲
        │ inherited by
location anchor set  →  prompt card  →  shot
```

The chain terminates at the anchor set rather than at a line of narration, which is
the structural difference from documentary and the reason it is cheap to run: you
evidence the *world*, once, and every shot generated against its anchors inherits it.
Documentary evidences each assertion because each assertion is separately spoken.

**Where the evidence runs out**, documentary's rule holds without modification
([documentary-history](../documentary-history/02_evidence_and_sourcing.md) §9): change
the register down, not the claim up; and **never ask a model to fill the gap**. In
fiction there is a third option documentary lacks and it is usually the right one —
**compose around it.** If the roof form is unattested, frame below the roofline. If
the script does not need to specify, do not specify. Fiction can be silent in ways a
narrator cannot, and that is the genre's advantage, not an excuse to invent.

## 4. Real places, real peoples, real institutions

- **A real place is depicted as it was, or the work relocates to an invented one.**
  Inventing a district, a building, or a topography inside a named real city and
  presenting it as part of that city is a setting assertion, and a false one.
- **Depicting a real people is a sensitivity category**, not a design decision. It
  falls under the hold authority at [06_adaptation.md](06_adaptation.md) §5, and
  [documentary-history](../documentary-history/07_cultural_sensitivity.md) §6's
  representation standards apply unchanged: specificity over generality, agency,
  internal complexity, colonial framing interrogated rather than inherited, and the
  corrective trap avoided. Generative models default hard to pastiche and will
  produce it unless the prompt and the review actively prevent it — a fiction framing
  removes none of that.
- **Sacred sites, ritual practice, human remains, and restricted material** are
  governed by [06_adaptation.md](06_adaptation.md) §5 whether the work is fiction or
  not. Fiction is not a lower standard here; in some traditions it is a higher one,
  because a fictional depiction circulates further and is corrected less.
- **Real institutions, organisations, and named living people** shown doing invented
  things are outside this pack. **Escalate** — [README.md](README.md).
- **Language and naming.** Which name form a place or people is given on screen is a
  recorded decision, per
  [documentary-history](../documentary-history/09_localization.md), and a sensitivity
  category.

## 5. The found-footage trap

> **Core prohibits generated material presented as a real record. This holds inside a
> fiction.**
> — [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 item 1

This is the boundary this pack is most likely to cross by accident, because the
crossing is a well-established narrative device and nobody thinks of it as fabrication.

Prohibited, regardless of framing:

- A generated newsreel, broadcast, or news report presented as a real one.
- A generated photograph presented as an authentic historical photograph — of a real
  event, a real person, or a real place.
- A generated document, letter, register, inscription, or manuscript presented as an
  authentic artefact, including in a historical hand or a real script.
- A generated audio recording presented as an authentic recording of a real person or
  event.
- A generated scientific, official, or archival artefact — a chart, a report, a
  record — presented as genuine.
- A found-footage or recovered-record framing in which the fabricated artefact is
  offered to the audience as real *outside* the fiction: released as a leak, seeded as
  a discovery, distributed without the fiction's frame. This is the case where the
  device stops being a device.

`not_suited_to` in [pack.yaml](pack.yaml) states it plainly: *anything framed as found
footage or recovered record, which core prohibits.*

**What remains permitted, and the distinction is precise:**

| Permitted | Why |
|---|---|
| A fictional newsreel about fictional events, in a work the audience reads as fiction, disclosed at production level | It is not presented as a record of anything real. Nothing about it could be mistaken for evidence of a real event |
| A prop document that is legible as a prop and is not offered as an artefact of a real archive | It makes no claim to be found |
| A stylistic homage to an archival form — grain, format, era grammar — where the content is plainly the fiction's own | The form is a language; the claim is what matters |
| A dramatised reconstruction of a real event, presented as a dramatisation | This is acting, not archive. The audience is told what it is |

**The test**, which is core's and is unchanged: *if a viewer learned exactly how this
was made, would they feel informed or deceived?*
([../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §8.)
For a fabricated artefact presented as found, the answer is always "deceived" — that
is the entire mechanism by which the device works.

**Why the fiction framing does not rescue it.** Artefacts leave their films. A
convincing fake photograph of a real historical event will be screenshotted, will
circulate without its frame, and will be indistinguishable from evidence to everyone
who encounters it that way. The fiction protected the audience in the cinema; it
protects nobody afterwards. This is not a hypothetical risk of the format — it is the
format's normal behaviour.

## 6. When the work belongs on a different pack

Setting fidelity has an upper bound, and past it the work is not narrative fiction
with a researched setting; it is documentary with actors.

**Move to [documentary-history](../documentary-history/) when:**

- The work asserts what actually happened, in its own voice or by implication.
- Named real people do specific documented things, and the audience is meant to take
  those things as true.
- The work would be diminished by a viewer learning that a central event was invented.

**Escalate rather than choosing a pack when:**

- The subjects are living, or within living memory with living descendants who are
  identifiable.
- The work touches an active dispute over land, succession, atrocity, or title.
- Real institutions are depicted doing invented things.

Choosing this pack because its gate set is lighter, for work that asserts what
happened, is the failure this section exists to name. A studio declares one pack
([../../core/00_platform_charter.md](../../core/00_platform_charter.md) §3), and the
declaration is meant to describe the work rather than to select its obligations.

## 7. Inheritance and enforcement

Adds to core; loosens nothing. §5 is
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md)
§2 item 1 applied to fiction, not weakened for it. Provenance on every asset (§4 of
that document) and production-level disclosure ([README.md](README.md)) are unchanged.
Where this document borrows from
[documentary-history](../documentary-history/02_evidence_and_sourcing.md), it borrows
that pack's rules as written and does not restate them in a looser form — a rule
quoted at reduced strength is a loosened rule, whatever the intention.

| Standard | Gate | Mechanism |
|---|---|---|
| §2 | Greenlight | Studio cannot greenlight with `setting_evidence_threshold` unresolved; level recorded in `studio.yaml` |
| §2, §3 | `story_bible_lock` | Setting elements at the declared level carry source records on the bible record |
| §3 anachronism pass | `continuity_lock`, `picture_audio_lock` | Named QC step, recorded |
| §4 | `sensitivity` | Real peoples, places, and restricted material; hold authority applies |
| §5 | `sensitivity`, `technical_qc` | No asset classed as a real record carries generative provenance |
| §6 | Greenlight | Pack fit assessed at greenlight, not discovered at delivery |
