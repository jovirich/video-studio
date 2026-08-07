# video-studio

A production platform for AI-assisted film and video.

It is not a show and it is not one studio. It is the engine — canon, standards,
schemas, prompt library, templates, and tooling — that any number of studios run on.

The first studio built on it is **[African History Studio](studios/african-history/)**,
whose first production line is **[Nigeria](studios/african-history/lines/ng-nigeria/)**.
Neither of those facts is baked into the platform.

> **This repository contains no historical claims.** It is infrastructure: schemas,
> templates, workflows, prompt scaffolding, review gates, and automation stubs.
> Every factual statement in a finished production must be entered by a researcher
> and traced to a source record before it can pass the gates.

---

## 1. The four tiers

```
PLATFORM        video-studio/
  the engine    core canon · canon packs · schemas · prompt library · templates
                automation · shared library · rights registers · ops framework
      │
      ▼
STUDIO          studios/african-history/
  the brand     declares a canon pack, adds its own bible and brand, owns its lines
      │
      ▼
LINE            studios/african-history/lines/ng-nigeria/
  the strand    a coherent body of work — a region, a series, a season strand.
                Owns its research, sources, entities, language, advisory, style.
      │
      ▼
PRODUCTION      .../productions/S01E01_slug/
  the unit      one episode, film, or short. Eleven pipeline stages, gated.
```

Each tier answers exactly one question:

| Tier | Question |
|---|---|
| Platform | How is any video made here, safely and traceably? |
| Studio | What kind of work is this, and by what editorial standard? |
| Line | What material does this strand cover, and who advises on it? |
| Production | What is this specific piece, and has it passed its gates? |

## 2. Canon packs — how the platform stays genre-neutral

[`core/`](core/) holds only what is true of **every** production: provenance, AI
disclosure, rights, delivery, accessibility, and the gate *framework*.

A **[canon pack](packs/)** supplies what core deliberately omits — evidence
standards, narrative doctrine, visual and sonic language, sensitivity procedure,
localisation, and the actual gate *set*. A studio declares one pack, and that
declaration determines what its productions are held to.

| | Historical documentary | Brand film | Narrative fiction |
|---|---|---|---|
| Claims need source records | **mandatory** | product claims only | no |
| Fact-check gate | **yes** | partial | no |
| Cultural advisory hold | **yes** | situational | situational |
| Client approval gate | no | **yes** | no |

Forcing a brand film through an evidence chain produces theatre, not rigour. Letting
a history documentary skip one produces something worse. The pack layer lets each be
correct without contaminating the other.

## 3. Spinning up new work

| You want to… | You run | It touches |
|---|---|---|
| Another Nigeria episode | `studio_ops new-production --line ng-nigeria` | that line **[NOT BUILT]** |
| Ghana, inside African History Studio | `studio_ops new-line --studio african-history --code gh-ghana` | that studio **[NOT BUILT]** |
| A different show, same genre | `studio_ops new-studio --code <x> --pack documentary-history` | `studios/` **[NOT BUILT]** |
| A different **kind** of video entirely | `studio_ops new-pack --code <genre>` then `new-studio --pack <genre>` | `packs/` + `studios/` **[NOT BUILT]** |

**Nothing on that table requires changing `core/`, `standards/`, `prompts/`,
`templates/`, or `automation/`.** That is the load-bearing claim of the architecture,
and it is tested in [ROADMAP.md](ROADMAP.md) Phase 6. If it ever fails, the finding
goes in [docs/architecture/evolution.md](docs/architecture/evolution.md).

## 4. Directory map

### Platform

| Path | What lives here |
|---|---|
| [core/](core/) | Canon binding on every production, whatever the genre |
| [packs/](packs/) | Genre canon packs. `documentary-history` is the first. |
| [standards/](standards/) | JSON schemas, ID system, naming, metadata, delivery specs |
| [prompts/](prompts/) | Prompt library — 8 modalities, ~40 vendors |
| [templates/](templates/) | Canonical skeletons: production, line, studio, records, legal |
| [automation/](automation/) | Python package `studio_ops` |
| [rights/](rights/) | Clearance log, model terms register, media provenance |
| [library/](library/) | Shared assets: LUTs, fonts, music beds, map bases, graphics kit |
| [ops/](ops/) | Roles, RACI, workflow states, checklists, risk register |
| [docs/](docs/) | Architecture, ADRs, runbooks, onboarding, glossary |

### Content

| Path | What lives here |
|---|---|
| [studios/](studios/) | The studios |
| [studios/african-history/](studios/african-history/) | Studio 01 — bible, brand, lines |
| [.../lines/ng-nigeria/](studios/african-history/lines/ng-nigeria/) | Line 01 — research, sources, entities, language, advisory, style, productions |

## 5. Quick start

```bash
python -m venv .venv
.venv\Scripts\activate                 # Windows
pip install -e ".[dev]"

python -m studio_ops validate --all    # what CI enforces. Works today.
python -m studio_ops status            # NOT BUILT — read docs/status.md instead
```

Exit codes: `0` clean · `1` findings · `2` a requested gate is NOT BUILT. `--all`
returns 2 today, on purpose: a green build that ran five of ten gates must not look
like a green build that ran ten.

`validate --all` never asks whether a claim is *true*. It asks whether a claim is
*sourced, cited, cleared, labelled, and signed*. Truth is a human's signature; the
machine only checks the signature exists and that nothing skipped a gate.

## 6. The pipeline

```
  BRIEF ──► RESEARCH ──► SOURCE LOCK ──► SCRIPT ──► FACT-CHECK ──► PICTURE LOCK
    │           │             │             │            │              │
    │           │             ▼             │            │              │
    │           │       every claim         │            │              │
    │           │       gets an ID          │            │              │
    │           ▼                           ▼            ▼              ▼
    │     open questions            prompt cards   sensitivity      asset
    │     register                  per shot       review           provenance
    │                                    │                          ledger
    ▼                                    ▼                             │
  greenlight                       GENERATION ──► EDIT ──► AUDIO POST ─┘
                                  (image/video/                │
                                   voice/music)                ▼
                                                        TECHNICAL QC ──► PUBLISH
```

The gate *framework* is [core/04](core/04_review_gate_framework.md); the gate *set*
comes from the pack — see [packs/documentary-history/gates.yaml](packs/documentary-history/gates.yaml).

## 7. Platform guarantees

Regardless of studio or genre, every production here:

1. **Is traceable** — every asset has a provenance record; nothing enters an edit without one.
2. **Is disclosed** — generated material is labelled, in-frame and in metadata.
3. **Is cleared** — nothing ships with a rights status of `pending`.
4. **Is gated** — a human signs each gate; no path exists from generation to publication without signatures.
5. **Is reproducible** — prompt cards, seeds, and parameters are recorded.
6. **Is accessible** — captions on every deliverable; contrast and legibility checked.

What the platform refuses is enumerated in
[core/01 §2](core/01_provenance_and_ai_disclosure.md). No pack may loosen it.

## 8. Contributing

[CONTRIBUTING.md](CONTRIBUTING.md), then
[docs/onboarding/first_week.md](docs/onboarding/first_week.md).
Terminology: [docs/glossary.md](docs/glossary.md).

## 9. Status — read this before trusting anything above

This repository is **DESIGNED**. Almost none of it is **IMPLEMENTED**, and *none* of
it is **TESTED**.

Those three words are used throughout this repository and mean different things:

| Label | Means |
|---|---|
| **DESIGNED** | The structure, schema, or standard exists on paper. No code runs. |
| **IMPLEMENTED** | Code exists and executes. Not proven at production scale. |
| **TESTED** | Exercised against a real workload, with a recorded result someone can review. |

A bare ✅ is banned here — it reads as *working* when it usually means *specified*.

Concretely, right now:

- `studio_ops validate` is **IMPLEMENTED** for four gates — schemas, naming, links,
  root hygiene — with a passing test suite. On its first run against this repository
  it found 130 broken internal links.
- Every **other** `studio_ops` command shown in this README is **NOT BUILT**. They
  exit non-zero and name what they are blocked on rather than passing silently. The
  commands are a specification, not a working CLI.
- The schemas are **DESIGNED** and have never been validated against a real record,
  because no real records exist.
- The vendor cheat sheets are **DESIGNED** from general knowledge and have **not been
  verified against current vendor documentation**.
- No production has been greenlit. No gate has ever been signed. No historical
  content exists anywhere in the repository.

The full, honest, per-capability account is **[docs/status.md](docs/status.md)**.
[ROADMAP.md](ROADMAP.md) has the phase gates and what would move a capability from
DESIGNED to TESTED.
