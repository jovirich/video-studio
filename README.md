# African History Studio

A production repository for cinematic, AI-assisted historical documentary.
Nigeria is the first production line. The architecture assumes there will be more.

> **This repository contains no historical claims.** It is infrastructure: schemas,
> templates, workflows, prompt scaffolding, review gates, and automation stubs.
> Every factual statement in a finished episode must be entered by a researcher and
> traced to a source record before it can pass the review gates defined in
> [bible/02_evidence_and_sourcing.md](bible/02_evidence_and_sourcing.md).

---

## 1. What this repo is

A documentary made with generative tools has a specific failure mode: the imagery is
cheap and the truth is expensive. Left unmanaged, output volume outruns verification
and the show quietly becomes fiction with a serious voiceover.

This repo is built to make that failure mode *structurally hard*:

- **Nothing is canon until it has a source record.** Claims live in
  [sources/](sources/), not in scripts. A script references a claim ID; it does not
  assert facts on its own authority.
- **Nothing generated is untraceable.** Every generated frame, clip, and voice line
  carries a provenance record produced by the prompt card that made it.
- **Nothing ships without passing gates.** Fact-check, sensitivity, rights, and
  technical QC are separate signatures with separate owners.

## 2. The studio / line / episode model

```
Studio level   ── canon, standards, prompt library, automation, templates
   │              (shared by every country line, forever)
   ▼
Production line ── productions/ng-nigeria/   ← the first line
   │              (country-specific research, characters, locations, language,
   │               advisory board, visual identity)
   ▼
Episode        ── productions/ng-nigeria/episodes/S01E01_.../
                  (one self-contained unit: brief → research → script →
                   storyboard → prompts → assets → edit → review → delivery)
```

Adding a second line is a single command and touches nothing that exists:

```bash
python -m studio_ops new-line --code gh-ghana --name "Ghana"
```

Studio-level assets (prompt library, schemas, review gates, LUTs, automation) apply
to every line automatically. This is the whole reason for the split — see
[docs/architecture/adr_index.md](docs/architecture/adr_index.md) and
[docs/decisions/0001-studio-not-show.md](docs/decisions/0001-studio-not-show.md).

## 3. Directory map

| Path | What lives here | Read first |
|---|---|---|
| [bible/](bible/) | The Production Bible — editorial constitution. Binding on all lines. | [bible/README.md](bible/README.md) |
| [standards/](standards/) | Machine-checkable rules: JSON schemas, naming, metadata, delivery specs. | [standards/README.md](standards/README.md) |
| [research/](research/) | Studio-wide research method: protocols, briefs, open questions, fact-check reports. | [research/README.md](research/README.md) |
| [sources/](sources/) | The source of truth. Source records, archive directory, permissions, citations, media provenance. | [sources/README.md](sources/README.md) |
| [prompts/](prompts/) | Prompt library for every major AI tool, organised by modality then vendor. | [prompts/README.md](prompts/README.md) |
| [templates/](templates/) | Canonical skeletons: episode, production line, record types, legal letters. | [templates/README.md](templates/README.md) |
| [productions/](productions/) | The production lines. `ng-nigeria/` is line one. | [productions/README.md](productions/README.md) |
| [automation/](automation/) | Python package `studio_ops` — scaffolding, validation, reporting, pipeline stubs. | [automation/README.md](automation/README.md) |
| [library/](library/) | Shared binary-adjacent assets: LUTs, fonts, music beds, map bases, graphics kit. | [library/README.md](library/README.md) |
| [brand/](brand/) | Channel identity, title cards, thumbnail system, naming. | [brand/README.md](brand/README.md) |
| [ops/](ops/) | Running the studio: roles, RACI, workflow states, checklists, risk register. | [ops/README.md](ops/README.md) |
| [docs/](docs/) | Engineering + process documentation, ADRs, runbooks, onboarding, training. | [docs/README.md](docs/README.md) |

## 4. Quick start

```bash
# 1. Environment
python -m venv .venv
.venv\Scripts\activate            # Windows
pip install -e ".[dev]"

# 2. Confirm the repo is internally consistent
python -m studio_ops validate --all

# 3. Scaffold the first episode (creates the folder; writes no facts)
python -m studio_ops new-episode --line ng-nigeria --season 1 --number 1 --slug working-title

# 4. See where everything stands
python -m studio_ops status --line ng-nigeria
```

`validate --all` is the gate that CI enforces. It never asks whether a claim is
*true* — it asks whether a claim is *sourced, cited, cleared, and reviewed*.
Truth is a human's signature; the machine only checks that the signature exists.

## 5. The pipeline in one picture

```
  BRIEF ──► RESEARCH ──► SOURCE LOCK ──► SCRIPT ──► FACT-CHECK ──► PICTURE LOCK
    │            │            │             │            │              │
    │            │            ▼             │            │              │
    │            │      every claim         │            │              │
    │            │      gets an ID          │            │              │
    │            ▼                          ▼            ▼              ▼
    │      open questions            prompt cards    sensitivity     asset
    │      register                  per shot        review          provenance
    │                                     │                          ledger
    ▼                                     ▼                             │
  greenlight                        GENERATION ──► EDIT ──► AUDIO POST ─┘
  checklist                        (image/video/                │
                                    voice/music)                ▼
                                                          DELIVERY QC ──► PUBLISH
```

Gate definitions live in [ops/workflow_states.md](ops/workflow_states.md).
Checklists for each gate are in [ops/checklists/](ops/checklists/).

## 6. Ground rules that are not negotiable

1. **No fact enters a script without a source record ID.** See
   [bible/02_evidence_and_sourcing.md](bible/02_evidence_and_sourcing.md).
2. **AI-generated imagery is never presented as archival.** It is labelled in-frame
   and in metadata. See [bible/06_ai_disclosure_and_ethics.md](bible/06_ai_disclosure_and_ethics.md).
3. **Real people, living or recently dead, are not synthesised into speech or
   performance without documented consent or estate clearance.** See
   [bible/07_cultural_sensitivity.md](bible/07_cultural_sensitivity.md).
4. **Sacred, restricted, and funerary material is out of bounds without an advisory
   ruling.** See [productions/ng-nigeria/advisory/README.md](productions/ng-nigeria/advisory/README.md).
5. **Uncertainty is spoken aloud, not smoothed over.** The narration register for
   contested history is defined in [bible/03_narrative_doctrine.md](bible/03_narrative_doctrine.md).

## 7. Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), then
[docs/onboarding/first_week.md](docs/onboarding/first_week.md). Branch naming, PR
gates, and review ownership are defined there and enforced in
[.github/workflows/validate.yml](.github/workflows/validate.yml).

## 8. Status

Pre-production. No episode has been greenlit. See
[docs/architecture/refinements_before_episode_one.md](docs/architecture/refinements_before_episode_one.md)
for the open architectural decisions that should be closed before S01E01 starts.
