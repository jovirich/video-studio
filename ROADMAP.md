# Roadmap

Where the studio is going, in the order it will get there. This is a *sequencing*
document — it says what must be true before the next thing starts, not when.

Dates are deliberately absent. Phases advance on **exit criteria**, not calendars;
an episode that ships before its gates close costs more than one that ships late.

Status keys: ⬜ not started · 🟡 in progress · ✅ complete · ⏸️ blocked

---

## Phase 0 — Infrastructure ✅

The repository you are reading.

- ✅ Studio / production line / episode three-tier architecture
- ✅ Production Bible, 13 documents
- ✅ Record schemas (10) and identifier system
- ✅ Prompt library structure across 8 modalities and 40 vendors
- ✅ `studio_ops` toolkit skeleton with validators, scaffolders, reporters
- ✅ Six review gates with owners and checklists
- ✅ CI validation workflow
- ✅ Nigeria opened as line 01 in `candidate` status

**Exit criteria met.** The repo validates against its own rules.

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

## Phase 6 — Second production line ⬜

The test of whether the architecture was worth it.

- ⬜ Select the next line from `productions/README.md` § Candidate lines
- ⬜ Run `studio_ops new-line`; measure how much studio-level work it forces
- ⬜ Any studio-level change required is an architecture finding — record it in
      `docs/architecture/evolution.md`
- ⬜ Localisation: first dub or subtitled release using the M&E stems

**Exit criterion:** a second line reaches greenlight without modifying `bible/`,
`standards/`, or `automation/`. If it cannot, the abstraction was in the wrong place
and the finding goes in the evolution log.

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
