# Roadmap

**Where we are going, and in what order.** This is a *sequencing* document: it says
what must be true before the next thing starts.

Dates are deliberately absent. Phases advance on **exit criteria**, not calendars.

## This document does not record what works

That belongs in exactly one place. Three documents, three jobs, no overlap:

| Document | Answers | Authority over |
|---|---|---|
| **ROADMAP.md** (here) | *Where are we going?* | Sequence, phases, exit criteria |
| **[docs/status.md](docs/status.md)** | *What actually works today?* | **Every per-capability maturity verdict** |
| **[docs/architecture/](docs/architecture/)** | *Why is it built this way?* | Structure, decisions, and their reversals |

**`docs/status.md` is authoritative.** Where this roadmap and the status ledger
disagree about whether something works, the ledger is right and this file is stale.

This separation exists because it already failed once. This roadmap carried
`studio_ops toolkit — NOT BUILT` and `CI will fail on first run` for several commits
after both were implemented and passing. Duplicated state drifts; with more than one
agent working the repository, a stale verdict is worse than a missing one, because it
invites someone to "fix" what is already done or to rebuild what already exists.

The `reality` gate now fails the build when a document contradicts the ledger in
either direction — claiming a command works when it does not, or claiming it does not
when it does. This specific drift cannot recur silently.

## Maturity vocabulary

Defined here because the roadmap uses the words; the *verdicts* live in the ledger.
A bare ✅ is prohibited — it reads as *working* when it usually means *specified*.

| Label | Means | Evidence required |
|---|---|---|
| **DESIGNED** | Structure, schema, or standard exists on paper. No code runs. | The document exists and is internally consistent |
| **IMPLEMENTED** | Code exists and executes. Not proven at production scale. | The command runs |
| **TESTED** | Exercised against a real workload, with a recorded, reviewable result. | A test run, a report, a dated artefact |
| **NOT BUILT** | Specified, no code. An honest and useful state. | — |

**Nothing in this repository is currently TESTED.** That single verdict is stated
here because it governs the sequence of every phase below. Per-capability detail is
[the ledger's](docs/status.md) job, not this file's.

---

## Phase 0 — Architecture designed, toolkit begun

The repository you are reading.

The architecture is specified and internally consistent. Some of the toolkit runs.
**None of it has been exercised against a real production**, which is what Phases 3
and 3.5 exist to change.

For what runs today and what does not, read
**[docs/status.md](docs/status.md)** — this phase deliberately does not restate it.

**Exit criterion: met for design.** No claim beyond that should be read into this
phase. Design being finished is not the same as anything working, and the gap between
those two is the entire remaining roadmap.

---

## Phase 1 — Ratification ⬜

Turning a scaffold into a studio. Nothing generates until this closes.

| Item | Owner | Status |
|---|---|---|
| Fill `bible/00` §1 mission, §3 audience, §8 success conditions | Showrunner | ⬜ |
| Decide AI-generated music policy — `bible/05` §4 | Showrunner + Cultural Advisor | ⬜ |
| Decide production language and orthography standards — `bible/09` §1–2 | Showrunner + Cultural Advisor | ⬜ |
| Decide target runtime and platform set — `bible/10` §1 | Showrunner | ⬜ |
| Decide audio description scope — `bible/05` §8 | Audio Lead | ⬜ |
| Decide licensing posture — see `docs/decisions/0009-licensing-posture.md` | Showrunner | ⬜ |
| Sign the Bible; record in `bible/12` | Showrunner + Cultural Advisor | ⬜ |

**Exit criterion:** `bible/12_amendment_log.md` carries a ratification entry with
two signatures and no open blocking items.

---

## Phase 2 — Opening the Nigeria line ⬜

The three conditions in `bible/00` §2, made concrete. `productions/ng-nigeria/line.yaml`
cannot move from `candidate` to `open` until all three are `true`.

| Item | Status |
|---|---|
| Name and engage a Research Lead with Nigerian historiographical competence | ⬜ |
| Recruit and contract advisory board; populate `advisory/register.md` | ⬜ |
| Survey the archive landscape; write `sources/archive_landscape.md` | ⬜ |
| Define line visual identity: palette, lens set, grade, show LUT | ⬜ |
| Define voice policy and cast narration | ⬜ |
| Build language style guides for each on-screen language | ⬜ |
| Select typefaces with full diacritic coverage — blocks all brand design | ⬜ |
| Set `line_status: open` | ⬜ |

**Exit criterion:** `studio_ops validate --schemas` passes with `line_status: open`,
which the schema only permits when all opening conditions are met.

---

## ARCHITECTURE FREEZE — in effect

**No new tiers, packs, or canon documents until EXP-001 reports.**

Every architectural claim in this repository is DESIGNED. Nothing is TESTED. Adding
more structure now increases untested design without increasing confidence in any of
it. Recorded as [AE-007](docs/architecture/evolution.md).

The freeze covers **structure**, not tooling. Building the scaffolders and adapters
is what the freeze exists to make room for.

| Frozen | Not frozen |
|---|---|
| New tiers | `studio_ops` scaffolders |
| New canon packs | Generation adapters |
| New canon documents | Validators |
| New record types | Bug fixes |
| Expanding existing canon | Reconciling docs with implementation |

Lifts when EXP-001's findings report lands. Findings may well *require* structural
change — that is the point, and a change driven by a finding is not a freeze breach.

---

## Phase 3 — Pipeline hardening ⬜

Do this *before* episode one, not during it. Every item here is something that is
cheap now and expensive under deadline.

| Item | Status |
|---|---|
| Implement the validators that are currently stubs (`validate/*.py`) | ⬜ |
| Implement `scaffold/new_episode.py` end to end | ⬜ |
| Stand up the asset store and prove round-trip ingest → manifest → conform | ⬜ |
| Wire **one** image adapter and **one** video adapter behind the cost ceiling | ⬜ |
| Build the style-anchor set and prove continuity across 20 test shots | ⬜ |
| Prove the M&E stem workflow on a 60-second test piece | ⬜ |
| Prove the vertical-crop workflow — a 16:9 shot cropping cleanly to 9:16 | ⬜ |
| Run a full dry-run episode: 3 minutes, all gates, no real subject | ⬜ |

**Exit criterion:** the dry-run piece passes all nine gates and delivers a complete
package per `standards/delivery_specs.md`. Find the pipeline's failures on a piece
nobody will see.

---

## Phase 3.5 — EXP-001, the laboratory production ⬜

[`studios/african-history/lines/ng-nigeria/productions/EXP001_laboratory-scene/`](studios/african-history/lines/ng-nigeria/productions/EXP001_laboratory-scene/)

Not an episode. Never published. ~20 shots, one location, one or two characters,
8–12 researched claims, run **at production pace**. The deliverable is the findings
report.

| Item | Status |
|---|---|
| Subject chosen, satisfying the constraints in the production README | ⬜ |
| 8–12 claims researched against real sources, by a human | ⬜ |
| One location continuity record, with `forbidden_objects` populated | ⬜ |
| One or two character continuity records | ⬜ |
| Anchors generated and checksummed | ⬜ |
| **Drift test run and recorded** — before the other nineteen shots | ⬜ |
| ~20 shot records and prompt cards | ⬜ |
| Generation, with every run recorded including rejections | ⬜ |
| Conform, edit, M&E stem | ⬜ |
| All nine gates attempted, shortfalls recorded as breakages | ⬜ |
| Findings report complete, seven questions answered | ⬜ |

**Exit criterion:** the findings report answers all seven questions with evidence,
and the actions arising are triaged. **A short findings list is a failed experiment**,
not a successful production — it means the piece was made too carefully to be
informative.

Prerequisites, all currently unmet: the line is `candidate`, there is no Research
Lead, no advisory contact, no archive survey, no visual identity, `new-record` is NOT
BUILT, and no adapter exists.

---

## Phase 4 — Episode one ⬜

| Stage | Gate | Status |
|---|---|---|
| Brief and question | Greenlight | ⬜ |
| Research pack | Source lock | ⬜ |
| Script | Script lock | ⬜ |
| Claim verification | Fact-check | ⬜ |
| Premise and prompts review | Sensitivity | ⬜ |
| Storyboard and prompt cards | — | ⬜ |
| Generation | — | ⬜ |
| Assembly and grade | Picture lock | ⬜ |
| VO, score, mix | Audio lock | ⬜ |
| Clearances | Rights | ⬜ |
| Package | Technical QC | ⬜ |
| Publish + evidence layer | — | ⬜ |

**Exit criterion:** episode published with its sources page, provenance summary, and
an open corrections log.

---

## Phase 5 — Season one ⬜

- ⬜ Retrospective on episode one; amend the Bible where it was wrong
- ⬜ Lock the season throughline
- ⬜ Establish sustainable cadence (measured, not assumed, from episode one's actuals)
- ⬜ Prompt library v2 — fold in what the `runs` notes taught
- ⬜ Advisory board review of the full season slate

---

## Phase 6 — Expansion ⬜

The test of whether the architecture was worth it. Three expansions, in increasing
order of what they prove.

### 6a — Second line, same studio

- ⬜ Select the next line from `studios/african-history/lines/README.md` § Candidate lines
- ⬜ Run `studio_ops new-line`; measure how much studio-level work it forces *(NOT BUILT)*
- ⬜ Localisation: first dub or subtitled release using the M&E stems

**Proves:** the studio → line split. **Exit criterion:** the line reaches greenlight
without modifying anything above `studios/african-history/`.

### 6b — Second studio, same pack

- ⬜ `studio_ops new-studio --pack documentary-history` *(NOT BUILT)*
- ⬜ Confirm no platform-level file needed a change

**Proves:** the platform → studio split, and that the pack is genuinely reusable
rather than tacitly African-history-shaped.

### 6c — Second **pack** — a different kind of video entirely

The real test.

- ⬜ Author a pack for a genre with different obligations — narrative, brand, or
      explainer
- ⬜ Write its gate set from scratch, from *what would we regret not checking?*
- ⬜ Produce one short piece under it, end to end

**Proves:** that `core/` is genuinely universal rather than documentary rules wearing
a general name.

**Exit criterion for the phase:** all three complete without modifying `core/`,
`standards/`, `prompts/`, `templates/`, or `automation/`.

If any of them cannot, the abstraction sits in the wrong place. Record the finding in
[docs/architecture/evolution.md](docs/architecture/evolution.md) and move the
boundary — that is what the log is for. Watch specifically for a second pack that is
largely a copy of the first: it means the shared material belonged in core.

---

## Deliberately not on this roadmap

Recorded so they are decisions rather than oversights:

| Not doing | Why | Revisit when |
|---|---|---|
| Fully automated generation pipeline | Human gates are the product, not the friction | Never |
| Real-time / live formats | Incompatible with the gate model | — |
| Interactive or branching documentary | Multiplies the claim surface without multiplying the research | Phase 6+ |
| Self-hosted model training | Cost and rights exposure far exceed the benefit at this scale | If vendor terms become untenable |
| Publishing raw archival scans | Custodian agreements rarely permit it | Per-source, if a custodian offers |

---

## How this document changes

The roadmap is revised at each phase boundary and at each season retrospective.
Changes to *what the phases are* — as opposed to their contents — are architecture
changes and are recorded in
[docs/architecture/evolution.md](docs/architecture/evolution.md).
