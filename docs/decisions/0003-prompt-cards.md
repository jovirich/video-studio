---
adr: 0003
title: Prompts are versioned records, not strings
status: accepted
date: 2026-08-07
deciders: [visual-director, pipeline-engineer]
supersedes: none
superseded_by: none
---

# ADR 0003 — Prompts are versioned records, not strings

## Context

A prompt kept as a text string in a document, a Discord message, or someone's
clipboard is:

- **unversioned** — nobody knows which variant produced the shot in the cut,
- **unreviewable** — the sensitivity gate has nothing concrete to look at before
  generation,
- **unattributable** — an output cannot be traced to its input six months later,
- **non-inheritable** — style consistency depends on people remembering to paste the
  same block,
- **non-portable** — rewriting for a different vendor means starting over,
- **non-cumulative** — nothing is learned across a season.

For a studio whose defining commitment is provenance, the second and third points
are disqualifying on their own.

## Decision

A prompt is a YAML record validated against
[`prompt_card.schema.json`](../../standards/schemas/prompt_card.schema.json), with:

| Block | Purpose |
|---|---|
| `tool` | Vendor, model, version, and the date its terms were last checked |
| `target` | Episode, sequence, shot, provenance class, and the shot's intent in one sentence |
| `inheritance` | The style block and style anchors inherited; every override carries a stated reason |
| `prompt` | Structured fields — subject, action, setting, period markers, composition, camera, light, palette, texture, mood, negatives |
| `parameters` | Vendor-specific, deliberately unconstrained |
| `inputs` | Reference images with a rights note where third-party |
| `evidence_basis` | **Required** when the class is `reconstruction` |
| `constraints` | Named-person, sacred-material, violence, and remains flags |
| `runs` | Append-only history: seed, outcome, cost, and *why it worked or did not* |
| `review` | Sensitivity and anachronism gate status |

Vendor strings are **rendered** from the structure by
`studio_ops promptlib render`, not hand-written. The same card can target a
different tool by changing one field.

## Consequences

**Positive**

- The sensitivity gate reviews prompts *before* generation, which is the only point
  at which review is cheap. Once a striking image exists, the conversation about
  whether it should exist is much harder.
- Style inheritance is mechanical, which is the only way continuity survives across
  hundreds of shots generated over months.
- `period_markers` as a required-by-convention field directly counters the models'
  strong prior toward generic pan-historical imagery — the specific failure mode
  flagged in `bible/07` §6.
- The `runs[].notes` field makes the library improve. A season of "this worked,
  this did not" is the most valuable artefact the studio will accumulate.
- Cost tracking per card feeds the per-episode generation ceiling.

**Negative**

- Writing a prompt card is slower than typing a prompt. Meaningfully slower.
- Vendor syntax evolves faster than the renderer will. Hence `raw_override`.

**Neutral**

- Requires a renderer per vendor. These are small and live in
  `automation/studio_ops/promptlib/`.

## Escape hatch

`prompt.raw_override` accepts a verbatim string when a tool's syntax cannot be
expressed structurally. It requires a reason in `notes`.

**A rising override rate is the failure signal.** Every override marks a place the
abstraction did not fit; if most cards use it, the structure is wrong for the tools
actually in use and should be revised rather than defended.

## Validation

Reviewed at the end of season one: what fraction of cards used `raw_override`, and
did the `runs` notes actually get written? An empty `runs` history across a season
means the record is being treated as paperwork, and the decision has failed even if
the schema validates.
