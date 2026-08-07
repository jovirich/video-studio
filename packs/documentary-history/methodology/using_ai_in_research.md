---
title: Using AI in research
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead, cultural-advisor]
---

# Using AI in research

The rules for using language models in research under this pack.

Referenced from [`../../../prompts/text/README.md`](../../../prompts/text/README.md)
and [`research_protocol.md`](research_protocol.md). Canon:
[`../02_evidence_and_sourcing.md`](../02_evidence_and_sourcing.md) §2 and
[`../../../core/01_provenance_and_ai_disclosure.md`](../../../core/01_provenance_and_ai_disclosure.md)
§1.

This pack is not squeamish about generative tools — the studio uses them heavily and
says so loudly. The position is that the technique is legitimate precisely to the
degree that it is disclosed and bounded. This document is the boundary for research.

## The rule

> **A language model is never a source.**
>
> Model output is tier **T5**. T5 is **never citable**. A model may help you find
> something; it may never be the thing you found.

Not "usually not". Not "unless it is confident". Not "unless it gave a citation".
Never.

The reason is specific to this genre and to this moment. The characteristic failure of
AI-assisted documentary is that **generation is fast and verification is slow**.
Everything else in the pipeline has been accelerated; checking has not. If model output
could support a claim, the evidence chain would be complete on paper and empty in fact,
and the studio would be producing fiction with a serious voiceover — and would not know
it, because everything would validate.

There is also a mechanical reason. A model produces a *plausible* continuation, and
plausibility is exactly the property this pack is built to distrust. A wrong claim that
sounds wrong gets challenged. A wrong claim that sounds right becomes history.

## Why the rule is in the schema as well as in prose

[`source_record.schema.json`](../../../standards/schemas/source_record.schema.json)
encodes it directly. A source record whose `tier` is `T5` has `supports_claims`
constrained to `maxItems: 0`:

```json
{
  "if":   { "properties": { "tier": { "const": "T5" } }, "required": ["tier"] },
  "then": { "properties": { "supports_claims": { "maxItems": 0 } } }
}
```

A T5 record may exist — as a lead, a note, a pointer worth chasing. It may support
**zero** claims, and a record that tries to support one fails validation.

**The prose and the schema say the same thing on purpose, because this is the rule most
likely to erode under deadline.** Every other rule in this pack degrades visibly when
it is broken: an unwritten critique block is an empty field, a missing consent record is
a missing file, an unsigned gate is an unsigned gate. This one degrades *invisibly*. A
researcher at 1am, one claim short, with a model that has just produced a fluent and
entirely reasonable paragraph, is not committing fraud — they are tired, and the
paragraph is probably right, and nobody will ever know.

A rule that depends on nobody being tired is not a rule. Stating it in the schema means
the check happens at a moment when tiredness is irrelevant: the validator does not care
what time it is, and a researcher who has to *defeat* a schema in order to cite a model
is doing something they cannot later describe as an oversight.

This is the same reasoning as the gate framework's separation of duties, and the same
reasoning as prompt cards being reviewed *before* generation. Wherever the honest path
and the fast path diverge under pressure, the structure has to hold rather than the
person.

**Applies equally to search tools that return citations.** A returned citation is a
*pointer*, not a verification — the tool can cite a real document that does not say
what the summary claims, and this happens often enough that it should be assumed rather
than checked for. Open the document. If you cannot open it, you do not have it.

## Permitted uses

All of these have the same shape: the model operates on material **you** have, or
proposes work **you** then do. None produces evidence.

| Use | What it is | The boundary |
|---|---|---|
| **Locating material** | "What kinds of primary sources would document X, and which institutions typically hold them?" | It suggests where to look. You then look. Its list of institutions is a lead; each one is verified before it appears anywhere. |
| **Summarising what you have read** | Condensing a document you have in front of you | Never a document you have not read. A summary of a document you have not read is model output about a title. |
| **Translation drafting** | A first pass on a text you hold | Human-reviewed always; the translator is named and credited. Never for restricted material on a hosted endpoint. Transcribe in the original first, then translate — never straight into English. |
| **Structuring** | Organising your notes, proposing an outline, extracting names and dates from a document you have read into a record form you then verify | The structure is a proposal. The content is yours. |
| **Adversarial critique** | "Which statements here would a hostile expert attack first?" "What is the strongest case against this reading?" | One of the highest-value uses. It produces questions, which are safe; answers are not. |
| **"What would falsify this?"** | "What evidence would show this reading is wrong, and where would it be found?" | The single most useful prompt in research. Its output is a search plan. |
| **Readability and register checks** | Does the prose hold? Where does attention drop? | Low risk, genuinely useful. The claims stay yours. |

## Prohibited uses

| Prohibited | Why |
|---|---|
| **Filling an evidentiary gap** | If the research does not know, the model does not get to decide. The honest moves are: narrow the question, lower the register, cut the sequence, delay. Never: proceed on thinner evidence at the same confidence. |
| **Generating a citation** | Models fabricate plausible references with complete confidence — correct-looking authors, correct-looking journals, correct-looking page ranges, for a work that does not exist. Every citation is verified against the actual item. |
| **Deciding a contested question** | Where scholars disagree, a model's synthesis is an average of its training data weighted by what was written in English and digitised — which for African history is a specific and knowable bias, not a neutral one. Record `contested` with named positions instead. |
| **Writing narration that asserts fact** | Help with phrasing is fine; the claims are the writer's. Every fact in a script carries a claim ID regardless of who typed the sentence. |
| **Processing restricted material on a third-party endpoint** | Unpublished archival scans, interview recordings, and community-controlled material never leave the building without a signed no-training contract **and** the source's permission — both, not either. See below. |
| **Cross-checking a claim against the model** | Asking "is this right?" feels like verification and is not. A model agreeing with you is not corroboration; it is a second draw from the same distribution that produced the doubt. |

## Data handling

| Rule | Detail |
|---|---|
| **Restricted material: local models only** | No transcription, translation, summarisation, or OCR on a hosted endpoint. A researcher working with restricted material needs a local model on their own machine *before* the interview. Arrange it at Stage 1 of the research protocol, not after. |
| **Contributor personal data never enters a prompt** | Names, contacts, locations, and anything that identifies an anonymised contributor. |
| **Consent must cover AI processing explicitly** | Consent that does not state the AI-processing scope is **not valid for this studio's purposes**. Someone who agreed to be recorded did not thereby agree to have their voice pass through a vendor's endpoint. |
| **The recording is never used to train or synthesise a voice** | Stated on the consent form, and binding regardless. |
| **Vendor terms are recorded per tool and per plan tier** | Whether the vendor trains on inputs, and whether it can be disabled, in the model terms register, with the date checked. Re-checked before every delivery — terms change without notice and a delivered master is not easily recalled. |

Procedure and the withdrawal path:
[`../../../docs/runbook/restricted_records.md`](../../../docs/runbook/restricted_records.md).
Oral sources additionally follow
[`oral_history_protocol.md`](oral_history_protocol.md), whose §7 governs restricted
knowledge disclosed in error: stop, do not transcribe further, flag it, raise it with
the Cultural Advisor — and the default is that it is not used.

If a leak has already happened, go to
[`../../../docs/runbook/incident_response.md`](../../../docs/runbook/incident_response.md)
immediately. Assume the material is permanently disclosed from the first minute and act
on that assumption, rather than working toward it.

## The two habits that materially improve output

Everything above is a constraint. These two are the reason a researcher should use
these tools at all.

### 1. Ask for the search, not the answer

> ✅ *"What kinds of primary sources would document a fourteenth-century trade dispute
> in this region, which institutions typically hold that class of material, and in what
> languages would it survive?"*
>
> ❌ *"When did the dispute happen?"*

The first produces a research plan you can execute, in a form you can check. The second
produces a confident sentence you now have to verify anyway — and which will **anchor
your thinking whether or not you meant it to**. That anchoring is the real cost and it
is not recoverable by being careful: once you have read a date, you are looking for
confirmation of it, and confirmation is much easier to find than refutation.

The reframing also surfaces the thing that most often derails a research plan: the
languages the evidence is actually in. If the material is in Arabic, Ajami, Portuguese,
German, or an unwritten oral corpus, you need a translator or a knowledge holder from
the outset, not as a late and expensive discovery.

### 2. Ask what would falsify it

> *"What evidence would show this reading is wrong, and where would it be found?"*
>
> *"What is the strongest scholarly case against this interpretation, and who makes
> it?"*
>
> *"What would this source not have recorded, and what does its silence therefore not
> prove?"*

This is the use that most improves the work, and it is underused precisely because it
is less satisfying than being told an answer. It is also the use where a model's
weakness — producing plausible material rather than true material — is harmless, because
you are asking for *hypotheses to test*, not conclusions to adopt. A fabricated
counter-argument that turns out not to exist costs you an hour. A fabricated citation
that survives to air costs the studio its credibility.

Falsification-first also matches how the rest of the pack works: the research brief
states what would falsify the working assumption, the critique block asks what a source
was *not* in a position to know, and the corroboration rule asks what a source is
demonstrably *not* derived from. The whole method is built on the question this prompt
asks. Asking it of a model early is cheap; asking it of yourself after picture lock is
not.

## Disclosure

Generative tools used in research are named in the production's credits by category,
per [`../../../core/01_provenance_and_ai_disclosure.md`](../../../core/01_provenance_and_ai_disclosure.md)
§3. "Assistance with locating and structuring material" is an honest description of the
permitted uses and is what the credit should say.

What is never disclosed, because it never happens: that a model supported a claim.
There is no honest way to write that line, which is a good test of the rule.
</content>
