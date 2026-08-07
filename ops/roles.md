---
title: Roles
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner]
---

# Roles

Fifteen role slugs are used across this repository. This document is the canonical
list. Every `owners:` field in front matter, every `owner:` in a `gates.yaml`, and
every `role:` in a signature draws from it.

## 1. Why roles are slugs and never names

Records reference **roles**, not people.

A record owned by `ejovi` is orphaned the day that person changes job, leaves, or
takes a different role on the next production — and nothing in the repository knows
it happened. There is no mechanical way to ask "who owns this now?", so the question
is answered by whoever remembers, until nobody does. A record owned by
`research-lead` is answerable by whoever holds that role today, which is a fact the
studio can look up.

This is not a naming preference. It is the difference between a registry that stays
navigable across a staffing change and one that quietly rots into a set of files with
no maintainer. `owners` is a list of slugs;
[../standards/metadata_spec.md](../standards/metadata_spec.md) enforces it and
[../standards/schemas/_common.schema.json](../standards/schemas/_common.schema.json)
constrains it to an enum.

People appear in exactly one place: the `person` field of a **signature**. A
signature is a statement by a specific human on a specific date, so it names one —
that is the entire point of a gate. Everywhere else, the slug.

## 2. The list

| Slug | Tier | Signs gates? |
|---|---|---|
| `platform-owner` | Platform | No |
| `pack-owner` | Platform (one pack) | No |
| `showrunner` | Studio | Yes — greenlight / brief approval / stakeholder approval |
| `line-lead` | Line | No |
| `research-lead` | Production | Yes — source lock, fact-check |
| `story-producer` | Production | Yes — script lock, story bible lock |
| `visual-director` | Production | Yes — picture lock, continuity lock, picture+audio lock, garment verification |
| `audio-lead` | Production | Yes — audio lock |
| `rights-and-clearances` | Production | Yes — rights, claim substantiation |
| `cultural-advisor` | Production | Yes — sensitivity, representation review |
| `pipeline-engineer` | Platform / production | Yes — technical QC |
| `editor` | Production | No |
| `composer` | Production | No |
| `translator` | Production | No |
| `advisor` | Line (external) | No |

Five roles sign nothing, and that is deliberate rather than an oversight — see §4.

## 3. Definitions

### `platform-owner`

| | |
|---|---|
| **Owns** | [../core/](../core) canon, [../standards/](../standards) (schemas, ID system, naming, delivery specs, metadata spec), [../automation/](../automation) and the validator gate set, the repository's structural contract, pack admission, licensing posture |
| **Decides alone** | Schema and standard changes that *tighten*; validator behaviour and severity; the root-directory contract; whether a proposed canon pack is admitted; which capabilities may be promoted from DESIGNED to IMPLEMENTED and on what evidence |
| **Cannot decide** | Anything editorial inside a pack, studio, line, or production. Whether a specific piece ships. Release of an advisory hold. Loosening a core guarantee — see the open question below |
| **Signs** | No production gate |

> `TBD — core has no written amendment procedure.` Whether the Platform Owner may
> weaken a guarantee in [../core/00_platform_charter.md](../core/00_platform_charter.md)
> §5–6 unilaterally, and what signatures a core amendment requires, is unresolved.
> Until it is, treat core's refusals as unamendable. Resolving it needs an ADR under
> [../docs/decisions/](../docs/decisions).

### `pack-owner`

| | |
|---|---|
| **Owns** | One canon pack: its documents, its `gates.yaml`, the `certifies:` text of each gate, its evidence and doctrine standards |
| **Decides alone** | The pack's gate set, gate owners, the blocking graph, what each gate certifies, and any constraint that *tightens* core |
| **Cannot decide** | Anything in core. Another pack. Whether a studio adopts this pack. The outcome of any individual gate. The body of a shared checklist in [checklists/](checklists) — that is a platform change, because other packs read the same file |
| **Signs** | No production gate |

A pack owner who needs a materially different checklist for a shared gate key
authors a new key and points their own `gates.yaml` at it. See
[README.md](README.md) §2.

### `showrunner`

| | |
|---|---|
| **Owns** | One studio: its bible, brand, slate, and the set of lines under it. Final editorial authority within the studio |
| **Decides alone** | Greenlight and shelving; slate order and runtime targets; budget allocation within the studio envelope; final cut; title, thumbnail, and description; which line opens and when |
| **Cannot decide** | Release of an advisory hold ([../core/04_review_gate_framework.md](../core/04_review_gate_framework.md) §6). Whether a claim is sourced. Whether an asset is cleared. Any core or pack rule |
| **Signs** | `greenlight` (documentary-history, narrative), `brief_approval` (product-marketing, fashion-film), `stakeholder_approval` (product-marketing, fashion-film) |

The advisory hold is the one structural check on this role's authority, and it exists
because the cost of being wrong about sensitive material is borne by people outside
the studio, who have no other route to a veto.

### `line-lead`

| | |
|---|---|
| **Owns** | One production line: its research registry, entity records, advisory register, language and orthography policy, `style/` folder, slate execution and scheduling |
| **Decides alone** | Line-level style and motif registration; scheduling within the studio's targets; which episodes it proposes for the slate; who sits on the line's advisory register, jointly with `cultural-advisor` |
| **Cannot decide** | Greenlight. Studio brand or bible. Whether the line's opening conditions are met — those are conditions, not judgements |
| **Signs** | No gate in any current pack |

Deliberately outside the signature chain. The Line Lead carries the schedule, and the
person carrying the schedule should not also be certifying that the work is finished.

### `research-lead`

| | |
|---|---|
| **Owns** | Source records, claim records, claim IDs, the open-questions register, the bias register, independence and corroboration checks, corrections triage |
| **Decides alone** | A source's tier (T1–T5); a claim's confidence register; whether corroboration is sufficient and whether two sources are genuinely independent; whether to register an open question; corrections triage outcome |
| **Cannot decide** | Whether a sequence survives editorially. Sensitivity rulings. Whether a source is *cleared* for use, which is a rights question and separate from whether it is *good* |
| **Signs** | `source_lock`, `fact_check` (documentary-history) |

Changing a register **down** is always this role's call and needs nobody's agreement.
Changing one up requires the evidence, not a conversation.

### `story-producer`

| | |
|---|---|
| **Owns** | Brief, question and thesis, outline, beat sheet, narration, shooting script, VO record sheet compilation; the story bible under the narrative pack |
| **Decides alone** | Structure and movement shares; phrasing; which verbal form expresses a given register; what is cut for time; the interpretive stance on an adapted source, declared in writing at greenlight |
| **Cannot decide** | Whether a fact is established, or at what register — both belong to `research-lead`. Whether sensitive material may be depicted. Whether a shot exists |
| **Signs** | `script_lock` (documentary-history, narrative), `story_bible_lock` (narrative) |

### `visual-director`

| | |
|---|---|
| **Owns** | Visual language, the look bible, style anchors, visual prompt cards, shot list and provenance classes, storyboard and safe zones, the show LUT and grade |
| **Decides alone** | Framing, lens set, camera grammar, motion policy; the style anchor set; which shots are regenerated and which survive; continuity anchors for recurring characters and locations |
| **Cannot decide** | Whether a depiction is culturally permissible. Whether an asset is cleared. Whether the claim a shot illustrates is supported |
| **Signs** | `picture_lock` (documentary-history), `continuity_lock` (narrative), `picture_audio_lock` (narrative, product-marketing, fashion-film), `garment_verification` (fashion-film) |

### `audio-lead`

| | |
|---|---|
| **Owns** | VO casting and sessions, the score commissioning brief, ambience and sound design, the mix, all stems including M&E, loudness compliance, the pronunciation verification workflow |
| **Decides alone** | Mix decisions and stem structure; take selection; ambience design within the pack's sound policy; whether the mix holds on a phone speaker |
| **Cannot decide** | Whether a music cue is cleared. Whether generated music that draws on a living tradition is permissible. Whether to synthesise a real or historical person's voice — that is prohibited outright by core and is not a decision at all |
| **Signs** | `audio_lock` (documentary-history) |

### `rights-and-clearances`

| | |
|---|---|
| **Owns** | The clearance log, the model terms register, the cue sheet, chain of title, contributor releases, font and LUT and stock licences, territorial restrictions, takedown intake |
| **Decides alone** | Whether an asset's clearance state permits it into a locked cut; whether a licence covers the intended media, territory, and term; whether a fair-dealing position is being taken and on what written rationale |
| **Cannot decide** | The editorial value of an asset. Whether to accept a clearance risk on the studio's behalf — an uncleared asset is a block, not a risk to be weighed |
| **Signs** | `rights` (documentary-history), `claim_substantiation` (product-marketing) |

Under [../core/02_rights_and_licensing.md](../core/02_rights_and_licensing.md) there
is no provisional delivery. `pending` is a stop.

### `cultural-advisor`

| | |
|---|---|
| **Owns** | Sensitivity procedure, the advisory register, written advisory rulings, representation standards, and **hold authority** |
| **Decides alone** | Whether to place an advisory hold, and whether to release one. Whether material is restricted. Whether a premise, a prompt set, or a cut clears review. This is the only authority the Showrunner cannot override |
| **Cannot decide** | Editorial structure, budget, or schedule. A hold stops work on an item; it does not redirect the production |
| **Signs** | `sensitivity` (documentary-history, narrative), `representation_review` (fashion-film) |

Distinct from `advisor`: this is a studio-side accountable role that rules and signs.
An `advisor` is an external expert whose input this role converts into a ruling.

### `pipeline-engineer`

| | |
|---|---|
| **Owns** | `studio_ops`, the schemas jointly with `platform-owner`, CI, the provenance manifest and ledger, the asset store, delivery packaging, the generation adapters and their cost ceilings |
| **Decides alone** | Tooling implementation and validator mechanics; asset store layout; how conform method is recorded; the delivery package structure; when an adapter refuses to run |
| **Cannot decide** | Whether a delivery target is the right target — that is a standards question. Editorial content. Whether to override a failing validator; there is no override flag, by design |
| **Signs** | `technical_qc` (all packs — core's universal gate) |

### `editor`

| | |
|---|---|
| **Owns** | The assembly and the cut under the Visual Director's direction; NLE project structure; keeping text on separate layers so a textless master is a render and not a rebuild |
| **Decides alone** | Shot selection and timing within the approved structure |
| **Cannot decide** | Picture lock. Any provenance class, label, or clearance question |
| **Signs** | Nothing |

### `composer`

| | |
|---|---|
| **Owns** | The score, cue delivery, and cue sheet entries for original music |
| **Decides alone** | Musical content within the commission and the pack's music policy |
| **Cannot decide** | Clearance of anything they did not originate. Audio lock |
| **Signs** | Nothing |

### `translator`

| | |
|---|---|
| **Owns** | Translated narration, subtitles, quotation translation, and the record of translation basis — including whether a text was retranslated through an intermediate language, which materially weakens the evidentiary chain |
| **Decides alone** | Rendering choices within the line's orthography and naming policy |
| **Cannot decide** | Naming policy itself. Whether a claim survives translation intact |
| **Signs** | Nothing — and is credited by name, because translation is an interpretive act |

### `advisor`

| | |
|---|---|
| **Owns** | Their own declared scope of competence on a line's advisory register: which traditions and communities they can rule on, and which they cannot |
| **Decides alone** | Nothing binding on the studio by itself. Advice becomes binding when `cultural-advisor` records it as a ruling |
| **Cannot decide** | Gate outcomes |
| **Signs** | Nothing — and is paid, credited, holds review rights, and may withdraw |

An advisor who is not paid is not an advisor.

## 4. The five roles that sign nothing

`editor`, `composer`, `translator`, `advisor`, and the management roles
(`platform-owner`, `pack-owner`, `line-lead`) hold no signature.

For the craft roles this is the separation-of-duties principle applied at its
sharpest point: **the person who made the thing cannot see it.** The Editor cut the
sequence; asking the Editor to certify the cut is asking a question whose answer was
determined an hour earlier. The gate exists to introduce a second pair of eyes, and a
gate signed by the maker introduces none.

For the management roles the reason is different: they carry schedule and budget, and
a signature is exactly the thing schedule pressure is most likely to bend.

## 5. Two open conflicts you will hit immediately

### 5.1 Every pack assigns one role two gates on the same production

[../core/04_review_gate_framework.md](../core/04_review_gate_framework.md) §5 states
flatly: *no person signs two gates on the same production*. Every current pack
declares a gate set that violates this if the role is held by one person:

| Pack | Doubled role | Gates |
|---|---|---|
| documentary-history | `research-lead` | `source_lock`, `fact_check` |
| product-marketing | `showrunner` | `brief_approval`, `stakeholder_approval` |
| narrative | `story-producer` | `story_bible_lock`, `script_lock` |
| narrative | `visual-director` | `continuity_lock`, `picture_audio_lock` |
| fashion-film | `showrunner` | `brief_approval`, `stakeholder_approval` |
| fashion-film | `visual-director` | `garment_verification`, `picture_audio_lock` |

The packs also declare `minimum_distinct_signatories` of 3 or 4 against gate sets of
5 to 9, which only adds up if a person may sign more than one gate.

Both readings are defensible. Either §5 means what it says and a doubled role must be
held by two different people for that production, or §5 means "no person signs two
*adjacent or dependent* gates" and the compatible pairs need enumerating. The pairs
above are not equally troubling: `source_lock` and `fact_check` are the same person
checking their own research pack twice, which is the failure §5 was written against;
`brief_approval` and `stakeholder_approval` are separated by the whole production.

`TBD — Platform Owner and pack owners to resolve, recorded as an ADR under`
[../docs/decisions/](../docs/decisions)`, and reflected in whichever of core/04 §5 or
the four gates.yaml files turns out to be wrong.` Until then, treat the literal
reading as binding: a doubled role needs two people.

### 5.2 The schema enum is three slugs short of this document

[../standards/schemas/_common.schema.json](../standards/schemas/_common.schema.json)
`$defs.roleSlug` enumerates twelve slugs. It omits `platform-owner`, `pack-owner`, and
`line-lead` — all three of which are already used: `platform-owner` in the front
matter of every core document and of
[../docs/status.md](../docs/status.md), and `line-lead` in
[../core/00_platform_charter.md](../core/00_platform_charter.md) §7.

Any record validated against that enum with one of those three in `owners:` will
fail. Nothing has failed yet only because `studio_ops validate --schemas` has never
run against a real record.

`TBD — Platform Owner to either extend the roleSlug enum to fifteen or split it into
a production-role enum and a governance-role enum.` The schema is outside this
directory's ownership; the drift is recorded here because this document is the one
that claims to be canonical.

## 6. Holding several roles at once

On a small team one person will hold several of these, and that is expected — see
[../core/00_platform_charter.md](../core/00_platform_charter.md) §7. The Showrunner
may also be the Story Producer, the Line Lead, and the Pipeline Engineer.

The single exception is **across gates on the same production**. That constraint is
core, not a preference, and it is the first thing a two-person team abandons. When it
is abandoned, every gate on that production becomes a formality performed by the
person who made the material, and the entire signature chain certifies nothing while
continuing to look exactly like a signature chain.

The structural consequence is stated plainly in
[risk_register.md](risk_register.md) `RSK-PLAT-0001`: a team that cannot field the
required number of distinct signatories cannot run the pack it has adopted, and the
honest responses are to bring in outside signatories, adopt a pack with a smaller gate
set, or not produce. Signing anyway is not on the list.

The full stage-by-stage allocation is in [raci.md](raci.md).
