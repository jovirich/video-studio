---
title: Refinements before episode one
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner, pipeline-engineer, showrunner]
---

# Refinements before episode one

Open decisions and known weaknesses that should be closed before the first
production. Everything here is cheap now and expensive under deadline; that is the
only criterion for inclusion.

This is not a backlog and it is not [ROADMAP.md](../../ROADMAP.md). The roadmap says
what happens next. This says what is *wrong or undecided* about the thing the roadmap
assumes.

Each item states the issue, why it matters, a recommendation, who decides, and what
it blocks. Where the recommendation is "do less", it says so — this repository's
characteristic risk is not under-design.

Every claim below was checked against the tree on 2026-08-07 and the check is named,
so a reader can re-run it rather than trust it.

## Summary

| # | Item | Severity | Decides | Blocks |
|---|---|---|---|---|
| [1](#1-nothing-is-tested-the-validators-have-never-seen-a-real-record) | Nothing is TESTED; the validators have never seen a real record | **High** | Pipeline Engineer | Any claim that a gate works |
| [2](#2-hand-allocated-ids-will-collide-and-nothing-will-notice) | Hand-allocated IDs, no allocator, no graph checker | **High** | Pipeline Engineer | Source lock on episode one |
| [3](#3-ci-is-still-red-at-rest-and-its-own-comments-describe-behaviour-that-does-not-occur) | CI red at rest; `\|\| true` masks crashes | Medium | Pipeline Engineer | Merge discipline |
| [4](#4-the-exit-code-contract-is-documented-but-not-implemented) | Exit code 2 does not exist at runtime | Medium | Pipeline Engineer | Trustworthy CI signal |
| [5](#5-separation-of-duties-needs-four-people-and-will-be-abandoned-quietly) | Separation of duties needs ≥4 people | **High** | Showrunner | Greenlight |
| [6](#6-the-claim-reference-renderstrip-step-does-not-exist) | `{{CLM-*}}` render/strip step unimplemented | **High** | Pipeline Engineer | Script lock |
| [7](#7-the-asset-store-does-not-exist-and-the-traceability-guarantee-depends-on-it) | Asset store and `conform` refusal do not exist | **High** | Pipeline Engineer | Picture lock, Technical QC |
| [8](#8-prohibited_patternsjson-has-never-been-generated) | `prohibited_patterns.json` never generated | Medium | Cultural Advisor + Showrunner | `validate --canon` |
| [9](#9-a-schema-checks-a-packs-shape-nothing-checks-that-a-pack-is-coherent) | `validate --packs` NOT BUILT; a pack's coherence is unchecked | Medium | Pipeline Engineer | Pack correctness |
| [10](#10-no-canon-has-been-ratified-and-the-pack-is-pinned-to-an-unratified-core) | No canon ratified; pack pinned to unratified core | **High** | Platform Owner + Showrunner | Everything downstream |
| [11](#11-cross-line-source-scoping-is-designed-and-has-no-promotion-path) | `SRC-STUDIO-*` scoping has no promotion path | Medium | Research Lead | Cheap now, very expensive later |
| [12](#12-the-platform-is-not-actually-unbranded) | 15 platform files name the studio; one is a schema enum | Medium | Platform Owner | ROADMAP Phase 6a and 6b |
| [13](#13-vendor-cheat-sheets-are-unverified-and-verifying-all-of-them-is-the-wrong-move) | ~49 unverified vendor sheets | Medium | Visual Director | Prompt card accuracy |
| [14](#14-the-link-gate-is-red-at-rest) | `validate --links` is red at rest | Medium | Pipeline Engineer | Every other gate's credibility |
| [15](#15-the-makefile-and-the-cli-disagree) | Makefile invokes commands that were never in the CLI | Low | Pipeline Engineer | New-contributor trust |
| [16](#16-licensing-is-undecided-and-it-constrains-the-repository-layout) | ADR 0009 is `proposed` | Medium | Showrunner + Platform Owner | Publishing anything |

---

## 1. Nothing is TESTED; the validators have never seen a real record

**Issue.** `validate --schemas` currently passes across 11 files, and the `pytest`
suite passes. Neither result is evidence about the schemas, because the repository
contains **no real records** — no source record, no claim, no shot, no prompt card, no
production. The eleven files are control records and templates.

**Why it matters.** The first record-shaped file the validators ever saw
(`templates/production/production.yaml`) failed immediately — and not on its content:
`updated: datetime.date(2026, 8, 7) is not of type 'string'`, because an unquoted YAML
date loads as a `date` object and the schema's `isoDate` constraint wants a string. The
fix taken was to quote the date in the record, with an explanatory comment in the
template.

That is a reasonable convention, and it is currently enforced by **a comment in one
template**. Every hand-written record in the repository will meet the same trap, and
the ones written at 1am will not have the template open. It is also a preview of the
general case: the failures a schema corpus finds are boring, mechanical, and numerous,
and finding them one at a time inside a production is how a schedule slips.

The gap that matters is IMPLEMENTED → TESTED. A validator that runs cleanly on a
repository with no records has proved that it does not crash.

**Recommendation.** Two things, in order.

1. **Move the date convention out of a comment.** Either normalise dates in
   `frontmatter.read_yaml` so a record on disk and the same record in memory are the
   same thing, or state the quoting rule in `standards/metadata_spec.md` where a
   record author will look for it. Preferably both.
2. **Build the deliberately-flawed fixture corpus** ROADMAP Phase 3 calls for: 100+
   records with known violations, at least one per rule, asserting both that each rule
   fires and that clean input is silent. Until that corpus exists, no validator row
   moves past IMPLEMENTED in [../status.md](../status.md), and no statement of the form
   "the gate catches X" is supportable.

**Decides.** Pipeline Engineer.

**Blocks.** Every statement in this repository of the form "the validator catches X".

---

## 2. Hand-allocated IDs will collide, and nothing will notice

**Issue.** [`standards/id_system.md`](../../standards/id_system.md) states that IDs
are "allocated by the toolkit, never by hand". The toolkit does not allocate them:
`new-record` is NOT BUILT, and its own CLI stub names the allocator "the
highest-priority scaffolder". So episode one's source and claim IDs would be typed by
a human into YAML front matter.

**Why it matters.** Two failure modes, and the second is the dangerous one.

- A duplicate ID is *noisy* if two files carry it — but records reference each other
  by **ID string**, not by path. A claim's `evidence[].source: SRC-NG-0042` resolves
  to whichever record wins. Nothing today detects that two records claim `SRC-NG-0042`
  or that `SRC-NG-0043` was skipped, because `validate --sources` — the only gate that
  walks the reference graph — is NOT BUILT.
- IDs are permanent and never reused by design, which is correct and means a collision
  cannot be cleaned up later without breaking the audit trail that justifies the whole
  system. The corruption is silent, retroactive, and unrecoverable.

**Recommendation.** Build `new-record` before episode one's research begins, not
before script lock. It is the smallest scaffolder and the only one that is load-bearing
for correctness rather than convenience — `new-studio`, `new-line`, and
`new-production` can stay NOT BUILT and be done by hand-copying a template, because a
mis-scaffolded folder is visible and a mis-allocated ID is not.

If it genuinely cannot be built in time, the fallback is a single append-only
`sources/registry/ID_LEDGER.md` with one line per allocated ID, and a rule that a
researcher edits the ledger *before* creating the record. That is worse, and it is
recoverable; hand-allocation without a ledger is not.

**Decides.** Pipeline Engineer, with the Research Lead on the fallback.

**Blocks.** Source lock on episode one. Do not open a line without one of the two.

---

## 3. CI is still red at rest, and its own comments describe behaviour that does not occur

**Issue.** [`.github/workflows/validate.yml`](../../.github/workflows/validate.yml) has
been restructured correctly: the four IMPLEMENTED gates are blocking, and
`validate --all` runs as a non-blocking coverage report so the NOT BUILT gaps stay
visible. That is the right shape. Two problems remain.

- **The required job still fails at rest**, because `validate --links` is blocking and
  the tree has unresolved dead links (item 14). Nothing in the workflow is wrong; the
  repository is.
- **`|| true` inside the coverage step masks more than intended.** It suppresses a
  genuine crash — an unhandled exception in a validator, a missing dependency, a
  `KeyError` on an unknown gate — exactly as quietly as it suppresses the expected
  NOT BUILT exit. The step is annotated `continue-on-error: true` already, which is
  sufficient on its own.
- **The step's own comment says `--all` "exits 2 because of them".** It does not; it
  exits 1, for the reason in item 4. A comment in CI that describes behaviour the code
  does not have is how the next person debugs the wrong thing.

**Why it matters.** CONTRIBUTING.md says "a red gate is a blocked merge. There is no
override flag." That rule survives only while red means something. A required job that
is red for reasons unrelated to the current change trains everyone, within about two
weeks, to read red as background — and then the first real failure arrives in a channel
nobody watches.

**Recommendation.** Drive `--links` to zero (item 14) so the required job is green at
rest, then keep it that way by treating any new link error as blocking. Drop the
`|| true` and rely on `continue-on-error`. Fix the comment when item 4 is fixed, or fix
it now to say what actually happens.

**Decides.** Pipeline Engineer.

**Blocks.** The merge discipline in CONTRIBUTING.md § Pull request gates being real
rather than aspirational.

---

## 4. The exit-code contract is documented but not implemented

**Issue.** [`automation/README.md`](../../automation/README.md), the `validate`
docstring in `cli.py`, and `RunReport.exit_code()`'s own docstring all state:
`0` clean, `1` findings, `2` a requested gate is NOT BUILT. At runtime,
`python -m studio_ops validate --sources` exits **1**.

The cause is two lines apart. `validate/not_built.py` records its NOT BUILT report as
a `Finding` with `Severity.ERROR`; `RunReport.exit_code()` tests `error_count` before
`not_built`. Any NOT BUILT gate therefore has an error and returns 1. Exit code 2 is
unreachable.

**Why it matters.** The distinction is the whole point of the design — "a green build
that ran four of nine gates must not look like a green build that ran nine". As
shipped, a build that ran four of nine and a build that found a genuine schema
violation are indistinguishable to any script.

It has already propagated into a second file: the CI workflow's coverage step carries
the comment *"`--all` … exits 2 because of them"*, describing behaviour that does not
occur. That is how a documented-but-unimplemented contract spreads — each new reader
trusts the previous statement rather than the program.

**Recommendation.** Either record NOT BUILT findings at `Severity.INFO` and let the
`not_built` list drive the exit code, or reorder `exit_code()` to test
`self.not_built` first — the second is one line and preserves the human-readable
output. Then add the test that is currently missing: assert that a run containing only
a NOT BUILT gate exits 2, and that a run with a real error exits 1 even when a NOT
BUILT gate is also selected.

While there: `delivery` appears in `validate.UNBUILT` and therefore in `ALL_GATES`,
but has no `--delivery` flag in `cli.py`, so it is reachable only through `--all`.
Either add the flag or drop it from the list.

**Decides.** Pipeline Engineer.

**Blocks.** Any automation that reads the exit code, which is all of CI.

---

## 5. Separation of duties needs four people, and will be abandoned quietly

**Issue.** [`core/04`](../../core/04_review_gate_framework.md) §5 states, as core
canon rather than a pack's choice: **no person signs two gates on the same
production.** The documentary-history pack declares nine gates across eight role
owners and sets `minimum_distinct_signatories: 4` in
[`gates.yaml`](../../packs/documentary-history/gates.yaml). The sensitivity gate runs
three times and carries hold authority the Showrunner cannot unilaterally release.

The repository's own evolution log already names this as the item most likely to be
quietly abandoned (AE-005), and the enforcement — a repeated name across a
production's signatures, flagged by `validate --canon` — is NOT BUILT.

**Why it matters.** This is not a process nicety; it is the single structural check on
the Showrunner's authority, placed exactly where being wrong harms people outside the
studio. It is also, unlike every other item on this page, a **staffing and budget**
constraint rather than an engineering one, which is why it will not be solved by
anyone reading this document at their desk.

The realistic failure is not a decision to abandon it. It is 1am before a release,
one person holding three roles, and a signature block filled in with the same name
three times because the alternative is missing the date. Nothing in the repository
prevents that today, and the person doing it will believe, correctly, that they had
no other option.

**Recommendation.** Decide it before greenlight, in writing, with signatures. Two
honest options and one dishonest one:

| Option | What it means |
|---|---|
| **A — staff it.** Contract a Research Lead and a Cultural Advisor as paid external signatories before the line opens. | The pack already requires paid advisors; this makes it a costed line item rather than a hope. Preferred. |
| **B — amend the pack.** Reduce the gate set for a small team, honestly, with named collapses (e.g. picture lock and audio lock share an owner) and a stated prohibition that never collapses — sensitivity must never be signed by anyone who made the material. | A smaller set that is actually followed beats a nine-gate set that is theatre. This is a pack amendment with the pack owner's signature, recorded in the amendment log. |
| **C — keep nine gates and sign them all yourself.** | The outcome if A and B are both skipped. It is the current default. |

Whichever is chosen, build the `--canon` signature check early — it is the cheapest
validator on the list (compare names across a production's gate block) and it is the
only one whose findings are a *staffing signal* rather than a paperwork problem.

**Decides.** Showrunner, with the Platform Owner (core/04 §5 is core canon; option B
does not touch it, but any weaker rule would).

**Blocks.** Greenlight. Do not start episode one without an answer.

---

## 6. The claim-reference render/strip step does not exist

**Issue.** The `{{CLM-NG-0117}}` convention is specified in at least four places —
[`docs/glossary.md`](../glossary.md),
[`packs/documentary-history/02`](../../packs/documentary-history/02_evidence_and_sourcing.md)
§5, [`standards/id_system.md`](../../standards/id_system.md), and
[ADR 0002](../decisions/0002-claims-as-records.md). The step that strips the braces at
render and compiles the citation appendix is `studio_ops report bibliography`, which
is NOT BUILT, as is the whole `report` family.

**Why it matters.** ADR 0002's most concrete promise is that "the bibliography,
sources page, and citation appendix are generated, not written". Without the
compiler, a locked script either goes to the VO booth with `{{...}}` in it, or someone
strips them by hand — at which point the reference is gone, the appendix is written by
hand from memory, and the evidence chain exists in the records but no longer connects
to the artefact that shipped. That is the exact failure mode the whole design was
built to prevent, arriving through the back door.

**Recommendation.** This is the smallest piece of code that makes ADR 0002 real, and
it should ship before script lock on episode one. In scope: parse `{{CLM-*}}` out of a
markdown script, emit the stripped narration, emit an ordered appendix keyed to
line/timecode, and fail on any reference with no matching claim record. Out of scope
until later: the full `report` family, provenance summaries, chain of title.

It also gives `validate --sources` most of its parser for free, which is item 2's
dependency.

**Decides.** Pipeline Engineer.

**Blocks.** Script lock on episode one, and the published sources page that
[core/01](../../core/01_provenance_and_ai_disclosure.md) §3 level 4 requires.

---

## 7. The asset store does not exist, and the traceability guarantee depends on it

**Issue.** [README.md](../../README.md) §7 guarantee 1 states, unconditionally, that
every production here "is traceable — every asset has a provenance record; nothing
enters an edit without one." The mechanism behind that sentence is the `pipeline
conform` step refusing a timeline clip with no manifest entry. `pipeline` is NOT
BUILT; the asset store is NOT BUILT; no round trip — ingest → manifest → conform →
package — has ever been run. The `ASSET_STORE_*` variables in
[`.env.example`](../../.env.example) are read by nothing.

Related: `rights/permissions/model_terms_register.md` now exists as a register, but is
unpopulated for the tools actually on the critical path, and
[core/02](../../core/02_rights_and_licensing.md) §5 makes it the record of whether a
tool's output may be used commercially at all. `library/` is still an empty directory,
so there is no shared LUT, font, or music-bed set for a production to inherit.

**Why it matters.** A guarantee stated without a hedge, backed by no implementation, is
the specific kind of claim this repository has otherwise been careful not to make. It
is also the guarantee most likely to be quoted externally, because it is the
distinctive one.

**Recommendation.** Two moves, in this order.

1. **Prove the round trip on the `local` driver before episode one.** Not S3, not R2 —
   a local path, one asset, ingest → SHA-256 → manifest entry → conform → package.
   That proves the contract; swapping drivers afterwards is a configuration change.
   The runbook is [../runbook/asset_storage.md](../runbook/asset_storage.md) and is
   DESIGNED, NOT BUILT.
2. **Populate `rights/permissions/model_terms_register.md` with the three tools
   actually on the critical path** and nothing else. An empty register that ~50 vendor
   sheets point at is worse than a three-row one, and the register is a rights-gate
   blocker regardless of tooling.

Until (1) lands, README §7 guarantee 1 should read as a design commitment rather than a
statement of fact. That is an edit to a file outside this document's scope; it is
recorded here as a finding.

**Decides.** Pipeline Engineer (1), Rights & Clearances (2).

**Blocks.** Picture lock and Technical QC — both certify provenance completeness
against a manifest that nothing writes.

---

## 8. `prohibited_patterns.json` has never been generated

**Issue.** [`standards/prohibited_language.md`](../../standards/prohibited_language.md)
§ Configuring the checker says the machine-readable list lives at
`standards/schemas/prohibited_patterns.json`, "generated from this document". No such
file exists, no generator exists, and `validate --canon` reports itself blocked on
exactly this.

**Why it matters.** Two things, one obvious and one not.

The obvious one: the canon gate cannot run, so the FAIL categories — unattributed
attribution, colonial framing, "archival footage" applied to a reconstruction — are
enforced only by a human reading carefully, which is the condition the list exists to
improve on.

The non-obvious one: because no generator exists, the JSON will in practice be
hand-written first and the prose document will drift into being a commentary on it.
The governance rule in the document — editing the JSON directly requires Showrunner
and Cultural Advisor sign-off, because "the list is canon, not configuration" — is
built on a generation direction that does not exist. Get this backwards once and the
canonical list is a JSON file nobody signs.

**Recommendation.** Write the generator, not the JSON. It is a markdown-table parser
over one document with a stable shape, and it makes the prose the source of truth by
construction.

Then split the list honestly, because roughly half of it is not mechanically
checkable. "Any bare numeral above ten, any date, any named person, any named place"
requires an adjacent claim ID — which is claim-adjacency parsing, not pattern
matching, and is a different piece of work from matching "it is believed". Ship the
literal-pattern half as `--canon`; move the rest to the fact-check and script-lock
checklists where a human owns them. A validator that claims to check something it
cannot is the same false-confidence failure the NOT BUILT convention was invented to
avoid.

**Decides.** Cultural Advisor and Showrunner own the list; Pipeline Engineer owns the
generator and the split.

**Blocks.** `validate --canon`, and therefore the separation-of-duties check in item 5.

---

## 9. A schema checks a pack's shape; nothing checks that a pack is coherent

**Issue.** `pack.schema.json` and `studio.schema.json` now exist, so `pack.yaml` and
`studio.yaml` are structurally validated — that gap is closed. What remains open is
larger: `validate --packs` is **NOT BUILT**, and it is the gate that would check the
things a JSON schema structurally cannot.

Two secondary defects, both verifiable:

- `validate/not_built.py` still reports the `packs` gate as "Blocked on:
  pack.schema.json has not been written." The blocker was removed and the message was
  not. A stale blocker in a NOT BUILT notice is worse than no notice, because the whole
  convention rests on those messages being true.
- A record routed to a schema that does not exist degrades to a **warning** —
  "no schema named X — record not validated" — and warnings do not block a merge. A
  future rename of a schema file would therefore silently stop validating a whole
  record type.

**Why it matters.** A schema can check that `pack.yaml` has a gate-set path. It cannot
check that the gates.yaml at that path declares a checklist file that exists, that
every document listed in `pack.yaml` was actually written, that technical QC is
present, or that no pack rule loosens a core rule. Those four checks are what make the
pack layer trustworthy, and precedence (`core > pack > studio > line`) is only a
guarantee if the last one runs.

Concretely today: the three draft packs each list documents in their READMEs that were
never written, and the only reason anyone knows is that `--links` catches the dead
links incidentally.

**Recommendation.** Build `--packs` before a second studio adopts any pack. It is
mostly file-existence checks over data that is already structured, which makes it one
of the cheapest remaining validators. Fix the stale blocker string in the same commit,
and promote "no schema named X" from WARNING to ERROR when the record was *explicitly
routed* to a named schema — asking for a schema that is not there is a broken
configuration, not a soft note.

**Decides.** Pipeline Engineer.

**Blocks.** Any confidence that a pack declares a gate set someone can actually run.

---

## 10. No canon has been ratified, and the pack is pinned to an unratified core

**Issue.** There are no signatures anywhere in this repository. `core/` documents are
`status: active`; `core/00` is `version: 0.2.0`; ROADMAP Phase 0 records core canon as
"DESIGNED, **not ratified**"; `core/05_amendment_log.md` carries no ratification
entry. Meanwhile `packs/documentary-history/gates.yaml` pins `core_version: "0.2.0"`,
so the pack declares conformance to a version of core that nobody has signed.

**Why it matters.** `status: active` on an unsigned document is the same class of
overclaim as a bare ✅, and it is more consequential, because "active" is what a
contributor reads to decide whether a rule binds them. Precedence
(`core > pack > studio > line`) assumes each layer is fixed before the one below
depends on it; today all four are simultaneously drafts.

There is also a procedural gap. Ratifying the *studio* bible is well defined —
ROADMAP Phase 1 names two signatories and an amendment-log entry. Ratifying *core* is
not defined anywhere. `core/00` lists `owners: [platform-owner]`, one role, which for
a document that constrains every studio on the platform is thin.

**Recommendation.** Ratify bottom-up in dependency order, and define what ratification
means for core before doing it:

1. Define core's ratification rule — minimum two signatories, one of whom is not the
   author, recorded in `core/05_amendment_log.md`. Write it as an ADR; it is a
   governance decision with a real negative consequence (it slows core changes down)
   and therefore qualifies.
2. Ratify `core/` at `0.2.0`, or bump to `1.0.0` at ratification and let `0.x` mean
   "unratified" permanently. Recommended — it makes the state readable from the
   version alone.
3. Ratify `documentary-history` against the ratified core version, updating the
   `core_version` pin.
4. Then Phase 1's studio ratification, which is already specified.

Until step 2, `status:` on core documents should read `draft`, not `active`.

**Decides.** Platform Owner and Showrunner.

**Blocks.** Everything downstream, in the precise sense that a line cannot be held to
a rule nobody has signed.

---

## 11. Cross-line source scoping is designed and has no promotion path

**Issue.** [`standards/id_system.md`](../../standards/id_system.md) and
[`02_evidence_and_sourcing.md`](../../packs/documentary-history/02_evidence_and_sourcing.md)
§5 both define `SRC-STUDIO-NNNN` for cross-line sources alongside line-scoped
`SRC-NG-NNNN`. Claims are line-scoped only. Nothing states when a source should be
studio-scoped, who decides, or what happens to a source that was registered
line-scoped and later turns out to matter to a second line.

**Why it matters.** The last case is the one that will happen, and IDs are permanent.
[ADR 0001](../decisions/0001-studio-not-show.md) explicitly anticipates it: "trade,
migration, and empire do not respect modern borders." When Ghana wants to cite
`SRC-NG-0042`, there are three options and two of them are bad:

| Option | Consequence |
|---|---|
| Re-register it as `SRC-STUDIO-0007` | Two records for one item. Corroboration counting breaks — 02 §3 requires independent sources, and two IDs for the same document look independent to any checker and to a tired human. |
| Cite `SRC-NG-0042` from a Ghana claim | Works, but the scope segment now lies, and every report grouped by scope is wrong. |
| Promotion record: keep the ID, add `promoted_to: SRC-STUDIO-0007` with the old ID as a permanent alias | Correct, and requires a schema field and a resolver that do not exist. |

The cost of deciding this is one paragraph and one schema field today. After 400
source records exist, it is a migration across every claim's `evidence` array.

**Recommendation.** Invert the default: **a source is studio-scoped unless there is a
reason it is not.** A document, an excavation report, or a monograph is an object in
the world; it does not belong to a production line. Line scoping is for material that
genuinely cannot recur — a line-specific interview, a locally-held object with a
line-specific custodian relationship.

If that is too large a change, adopt the promotion record and add
`promoted_to` / `promoted_from` to `source_record.schema.json` now, while the field
costs nothing.

**Decides.** Research Lead, with the Pipeline Engineer on the schema.

**Blocks.** Nothing today, which is exactly why it will be skipped. Decide it anyway.

---

## 12. The platform is not actually unbranded

**Issue.** [ADR 0005](../decisions/0005-platform-and-canon-packs.md) § Validation
names failure signal #1 and gives the command:
`grep -ri "african\|nigeria" core/ standards/ prompts/ templates/ automation/` should
return nothing. Extended to the root build files it currently returns **15 files** —
down from 24 and still not zero. Re-run it; the remaining categories are:

| Category | Files | Example |
|---|---|---|
| Build metadata | `pyproject.toml`, `Makefile`, `.env.example` | `description = "Operations toolkit for African History Studio…"`; `STUDIO_DEFAULT_LINE=ng-nigeria` |
| Schema content | `_common.schema.json`, `production_line.schema.json` | `"ng-nigeria"` in a `lineCode` enum; `"Line number. Nigeria is 1."` |
| Standards examples | `id_system.md`, `naming_conventions.md`, `metadata_spec.md`, `delivery_specs.md`, `data_graphics.md`, `prohibited_language.md` | `SRC-NG-0042`, `ng-nigeria` |
| Core | `00_platform_charter.md`, `03`, `05` | §1 names the first studio deliberately; §8 states the rule the file then breaks |

**Why it matters.** Three kinds, and they should not be fixed the same way.

*A line code in a schema enum is the serious one.* `_common.schema.json` enumerating
`ng-nigeria` means the platform's shared schema has to be edited to open a line — which
is a direct violation of `arch-2` clause 5, the load-bearing claim that spinning up new
work touches no platform file. It is also the one that will be discovered at exactly
the wrong moment, when a second line is being opened under deadline.

*Build metadata* is cosmetic but is the first thing an external reader sees, and it
contradicts the repository's own framing on line 3 of `pyproject.toml`.

*Examples* using `NG` are the ambiguous case. A neutral example scope (`XX`) costs one
pass now and removes the argument permanently.

**Recommendation.** Before episode one: replace the `lineCode` enum with a pattern
(`^[a-z]{2}-[a-z-]+$`) so opening a line never edits a platform schema, and fix the
three build files. Sweep the doc examples to a neutral scope as a lower priority. Add
the grep to CI as a *warning* so the count can fall but not silently grow. Do not touch
`core/00` §1, which names the first studio deliberately and correctly — but reword §8
so the charter is not in violation of itself.

**Decides.** Platform Owner.

**Blocks.** ROADMAP Phase 6a and 6b — a second line and a second studio are supposed to
prove that no platform file needed a change, and a line code sitting in a shared schema
enum guarantees one does.

---

## 13. Vendor cheat sheets are unverified, and verifying all of them is the wrong move

**Issue.** ~49 vendor sheets across eight modalities, written from general knowledge
and, per [../status.md](../status.md), "not verified against current vendor
documentation". `validate --prompts`, which would flag sheets older than 90 days, is
NOT BUILT.

**Why it matters.** Parameter details in these sheets will be wrong — not maliciously,
but because vendor syntax, model names, and aspect-ratio flags change on a timescale
of weeks. A prompt card that renders to an invalid parameter string fails at
generation time, which is annoying but visible. The dangerous case is a parameter that
is *valid and means something different*, which produces a plausible wrong image that
passes review.

**Recommendation.** Do less, deliberately. Verifying 49 sheets is a week of work that
decays immediately and that nobody will repeat.

1. Verify the **three vendors on episode one's critical path** — one image, one video,
   one voice — against live vendor documentation, and stamp each with a
   `terms_checked` / `docs_checked` date in front matter.
2. Add an explicit `verified: false` field to the other 46 and surface it in the sheet
   header, so a reader sees the status without consulting the status ledger.
3. Build the staleness check as a front-matter date comparison — that is `--prompts`
   in about thirty lines, and it is worth more than any amount of one-time
   verification because it keeps working.

**Decides.** Visual Director, with Audio Lead on the voice vendor.

**Blocks.** Nothing hard, but every prompt card written against an unverified sheet
inherits its errors, and prompt cards are versioned records that persist.

---

## 14. The link gate is red at rest

**Issue.** `python -m studio_ops validate --links` reports errors on a clean tree — a
three-figure count when this list was first compiled, **24 at the time of writing**,
falling as the missing files are written. Re-run it for the current number; the count
is not the finding, the *class* is. Every error is a reference to a file that was
specified but never created — currently all of them in `templates/records/_TEMPLATE_*`
and `templates/legal/*`, referenced from the pack methodology documents.

**Why it matters.** Same mechanism as item 3, one layer down. A gate that is red at
rest cannot distinguish "someone broke a link" from "the repository is as it always
is". It also makes the gate unusable as a merge check, which is what it is for — and
`--links` is one of only four IMPLEMENTED gates, so this is a meaningful fraction of
the working validation surface.

Note that this is a *good* failure: the link gate is doing exactly its job and telling
the truth about a repository whose navigation is its primary interface.

**Recommendation.** Drive it to zero before episode one, by the cheapest correct route
per case:

| Case | Fix |
|---|---|
| The file should exist and is on the critical path (record and legal templates, gate checklists) | Create it, even as a stub with front matter and a `TBD — needs research` body |
| The file is a genuine forward reference to unwritten pack documents | Remove the link; keep the plain text. A link is a promise. |
| Path is simply wrong (several `../bible/…` links survive the `arch-2` move) | Repoint it |

Then treat any new link error as blocking, which is only credible from zero.

**Decides.** Pipeline Engineer, coordinating with whoever owns each missing file.

**Blocks.** Every other gate's credibility, by association.

---

## 15. The Makefile and the CLI disagree

**Issue.** [`Makefile`](../../Makefile) invokes `studio_ops new-episode` and
`studio_ops new-line --code X --name Y`. The CLI has no `new-episode` command — it is
`new-production` — and `new-line` takes `--studio --code --title`. The `status` target
calls a NOT BUILT command. The `.vscode` tasks mirror the Makefile.

**Why it matters.** Low stakes on its own; corrosive in aggregate. It is the first
thing a new contributor runs, per the onboarding path, and a `make` target that fails
with an unrecognised-command error on day one sets the expectation that the tooling is
decorative. It is also a leftover of the `arch-1` → `arch-2` rename that no validator
can catch, which makes it a good argument for a trivial one.

**Recommendation.** Fix the Makefile and `.vscode/tasks.json` to the real CLI surface;
mark NOT BUILT targets in their `##` help text so `make help` tells the truth. Then
consider a ten-line test that asserts every `python -m studio_ops <cmd>` string
appearing in `Makefile`, `.vscode/tasks.json`, and `README.md` resolves to a
registered command — that is a real check nothing else performs.

**Decides.** Pipeline Engineer.

**Blocks.** Nothing. Fix it anyway; it is fifteen minutes.

---

## 16. Licensing is undecided, and it constrains the repository layout

**Issue.** [ADR 0009](../decisions/0009-licensing-posture.md) is `status: proposed`.
`LICENSE` holds the conservative default. The ADR's own recommendation — Apache-2.0 on
code and schemas, CC BY on `core/` and `packs/` prose, proprietary on `studios/` and
`rights/` — is unratified, and ROADMAP Phase 1 lists it as a blocker.

**Why it matters.** It is not only a legal question; it determines physical layout. If
`studios/` stays private while the engine is published, that is either a repository
split or a mirror with a filtered history, and history filtering is dramatically
easier before there is much history. It also determines whether a contributor
agreement must distinguish engine contributions from production work — which needs to
be in place before anyone outside the founding group commits anything.

**Recommendation.** Decide it before the first external contributor, not before the
first episode. The ADR's option B with C's prose variant is well argued and there is
no new information to wait for. If the answer is "not yet", record that as an explicit
deferral with a trigger ("decide before the first non-founder commit") rather than
leaving the ADR open indefinitely — an ADR that stays `proposed` for a year is
functionally a decision to do nothing, made without anyone signing it.

**Decides.** Showrunner and Platform Owner.

**Blocks.** Publishing anything, and any external contribution.

---

## What is deliberately not on this list

Recorded so they are judgements rather than oversights.

| Not here | Why |
|---|---|
| "Four tiers is over-engineering for one studio" | It is, visibly, and it is the right call anyway — the cost asymmetry argument in ADR 0005 is correct. Revisit only if a second pack turns out to be 80% a copy of the first. |
| Wiring a generation adapter | Deliberately NOT BUILT with a cost ceiling. Wiring one is a separate budgeted decision, not a refinement. |
| Building the full `report` family | Only the citation compiler (item 6) is load-bearing. The rest can wait for records to exist. |
| Implementing `new-studio` / `new-line` / `new-production` | A mis-scaffolded folder is visible and cheap to fix. Only `new-record` (item 2) is load-bearing, because ID collisions are silent. |
| Verifying all 49 vendor sheets | See item 13. The staleness check is worth more than the sweep. |
| More documentation | The ratio of specification to working code is already the central risk in this repository. Nothing here is blocked on a document that has not been written. |
</content>
