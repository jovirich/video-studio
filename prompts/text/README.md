---
title: Text and reasoning models
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead, story-producer]
---

# Text and reasoning models

## The rule that governs this entire folder

> **A language model is never a source.**

Under packs with an evidence chain it is tier **T5** — usable to find a lead, never
to support a claim. Under every other pack the same principle applies in its own
terms: a model may not introduce a fact, a date, a name, a figure, or a product claim
that a human has not verified against something real.

This is the rule most likely to erode under deadline, which is why it is stated in
the schema as well as in prose: a T5 source may support zero claims, and validation
fails if it does.

Everything in this folder is therefore **assistance** tooling. There are no research
*authority* templates here, deliberately.

## Vendors

| Vendor | Typical use |
|---|---|
| [claude](claude/) | Long-context document work, structural critique, drafting assistance |
| [gpt](gpt/) | General assistance, structured extraction |
| [gemini](gemini/) | Long context, multimodal document review |
| [llama](llama/) | Local and self-hosted, where material must not leave the building |
| [perplexity](perplexity/) | Search with citations — **follow every citation to the actual document** |

Perplexity-style tools deserve a specific warning: a returned citation is a *pointer*,
not a verification. The tool can cite a real document that does not say what the
summary claims. Open the document.

## Legitimate uses

| Task | Boundary |
|---|---|
| **Locating material** | Suggests where to look. You then look. |
| **Summarising a document you have read** | Never a document you have not. |
| **Translation drafting** | Human-reviewed always; translator credited. |
| **Structuring notes** | The structure is a proposal. |
| **Structural critique of a script** | Does it hold? Where does attention drop? |
| **Alternative phrasings** | The claims stay yours. |
| **Readability and register checks** | Useful and low-risk. |
| **Extraction into records** | Pulling names or dates from a document *you* have read, into a form you then verify. |
| **Devil's advocate** | "What is the strongest case against this reading?" — one of the highest-value uses. |
| **Adversarial review** | "Which statements here would a hostile expert attack first?" |

## Prohibited uses

- **Filling an evidentiary gap.** If the research does not know, the model does not
  get to decide.
- **Generating a citation.** Models fabricate plausible references with complete
  confidence. Every citation is verified against the actual item.
- **Writing narration that asserts fact.** Assistance with phrasing is fine; the
  claims are the writer's.
- **Deciding a contested question.** Where scholars disagree, a model's synthesis is
  an average of its training data, not a judgement.
- **Processing restricted material** on a third-party endpoint. Unpublished archival
  scans, interview recordings, and community-controlled material never leave the
  building without a no-training contract and the source's permission. Use a local
  model for that.

## Data handling

- Contributor personal data never enters a prompt.
- Unpublished material goes to a local or self-hosted model, or nowhere.
- The vendor's training-on-inputs position is recorded in the
  [model terms register](../../rights/permissions/model_terms_register.md), per plan
  tier, with the date checked.

## Prompting for research assistance

Two habits that materially change output quality:

**Ask for the search, not the answer.**
> ✅ "What kinds of primary sources would document X, and which institutions typically hold them?"
> ❌ "When did X happen?"

The first produces a research plan you can execute. The second produces a confident
sentence you now have to verify anyway — and which will anchor your thinking whether
or not you meant it to.

**Ask what would falsify it.**
> "What evidence would show this reading is wrong, and where would it be found?"

This is the use that most improves the work, and it is underused because it is less
satisfying than being told an answer.
