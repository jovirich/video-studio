---
title: Risk register
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner]
---

# Risk register

Two things: the register **template**, and the standing platform-level risks that are
**structural** rather than speculative.

The distinction matters. A speculative risk is a thing that might happen — a vendor
outage, a contributor falling ill. A structural risk is a consequence of how the
platform is built: it is present from the moment the design is adopted, it does not
arrive, and it does not go away on its own. Every risk in §3 is structural. They are
listed not because someone brainstormed them but because the architecture implies
them, and a register that omits its own architecture's consequences is a register of
other people's problems.

Line- and production-scoped risks are deliberately empty here (§4). They belong to
the line and the production, and they are not the platform's to guess at.

## 1. The template

A risk row carries seven fields. Fewer than seven and it is a worry, not a risk.

| Field | Rule |
|---|---|
| `id` | `RSK-<SCOPE>-<NNNN>`. `SCOPE` is `PLAT`, the line code in caps, or the episode code. Permanent, never reused |
| `risk` | One sentence naming the *failure*, not the hazard. "Model terms change" is a hazard; "a delivered master relies on a licence that no longer permits it" is a risk |
| `likelihood` | High / Medium / Low, per §2. A judgement, recorded as one |
| `impact` | Severe / Major / Moderate, per §2 |
| `signal` | The **observable** early warning. A metric, a field value, a validator finding, a date going stale. If it cannot be observed without asking someone how they feel, it is not a signal |
| `mitigation` | What is already in place, plus what is not yet. Naming a mitigation that does not exist as though it does is worse than naming none |
| `owner` | A role slug from [roles.md](roles.md). Never a person |

Two rules about the `signal` column, because it is the field that decides whether a
register is useful or decorative:

- **A signal is something that is already true before the risk lands.** "The
  production overran its generation budget" is not a signal, it is the event.
  "Cumulative generation spend passed half the ceiling before picture lock" is a
  signal.
- **A signal nobody looks at is not a signal.** Each row below names what would
  surface it — a validator gate, a gate checklist item, or a scheduled review. Where
  that thing is **NOT BUILT**, the row says so, because a mitigation that depends on
  unbuilt tooling is not currently a mitigation.

> `TBD — the RSK type is not registered in` [../standards/id_system.md](../standards/id_system.md).
> Adding it, or deciding risks are not ID-bearing entities, is a Platform Owner
> decision. The IDs below are used on the assumption it will be added.

## 2. Scales

Qualitative, and deliberately so. Numeric probabilities on a platform that has never
produced anything would be false precision — the exact failure
[../packs/documentary-history/02_evidence_and_sourcing.md](../packs/documentary-history/02_evidence_and_sourcing.md)
§6 prohibits in scripts, and there is no reason to permit it in ops.

| Likelihood | Means |
|---|---|
| **High** | Expected to occur on the first production unless something is done. Not a forecast — an implication of the current design |
| **Medium** | Plausible within the first season |
| **Low** | Requires two things to go wrong together |

| Impact | Means |
|---|---|
| **Severe** | The production cannot ship, a published work must be withdrawn, or harm falls on someone outside the studio |
| **Major** | Recoverable, at the cost of schedule and money — a re-open cascade, a re-generation, a re-mix |
| **Moderate** | Absorbed within a stage |

Impact is judged **after** existing controls, not before. A risk whose impact is
Severe on paper and Moderate in practice because a gate catches it is recorded as
Moderate, with the gate named — otherwise the register argues for controls that
already exist.

## 3. Standing platform risks

| ID | Risk | Likelihood | Impact | Owner |
|---|---|---|---|---|
| `RSK-PLAT-0001` | Gate collapse: fewer distinct signatories than the adopted pack requires, so gates are signed by the people who made the material | **High** | **Severe** | `platform-owner` |
| `RSK-PLAT-0002` | A delivered master relies on vendor terms that changed after the asset was generated | **High** | **Severe** | `rights-and-clearances` |
| `RSK-PLAT-0003` | Generation spend on one production exceeds its ceiling, or consumes budget reserved for people | **High** | **Major** | `showrunner` |
| `RSK-PLAT-0004` | A production proceeds on material outside its line's advisory coverage | **Medium** | **Severe** | `cultural-advisor` |
| `RSK-PLAT-0005` | The entire evidence chain depends on one Research Lead who cannot be replaced mid-season | **High** | **Severe** | `showrunner` |
| `RSK-PLAT-0006` | A model version changes mid-season and previously-generated material can no longer be matched or regenerated | **High** | **Major** | `pipeline-engineer` |
| `RSK-PLAT-0007` | Asset store loss or corruption breaks the provenance chain for delivered work | **Low** | **Severe** | `pipeline-engineer` |

### `RSK-PLAT-0001` — Gate collapse on a small team

[../core/04_review_gate_framework.md](../core/04_review_gate_framework.md) §5
prohibits one person signing two gates on the same production, and
documentary-history declares `minimum_distinct_signatories: 4` against a nine-gate
set. A two- or three-person team physically cannot satisfy this. What happens next is
not that the team stops; it is that the same person signs several gates and the
production record continues to look exactly like a production record that passed nine
independent reviews.

This is the risk the whole platform is most exposed to, because every other control
in the repository terminates in a signature. If the signatures are one person's, the
provenance ledger, the claim chain, and the clearance log all still work perfectly and
all certify nothing that was independently seen.

**Signal.** The same `person` value appearing in two signature blocks on one
production record. A production whose distinct signatory count is below the pack's
`minimum_distinct_signatories` at greenlight. Gates entering `in-review` and reaching
`signed` on the same day, repeatedly — a checklist that takes no elapsed time was not
worked through.

**Mitigation.** In place: the constraint is written into core, the packs declare a
minimum, and separation of duties is a stated condition of adopting a pack. Not in
place: `studio_ops validate --canon` is specified to flag a repeated name across a
production's signatures and is **NOT BUILT**, so today nothing detects this
automatically. The honest responses when the count cannot be met are to retain named
outside signatories, adopt a pack with a smaller gate set, or not produce. Signing
anyway is not one of them. See also the unresolved conflict in
[roles.md](roles.md) §5.1, which makes the required count ambiguous in every pack.

### `RSK-PLAT-0002` — Vendor terms change without notice

Generative vendors change terms of service, output ownership, indemnity scope,
training-on-inputs defaults, and plan tiers, without announcement and sometimes
retroactively.
[../core/02_rights_and_licensing.md](../core/02_rights_and_licensing.md) §5 records
the position per tool with the date checked, precisely because the position has a
shelf life. A master delivered on the basis of terms that have since changed is not
easily recalled, and a distributor's chain-of-title review is where this surfaces.

**Signal.** A `terms_checked` date in the model terms register older than the
production's delivery date. A vendor changing plan tiers or introducing a new
acceptance prompt in an adapter. A modality with exactly one vendor in the register —
that is not a signal of a change, it is a signal that a change would be unsurvivable.

**Mitigation.** In place: model terms are re-checked before **every** delivery, and
the rights gate certifies it. Not in place: the register itself at
[../rights/permissions/](../rights/permissions) is empty, and
`studio_ops validate --prompts` — which is specified to flag vendors whose
`terms_checked` date is missing or expired — is **NOT BUILT**. Structural mitigation:
keep a second viable vendor per modality, and never let a production's look depend on
a single vendor's continued permission.

### `RSK-PLAT-0003` — Generation cost overrun

Generated imagery is cheap per attempt and unbounded in attempt count. The cost curve
of "one more variation" is flat enough that nobody notices crossing it, and the money
comes out of the same envelope as consultation fees, translation, and archive access —
the lines that pay people. That substitution is the failure:
[../core/01_provenance_and_ai_disclosure.md](../core/01_provenance_and_ai_disclosure.md)
§7 states the studio's position that generative tools change what work costs but not
who it belongs to, and a budget that quietly moves money from advisors to GPU time
contradicts it in practice while affirming it in the credits.

**Signal.** Cumulative generation spend past half the production's
`budget.generation_ceiling_usd` before picture lock. Rising attempt count per shot in
the manifest — a shot on its eighth generation is a prompt or a brief problem, not a
generation problem. `consultation_fees_budgeted: false` on the production record at
any point after greenlight.

**Mitigation.** In place: a hard per-production ceiling
(`GENERATION_BUDGET_USD_PER_EPISODE` in [../.env.example](../.env.example)) that the
adapters refuse to run past, `GENERATION_DRY_RUN=true` as the default, prompt review
before generation rather than after, and a dedicated budget line in
[budget_template.md](budget_template.md) §3. Not in place: the adapters are stubs, so
the ceiling is currently enforced by nothing.

### `RSK-PLAT-0004` — Advisory coverage gaps

[../packs/documentary-history/07_cultural_sensitivity.md](../packs/documentary-history/07_cultural_sensitivity.md)
§5 states it plainly: a line does not begin production on material outside its
advisory coverage. The pressure to breach this is entirely schedule-shaped — an
episode is slotted, the advisor for that tradition has not been found, and the work
is *nearly* within coverage. It is either within coverage or it is not.

The impact is Severe rather than Major because it lands outside the studio, on people
who had no route into the process, and no amount of subsequent correction returns
their position to what it was.

**Signal.** `advisory_coverage.gaps` non-empty on a production record at greenlight.
The same category appearing in a second sensitivity hold — one hold is a catch, two on
one theme is a coverage gap. Advisor response latency increasing, which usually means
an advisor is being asked to work unpaid or beyond their declared competence.

**Mitigation.** In place: the schema requires `advisory_coverage.covered` and the
greenlight checklist blocks on it; the advisory hold gives any contributor a stop
button; advisors are paid, credited, and may withdraw. Not in place: no line has an
advisory register yet — it is listed as **NOT STARTED** in
[../docs/status.md](../docs/status.md) and it blocks line opening, which is the
correct ordering.

### `RSK-PLAT-0005` — Key-person dependency on one Research Lead

The claim chain is the load-bearing structure of a documentary line, and it is built
by one role. That role holds the tier judgements, the independence checks, the
unrecorded reasoning behind why a register is `probable` rather than `established`,
and the working relationships with archives. If the person holding it leaves
mid-season, the records survive and the judgement does not — and a successor cannot
safely sign a fact-check gate over a research pack whose reasoning they cannot
reconstruct.

Note that documentary-history assigns `source_lock` **and** `fact_check` to this one
role, which concentrates the dependency further and is part of the unresolved
separation-of-duties conflict in [roles.md](roles.md) §5.1.

**Signal.** A rising share of claim records whose reasoning exists only in the
`critique` block's brevity — a one-line critique is a claim nobody else can audit.
Open questions accumulating while claim creation continues, meaning gaps are being
noted and not worked. Any period where a second person has not read a source record
before it is cited.

**Mitigation.** In place: the record structure is designed so that judgement is
written down rather than held — the `critique` block, the corroboration requirement,
the confidence register, the bias register, and the open-questions register all exist
to externalise reasoning. Retention of scans, transcripts, and correspondence under
the source ID means a successor inherits the material as well as the conclusion. Not
in place: `TBD — no succession or handover procedure exists. Needs a Showrunner
decision and a runbook under` [../docs/runbook/](../docs/runbook).

### `RSK-PLAT-0006` — Model version drift mid-season

Vendors deprecate and silently update models. A shot generated in month one may be
impossible to reproduce in month four, and a regenerated shot may no longer match the
sequence around it — which is the expensive form, because it surfaces at picture lock
when the fix is a re-cut rather than a re-prompt. Style anchors reduce drift; they do
not eliminate it, because the anchor constrains the input and the model changes the
transformation.

**Signal.** `tool.version` values differing between assets inside one sequence in the
manifest. A vendor deprecation notice. A regenerated shot failing the style-anchor
comparison at picture lock when the original passed. A seed that no longer reproduces
its recorded output — the cleanest possible signal, and worth testing deliberately at
the start of each production.

**Mitigation.** In place: every generated asset records vendor, model, **version**,
prompt card, seed, and parameters, so drift is at least detectable rather than
mysterious; style anchors are versioned files with checksums; prompt cards are
versioned rather than overwritten. Structural: pin a model version per production and
treat a version change as a sequence-level regeneration decision, not a shot-level
one. Not in place: nothing currently compares versions across a sequence — that is a
`studio_ops` report that does not exist.

### `RSK-PLAT-0007` — Asset store loss

Media lives outside git by design. That is correct — a repository holding four
hundred generated clips is unusable — and it means the provenance chain has two ends
in two systems, and only one of them has git's guarantees. If the store loses an
asset, the manifest entry survives and describes a file nobody can produce, which is a
worse position than losing both, because the delivered work still asserts a provenance
it can no longer evidence.

Likelihood is Low and impact Severe, which is the classic shape of a risk that gets
deferred until it is the only one left.

**Signal.** Manifest entries whose asset does not resolve in the store. Checksum
mismatch on any archived package. A `last verified restore` date going stale — the
only meaningful signal, because a backup that has never been restored is a hypothesis.

**Mitigation.** In place, on paper:
[../core/03_distribution_and_formats.md](../core/03_distribution_and_formats.md) §8
requires two copies in two locations with one offline, verified annually, and every
archive package carries a README explaining how to rebuild, written for someone who
was not there. The delivered master embeds the manifest hash, so a file can be tied
back to the record set that produced it. Not in place: the asset store is **NOT
BUILT** and no round trip — ingest, manifest, conform, package — has ever been proved.

## 4. Line-scoped risks

Empty by design. A line's risks belong to the line, and the platform inventing them
would be inventing facts about material it knows nothing about.

| ID | Risk | Likelihood | Impact | Signal | Mitigation | Owner |
|---|---|---|---|---|---|---|
| `RSK-<LINE>-0001` | *One sentence naming the failure, not the hazard* | High / Medium / Low | Severe / Major / Moderate | *The observable thing that is already true before it lands* | *What exists, then what does not yet* | *role slug* |

## 5. Production-scoped risks

| ID | Risk | Likelihood | Impact | Signal | Mitigation | Owner |
|---|---|---|---|---|---|---|
| `RSK-<S01E01>-0001` | *One sentence naming the failure, not the hazard* | High / Medium / Low | Severe / Major / Moderate | *The observable thing that is already true before it lands* | *What exists, then what does not yet* | *role slug* |

## 6. Review

| When | Who | What |
|---|---|---|
| At greenlight | `showrunner` | Open the production's risk table. A production with no rows has not looked |
| At each gate | Gate owner | Any signal in §3 observed during the review is recorded, whether or not it blocks the gate |
| At delivery | `pipeline-engineer` | Re-check `RSK-PLAT-0002`, `0006`, `0007` — the three whose state can have changed since the material was made |
| Per season | `platform-owner` | Re-score §3. Move anything that has become observable out of "structural" and into a mitigation with a date |

A risk whose likelihood, impact, and signal have not changed in a year has either been
mitigated or has never been looked at, and the register cannot tell the difference.
Say which in the row.

## 7. Maturity

| Capability | Status |
|---|---|
| Register template and scales | **DESIGNED** |
| Platform risk rows | **DESIGNED** — none has been observed, because nothing has been produced |
| Signals as validator findings | **NOT BUILT** — every automated signal named above depends on a `studio_ops` gate that does not exist |
| Scheduled review cadence | **DESIGNED** — no review has been held |
