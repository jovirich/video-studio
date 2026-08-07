---
title: research — briefs, open questions, fact-checks
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [research-lead]
---

# research

The line's working research layer. Method comes from the pack
([../../../packs/documentary-history/methodology/](../../../packs/documentary-history/methodology/));
what lives here is this line's application of it.

```
research/
├── briefs/          one per scoped research assignment
├── open_questions/  QST-* — what is not known, tracked rather than carried
├── fact_checks/     FCK-* — completed reports, one per production
└── interviews/      interview plans, consent references, transcript pointers
```

Templates: [../../records/_TEMPLATE_research_brief.md](../../records/_TEMPLATE_research_brief.md),
[../../records/_TEMPLATE_open_question.md](../../records/_TEMPLATE_open_question.md),
[../../records/_TEMPLATE_fact_check.md](../../records/_TEMPLATE_fact_check.md).

## Why open questions are a register and not a to-do list

An open question is a **publishable state**. "The record does not tell us" is a
finding about the archive, it belongs to the viewer, and it is usually more
interesting than the hedge that would replace it.

An unregistered open question is different in kind. It sits in one person's head,
survives their week off, and gets resolved under deadline pressure by whoever needs
the sentence to end — which is how a plausible placeholder enters a script.
Registering it converts a private uncertainty into a tracked one with an owner.

Each question records what would resolve it, so the register doubles as the research
queue.

## Interviews

Every interview requires a consent instrument in place **before** recording, not
after: [../../legal/interview_consent.md](../../legal/interview_consent.md). The
instrument covers attribution choice, right of review, right of withdrawal, and the
scope of AI processing — including that the recording will not be used to train or
synthesise a voice.

Recordings are sources and get source records
([../../records/_TEMPLATE_source_record.md](../../records/_TEMPLATE_source_record.md))
at tier T4, with the oral protocol block completed. The protocol block is required by
the schema for oral material, and its `holder_standing` field is the one that matters:
the relationship between the person and the knowledge — lineage, office, training — is
what makes the testimony evidence rather than an anecdote.

## AI in research

Permitted for locating material, summarising documents you have also read, drafting
translations, and structuring notes. **Model output is never a source** — it is T5,
never citable, and every lead is verified against the actual document before it
becomes a claim.
[../../../core/01_provenance_and_ai_disclosure.md](../../../core/01_provenance_and_ai_disclosure.md) §1.

The specific failure: a model produces a fluent, correctly formatted, entirely
fictitious citation, and it survives review because it looks exactly like the real
ones next to it.
