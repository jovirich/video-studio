---
title: Capability status ledger
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner]
---

# Capability status ledger

The honest account of what this repository actually does, as opposed to what it
specifies.

## The three words

They are not degrees of the same thing. They are different claims.

| Label | Means | Evidence required |
|---|---|---|
| **DESIGNED** | The structure, schema, contract, or standard exists on paper. No code runs. A human could follow it manually. | The document or schema exists and is internally consistent |
| **IMPLEMENTED** | Code exists and executes. Behaviour matches the design on the paths that were exercised during development. | The command runs and produces output |
| **TESTED** | Exercised against a real workload, with a recorded result someone else can review. Failure modes observed, not assumed. | A test run, a report, a dated artefact |

A bare ✅ or "complete" is banned in this repository. It reads as *working* when it
usually means *specified*, and that gap is how a plan gets mistaken for a product.

### The gap that matters most

**IMPLEMENTED → TESTED** is where most of the risk lives. A validator that runs
cleanly on an empty repository has proved almost nothing; the same validator against
400 real records with three deliberate violations has proved something.

Every `IMPLEMENTED` row below should be read as *"we believe this works"*, not
*"this works"*.

## Platform status

### Architecture and canon

| Capability | Status | Notes |
|---|---|---|
| Four-tier model (platform / studio / line / production) | **DESIGNED** | `arch-2`. Not exercised — one studio, no productions. |
| Core canon — 6 documents | **DESIGNED** | Written; **not ratified**. No signatures. |
| Canon pack system | **DESIGNED** | 4 packs authored. None used to produce anything. |
| Precedence rule (core > pack > studio > line) | **DESIGNED** | No conflict has yet arisen to test it. |
| Gate framework | **DESIGNED** | No gate has ever been signed. |
| Gate sets declared as data (`gates.yaml`) | **DESIGNED** | Not yet read by any code. |

### Standards

| Capability | Status | Notes |
|---|---|---|
| 17 JSON schemas | **DESIGNED** | Valid JSON Schema; all parse and cross-`$ref` resolves. **Never validated against a real record** — no real records exist. The five late additions (`open_question`, `fact_check`, `advisory_ruling`, `correction`, `style_anchor`) closed a hole where records of those types passed validation by being invisible to the router. |
| Identifier system | **DESIGNED** | No IDs allocated. Collision behaviour untested. |
| Naming conventions | **DESIGNED** | |
| Delivery specs | **DESIGNED** | No master has been produced against them. |
| Prohibited-language list | **DESIGNED** | `prohibited_patterns.json` **not yet generated** from the source document. |
| Data-graphics standard | **DESIGNED** | |

### Canon packs, ops, rights, templates

| Capability | Status | Notes |
|---|---|---|
| 4 canon packs, 26 canon documents | **DESIGNED** | None has produced anything. |
| 17 gate checklists in `ops/checklists/` | **DESIGNED** | No checklist has ever been completed or signed. |
| Roles, RACI, workflow states, risk register, budget template | **DESIGNED** | |
| Clearance log, takedown log, chain-of-title template | **DESIGNED** | Empty registers with template rows. |
| Model terms register — 49 vendor rows | **DESIGNED** | Every cell reads `TBD — not yet checked`, **including the terms URL**. Asserting an unopened URL is the same error as asserting the terms. |
| Production / line / studio skeletons, 11 record templates, 6 legal instruments | **DESIGNED** | Legal instruments are starting points requiring a qualified lawyer; they are not legal advice. |
| Shared library structure | **DESIGNED** | All eight folders empty. |

### Prompt library

| Capability | Status | Notes |
|---|---|---|
| Prompt-card architecture | **DESIGNED** | |
| Prompt-card schema | **DESIGNED** | Never validated against a real card. |
| 8 modality guides | **DESIGNED** | |
| ~49 vendor cheat sheets | **DESIGNED** | Written from general knowledge. **Not verified against current vendor documentation.** Treat parameter details as indicative until a human checks each one. |
| 5 chain recipes | **DESIGNED** | No chain has been run. |
| Prompt-card generator (`new-prompt`) | **NOT BUILT** | |
| Prompt renderer (card → vendor string) | **NOT BUILT** | The main practical payoff of the card structure. Unproven. |
| Style inheritance | **DESIGNED** | Mechanism specified; nothing resolves it yet. |
| 20-shot continuity test | **NOT RUN** | The test that would show whether the continuity toolkit works at all. |

### Automation (`studio_ops`)

| Capability | Status | Evidence |
|---|---|---|
| CLI skeleton | **IMPLEMENTED** | `python -m studio_ops --help` runs |
| `validate --root-hygiene` | **IMPLEMENTED** | Runs against the real tree; PASS, 28 entries |
| `validate --naming` | **IMPLEMENTED** | Runs against the real tree; PASS, 177 files |
| `validate --links` | **IMPLEMENTED** | Runs against the real tree; **found 130 real broken links on first run** |
| `validate --schemas` | **IMPLEMENTED** | Runs; routes YAML and front matter to `standards/schemas/` |
| Test suite for the above | **IMPLEMENTED** | 20 tests, fixture trees with deliberate violations, all passing |
| `validate --sources` | **NOT BUILT** | Reports its own absence and exits 2 |
| `validate --canon` | **NOT BUILT** | Blocked on `prohibited_patterns.json` |
| `validate --prompts` / `--packs` / `--delivery` | **NOT BUILT** | |
| `new-studio` / `new-line` / `new-production` / `new-pack` / `new-record` | **NOT BUILT** | Exit 2 with the blocking reason |
| `report` family | **NOT BUILT** | |
| `promptlib render` / `run` | **NOT BUILT** | |
| Manifest / provenance ledger | **DESIGNED** | Schema exists. No code writes to it. |
| Conform step (refuses untracked files) | **NOT BUILT** | This is the mechanism behind the traceability guarantee. It does not exist yet. |
| Generation adapters | **DESIGNED** | Deliberate stubs. `Adapter.generate` enforces dry-run and budget before any subclass runs, so no adapter can bypass the ceiling by forgetting to check. |
| Asset store | **NOT BUILT** | No round trip has been proved. |

**Why none of these is TESTED.** The validators run and their unit tests pass against
fixture trees. That is IMPLEMENTED. TESTED would mean running them against a real
production's worth of records — several hundred, with known violations planted — and
recording the result. No such corpus exists, because no production exists.

The `--links` gate is the closest to earning it: on its first run against the real
repository it found 130 broken links, all genuine. That is evidence it works on real
input, but it is one gate against one repository state.

### CI and process

| Capability | Status | Notes |
|---|---|---|
| CI workflow | **IMPLEMENTED** | Runs the four implemented gates as blocking, plus lint, types, and tests. `--all` runs non-blocking so the NOT BUILT gap is visible in every run rather than hidden by a green build. |
| Issue and PR templates | **IMPLEMENTED** | These are declarative; they work as written. |
| VS Code workspace, tasks, launch | **IMPLEMENTED** | Tasks invoke commands that do not exist yet. |
| Git repository and remote | **IMPLEMENTED** | Pushed to `jovirich/video-studio`. |

## Studio status — African History Studio

| Capability | Status | Notes |
|---|---|---|
| Studio record | **DESIGNED** | 11 decisions unresolved. Cannot greenlight. |
| Charter | **DESIGNED** | Mission, audience, success conditions all `TBD`. |
| Nigeria line registered | **DESIGNED** | `line_status: candidate`. All three opening conditions false. |
| Advisory board | **NOT STARTED** | Blocks line opening. |
| Archive landscape survey | **NOT STARTED** | Blocks line opening. |
| Visual identity | **NOT STARTED** | Blocks brand design and every prompt card. |
| Any historical content | **NONE, DELIBERATELY** | No claims, sources, entities, or scripts exist. |

## What "TESTED" would require

Nothing in this repository is TESTED. The first things that could be:

| Test | What it would prove |
|---|---|
| Validators run against 100+ deliberately-flawed records | The gates catch what they claim to |
| 20-shot continuity test | Whether style anchors and character references actually hold across a sequence |
| Asset store round trip: ingest → manifest → conform → package | The provenance chain is real, not documented |
| One 3-minute dry-run production through all nine gates | The process is workable by actual humans under time |
| M&E stem produced and used for a test dub | The localisation path exists |
| 16:9 master cropping cleanly to 9:16 | Cutdowns are crops, as designed |
| A second pack producing one finished piece | The platform abstraction holds |

These are [ROADMAP](../ROADMAP.md) Phase 3, and Phase 3 exists precisely so these
failures are found on work nobody will see.

## Maintaining this ledger

- Update in the **same commit** that changes a capability's maturity. A status change
  is not a separate chore.
- Never promote a row without naming the evidence.
- `NOT BUILT` is an honest, useful state. Delete nothing; downgrade when something
  breaks.
- When reporting progress to anyone — in a commit, a README, or a conversation — use
  these three words rather than "built", "done", or "finished".
