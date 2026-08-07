---
doc: packs/narrative/07
title: Visual continuity
status: active
version: 0.1.0
updated: 2026-08-07
owners: [visual-director]
---

# 07 — Visual continuity

[05_story_bible.md](05_story_bible.md) fixes what is true. This fixes whether the
tools can hold it across three hundred shots. They are different problems and they
fail in different places, which is why they are different gates.

## 1. The problem, stated precisely

A generative system produces each shot independently. It has no representation of
"this character" persisting between calls — only whatever conditioning you supply at
the moment of the call. Two consequences follow, and both are structural rather than
incidental:

1. **Drift is the default and coherence is the intervention.** Nothing in the tool is
   trying to keep the face the same. If nothing external holds it, it does not hold.
2. **Drift is not uniform.** Identity, costume, palette, lighting, spatial geometry,
   and motion each drift at different rates under different conditions. A pipeline
   that holds faces beautifully and lets the room reverse itself has solved a third
   of the problem and will still read as incoherent.

Documentary manages this with style anchors and prompt inheritance
([documentary-history](../documentary-history/04_visual_language.md) §1) because its
shots are mostly of places and material culture. Narrative has recurring *people*, in
scenes, across a cut, and needs more.

## 2. Continuity toolchain

`studio_must_decide: continuity_toolchain` — [pack.yaml](pack.yaml). Decided at studio
level, before the first line opens, because it constrains everything downstream:
casting, budget, schedule, the rights the studio must hold, and what the anchor sets
at §3 even are.

The studio picks one **primary** mechanism per recurring character class, and records
it on each `story_character` under `anchors.performance_source`
([05_story_bible.md](05_story_bible.md) §3). Mixing mechanisms within one character
across a work is permitted and is a decision, recorded, not a drift.

| Mechanism | What it is | Known drift limits | Rights position |
|---|---|---|---|
| **Character reference** | One or more fixed reference images supplied as conditioning on every generation of that character. | Holds coarse identity — build, colouring, silhouette, broad facial structure. **Degrades with distance from the reference's pose, expression, angle, lighting, and framing.** Profile and extreme angles drift first; expression under emotion drifts next; fine features (eye shape, mouth corners, ear and hairline detail) are the least stable. Close-ups are the hardest case and are where the audience is looking. | Simplest. The reference itself needs provenance and clearance like any asset. If the reference depicts a real person, everything in the row below applies. |
| **Trained adapter** | A small model component trained on a set of images of one subject, applied at generation. | Holds identity substantially better than a reference across angle, expression, and lighting. **Drifts with distance from its training distribution** — a subject trained only in one costume, one lighting setup, or one age will resist being placed outside it, and will pull the whole frame toward its training set (costume, background, and grade bleed). Ageing and costume changes usually need separate adapters or a mixed training set planned in advance. | Heaviest. Training data must be cleared for training, not merely licensed for display — these are different permissions. If the subject is a real person, training on their likeness requires their documented consent covering training specifically ([../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §7). Vendor terms on training and output ownership are recorded per [../../rights/permissions/](../../rights/permissions/) and re-checked before delivery. |
| **Cast performer with likeness rights** | A real performer is filmed or photographed, and generative work is applied over, around, or from that footage within the scope of their contract. | Identity does not drift, because it was never synthesised. **Drift moves to the boundary** — the seam between captured performance and generated environment, grade mismatch, edge artefacts, and temporal instability in the generated portion. Costume and prop continuity become physical production problems, which are solved problems. | Most constrained and most durable. The contract states exactly what may be generated from, over, and around the performance; what may be trained on; the term; and the territories. **A contract that does not mention AI processing does not permit it.** |

**Rules that hold whatever is chosen:**

- **Named and recorded before generation.** The mechanism, its version, and its
  identifiers are on the character record and on every prompt card that invokes it.
  [pack.yaml](pack.yaml) requires anchors on any prompt card touching a recurring
  character or location.
- **The drift limits above are qualitative, and the studio measures its own.** Actual
  limits depend on the tools, versions, and settings in use and change with every
  vendor update. **TBD — the studio runs a drift test per mechanism before its first
  production** (§6) and records the result in its `style/` folder. Adopting another
  studio's numbers is worse than having none, because it produces false confidence.
- **A real person's likeness never enters any of these mechanisms without documented
  consent** — including a historical figure, for whom no consent is possible. This is
  [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md)
  §2 item 2 and it is the constraint this pack's authors most often underestimate. See
  [08_performance_and_voice.md](08_performance_and_voice.md) §1.
- **Changing mechanism mid-production is a re-open, not an optimisation.** It
  invalidates every anchor derived from the old one and returns `continuity_lock` to
  `pending`.
- **The choice is a budget and schedule decision as much as a craft one.** Adapters
  cost training time and data preparation up front and save it per shot; references
  cost nothing up front and cost re-generation forever; cast performers cost
  production days and remove an entire class of risk. Deciding this at the first shot
  instead of at studio level is how a production discovers in week six that it cannot
  afford the only option that works.

## 3. Character anchors

An **anchor set** is a fixed, versioned, checksummed collection of reference material
for one character, stored in [../../library/style_refs/](../../library/style_refs/)
and referenced by ID from every prompt card that generates them. Not a mood board —
specific files, immutable once locked.

A complete character anchor set contains, at minimum:

| Element | Why |
|---|---|
| **Neutral front, three-quarter, and profile** at the character's canonical age and costume | The angles a face is most often required at, and the ones that drift apart first |
| **One expression range set** — at least neutral, and the two emotional states the script requires most | Expression is where identity slips while every individual frame still looks correct |
| **One set per costume state** declared on the character record | Costume drift is the most-noticed and least-tracked failure. A character who changes cloak between two shots in a scene reads as an error to everyone |
| **One set per ageing point** on the timeline | Derived from `ageing` on the character record ([05_story_bible.md](05_story_bible.md) §3) |
| **A written invariant list** — the two or three features that must never move | The checkable artefact. "Looks like the reference" is not reviewable; "the scar crosses the left brow" is |
| **Scale references** — the character beside a known object or another character | Generative tools have no stable sense of height, and inconsistent scale is invisible per-shot and glaring in a two-shot |

**Versioning.** Anchor sets are numerically versioned per
[../../standards/naming_conventions.md](../../standards/naming_conventions.md). A new
version does not silently supersede: it lists which shots were generated against the
old one, so the decision to re-generate or accept is made rather than discovered.

## 4. Location anchors

The same structure, with different invariants. Locations fail differently from
characters: nobody notices that the room is a slightly different room, and everybody
notices when the door is on the wrong side.

A complete location anchor set contains:

- **A plan or spatial diagram** — what is where, what faces what, where the entrances
  and light sources are. Derived from the geography in
  [05_story_bible.md](05_story_bible.md) §5, and authoritative over any individual
  generated frame.
- **Establishing views from the compass points the script uses**, so that reverse
  angles are constrained rather than invented.
- **Light behaviour per time of day** used in the work — direction, quality, colour.
  Light having a consistent source and direction is a platform-wide QC failure mode
  ([documentary-history](../documentary-history/04_visual_language.md) §3), and in a
  scene cut from independent generations it is the single most common break.
- **Material and texture references** — the surfaces, so that stone does not become
  brick between shots.
- **Persistent-object list** — what is always in this space, and where. A prop that
  appears in the wide and vanishes in the reverse is a continuity note.
- **State variants** where the location changes across the work: damaged, seasonal,
  occupied, abandoned. Each is a separate set, and the timeline says which applies
  when.

## 5. The style block

Above characters and locations sits the work's visual identity: palette, grade, lens
set, depth-of-field discipline, motion behaviour, texture, atmosphere. It inherits
through prompt cards exactly as documentary's does
([../../prompts/README.md](../../prompts/README.md) § Inheritance):

```
line style block  →  sequence style block  →  prompt card
```

A prompt card that overrides an inherited style block records why. This is not
bureaucracy: an unexplained override is indistinguishable from a mistake six weeks
later, and it is usually a mistake.

Two narrative-specific requirements on top of documentary's:

- **Motion is motivated and largely still.** A drifting camera on every shot is the
  signature tell of generated video, and in fiction it also destroys the grammar of
  coverage — the audience cannot read a scene where every angle floats.
- **The lens set is fixed and small.** A defined set is the cheapest coherence
  available, and in narrative it additionally makes eyelines and coverage sizes
  consistent enough to cut.

## 6. Drift detection

Drift is found by looking for it on a schedule, not by noticing it in the edit.

**Per shot, at generation:** the prompt card names its anchor set; the operator checks
the invariant list; the shot record carries `continuity_refs`
([pack.yaml](pack.yaml)) naming every anchor it was generated against. A shot with no
`continuity_refs` cannot be conformed.

**Per scene, before the scene is considered complete:**

- [ ] Invariants hold on every shot with the character in it
- [ ] Costume state matches the state declared for this point in the timeline
- [ ] Scale is consistent between characters across the coverage
- [ ] Screen direction is consistent with the location plan
- [ ] Light direction, quality, and colour are consistent within the scene
- [ ] Persistent objects are present and in place across angles
- [ ] Time of day matches the timeline entry
- [ ] Temporal stability within each clip — no flicker, morph, or drift mid-shot

**Per work, at picture lock:** a continuity pass across every recurring element —
face, costume, prop, geography, time of day, weather — which is what
`picture_audio_lock` certifies in [gates.yaml](gates.yaml).

**The drift test**, run once per mechanism per studio and repeated when a tool or
version changes: generate the same character across the full range of angles,
expressions, distances, and lighting the work requires, and record where identity
breaks. The output is the studio's own limits table for §2 and it is the difference
between planning around a known boundary and discovering it in week six.
`TBD — the studio runs and records this`; the Visual Director owns it.

**A `continuity_note` is the escalation path** ([05_story_bible.md](05_story_bible.md) §7).
Anyone may raise one. Open notes block picture lock.

## 7. Why continuity lock precedes generation

The `continuity_lock` gate sits at `04_prompts` and blocks `05_assets`
([gates.yaml](gates.yaml)). Generation may not begin before it is signed.

This ordering is the pack's most expensive-looking rule and its cheapest one.

**The asymmetry:** fixing continuity *before* generation costs the time it takes to
build anchor sets. Fixing it *after* costs re-generation of every affected shot, plus
the re-conform, plus the edit decisions that were made around the old material, plus
— and this is the part teams do not budget for — the shots that get kept because
re-doing them is unaffordable, which is how a production ends up shipping the drift it
noticed.

**It is also the only point at which the problem is still small.** At `04_prompts`
there are anchor sets and a shot list. At `06_edit` there are three hundred assets, a
cut, and a delivery date. The same fix is a different order of magnitude on either
side of that line, and nothing about the fix gets easier by waiting.

`continuity_lock` certifies:

1. Every recurring character has a complete anchor set per §3, versioned and locked.
2. Every recurring location has a complete anchor set per §4, with a spatial plan.
3. The style block is fixed at line and sequence level.
4. The toolchain mechanism per character is recorded, with the studio's own measured
   drift limits available to the operators.
5. Every prompt card touching a recurring character or location references its anchor
   set by ID.
6. Every likeness requiring rights has them on file.

It does **not** certify that the shots are good, or that continuity held — that is
picture lock. Bible lock said what is true; continuity lock says the tools are
configured to hold it; picture lock says they did.

## 8. Inheritance and enforcement

Adds to core; loosens nothing. Inherits without modification
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2 —
in particular item 2, which governs every mechanism at §2, and item 1, which prohibits
using these mechanisms to produce a generated artefact presented as a real record even
inside the fiction ([09_setting_fidelity.md](09_setting_fidelity.md) §5). Provenance
recording per §4 of that document applies to every generated asset here, including
anchor material that was itself generated. Rights on training data and vendor terms per
[../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md) §5.

| Standard | Gate | Mechanism |
|---|---|---|
| §2 | Greenlight | Studio cannot greenlight with `continuity_toolchain` unresolved |
| §3, §4 | `continuity_lock` | Complete, versioned anchor set per recurring entity |
| §5 | `continuity_lock` | Style block fixed; overrides carry a reason |
| §6 | `picture_audio_lock` | Continuity pass complete; no open continuity note |
| §6 | `technical_qc` | Every shot carries `continuity_refs`; prompt card and seed in the manifest |
| §7 | `continuity_lock` | Blocks `05_assets`. Generation before lock is a validation failure, not a scheduling choice |
