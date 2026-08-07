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

## This file is authoritative

**Every per-capability maturity verdict in this repository lives here and nowhere
else.** Where any other document disagrees with this one about whether something
works, this one is right and the other is stale.

| Document | Answers | Authority over |
|---|---|---|
| [ROADMAP.md](../ROADMAP.md) | *Where are we going?* | Sequence, phases, exit criteria |
| **status.md** (here) | *What actually works today?* | **Maturity verdicts** |
| [architecture/](architecture/) | *Why is it built this way?* | Structure, decisions, reversals |

Other documents may *name* a capability and *link* here. They must not restate its
maturity, because duplicated state drifts.

### Why this is enforced rather than requested

It already failed. `ROADMAP.md` carried `studio_ops toolkit — NOT BUILT` and `CI will
fail on first run` for several commits after both were implemented and passing.

That is not cosmetic. With more than one agent working the repository, a stale verdict
is worse than a missing one: it invites someone to "fix" what is already done, or to
rebuild what already exists, and the second agent has no way to tell which document is
current.

`studio_ops validate --reality` now fails the build when a document marks NOT BUILT
next to a command that is implemented. The drift that happened cannot recur silently.

### Updating

A maturity change lands **in the same commit** as the code that caused it. Promotion
names its evidence. `NOT BUILT` is a legitimate, useful state — downgrade freely when
something breaks, and delete nothing.

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
| Prompt renderer (card → vendor string) | **IMPLEMENTED** | Generic + Midjourney. The same card rendering differently per vendor is asserted, so the payoff is no longer merely claimed. |
| Style inheritance | **IMPLEMENTED** | `resolve` applies block → card → overrides; list fields merge; an override without a reason raises. Exercised by the round trip from a real continuity record. |
| 20-shot continuity test | **NOT RUN** | Still the open question. The round trip proves continuity *reaches* the prompt; only twenty shots show whether it *holds*. |

### Automation (`studio_ops`)

| Capability | Status | Evidence |
|---|---|---|
| CLI skeleton | **IMPLEMENTED** | `python -m studio_ops --help` runs |
| `validate --root-hygiene` | **IMPLEMENTED** | Runs against the real tree; PASS, 28 entries |
| `validate --naming` | **IMPLEMENTED** | Runs against the real tree; PASS, 177 files |
| `validate --links` | **IMPLEMENTED** | Runs against the real tree; **found 130 real broken links on first run** |
| `validate --schemas` | **IMPLEMENTED** | Runs; routes YAML and front matter to `standards/schemas/` |
| `validate --reality` | **IMPLEMENTED** | Enforces this document's own discipline: prose naming an unimplemented command must say so. **Found 63 violations on its first run.** |
| Test suite | **IMPLEMENTED** | 220 tests across validators, scaffold, promptlib, manifest, adapters, execution modes, and both round trips. Fixture trees carry deliberate violations. |
| `new-record` — ID allocator | **IMPLEMENTED** | 47 tests. Refuses on any duplicate in the namespace being allocated. Smoke-run against all 14 real templates. |
| `check-ids` — repo-wide duplicate audit | **IMPLEMENTED** | Returns clean on the current repository |
| `promptlib render` | **IMPLEMENTED** | 63 tests. Generic + Midjourney renderers; the same card renders differently per vendor, asserted. |
| `promptlib override_rate` | **IMPLEMENTED** | The ADR 0003 falsification signal is now computable |
| Asset store (`local` driver) | **IMPLEMENTED** | Hashes bytes as written, refuses to overwrite, refuses a store path inside the git tree |
| Manifest — the provenance ledger | **IMPLEMENTED** | 31 tests. `ingest_generation` is the only path joining bytes to a record. |
| Execution modes (`local` / `interactive` / `api`) | **IMPLEMENTED** | 16 tests. Declared per backend on `Capabilities.execution_mode`; conservative default is `api`. Behind the existing adapter interface — no new tier. |
| `generation_job` v2 — full handoff packet | **IMPLEMENTED and TESTED** | Production/scene/shot IDs, modality, creative purpose, continuity records, character and style references, evidence constraints, prompt, negatives, hard stops, framing, lens, lighting, performance, aspect, resolution, duration, seed, preferred vendor/model, output filename, incoming folder, acceptance checklist — plus an image-to-video block. Demonstrated on EXP-001. |
| `prepare-job` / `fulfil-job` | **IMPLEMENTED and TESTED** | The manual fulfilment loop. `fulfil-job` is aliased as `ingest`; every mode converges on it. |
| Operator brief (copy-ready) | **IMPLEMENTED** | Prompt in one unbroken block; references before prompt; authorisation banner first. |
| Run-plan phase control | **IMPLEMENTED and TESTED** | Refuses jobs outside the active phase and **never consults the budget** while doing so. |
| `generation_job` v1 | **SUPERSEDED** | A derived work order, **not a record**: no ID, no schema, regenerable, nothing cites it. Assembled from prompt card + continuity + shot. Carries forbidden list, hard stops, and acceptance checklist so an operator never reconstructs constraints from four files. |
| `InteractiveAdapter` (two-phase) | **IMPLEMENTED** | `generate()` runs every guard then raises `AwaitingFulfilmentError` — it never fabricates a result for work that has not happened. `fulfil()` hashes the delivered bytes; the hash is never taken on report. |
| `studio_ops modes`, `prepare-job` | **IMPLEMENTED** | `prepare-job` verified against the real EXP-001 records: 5 constraints, 22 forbidden terms, 5 hard stops correctly separated. |
| `studio_ops ingest` | **IMPLEMENTED and TESTED** | Closes the interactive round trip. Reads destination, provenance class, and manifest from the *job*, so a fulfilment cannot be told something different from what was specified. Hashes the delivered bytes twice — at fulfilment, and again inside `ingest_generation`, which refuses if they disagree. |
| Vendor (`api`) adapter | **NOT BUILT — deliberately** | Not until a vendor is chosen, its terms verified, and a ceiling set. |
| `local` generation adapter | **IMPLEMENTED** | 26 tests. Deterministic, offline, free, real PNG. Same seed + prompt → identical bytes. |
| **The round trip** | **IMPLEMENTED and TESTED** | See below — the first thing in this repository to reach TESTED |
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

### Both round trips — the only TESTED capabilities

**One-phase** (`local`, and the shape any `api` backend will take):
`continuity + shot → card → render → adapter → asset → manifest`.

**Two-phase** (`interactive`): `prepare → job → (operator, out of band) → fulfil →
manifest`. Verified against the real EXP-001 records, with the `local` backend
standing in for the operator — it is the only backend that can produce a real file
offline, which is why it exists.

What the two-phase test proves is not that an operator behaves. It is that an
operator does not have to: the pipeline hashes what it is handed, records what it
verified, and marks what it merely received as unverifiable.

### The one-phase round trip in detail

`automation/tests/test_roundtrip.py`, 11 tests, all passing:

```
continuity record + shot record
    → prompt card
    → render                 (offline, no spend)
    → local adapter          (guarded by dry-run and a cost ceiling)
    → PNG on disk            (654 KB, valid signature)
    → manifest entry         (sha256 matches the bytes)
```

What is asserted, not merely hoped:

| Assertion | Why it matters |
|---|---|
| The manifest sha256 equals the hash of the file on disk | This *is* the traceability guarantee |
| The manifest on disk validates against its schema afterwards | A round trip must not leave the ledger invalid |
| The continuity record's lighting reaches the prompt, and its `forbidden_objects` become negatives | Otherwise the continuity registry is decoration |
| Same seed + same prompt → identical bytes | Determinism is what makes any of this assertable |
| A `reconstruction` shot with no evidence basis **refuses** | This is what keeps a no-claims laboratory production honest |
| A generated asset can never be `archival` | The prohibition that matters most, enforced in code as well as schema |
| **When a record is refused, no bytes land in the store** | The ordering property behind "no asset without a manifest entry" |
| The budget guard still refuses a priced run with no ceiling | A free backend did not widen the guard for paid ones |

This is a *mechanics* result. It says nothing about output quality, about continuity
holding across twenty shots, or about the claim chain. Those are EXP-001's job.

**Why none of the rest is TESTED.** The validators run and their unit tests pass against
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

### Continuity registry

| Capability | Status | Notes |
|---|---|---|
| `continuity_character` / `continuity_location` schemas | **DESIGNED** | Kept separate from the `CHR-*` / `LOC-*` evidence records on purpose — see `standards/id_system.md`. |
| Templates for both | **DESIGNED** | |
| Line registry folder | **DESIGNED** | Empty. No continuity record exists. |
| Drift test methodology | **DESIGNED, NEVER RUN** | The schema requires a drift test before a record can lock. Nothing has ever been drift-tested, so the central claim — that these mechanisms hold across twenty shots — is entirely unverified. |

### EXP-001, the laboratory production

| Capability | Status | Notes |
|---|---|---|
| `kind: laboratory`, `EXP<NNN>` codes, `findings` block | **DESIGNED** | Schema extended; the production record validates. |
| EXP-001 scaffold | **DESIGNED** | Folder, brief, research README, shot plan, findings template. |
| Subject | **NOT CHOSEN** | Human decision. |
| Claims | **NONE** | Human research. Nothing in this repository may author them. |
| Everything downstream | **NOT STARTED** | Blocked on the line being `candidate`, no Research Lead, no advisory contact, no archive survey, no visual identity, `new-record` NOT BUILT, no adapter. |

## Known gaps found while implementing

Real defects surfaced by writing the code against the schemas. Recorded here rather
than fixed immediately: the architecture freeze is in force and none of these blocks
the first generated shot. Each is a candidate for the post-EXP-001 pass.

| # | Gap | Where | Why deferred |
|---|---|---|---|
| G1 | **`raw_override` carries no machine-checkable justification.** ADR 0003 and the card template both say it "requires a reason in `notes`" — the schema enforces nothing. Ordinary `inheritance.overrides` entries *do* require a reason. So the one deviation most in need of justification is the only one without it. | `prompt_card.schema.json` | One-line `allOf`. Tightens an existing documented rule rather than adding a concept, so it is freeze-compatible — but it may invalidate the shipped template, and that check is not worth doing before Shot 001. |
| G2 | **`inheritance.overrides[].value` is `type: string` only.** An override can never target a list field (`negative`, `period_markers`) or a numeric parameter without stringifying it. `parameters.stylize` overrides land as `"50"`, not `50`. | `prompt_card.schema.json` | Renderable but lossy. No effect on the round trip. |
| G3 | **Schema validation alone does not catch an unfilled template.** Every placeholder is a free-form string, so a card of pure `TBD` is schema-valid. | `prompt_card.schema.json` | Correct division of labour — placeholder detection belongs to the unbuilt `--prompts` gate, not to the schema. Pinned by a test so it cannot be forgotten. |
| G4 | **`inheritance.style_block` is a string with no schema behind it.** "Path or ID of the inherited style block", but no `style_block.schema.json` exists, so `resolve` cannot follow the reference — it takes the resolved mapping as an argument. | `prompt_card.schema.json` | Whoever wires the CLI decides how a `style_block` string becomes a mapping. EXP-001 supplies one directly. |
| G5 | ~~`asset_manifest.episode` rejected `EXP` codes~~ | `asset_manifest.schema.json` | **Fixed.** Every ID in the file already admitted `EXP\d{3}`; the production code did not, so a manifest whose every entry was valid would still be refused. |

| G6 | **`TBD` is illegal in typed and pattern-constrained fields, and nothing says so.** `metadata_spec.md` presents `TBD` as the repo-wide convention for an unresolved value, but `facial_reference` wants an `STA-*` id, `drift_test.shots_tested` an integer, `held` a boolean. Writing `TBD` there fails validation. | `metadata_spec.md`, all record schemas | **Correct resolution needs no schema change:** for an optional typed field, "not yet decided" is *absence*. The convention doc should say that. Found by writing the first real records. |
| G7 | **A location has one lighting state and no way to record variants.** The EXP-001 shot plan deliberately varies light — backlit, overhead, low key, exterior — to stress identity. `lighting_language` holds a single setup, so the variants live in the record body as prose a validator cannot check. | `continuity_location.schema.json` | Prose works for one production. If varying light per shot turns out to be routine, this needs a field. |
| G8 | **No field for facial hair; `jewellery_and_adornment` is narrower than "accessories".** Facial hair goes under `appearance.hair` by convention only. A working cord at the wrist is neither jewellery nor adornment. | `continuity_character.schema.json` | Both are naming problems, not gaps. Cheap to fix, no urgency. |
| G9 | **`historical_uncertainty` assumes a historical subject.** For an invented character it is not empty-because-unknown, it is inapplicable — there is no fact of the matter. An empty array cannot distinguish "nothing uncertain" from "nothing to be uncertain about". | `continuity_character.schema.json` | Only bites for laboratory productions. Recorded in the records' prose meanwhile. |

| G10 | **`*.prompt.yaml` collides with an editor-recognised format.** VS Code applies a built-in association for that extension (chat-prompt files, which require a `messages` key), so every prompt card showed a phantom `Missing property "messages"` error despite validating cleanly against the repo's own schema. | naming convention, `.vscode/settings.json` | Worked around with a `# yaml-language-server: $schema=` modeline on each card and on the template — no schema or convention change. The alternative, renaming the extension, is a `standards/naming_conventions.md` change and not worth it under the freeze. |

G1 is the one worth doing first after EXP-001. **G6 is the one that will bite everyone
else**, because it makes a documented convention fail validation with no explanation.

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
