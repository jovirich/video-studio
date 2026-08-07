---
title: Research — Nigeria line
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# Research

Where the work of this line actually happens. Everything downstream — script, prompts,
images, sound, cut — is a rendering of what is decided here, and no amount of craft
later recovers from a shortcut taken at this stage.

Maturity: **DESIGNED** for structure, **NOT STARTED** for content. Every register
below is empty. No brief exists, no question has been opened, no fact has been
checked, no interview has been recorded.

## 1. The method is the pack's

This line does not have its own research method and must not grow one. The authority
is:

| Document | Governs |
|---|---|
| [research_protocol.md](../../../../../packs/documentary-history/methodology/research_protocol.md) | The eight-stage sequence from a question to a source-locked research pack |
| [02_evidence_and_sourcing.md](../../../../../packs/documentary-history/02_evidence_and_sourcing.md) | Source tiers, corroboration, the claim ID chain, what to do when the evidence runs out |
| [bias_register.md](../../../../../packs/documentary-history/methodology/bias_register.md) | The recurring distortions in the surviving record, recorded once so they are not re-derived per source |
| [oral_history_protocol.md](../../../../../packs/documentary-history/methodology/oral_history_protocol.md) | T4 sources — approach, consent, recording, transcription, restricted material |
| [01_editorial_standards.md](../../../../../packs/documentary-history/01_editorial_standards.md) | Certainty registers and attribution discipline |

Read the bias register **before** writing a critique block, not after. Its purpose is
that a researcher who does not account for these patterns will reproduce them
faithfully while believing they are simply following the evidence — and the evidence
will agree with them, because the evidence is what the patterns produced.

What is line-specific — which archives, which languages, which advisors, which gaps —
belongs here and in [../sources/archive_landscape.md](../sources/archive_landscape.md).
Nothing in this folder restates the pack.

## 2. The register folders

Four registers. All are **currently empty**, and each empty folder is a statement
about where this line is rather than a gap in the scaffolding.

### [briefs/](briefs/)

One research brief per production, written **before** searching. An unframed search
returns whatever is easiest to find, and what is easiest to find is a product of who
catalogued, digitised, and translated — not of where the history was.

A brief states the question and its sub-questions, what would count as an answer to
each, **what would falsify the working assumption**, the periods and peoples in scope,
the known scholarly disputes, and the languages the evidence is likely to be in.

That last field drives budget and schedule and is the one most often discovered late.
If the relevant material sits in a language nobody on the production reads, or in an
oral corpus rather than a document, the plan needs a translator or a knowledge holder
from the outset — engaging one in week nine is a re-plan, not an addition.

Template: [templates/records/](../../../../../templates/records/) — **NOT BUILT**.
Naming: `<production-code>_<slug>.md`.

### [open_questions/](open_questions/)

`QST-NG-*` records. **Gaps are findings, and this register is where they are kept.**

An open question records what was asked, what was searched, where, in what languages,
and what was not reachable. Its value is symmetric: it stops the next researcher
repeating a fruitless search, and it stops a gap being quietly filled with something
plausible. It is also frequently the most interesting material in an episode — the
shape of what did not survive is itself historically informative
([bias_register.md](../../../../../packs/documentary-history/methodology/bias_register.md)
§ Survival bias).

A question is closed by being answered *or* by being recorded as unanswerable with the
search recorded. It is never closed by being dropped, and never by a model's answer.

At source lock, no open question may be load-bearing for a claim at `established`.

### [fact_checks/](fact_checks/)

`FCK-NG-S01E01-*` records — episode-scoped, one per fact-check pass. Owned by the
Research Lead, who signs the fact-check gate.

The check runs against the **claim records**, not against the script's plausibility
and not against the researcher's memory of the source. Checking a figure against the
script that quoted it is the failure mode that produces a correction entry beginning
"a transcription error survived fact-check because…".

Independence is checked explicitly, not assumed from source count. A claim repeated
across five sources that all trace to one original is one source, and circular
sourcing through repetition is the most consequential failure in popular history
precisely because it looks like overwhelming corroboration.

### [interviews/](interviews/)

Interview and oral-history working material: schedules, consent status, interpreter
arrangements, transcripts in progress, review status.

The protocol is
[oral_history_protocol.md](../../../../../packs/documentary-history/methodology/oral_history_protocol.md)
and it is followed in full. The steps that are skipped when a schedule is tight, and
that must not be:

- The **approach route** is agreed with the Cultural Advisor first. An unannounced
  approach to a knowledge holder can itself be a breach.
- The boundary around **restricted knowledge** is established with the advisor
  *before* the conversation. Asking for restricted knowledge puts the holder in an
  impossible position: refusing a guest is costly, disclosing is a breach.
- **Consent covers AI processing explicitly** — transcription, translation, any voice
  handling — or it is not valid for this studio's purposes.
- **Fees are agreed and budgeted before the approach**, and paid on the holder's
  terms rather than the studio's.

Recordings themselves never live in git. They go to the asset store against the source
record's ID; restricted material does not enter the general store at all.

## 3. Where research output goes

| Output | Destination |
|---|---|
| A source, with its critique block | [../sources/records/](../sources/README.md) — `SRC-NG-*` |
| A fact the production will state | [../sources/claims/](../sources/README.md) — `CLM-NG-*`, with a confidence register |
| A person or collective actor | [../characters/](../characters/README.md) — `CHR-NG-*` |
| A place | [../locations/](../locations/README.md) — `LOC-NG-*` |
| A dated event | [../timeline/](../timeline/README.md) — `EVT-NG-*` |
| A language decision | [../languages/](../languages/README.md) |
| A gap | `open_questions/` — `QST-NG-*` |
| Where the evidence could exist at all | [../sources/archive_landscape.md](../sources/archive_landscape.md) |

Create the **source record first, then read**. Creating it first forces the custody,
access, and rights fields to be captured while the item is in front of you, rather
than reconstructed later from memory — and reconstructed provenance is the most common
reason a source record cannot be verified when it is challenged.

IDs are allocated by the toolkit, never by hand
([standards/id_system.md](../../../../../standards/id_system.md)). The allocator is
**NOT BUILT**; until it is, any hand-allocated ID is recorded with the risk noted,
because silent ID reuse corrupts the audit trail irreversibly.

## 4. Under time pressure

The order is fixed and it is the protocol, not a preference:

1. **Narrow the question.** A tighter question needs less evidence.
2. **Lower the register.** `probable` honestly beats `established` falsely.
3. **Cut the sequence.** A shorter production is not a failure.
4. **Delay.**

Not on the list, and never available: proceeding on thinner evidence while keeping the
same confidence level. That is the one move that cannot be undone after publication,
and it is the move that turns a documentary into fiction with a serious voiceover.

## 5. Status

Nothing has started. There is no research lead — condition 1 of three blocking this
line from opening ([../README.md](../README.md) §2), and the condition that must be
satisfied before any of the above is anyone's responsibility.
