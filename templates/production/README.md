---
title: Production skeleton
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [showrunner, pipeline-engineer]
---

# Production skeleton

The canonical folder for one episode, film, or short. Copied by
`studio_ops new-production --line <line>` into
`studios/<studio>/lines/<line>/productions/S<NN>E<NN>_<slug>/`.

Maturity: **DESIGNED**. The scaffolder is **NOT BUILT**
([../../docs/status.md](../../docs/status.md)).

## 1. What a production folder is

A production folder is a **claim about state**. At any moment, the stage a piece has
reached is readable from which folders have content and which gates on
[production.yaml](production.yaml) are signed. Nothing else is authoritative — not a
spreadsheet, not a message thread, not the fact that footage exists.

The eleven `NN_` prefixes are load-bearing. They make the directory listing itself a
statement of workflow order, and they are what a gate's `stage` field in
[../../packs/documentary-history/gates.yaml](../../packs/documentary-history/gates.yaml)
points at.

```
S<NN>E<NN>_<slug>/
├── production.yaml     the control record — stage, gates, signatures
├── manifest.yaml       the provenance ledger — every asset that reaches the edit
├── 00_brief/           the question, the thesis, the greenlight case
├── 01_research/        the research pack; claims and sources live at LINE level
├── 02_script/          outline, beats, narration, shooting script, VO sheet
├── 03_storyboard/      shot list and per-shot records
├── 04_prompts/         one prompt card per generated asset
├── 05_assets/          media — NEVER in git; the manifest is the git-side record
├── 06_edit/            NLE project, EDL/XML, cut versions
├── 07_audio_post/      mix, stems, loudness reports
├── 08_review/          fact-check report, cut notes, sensitivity findings
├── 09_delivery/        the delivery package
└── 10_publish/         description, credits, cue sheet, AI-use statement
```

## 2. Stage by stage

Each row is a contract: what must exist before the stage starts, what the stage
produces, and which gate closes it. The gate column names the documentary-history
gate set; a studio on another pack substitutes its own.

| Stage | Enters with | Leaves with | Closed by |
|---|---|---|---|
| [00_brief](00_brief/) | A slate slot and a line that is `open` | A question with stakes, a thesis, a declared advisory position | **Greenlight** (Showrunner) + **Sensitivity** pass 1 (Cultural Advisor) |
| [01_research](01_research/) | A signed greenlight | A research pack; every claim the outline will need existing as a claim record at the line | **Source lock** (Research Lead) |
| [02_script](02_script/) | A signed source lock | Narration and shooting script in which every factual statement carries a `{{CLM-XX-0000}}` reference | **Script lock** (Story Producer) |
| [03_storyboard](03_storyboard/) | A locked script | A shot list, one shot record per shot, safe zones marked | — (feeds picture lock) |
| [04_prompts](04_prompts/) | A locked script and a shot list | One reviewable prompt card per generated asset, before any generation | **Sensitivity** pass 2 (Cultural Advisor) |
| [05_assets](05_assets/) | Reviewed prompt cards | Media in the asset store, one manifest entry per file | — (feeds rights + picture lock) |
| [06_edit](06_edit/) | Assets present in [manifest.yaml](manifest.yaml) | A locked cut; every reconstruction and interpretive shot labelled | **Picture lock** (Visual Director) |
| [07_audio_post](07_audio_post/) | A locked picture | Mix at spec, all stems including M&E, every proper noun verified | **Audio lock** (Audio Lead) |
| [08_review](08_review/) | A locked script; a locked cut | Fact-check report, cut notes, sensitivity findings, all resolved | **Fact-check** (Research Lead) + **Sensitivity** pass 3 + **Rights** |
| [09_delivery](09_delivery/) | Fact-check, sensitivity, rights, picture and audio locks all signed | A packaged, spec-conformant delivery with a frozen manifest | **Technical QC** (Pipeline Engineer) |
| [10_publish](10_publish/) | A signed technical QC | Description, credits, AI-use statement, cue sheet, provenance summary | — (publication is an act, not a gate) |

Two things this table is deliberately explicit about:

**Sensitivity runs three times.** At the brief, before generation, and at the locked
cut. It is the only gate with hold authority the Showrunner cannot unilaterally
override ([../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §6).
Running it once, at the end, is the same as not running it: by then the images
exist and the argument is about sunk cost.

**Generation does not begin before script lock.** Not "should not" — the gate blocks
`04_prompts` and `05_assets`. A production that generates against an unlocked script
starts writing toward the footage it happens to have, and the direction of authority
inverts without anyone deciding that it should.

## 3. The two control files

| File | Schema | What it is |
|---|---|---|
| [production.yaml](production.yaml) | [episode.schema.json](../../standards/schemas/episode.schema.json) | Stage, gates, signatures, scope, budget, schedule. The one place the state of the production is true. |
| [manifest.yaml](manifest.yaml) | [asset_manifest.schema.json](../../standards/schemas/asset_manifest.schema.json) | Every asset that reaches the edit, generated or not, with its provenance. |

An asset absent from the manifest cannot be conformed into the edit. That refusal —
not a policy document — is the mechanism behind the platform's traceability
guarantee ([../../README.md](../../README.md) §7).

## 4. Working rules inside a production folder

- **Media never enters git.** Not a reference frame, not a proxy, not "just this
  one". See [05_assets/README.md](05_assets/README.md).
- **Claims and sources live at the line, not here.** A claim used by two episodes is
  one record. Copying it into a production folder guarantees the two copies diverge,
  and the divergence is invisible until a fact-check catches it, or does not.
- **Versions are numeric.** `_v01`, `_v02`. Never `_final`. See
  [../../standards/naming_conventions.md](../../standards/naming_conventions.md).
- **Every `TBD` carries its clause.** `TBD — needs the advisory ruling on depicting
  the regalia` is actionable; `TBD` is a shrug.
- **Nobody signs two gates.** ([../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §5.)
  If the same name would appear twice, the production is understaffed, and that is a
  staffing finding rather than a paperwork one.
