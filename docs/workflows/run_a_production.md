---
title: Run a production
status: active
version: 0.1.0
updated: 2026-08-07
owners: [showrunner, pipeline-engineer]
---

# Run a production

Brief to publish, naming each gate. Written against the
[documentary-history](../../packs/documentary-history/) gate set — nine gates, declared
as data in [`gates.yaml`](../../packs/documentary-history/gates.yaml). A studio on a
different pack has a different set; the *framework* is the same and is
[core/04](../../core/04_review_gate_framework.md).

**Every `studio_ops` command below is NOT BUILT** except `validate`. The manual
equivalent follows each one.

A gate is a named point where a **specific human** certifies a **specific claim**
against a **written checklist** and records a signature. `signed` is the only state
that permits downstream work. **No person signs two gates on this production.**

---

## 0 · Brief → **Greenlight** (Showrunner)

1. Scaffold:

   ```bash
   python -m studio_ops new-production --line <line> --season 1 --number 1 --slug <slug>
   ```

   **NOT BUILT.** Will copy `templates/production/` into the line, build the gate block
   from the pack's `gates.yaml`, and allocate the production ID.

   **Today:** copy [`templates/production/`](../../templates/production/) by hand, and
   transcribe the gate block from `gates.yaml` into the production record. Transcribe
   it, do not summarise it — a gate that is missing from the record is a gate nobody
   will run.

2. Write the brief: the question, the sub-questions it decomposes into, what would
   count as an answer, and **what would falsify the working assumption**.
3. Check advisory coverage. If the register has no one competent on a tradition this
   production needs, it does not proceed — the production waits or the scope changes.
4. Budget consultation fees, translation, digitisation, and archive access. If the
   budget cannot reach the primary material, the scope shrinks; it does not proceed on
   secondary material while claiming otherwise.
5. Declare conflicts of interest.

**Sensitivity gate, first of three runs:** does the *premise* clear cultural review?

> **Greenlight certifies:** the question has stakes, sits inside advisory coverage, has
> a research lead assigned, has consultation fees budgeted, and has declared conflicts.

## 1 · Research → **Source lock** (Research Lead)

Method: [`methodology/research_protocol.md`](../../packs/documentary-history/methodology/research_protocol.md).
Registry mechanics: [`sourcing/README.md`](../../packs/documentary-history/sourcing/README.md).

1. Survey the landscape before assessing reach. Prioritise by evidentiary weight, not
   convenience.
2. For each item, **create the source record first, then read.** Creating it first
   forces custody, access, and rights to be captured while you are looking at the item
   rather than reconstructed later from memory.

   ```bash
   python -m studio_ops new-record --type source --line <line>
   ```

   **NOT BUILT**, and this is the risky manual step. Allocate from the ID ledger before
   writing the file. Never guess the next serial.
3. Complete the **critique block** on every source. A citation is a location, not a
   warrant.
4. Form claims — one per statement the production will make. Set the register from the
   evidence, then check the corroboration requirement.
5. **Check independence explicitly.** Record on each evidence entry which sources it is
   demonstrably *not* derived from. Repetition is not corroboration.
6. Record every gap as a `QST-*` open question with what was searched. Gaps are
   findings.

> **Source lock certifies:** every claim the outline requires exists at its required
> tier; independence checked on every `established` claim; contested claims carry named
> positions; T4 sources have consent records and named holders; open questions are
> registered and none is load-bearing for an `established` claim; critique blocks
> complete.

After source lock, new evidence requires a documented re-open. That friction is
deliberate — without it, research continues indefinitely and the script never locks.

## 2 · Script → **Script lock** (Story Producer)

1. Write narration containing `{{CLM-*}}` references and **no bare facts**. Every date,
   name, figure, and superlative carries a claim ID.
2. Set the on-screen certainty language to match each claim's register. `probable`
   honestly beats `established` falsely.
3. Check against
   [`standards/prohibited_language.md`](../../standards/prohibited_language.md) by hand.
   `validate --canon` is NOT BUILT and `prohibited_patterns.json` has never been
   generated, so the FAIL categories — unattributed attribution, colonial framing,
   "archival footage" applied to a reconstruction — are enforced by a human reading
   carefully. Read carefully.

> **Script lock certifies:** narration and shooting script final; every factual
> statement carries a claim ID; certainty register matches the evidence; no prohibited
> pattern remains.

**Nothing generates before this gate.** Generating for an unlocked script is how a
production ends up writing toward the footage it happens to have.

## 3 · Verification → **Fact-check** (Research Lead)

Every `{{CLM-*}}` in the locked script resolves to a claim record at its required tier
— and **on-screen text, graphics, maps, and the episode description are checked to the
same standard as narration.** Maps are where this is skipped and where errors are most
visible.

```bash
python -m studio_ops validate --sources
```

**NOT BUILT.** Today: walk the chain by hand — every reference in the script to a claim
record, every claim's evidence array to a source record, every `established` claim to
its independence assertion. Record the walk as the fact-check report (`FCK-*`); a
verification nobody can review later did not happen.

The Research Lead signs this and signed source lock. That is permitted — they are
different certifications by the same accountable role — but they may sign **no other
gate on this production**.

## 4 · Premise and prompts → **Sensitivity** (Cultural Advisor)

Second of three runs, and the important one: **before generation.**

1. Review the prompt set as records, not as images. A prompt card is reviewable
   precisely because nothing has been generated yet.
2. Check the categories in
   [`07_cultural_sensitivity.md`](../../packs/documentary-history/07_cultural_sensitivity.md)
   §2 — sacred and ritual, masquerade and regalia, remains and burial, living lineages,
   atrocity and enslavement, contested territory, bodies, naming.
3. Any contributor may raise an advisory hold at any point. It takes effect
   immediately; only a written Cultural Advisor ruling releases it; **the Showrunner
   cannot.**

## 5 · Storyboard and prompt cards (no gate)

One card per generated shot: structured fields, inherited style block and anchors,
`evidence_basis` **required** where the provenance class is `reconstruction`,
constraint flags for named persons, sacred material, violence, and remains.

```bash
python -m studio_ops promptlib render --card <id> --vendor <vendor>
```

**NOT BUILT.** Today: write the vendor string by hand from the card's fields and paste
it into `runs[].notes` so the mapping is recoverable. This is the main practical payoff
of the card structure and it is currently unproven.

## 6 · Generation (no gate)

1. Generate only from reviewed cards, only after script lock.
2. Record every run in the card's append-only `runs` history: seed, outcome, cost, and
   **why it worked or did not**. A season of those notes is the most valuable artefact
   the studio will accumulate; an empty `runs` history across a season means the record
   is being treated as paperwork.
3. Ingest every asset to the store, hash it, and write its manifest entry —
   [../runbook/asset_storage.md](../runbook/asset_storage.md). **Never commit media.**
4. Adapters are deliberate stubs behind a cost ceiling
   (`GENERATION_BUDGET_USD_PER_EPISODE`, `GENERATION_DRY_RUN=true`). Wiring one is a
   separate, budgeted decision.

## 7 · Assembly and grade → **Picture lock** (Visual Director)

```bash
python -m studio_ops pipeline conform
```

**NOT BUILT** — and this is the mechanism behind the platform's traceability guarantee:
the conform step refuses any timeline clip with no manifest entry. Until it exists,
that guarantee is enforced by hand. Reconcile the timeline against the manifest clip by
clip, and record that you did.

> **Picture lock certifies:** the cut is final; every generated shot passed anatomy,
> anachronism, light-consistency, skin-tone, and temporal-stability checks; every
> reconstruction and interpretive shot carries its label; vertical and square safe zones
> hold.

**Sensitivity, third run:** does the *cut* clear?

## 8 · VO, score, mix → **Audio lock** (Audio Lead)

> **Audio lock certifies:** loudness and true-peak targets met; all stems rendered
> **including M&E**; every proper noun pronounced per the VO record sheet and verified
> by a speaker of the language; no synthesised voice of a real or historical person.

Produce the M&E stem on episode one even if no dub is planned. Retrofitting it later
means re-mixing.

## 9 · Clearances → **Rights** (Rights & Clearances)

> **Rights certifies:** every asset in the manifest has a rights status other than
> `pending`; model terms were **re-checked at delivery**, not at generation; the cue
> sheet is complete; chain of title assembles.

```bash
python -m studio_ops report chain-of-title --episode <code>
```

**NOT BUILT.** Today: assemble it by hand from the clearance log. Distributors will ask
for it, and assembling it from memory at that point is how deliveries slip.

Maintain the cue sheet from episode one even if the score is entirely original.

## 10 · Package → **Technical QC** (Pipeline Engineer)

The universal gate. Every pack has it, because it is where the platform's own
guarantees are verified.

> **Technical QC certifies:** delivery specs met; captions validate; provenance manifest
> complete and frozen; Content Credentials applied where supported; package assembled;
> evidence layer generated — sources page, provenance summary, corrections log.

```bash
python -m studio_ops validate --schemas --naming --links --root-hygiene
python -m studio_ops pipeline package        # NOT BUILT
python -m studio_ops report provenance       # NOT BUILT
```

The evidence layer is generated by hand today, which is a real risk: ADR 0002's promise
is that the bibliography and sources page are *generated, not written*, and a
hand-written one can silently disagree with the records. See
[../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md)
item 6.

## 11 · Publish (no gate)

1. Publish with the sources page, the provenance summary, and an **open corrections
   log**.
2. Publish the takedown route on the episode page — see
   [../runbook/takedown_procedure.md](../runbook/takedown_procedure.md).
3. Provide the finished work to every contributor, knowledge holder, and community that
   informed it, in a form they can actually access, before or at release.
4. Freeze the manifest. Tag the commit.

---

## Re-opening a signed gate

Sometimes necessary; always recorded.

1. Anyone may request a re-open with a stated reason.
2. The gate owner decides.
3. On re-open the gate returns to `pending`, the prior signature is **retained in
   history**, and **every downstream gate signed on the basis of it returns to
   `pending` too.**

That cascade is what makes late changes visible rather than quiet. A change to a locked
script after picture lock is not a small edit, and the framework makes it feel like
what it is.

## Under time pressure

In order of preference, and this order is the protocol:

1. **Narrow the question.** A tighter question needs less evidence.
2. **Lower the register.** `probable` honestly beats `established` falsely.
3. **Cut the sequence.** A shorter production is not a failure.
4. **Delay.**

Not on the list: proceeding on thinner evidence at the same confidence level, or one
person signing two gates. Both are the moves that cannot be undone after publication.
</content>
