---
title: Source and claim registry — method
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# Source and claim registry — method

How evidence becomes something a script can reference and a machine can check.

The canon is [`../02_evidence_and_sourcing.md`](../02_evidence_and_sourcing.md); where
this file and that one differ, that one governs. This is the working method.

> **No records live in this folder.** It holds method only. Actual `SRC-*` and `CLM-*`
> records live at the **line** level — see § Where records physically live.

## The chain

```
   ┌─────────────────────────────────────────────────────────────────┐
   │  THE EVIDENCE                                                   │
   │  <line>/sources/registry/records/SRC-NG-0042.yaml               │
   │  tier · source_type · custody · CRITIQUE · rights                │
   └────────────────────────────┬────────────────────────────────────┘
                                │  cited by, with a locator
                                ▼
   ┌─────────────────────────────────────────────────────────────────┐
   │  THE FACT                                                       │
   │  <line>/sources/registry/claims/CLM-NG-0117.yaml                │
   │  statement · confidence register · evidence[] · independence     │
   └────────────────────────────┬────────────────────────────────────┘
                                │  referenced by ID, never restated
                                ▼
   ┌─────────────────────────────────────────────────────────────────┐
   │  THE SCRIPT                                                     │
   │  .../productions/S01E01_slug/02_script/narration.md             │
   │  "... the walls enclosed a substantial area {{CLM-NG-0117}} ..." │
   └────────────────────────────┬────────────────────────────────────┘
                                │  stripped at render
                                ▼
              narration (clean)  +  citation appendix  +  sources page
```

Read it in both directions. Downward it is a research workflow. Upward it is the
question the studio has to be able to answer in public: *where did that come from?* —
for any frame, at any point in the future, without the original researcher present.

**The script contains references, not facts.** That is the whole design. A footnote
convention does not survive a re-cut, a re-ordering, or a cutdown; a claim ID does,
because the cutdown inherits it and the validator runs on the cutdown too.

## Tiers, in summary

Canon: [`../02_evidence_and_sourcing.md`](../02_evidence_and_sourcing.md) §2.

| Tier | What | Alone sufficient for `established`? |
|---|---|---|
| **T1** | Primary and archival — documents, inscriptions, excavation reports, contemporaneous accounts, provenanced objects, datasets | Yes, with §4's caveats |
| **T2** | Peer-reviewed secondary scholarship | Yes |
| **T3** | Reputable general — catalogue entries, encyclopedias of record, serious journalism | No. `probable` at best. |
| **T4** | Oral testimony, tradition, community knowledge, recorded under the protocol | Sufficient for `traditional`. Never promoted by volume. |
| **T5** | Everything else — undated web pages, aggregators, popular video, **and all language-model output** | **Never citable.** A lead only. |

Two things the table does not say and that matter more than it does:

**The tiers describe what kind of verification a claim needs, not whose knowledge is
worth more.** Oral tradition frequently preserves what written archives never recorded,
and colonial-era T1 documents are often less reliable about African societies than the
T4 testimony of people inside them. A T4 account may contradict a T1 record on screen,
with both stated — often the most valuable thing a production can do.

**Never launder T4 into `established` by finding a T3 that repeats it.** Circular
sourcing through repetition is the most common failure in popular history, and it is
invisible at the point it happens.

T5 has its own document: [`../methodology/using_ai_in_research.md`](../methodology/using_ai_in_research.md).

## Registers and what each demands

| Register | Requirement |
|---|---|
| `established` | ≥2 **independent** sources, at least one T1 or T2 |
| `probable` | ≥1 T1/T2, or ≥2 demonstrably independent T3 |
| `contested` | Sources for **each** position, at tier, with named holders |
| `inferred` | Adjacent evidence recorded, plus a written inference chain |
| `traditional` | ≥1 T4 under protocol, with the holder and the context of transmission named |
| `unknown` | Record what was searched and where, so the next researcher does not repeat it |

`unknown` is a first-class recordable state. Recording it is a result.

## The critique block

**Mandatory on every source record.** `creator_context`, `position_to_know`, and
`interests` are required by
[`source_record.schema.json`](../../../standards/schemas/source_record.schema.json);
`transmission`, `silences`, and `known_disputes` are provided and should be filled
whenever they are not trivially empty.

> A citation is a location, not a warrant.

| Field | The question | The mistake it prevents |
|---|---|---|
| `creator_context` | Who made this, when, for whom? | Treating a document as a neutral window onto events |
| `position_to_know` | What were they actually in a position to observe or record? | An eyewitness to a battle knows one flank; a treasury clerk knows what was recorded, not what was traded |
| `interests` | What interest shaped what was recorded, and how? | Colonial administrators, missionaries, rival dynasties, and modern states all had reasons to shape a record |
| `transmission` | What has happened to it since? | Translation, transcription, restoration, selective preservation, and archival rearrangement all edit the record |
| `silences` | What would this source not have recorded, and what does its absence therefore prove? | Absence of evidence in a record that would never have recorded the thing is not evidence of absence |
| `known_disputes` | Who has challenged its reliability, and on what grounds? | Rediscovering a well-known problem three weeks before delivery |

**A source is not "reliable" or "unreliable". It is reliable *about certain things*.**
The critique block's job is to establish which. Recurring patterns are held in
[`../methodology/bias_register.md`](../methodology/bias_register.md) so they are not
re-derived per source.

Write the critique when you create the record, not later. Reconstructed provenance is
the most common cause of a source record that cannot be defended when challenged.

## The independence check

The single most-skipped step, and the one that lets a false claim survive.

On every evidence entry, `independent_of` lists the sources this one is demonstrably
**not** derived from. Two sources sharing an upstream origin are **one source**.

```yaml
evidence:
  - source: SRC-NG-0042
    locator: "f. 17v"
    supports: fully
    independent_of: [SRC-NG-0043]
  - source: SRC-NG-0043
    locator: "pp. 88–91"
    supports: partially
    independent_of: [SRC-NG-0042]
```

How dependence hides:

| Pattern | Looks like | Is |
|---|---|---|
| Two monographs both citing the same chronicle | Two T2 sources | One source |
| A catalogue entry summarising the scholarship | An independent T3 | The same scholarship |
| Ten holders of the same tradition | Ten T4 accounts | One tradition |
| A translation and its original | Two items | One item, and the translation may have edited it |
| A modern edition and the manuscript it edits | Two items | One item plus an editor's judgement |

**Assert independence deliberately.** The schema does not require `independent_of` —
`evidence[]` requires only `source` and `supports` — and `validate --sources`, which
would check corroboration against the register, is **NOT BUILT**. So today this check
exists only because a researcher performs it and the Research Lead certifies it at
source lock. Nothing else catches it.

## Where records physically live

At the **line**, because they are line-scoped:

```
studios/<studio>/lines/<line>/
  sources/
    archive_landscape.md            what exists, what is reachable, what is not
    registry/
      records/   SRC-*.yaml         the evidence
      claims/    CLM-*.yaml         the facts
  research/
    open_questions/  QST-*.yaml     the gaps
  entities/                         CHR-* LOC-* ORG-* OBJ-* EVT-*
```

Method lives in the pack; records live in the line. That separation is what lets a
second studio adopt this pack unchanged — see
[`../README.md`](../README.md) and
[`../../../docs/architecture/spinning_up.md`](../../../docs/architecture/spinning_up.md).

### IDs

```
SRC-<LINE>-<NNNN>       SRC-NG-0042      line-scoped source
SRC-STUDIO-<NNNN>       SRC-STUDIO-0007  cross-line source
CLM-<LINE>-<NNNN>       CLM-NG-0117      claim (always line-scoped)
QST-<LINE>-<NNNN>       QST-NG-0023      open question
```

Permanent, never reused, never renumbered. A retracted claim keeps its ID and records
what replaced it — deleting a record destroys the audit trail that justifies keeping the
whole system.

Grammar: [`../../../standards/id_system.md`](../../../standards/id_system.md).

> **Allocate IDs from a ledger, not from memory.** `studio_ops new-record` — the
> allocator, which reads the highest existing serial for the (type, scope) pair and
> refuses on a gap-and-collision pattern — is **NOT BUILT**. Records reference each
> other by ID *string*, not by path, so a duplicate ID silently resolves to whichever
> record wins and corrupts the reference graph in a way nothing currently detects. See
> [`../../../docs/architecture/refinements_before_episode_one.md`](../../../docs/architecture/refinements_before_episode_one.md)
> item 2.
>
> Cross-line scoping (`SRC-STUDIO-*`) is designed and untested, and there is no defined
> promotion path from a line-scoped source to a studio-scoped one. Since IDs are
> permanent, that decision is cheap now and a migration later — item 11.

## Working the registry

Full sequence: [`../methodology/research_protocol.md`](../methodology/research_protocol.md).
The parts specific to the registry:

1. **Create the source record before you read the item.** This forces custody, access,
   and rights to be captured while you are looking at it, rather than reconstructed
   later from memory.
2. **Write the critique while the item is in front of you.**
3. **One claim per statement the production will make.** Not one per paragraph, not one
   per source.
4. **Set the register from the evidence**, then check the corroboration requirement —
   in that order. Choosing the register first and then finding sources for it is how
   the discipline inverts.
5. **Assert independence explicitly**, per the table above.
6. **Record every gap as a `QST-*`** with what was searched and where.
7. **Link entities.** Every person, place, polity, and organisation on screen gets a
   record carrying the on-screen name form and why it was chosen. This is what makes
   cross-production consistency mechanical rather than hopeful.

Restricted, embargoed, or community-controlled material:
[`../../../docs/runbook/restricted_records.md`](../../../docs/runbook/restricted_records.md).
The record goes in git; the material never does, in any form. Oral sources additionally
follow [`../methodology/oral_history_protocol.md`](../methodology/oral_history_protocol.md).

## Reporting

All **NOT BUILT**. Listed because they are the specification, and because knowing what
the registry is *for* changes how it is filled in.

| Command | Will produce | Manual equivalent today |
|---|---|---|
| `studio_ops validate --sources` | Walks every `{{CLM-*}}` → claim → source; checks corroboration against the register; checks independence on every `established` claim | Walk it by hand at fact-check and record the walk as the `FCK-*` report |
| `studio_ops report bibliography --episode <code>` | The citation appendix and the published sources page, generated from the records | Hand-compiled — and it will silently disagree with the records, which is the risk ADR 0002 was written to remove |
| `studio_ops report source-coverage` | Claims per source, sources per claim, and which claims rest on a single source | Read the registry |
| `studio_ops report dependents --claim <id>` | Everything referencing a claim — needed when a claim is corrected or retracted | Grep the scripts and on-screen text |
| `studio_ops report open-questions` | Every `QST-*` with status and what was searched | Read the folder |

The gap matters more than it looks. ADR 0002's most concrete promise is that the
bibliography and sources page are **generated, not written**; until the compiler exists,
they are written, and a hand-written sources page that disagrees with the registry is
the exact failure the record graph was built to prevent. Tracked as item 6 of the
refinements list.

## When the evidence runs out

In order. This order is the protocol.

1. Record an open question.
2. Change the **register** down, not the claim up.
3. If the sequence cannot survive the honest register, **cut the sequence**.
4. Never fill the gap with a plausible reconstruction stated as fact. **Never ask a
   model to fill it.**

Step 4 is the reason all of this exists.
</content>
