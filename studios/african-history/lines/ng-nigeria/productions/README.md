---
title: Productions — Nigeria line
status: active
version: 0.1.0
updated: 2026-08-07
owners: [showrunner]
---

# Productions

The pieces this line makes.

> **None exist.** No production has been created, greenlit, or scaffolded in this
> line. No script, no shot list, no prompt card, no asset. **No gate has ever been
> signed anywhere in this repository.**

## 1. Naming

One folder per production, at this level:

```
S01E01_slug/
S01E02_slug/
```

`S<NN>E<NN>_<slug>` — season and episode zero-padded to two digits, underscore, then a
kebab-case slug describing the subject. ASCII only, lowercase slug, no spaces
([standards/naming_conventions.md](../../../../../standards/naming_conventions.md)).

The zero padding is load-bearing: `S01E10` must sort after `S01E09` in every tool that
touches the tree, and unpadded numbers sort lexically into nonsense at exactly the
point a season becomes big enough for it to matter.

The **production code** is `S01E01` and it is what appears in record IDs
(`SHT-NG-S01E01-0142`, `PC-NG-S01E01-0037`, `AST-NG-S01E01-0142`,
`FCK-NG-S01E01-0003`). The slug is for humans reading a directory listing and never
enters an ID — a slug can be corrected, and an ID cannot.

Shorts and other non-episodic pieces take the same shape under whatever season they
belong to, or a season reserved for them. Decide it once, in
[../line.yaml](../line.yaml) under `seasons`, rather than per piece.

## 2. Creating one

```
python -m studio_ops new-production --line ng-nigeria
```

**NOT BUILT** ([docs/status.md](../../../../../docs/status.md)). Every `studio_ops`
command in this repository is currently a specification rather than a working CLI.

When it exists, it scaffolds the eleven-stage pipeline folder structure from
[templates/production/](../../../../../templates/production/), reads the pack's
[gates.yaml](../../../../../packs/documentary-history/gates.yaml) to build the
production record's `gates` block, and allocates the production code. A production
cannot be created without a pack and therefore never has an undefined gate set.

It refuses to run — by design — while any of the following is true, and **all of them
are currently true**:

| Blocker | State |
|---|---|
| `line_status` is not `open` | `candidate`; all three opening conditions false ([../README.md](../README.md) §2) |
| Any studio decision is `unresolved` | Eleven are ([studio.yaml](../../../studio.yaml)) |
| The studio bible is not ratified | It is not ([bible/amendment_log.md](../../../bible/amendment_log.md)) |
| No advisory coverage for the premise | No advisor engaged ([../advisory/README.md](../advisory/README.md)) |
| No line visual identity | **NOT STARTED** ([../style/visual_identity.md](../style/visual_identity.md)) |

## 3. What a production folder holds

Eleven numbered pipeline stages, `NN_name`, so that the folder listing is itself a
readable statement of the workflow order — brief, research, script, storyboard,
prompts, assets, edit, audio, review, delivery, publish. The canonical skeleton is
[templates/production/](../../../../../templates/production/); the structure is not
re-specified here, because a second copy would drift from the template that scaffolds
it.

What is worth stating at line level:

- **`05_assets/` is not in git.** Media goes to the asset store; git holds the
  manifest. An asset without a manifest entry cannot be conformed into the edit — the
  pipeline refuses it, and that refusal is the mechanism behind the platform's
  traceability guarantee ([core/01 §4](../../../../../core/01_provenance_and_ai_disclosure.md)).
  The conform step is **DESIGNED** and does not exist yet.
- **The script references claims; it does not assert.** A date, name, figure, or
  quantity in prose without a `{{CLM-NG-NNNN}}` reference is a defect
  ([../sources/README.md](../sources/README.md)).
- **Generation does not begin before script lock.** Generating for an unlocked script
  is how a production ends up writing toward the footage it happens to have
  ([gates.yaml](../../../../../packs/documentary-history/gates.yaml)).

## 4. Gates

Nine, from the pack
([documentary-history README](../../../../../packs/documentary-history/README.md)):
greenlight, source lock, script lock, fact-check, sensitivity, rights, picture lock,
audio lock, technical QC. The framework — what a gate *is*, what states it has, how a
re-open cascades — is [core/04](../../../../../core/04_review_gate_framework.md).

Three properties that bind at this level:

- **No person signs two gates on the same production**
  ([core/04 §5](../../../../../core/04_review_gate_framework.md)). It is the constraint
  most likely to be quietly abandoned on a small team, and it exists because the most
  common review failure is not incompetence but proximity — the person who made the
  thing cannot see it. `distinct_signatories_available` is currently **0** in
  [studio.yaml](../../../studio.yaml). **With fewer than four distinct people this
  studio cannot ship**, and that is an arithmetic fact rather than a policy position.
- **A re-open cascades.** Re-opening a signed gate returns every downstream gate signed
  on the basis of it to `pending`. That cascade is what makes a late change feel like
  what it is.
- **An advisory hold is not a failed gate and is released only in writing by the
  Cultural Advisor.** The Showrunner cannot release it
  ([../advisory/README.md](../advisory/README.md) §5).

## 5. On publication

Each published production carries, alongside the video: a **sources page**, a
**provenance summary**, and a **correction log** — generated from records that already
exist, not written by hand
([core/03 §5](../../../../../core/03_distribution_and_formats.md)). It costs almost
nothing and is the studio's primary differentiator against the volume of unsourced
history content the audience will otherwise compare it to.

Corrections after publication go to the studio-wide log,
[bible/corrections.md](../../../bible/corrections.md), which is append-only and public.

## 6. Status

Nothing exists. The first production in this line is blocked behind a named research
lead, an engaged advisor, a completed archive landscape survey, a confirmed language
register, a defined visual identity, eleven studio decisions, and a ratified bible.

That list is long on purpose. Every item on it is cheap now and expensive after the
first frame is generated.

## Productions

| Code | Kind | Subject | Tests | Status |
|---|---|---|---|---|
| [EXP001](EXP001_laboratory-scene/) | laboratory | Invented workshop household | **Continuity drift across 20 shots** | scaffolded, not started |
| EXP002 | laboratory | *A Morning in Benin City, c. 1600* | **H1 — whether the claim chain survives a production schedule** | **not scaffolded** — blocked |

### EXP-002 — why it is registered here and not built

EXP-001 makes no historical claims, so it cannot test H1: *can facts be researched
into claim records, before the script, at production pace?* That is the load-bearing
assumption of the entire architecture, and a green EXP-001 says nothing about it.

EXP-002 is the experiment that does. Same shot plan, same continuity mechanism —
but with 8–12 real claims researched against real sources, and period-specific
architecture and dress carrying an evidence basis.

It is blocked on the things a claims-bearing production is properly blocked on, and
those blocks are not a nuisance — they are the point:

| Blocked on | Why it genuinely blocks |
|---|---|
| A named Research Lead | Someone must own the claims |
| An agreed advisory contact | The subject is a real place and a real people |
| An archive landscape survey | The claims have nowhere to come from |
| Line status `open` | The laboratory exemption does not extend to a production that makes claims |

**The laboratory exemption does not cover EXP-002 and must not be stretched to.**
The moment a production encodes historically specific detail, every ordinary
condition applies — which is exactly what the exemption's `Watch for` clause in
[the amendment log](../../../bible/amendment_log.md) says to look out for.

