---
doc: packs/narrative/05
title: Story bible framework
status: active
version: 0.1.0
updated: 2026-08-07
owners: [story-producer]
---

# 05 — Story bible framework

This is the load-bearing document of the pack, and it is load-bearing for a reason
that has nothing to do with ethics.

Generative tools have no memory. A model asked for the same character on Tuesday and
on Friday will produce two people, and neither of them will be the one in the shot
you already cut. Across three hundred shots, a world's rules, a character's face, a
city's geography, and a season's chronology will each drift — not because anyone
decided anything, but because nothing was holding them. Documentary handles this with
entity records as a side effect of its evidence chain. Here there is no evidence chain
to inherit from, so coherence has to be built deliberately or it does not exist.

The story bible is the external memory. **It is the authority, and the script defers
to it** — not the other way round, and not "whichever the writer remembered."

## 1. What the bible holds, and what it does not

| In the bible | Not in the bible |
|---|---|
| What is true in this world | What happens in this story |
| Who a character is, permanently | What a character does in episode four |
| The rules governing the world's mechanics, society, and limits | Individual scenes |
| Chronology of events prior to and across the work | Beat sheets |
| Geography and the spatial relationships between places | Shot lists |
| Naming, language, and orthography for invented and adapted terms | Dialogue |
| Every deliberate departure from a source text, with its reason | Undocumented departures — there is no such thing |

The line is: **the bible holds what must be the same in every scene.** If it changes
scene to scene, it is script. If it must not, it is bible, and putting it in the
script instead is how it drifts.

## 2. World rules

A `world_rule` is a statement about what is possible, permitted, or consequential in
this world. Fiction fails audiences less often through implausibility than through
*inconsistency* — a world that establishes a cost and then quietly waives it has
broken its contract, and viewers feel it before they can name it.

Every world rule states its **limit and its cost**. A rule without a limit is not a
rule; it is a capability, and a capability without a cost dissolves every subsequent
stake.

| Category | Examples of what to fix |
|---|---|
| **Physical** | What the world's mechanics permit; what they cost; what they cannot do |
| **Social and political** | Who holds authority and on what basis; how it is transferred; what is taboo |
| **Material** | Technology level, available materials, what is scarce, what is common |
| **Economic** | What is traded, what is valuable, what work people do |
| **Temporal** | How time is reckoned, seasons, calendars, the duration of travel between places |
| **Belief** | What the world's people believe is true, which is separate from what *is* true in the world |
| **Language** | What is spoken where, by whom, and how it is rendered on screen |
| **Constraint** | What the story has decided *not* to have. The most useful and least written category. |

The last row is worth its own sentence. A bible that only records what exists gives a
generative tool nothing to exclude, and models fill unspecified space with genre
defaults. "There are no horses in this world" prevents more drift than three
paragraphs describing the ones there are.

### The `world_rule` record

```yaml
id: WRL-<SCOPE>-0007
type: world_rule
status: draft | review | locked | superseded | retracted
category: physical | social | material | economic | temporal | belief | language | constraint
statement: >
  One sentence, testable against a frame or a line of dialogue.
limit: What this rule does not extend to.
cost: What it costs the person who uses or breaks it. Required for any capability.
established_in: [<scene, sequence, or episode where the audience learns it>]
source_basis: <source text reference, or `original`>       # see 06_adaptation.md
variant_resolution: <resolution id>                        # where sources disagree — §6
contradicts: [<rule ids this replaces or tensions with>]
visible_consequences: [<what must appear on screen if this rule holds>]
supersedes: <rule id>
```

`visible_consequences` is the field that turns a bible from documentation into a
production instrument. If the rule is "iron is scarce", the consequence is that iron
appears in three named places and nowhere else — and that is a line the continuity
pass can actually check, and a constraint a prompt card can inherit.

## 3. Character canon

Every recurring character has a `story_character` record. "Recurring" means appears in
more than one shot, which is a lower bar than writers expect and is deliberate: the
second appearance is where drift begins.

```yaml
id: SCH-<SCOPE>-0012
type: story_character
status: draft | review | locked | superseded | retracted
name: { canonical: <name as used on screen>, variants: [<other forms>], pronunciation: <guide> }
source_basis: <source text reference, or `original`>
canon:
  identity: Who they are in one sentence, independent of plot.
  age_range: <at the work's present>
  wants: What they pursue.
  fears: What they avoid.
  contradiction: The tension inside them. A character without one is a function.
appearance:
  description: >
    Written to be inherited by a prompt. Specific, finite, and free of adjectives a
    model cannot act on. Height, build, hair, skin, distinguishing features.
  invariants: [<the two or three features that must never drift>]
  costume_states: [{ state: <name>, applies_to: <scenes>, description: <...> }]
  ageing: <how appearance changes across the work's timeline, and at which points>
anchors:
  character_anchor_set: <anchor set id>        # 07_visual_continuity.md §3
  performance_source: <cast performer | licensed synthetic voice | both>   # 08 §1
  likeness_rights: <contract or clearance reference, required if a real person's likeness>
relationships: [{ to: <character id>, nature: <...>, known_to_audience_from: <point> }]
knowledge: [{ fact: <...>, knows_from: <point>, does_not_know_until: <point> }]
arc_summary: Where they begin and where they end. Not the plot.
variant_resolution: <resolution id>
```

Three fields do the real work:

- **`invariants`.** A model cannot hold twelve features stable. It can hold two or
  three. Naming which ones matter — the scar, the asymmetric hairline, the particular
  grey — converts an unwinnable fight into a checkable one. Everything else is allowed
  to breathe.
- **`knowledge`.** Who knows what, when. The most common continuity error in generated
  and in traditionally produced fiction alike is a character acting on information
  they have not been given. It is invisible in a scene and obvious in a cut.
- **`likeness_rights`.** Present or the character does not exist. See
  [08_performance_and_voice.md](08_performance_and_voice.md) §1 — core prohibits
  synthesising a real person's likeness or voice without documented consent, including
  historical figures for whom no consent is possible
  ([../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 item 2).

Locations follow the same pattern as `story_location`, declared in
[pack.yaml](pack.yaml). Their invariants are architectural and spatial rather than
facial, and their anchor sets are governed by
[07_visual_continuity.md](07_visual_continuity.md) §4.

## 4. Timeline

A single chronology, held in one place, covering the work's present and everything
before it that the story depends on.

- **Every dated event has one entry.** Not one per script that mentions it.
- **Record durations, not only dates.** How long a journey takes is the constraint
  scripts violate most often, and it is a `world_rule` (temporal) as much as a
  timeline entry.
- **Record ages at events.** Character ages derived at read-time from birth dates and
  event dates catch a large class of error automatically, and they drive the `ageing`
  field on the character record, which drives the anchor set.
- **Record what the audience knows and when**, separately from what is true. Narrative
  chronology and story chronology are different objects; conflating them is how a
  flashback contradicts a scene the audience has not reached yet.
- **Where the work is set in a real period**, timeline entries touching real events
  cross into [09_setting_fidelity.md](09_setting_fidelity.md) and carry its evidence
  requirement. The plot does not. The distinction is that document's whole subject.

## 5. Geography

- **One map, and it is authoritative.** Distances, directions, adjacency, and travel
  times are read from it, not invented per scene.
- **Spatial relationships inside a location are fixed** before generation: which way
  the door faces, where the light comes from, what is visible from the window. This is
  the level at which generated interiors fail — the room is beautiful in every shot
  and a different room in each.
- **Named places get records.** Unnamed places do not, until the second time they
  appear.
- **Screen direction follows geography.** If the city is north, characters travelling
  to it move consistently across the cut. Generative tools have no opinion about this
  and will happily reverse it.

## 6. Resolving contradictions between source variants

Where the work adapts material that exists in more than one version — variant
manuscripts, regional tellings, translations that diverge, a tradition with several
lines of transmission — the versions will contradict each other. That is normal and it
is not a problem to be hidden.

**The rule:**

> **Every contradiction between source variants is resolved deliberately, by a named
> person, with the reason recorded and the rejected variants named. It is never
> resolved by whichever version a writer happened to remember.**

The failure this prevents is specific and common: a production adopts variant A in
episode one because that is the version the writer read, variant B in episode four
because a different writer read a different edition, and then discovers at picture
lock that the two are incompatible in a way the audience will notice — and that the
audience holding the source will read as a claim about the source, per
[06_adaptation.md](06_adaptation.md) §1.

### The resolution record

```yaml
id: RES-<SCOPE>-0003
type: variant_resolution
status: draft | review | locked
question: What the variants disagree about, in one sentence.
variants:
  - { source: <text, tradition, edition, or recension>, position: <what it holds>, held_by: <who transmits it> }
adopted: <which variant, or `synthesis`, or `neither — the work is silent`>
rationale: >
  Why. Narrative, interpretive, or practical — but stated. "It plays better" is a
  legitimate reason and is recorded as one.
declared_publicly: true | false     # does the audience learn this? see 06_adaptation.md §1
advisory_ruling: <ADV reference>    # required where a living tradition holds the text
affects: [<world rule, character, timeline, and location ids>]
```

Three rules on resolutions:

1. **"Neither" is a legitimate resolution.** Where variants disagree and the work does
   not need to decide, the work is silent — and being silent *on purpose* is recorded,
   so that a later writer does not resolve it by accident.
2. **Synthesis is declared.** Combining variants produces a version that exists in no
   tradition. That is permitted; presenting it as *the* tradition is not
   ([06_adaptation.md](06_adaptation.md) §2).
3. **Where a living community holds the text, the resolution is not solely the
   studio's.** It goes to the sensitivity gate, which carries hold authority
   ([gates.yaml](gates.yaml)), before it is locked.

## 7. Continuity notes

A `continuity_note` records something the bible did not anticipate and the production
decided in flight — a prop that acquired significance, a line that established
something, a location detail that a shot made canonical.

- **Raised by anyone**, at any stage. The person who notices is usually not the person
  who owns the record.
- **Triaged by the Story Producer** into: promote to a bible record, correct the
  material, or record as accepted variance.
- **A note is not a fix.** An open note at picture lock blocks the gate. The point of
  the note is that the decision is made by someone, not that it is written down.

## 8. What story bible lock certifies

The `story_bible_lock` gate ([gates.yaml](gates.yaml)) is owned by the Story Producer,
sits at `01_research`, and blocks `02_script`. It certifies, specifically:

1. **Every recurring character and location has a record**, and the records are
   internally consistent with each other.
2. **World rules are stated with limits and costs**, and no two rules contradict
   without a recorded resolution.
3. **The timeline is single, complete for what the work depends on, and free of
   derived-age contradictions.**
4. **Geography is fixed** and travel times are consistent with the temporal rules.
5. **Every contradiction between source variants is resolved under §6**, with a named
   resolver and a recorded rationale — not left to the first writer who reaches it.
6. **Every departure from a source text is intentional and recorded**
   ([06_adaptation.md](06_adaptation.md) §2).
7. **Every character requiring likeness rights has them**, or does not exist.
8. **No record is `draft`.** `locked` records permit no `TBD`
   ([../../standards/id_system.md](../../standards/id_system.md)).

What it does **not** certify: that the story is good, that the script is finished, or
that the visual anchors exist. That last one is `continuity_lock`, a separate gate at
`04_prompts` owned by a different role
([07_visual_continuity.md](07_visual_continuity.md) §7) — the split is deliberate,
because bible lock is about *what is true* and continuity lock is about *whether the
tools can hold it*.

**Re-opening.** Bible lock is re-opened often and legitimately; production discovers
things. Core's cascade applies
([../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §4):
re-opening returns script lock and continuity lock to `pending` too. That cascade is
what makes a late world-rule change feel like what it is — expensive — rather than
quiet.

## 9. Inheritance and enforcement

Adds to core; loosens nothing. Inherits without modification the prohibitions at
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 —
in particular item 2, which is why `likeness_rights` is a required field rather than a
recommended one, and item 1, which is why a story bible may not contain a fabricated
document, newsreel, or photograph presented within the fiction as a real record
([09_setting_fidelity.md](09_setting_fidelity.md) §5).

Record types are declared in [pack.yaml](pack.yaml); ID grammar follows
[../../standards/id_system.md](../../standards/id_system.md), with this pack
allocating `WRL`, `SCH`, and `RES` at line scope. Schemas:
[../../standards/schemas/](../../standards/schemas/). Record templates:
[../../templates/records/](../../templates/records/).

| Standard | Gate | Mechanism |
|---|---|---|
| §2, §3, §5 | `story_bible_lock` | Every recurring entity has a locked record |
| §4 | `story_bible_lock` | Derived ages and travel times checked against temporal rules |
| §6 | `story_bible_lock`, `sensitivity` | Every variant contradiction has a resolution record |
| §3 `likeness_rights` | `technical_qc` | Clearance reference present on any real-person likeness |
| §7 | `picture_audio_lock` | No open continuity note survives the gate |
