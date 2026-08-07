---
title: Studio bible amendment log
status: active
version: 0.1.0
updated: 2026-08-07
owners: [showrunner]
---

# Amendment log — African History Studio

Append-only. Every change to any document in [bible/](README.md) is recorded here
**before it takes effect**. An amendment absent from this log has no force, and the
prior text stands.

This log governs the studio layer only. Changes to the
[documentary-history pack](../../../packs/documentary-history/) are recorded in the
pack; changes to core are recorded in
[core/05_amendment_log.md](../../../core/05_amendment_log.md). Recording a pack
change here would create a second, divergent history of the same rule — see
[README.md](README.md) §1.

Maturity: **DESIGNED**. No amendment has been signed. No signature in this repository
has ever been recorded.

## Format

```
## <YYYY-MM-DD> — <short title>

**Documents:** bible/<name>, bible/<name>
**Version:** <old> → <new>
**Signatures:** <role: name>, <role: name>
**Supersedes:** <link to the prior text, or "n/a — new section">

**Change**
<What is different, stated so a reader who has not seen the diff understands it.>

**Rationale**
<Why. What went wrong, or what was learned, that made the old text inadequate.>

**Migration**
<What existing records, scripts, assets, or line addenda are invalidated, and the
procedure that brings them into compliance. "None" is acceptable only if it is true.>
```

Entries are appended, newest last. Nothing is edited in place; a mistaken entry is
corrected by a subsequent entry that supersedes it, because an amendment log that can
be rewritten is not evidence of anything.

## Required signatures

| Section changed | Signatures required |
|---|---|
| Any document in `bible/` | Showrunner + Cultural Advisor |
| `00_charter.md` §2 Scope, or opening/closing a production line | + the affected line's Research Lead and advisory contact |
| `00_charter.md` §6 Editorial independence | + Showrunner, recorded with the disclosure it creates |
| `00_charter.md` §7 Standing commitments | + Research Lead and Rights & Clearances |
| `corrections.md` — the *procedure*, not an entry | + Research Lead |
| Anything that tightens a pack rule for this studio | + the Pack Owner, confirming it is a tightening and not a loosening |
| Anything touching a brand specification with a technical constraint | + Visual Director and Pipeline Engineer |

Adding a correction *entry* to [corrections.md](corrections.md) is not an amendment
and needs no signature here. It follows the intake path in that document. Requiring a
signature to publish a correction would make correcting slower than not correcting,
which inverts the incentive the log exists to create.

## Standing rules

1. A bible amendment is never bundled into a production PR. It rides on a
   `studio/bible-*` branch. See [CONTRIBUTING.md](../../../CONTRIBUTING.md)
   § Branching.
2. An amendment that would loosen a pack or core rule is out of scope here. Route it
   to the layer that owns the rule, with that layer's signatures.
3. Version bumps are semantic at the document level: a clarification is a patch, a
   new obligation is a minor, a reversal of a standing commitment is a major and
   requires the migration section to be non-trivial.

---

# Log

## 2026-08-07 — Studio established; **not ratified**

**Documents:** bible/README.md, bible/00_charter.md, bible/amendment_log.md, bible/corrections.md
**Version:** — → 0.1.0
**Signatures:** `TBD — none. The studio bible is a draft. It becomes canon when the`
`Showrunner and the Cultural Advisor sign this entry, and not before.`
**Supersedes:** n/a — new studio

**Change**
Establishes African History Studio as a studio on the video-studio platform: its
charter, this log, the public correction log, the brand folder, and one production
line ([ng-nigeria](../lines/ng-nigeria/README.md)) at `line_status: candidate`. The
studio declares the [documentary-history](../../../packs/documentary-history/) canon
pack in [studio.yaml](../studio.yaml).

**Rationale**
The studio's method — heavy generative tooling applied to contested and unevenly
documented history belonging to living communities — has failure modes that informal
judgement does not reliably catch under deadline. Establishing the layer before any
content exists means the constraints are cheap to accept; establishing it after the
first season means arguing about them while holding footage.

**Migration**
None. No production work predates this entry, and no historical claim exists anywhere
in the studio.

**Open items blocking ratification**

All eleven `decisions` in [studio.yaml](../studio.yaml) are `unresolved`. Ratification
requires each to be resolved or explicitly deferred with a named owner and a date:

| Key | Owner | Where it is settled |
|---|---|---|
| `mission` | Showrunner | [00_charter.md](00_charter.md) §1 |
| `audience` | Showrunner | [00_charter.md](00_charter.md) §3 |
| `success_conditions` | Showrunner | [00_charter.md](00_charter.md) §8 |
| `ai_music_policy` | Showrunner + Cultural Advisor | [pack 05 §4](../../../packs/documentary-history/05_sound_and_score.md) |
| `production_language` | Showrunner + Cultural Advisor | [pack 09 §1](../../../packs/documentary-history/09_localization.md), line [languages/](../lines/ng-nigeria/languages/README.md) |
| `orthography_standards` | Cultural Advisor | [pack 09 §2](../../../packs/documentary-history/09_localization.md) — **blocks typeface selection and therefore all brand design** |
| `narration_voice_policy` | Audio Lead | [voice_policy.md](../lines/ng-nigeria/languages/voice_policy.md) |
| `visual_identity` | Visual Director | [visual_identity.md](../lines/ng-nigeria/style/visual_identity.md) |
| `runtime_and_platforms` | Showrunner | [core/03 §1](../../../core/03_distribution_and_formats.md) |
| `audio_description_scope` | Audio Lead | [pack 05 §8](../../../packs/documentary-history/05_sound_and_score.md) |
| `licensing_posture` | Showrunner | [ADR 0009](../../../docs/decisions/0009-licensing-posture.md) |

Three of these are ordering hazards rather than open questions, and are called out
because they are routinely discovered late:

- **`orthography_standards` gates `brand_design`.** Typeface selection depends on the
  union of diacritic coverage across every language the studio's lines will put on
  screen. Choosing a face first and discovering a missing glyph later means either
  stripping marks — prohibited by
  [pack 09 §2](../../../packs/documentary-history/09_localization.md) — or re-typesetting
  every graphic already produced.
- **`ai_music_policy` is the decision most likely to be regretted if made casually.**
  The pack records a default pending the ruling; the default is not the ruling.
- **`visual_identity` blocks every prompt card**, because a prompt card inherits a
  style block from the line and there is nothing yet to inherit.

Separately, the Nigeria line cannot open — and therefore nothing can be greenlit —
until its three opening conditions hold. All three are currently false in
[line.yaml](../lines/ng-nigeria/line.yaml): no research lead named, no advisory
contact agreed, no archive landscape surveyed. The
[production_line schema](../../../standards/schemas/production_line.schema.json)
refuses `line_status: open` while any is false.

## 2026-08-07 — Laboratory productions may run before a line opens

**Documents:** this log; scope is laboratory productions only
**Signatures:** `TBD — Showrunner.` Directed but not yet countersigned. The relaxation
is in force for EXP-001 pending signature; it does not extend further until signed.
**Supersedes:** n/a — new exemption

**Change**

A production with `kind: laboratory` that makes **no historical claims** may exercise
production mechanics before its line reaches `line_status: open`.

Concretely, for such a production these cease to be blockers: line status, a named
Research Lead, an agreed advisory contact, an archive landscape survey, and a line
visual identity.

These remain in force, unchanged:

- **The sensitivity gate is not relaxed.** Generated imagery of people is still
  imagery of people. It is the one gate whose failure harms someone outside the
  studio.
- **The production is never published**, in any form, including as a clip.
- **No historical claim, name, date, or real place may appear.** The moment one does,
  the exemption lapses and every ordinary condition applies.
- Provenance, rights, and technical QC are unchanged. The platform's guarantees do not
  bend for an experiment.

**Rationale**

The line-opening conditions exist to protect *people and evidence*: they make sure a
line does not depict a community without someone competent to advise, or assert
history without someone competent to source it. A production that depicts nothing real
and asserts nothing engages neither risk, so the conditions protect nothing while
blocking everything.

The alternative was to open the Nigeria line prematurely in order to run a test — which
would have hollowed out the opening conditions far more seriously than exempting a
piece that makes no claims.

**Cost, stated plainly**

EXP-001 no longer tests the research pipeline. It was previously designed around 8–12
researched claims; with none, hypothesis **H1** — whether the claim chain survives a
production schedule — goes untested, and it is the load-bearing assumption of the whole
architecture.

**A green EXP-001 is not evidence that
[ADR 0002](../../../docs/decisions/0002-claims-as-records.md) works.** A separate
experiment with real research must run before episode one. That is now the largest
unproven assumption in the repository and it should be recorded as such wherever the
roadmap is read.

**Migration**

None. No production predates this.

**Watch for**

A second laboratory production quietly acquiring historical content while keeping the
exemption. The exemption is conditional on making no claims, and the condition is the
whole of it — if a laboratory piece starts naming a period or a people, it is no longer
a laboratory piece under this entry.

<!-- New entries are appended below this line, newest last. -->
