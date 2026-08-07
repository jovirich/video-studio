---
title: 02_script — outline to shooting script
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [story-producer]
---

# 02_script

Where the evidence becomes an argument with a shape. Four documents in sequence,
each one narrower than the last, plus the sheet that makes the VO session possible.

## What goes here

| File | Template | What it is |
|---|---|---|
| `outline.md` | [_TEMPLATE_outline.md](_TEMPLATE_outline.md) | The argument in sections, before any prose |
| `beat_sheet.md` | [_TEMPLATE_beat_sheet.md](_TEMPLATE_beat_sheet.md) | Beat-by-beat, with the claim each beat rests on and the evidence gap it exposes |
| `narration_v<NN>.md` | [_TEMPLATE_narration.md](_TEMPLATE_narration.md) | The spoken text, every factual statement carrying a claim reference |
| `shooting_script_v<NN>.md` | [_TEMPLATE_shooting_script.md](_TEMPLATE_shooting_script.md) | Narration against picture, sequence by sequence |
| `vo_record_sheet.md` | [_TEMPLATE_vo_record_sheet.md](_TEMPLATE_vo_record_sheet.md) | Every proper noun, its IPA, its reference recording, and who verified it |

Versions are numeric and zero-padded: `narration_v01.md`, `narration_v02.md`. Never
`_final`. A previous version is never overwritten, because "what did the script say
when the fact-check ran" is a question that gets asked.

## The mechanism that makes this stage work

**A script references claims. It does not contain facts.**

Every factual statement in narration carries an inline claim reference:

```
TBD — a clause asserting one fact. {{CLM-XX-0000}} TBD — a second clause,
resting on different evidence. {{CLM-XX-0001}}
```

The reference follows the clause it supports, not the paragraph. A
paragraph-level reference cannot say which sentence the source actually backs,
which is exactly what fact-check needs to know.

Double braces, stripped at render. The braces are not decoration — they are what
`studio_ops validate --sources` reads to check that every asserted fact resolves to
a claim record at the required tier, and what `studio_ops report dependents` reads *(NOT BUILT)*
to answer "if this source is withdrawn, which lines of narration die".

A sentence with a date, a name, a figure, or a superlative and no claim reference is
a fact the script is asserting on its own authority. There is no such authority. See
[_TEMPLATE_narration.md](_TEMPLATE_narration.md) for the convention in use.

## Before this stage starts

- **Source lock is signed.** The registry is fixed. Writing before source lock
  produces a script that then goes looking for evidence to support it, which is the
  inverse of the process and reliably finds something.

## Before this stage can be left

The **script lock** gate is signed by the Story Producer, certifying:

1. Narration and shooting script are final.
2. **Every factual statement carries a claim ID** that resolves.
3. **The certainty register matches the evidence.** A `probable` claim spoken as
   established is a failure of this gate, not of the claim record.
4. **No prohibited language pattern remains** —
   [../../../standards/prohibited_language.md](../../../standards/prohibited_language.md).
5. The VO record sheet is complete: every proper noun has IPA and a reference
   recording from a speaker of the language.

## What script lock unblocks, and why the order matters

Script lock blocks [03_storyboard](../03_storyboard/), [04_prompts](../04_prompts/),
and [05_assets](../05_assets/). **Generation does not begin before it.**

The reason is not tidiness. Generated imagery is cheap and striking, and a
production that has generated first will write toward the footage it happens to
have. The gate exists so that the argument determines the pictures rather than the
other way round, and it is the gate most often argued about under schedule pressure
for exactly that reason.
