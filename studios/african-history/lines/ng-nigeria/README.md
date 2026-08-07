---
title: Nigeria line
status: active
version: 0.1.0
updated: 2026-08-07
owners: [showrunner, research-lead]
---

# Nigeria — line 01

The first production line of [African History Studio](../../README.md), running the
[documentary-history](../../../../packs/documentary-history/) canon pack.

| | |
|---|---|
| Code | `ng-nigeria` |
| ID scope | `NG` — records are `SRC-NG-*`, `CLM-NG-*`, `CHR-NG-*`, `LOC-NG-*`, `EVT-NG-*`, `QST-NG-*`, `ADV-NG-*` |
| Order | 01 |
| Status | **`candidate`** — considered, not opened. No production can be greenlit. |
| Control record | [line.yaml](line.yaml) |
| Maturity | **DESIGNED** for structure. **NOT STARTED** on advisory, archives, and visual identity. |

## 1. No historical content exists here, and none may be added informally

**Nothing in this line asserts anything about the past.** There are no claims, no
sources, no people, no places, no events, no dates, and no scripts. Every register
below is empty. That is the deliberate state of the line, not a stage it is
embarrassed to be at.

Facts enter this line by exactly one route:

```
sources/records/SRC-NG-NNNN.yaml     the evidence, with a critique block
              ▲
              │ cited by
sources/claims/CLM-NG-NNNN.yaml      the fact, its confidence register, its sources
              ▲
              │ referenced by
productions/S01E01_slug/02_script/   the script, which references and never asserts
```

The chain is defined in
[02_evidence_and_sourcing.md](../../../../packs/documentary-history/02_evidence_and_sourcing.md)
and is not restated here. Three consequences of it govern everything in this folder:

1. **A script contains no facts.** It contains references to claims. A date, a name, a
   figure, or a quantity that appears in prose without a claim ID is a defect, and
   `studio_ops validate --sources` fails the build on it — when it is built.
2. **No model output is a source.** It is T5. It may locate a lead; it may never
   support a claim, and a lead is verified against the actual document before it
   becomes anything.
3. **A gap is recorded, never filled.** An unanswered question becomes a `QST-NG-*`
   record in [research/open_questions/](research/README.md) with what was searched.
   The register goes down; the claim does not go up. If the sequence cannot survive
   the honest register, the sequence is cut.

Anyone adding content here should read
[research/README.md](research/README.md) first and
[CONTRIBUTING.md](../../../../CONTRIBUTING.md) § Writing rules second.

## 2. What blocks opening

`line_status` can move to `open` only when all three conditions in
[bible/00_charter.md](../../bible/00_charter.md) §2 are true. All three are currently
**false** in [line.yaml](line.yaml), and the
[production_line schema](../../../../standards/schemas/production_line.schema.json)
refuses `line_status: open` while any is — so this is a red build, not a convention.

| # | Condition | State | Where it is satisfied |
|---|---|---|---|
| 1 | A named research lead with domain competence has agreed to own the line | **NOT STARTED** | `TBD — Showrunner`. Domain competence is the qualifier; availability is not. |
| 2 | At least one advisory contact with standing in the region has agreed to review, on recorded terms | **NOT STARTED** | [advisory/README.md](advisory/README.md) |
| 3 | The archive landscape has been surveyed, including what could not be reached | **NOT STARTED** | [sources/archive_landscape.md](sources/archive_landscape.md) — a template, not a survey |

Condition 2 is the one that gets skipped under enthusiasm, and it is the one that
cannot be repaired after publication. A line does not begin production on material
outside its advisory coverage
([pack 07 §5](../../../../packs/documentary-history/07_cultural_sensitivity.md)); if
the register has no one competent on what a production needs, the production waits.

Beyond the three conditions, and independent of them:

- The **studio bible is not ratified** — [bible/amendment_log.md](../../bible/amendment_log.md).
- Eleven studio **decisions are `unresolved`** — [studio.yaml](../../studio.yaml).
- **Visual identity is undefined** — [style/visual_identity.md](style/visual_identity.md).
  This blocks every prompt card in the line, because a prompt card inherits a style
  block from the line and there is nothing yet to inherit.
- **The language register is unconfirmed** — [languages/README.md](languages/README.md).
  This blocks typeface selection, which blocks all brand design
  ([brand/README.md](../../brand/README.md) §3).

None of these is a formality that can be discharged by writing it down. Each names a
person who has to agree to something.

## 3. What lives where

| Path | Holds | State |
|---|---|---|
| [line.yaml](line.yaml) | The control record: status, opening conditions, language register, visual identity pointers, seasons | **DESIGNED** |
| [research/](research/README.md) | Method for this line, and the registers: briefs, open questions, fact checks, interviews | empty |
| [sources/](sources/README.md) | Source records and claim records — the evidence base | empty |
| [sources/archive_landscape.md](sources/archive_landscape.md) | The survey template. Blocks opening. | **NOT STARTED** |
| [characters/](characters/README.md) | `CHR-NG-*` — people and collective actors | empty |
| [locations/](locations/README.md) | `LOC-NG-*` — places | empty |
| [timeline/](timeline/README.md) | `EVT-NG-*` — dated events | empty |
| [languages/](languages/README.md) | The on-screen language register and orthography decisions | candidate entries only |
| [languages/voice_policy.md](languages/voice_policy.md) | Narration voice policy for this line | **NOT STARTED** |
| [advisory/](advisory/README.md) | Advisors, standing, coverage, gaps, terms, rulings. Blocks opening. | **NOT STARTED** |
| [style/](style/README.md) | The line's own look | **NOT STARTED** |
| [style/motifs.md](style/motifs.md) | Recurring visual and narrative motifs, so they are deliberate | empty |
| [productions/](productions/README.md) | The productions | none exist |

What is **not** here, on purpose: evidence rules, narrative doctrine, sensitivity
procedure, and localisation policy are the
[pack's](../../../../packs/documentary-history/); provenance, rights, delivery, and the
gate framework are [core's](../../../../core/); schemas, naming, and the ID system are
[standards'](../../../../standards/). A line addendum that restates them creates a
second copy that will drift, and the copy nobody updates is the one nearest the work.

## 4. Precedence, for anything decided here

```
core  >  pack  >  studio bible  >  this line  >  a production
```

This line may **tighten** anything above it and may **never loosen** it. Where the
region's material needs a rule the pack does not have, the rule is written here and
says plainly what it constrains. Where it needs an exemption from a rule the pack
does have, there is no mechanism at this layer — amend the pack, with the pack's
signatures.

## 5. Creating a production

Not possible yet, and the toolkit is **NOT BUILT**
([docs/status.md](../../../../docs/status.md)). The specified command is:

```
python -m studio_ops new-production --line ng-nigeria
```

Naming and gate structure are in [productions/README.md](productions/README.md).
`studio_ops` refuses a greenlight while `line_status` is not `open` or any studio
decision is `unresolved` — both are currently true.
