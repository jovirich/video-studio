---
title: Architecture evolution log
status: active
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer, showrunner]
---

# Architecture evolution log

A running record of how this repository's architecture changed, why, and what it
cost. This is not a changelog — [CHANGELOG.md](../../CHANGELOG.md) records *what
shipped*. This records *what we learned about the shape of the thing*.

## Why track this separately

Three specific failures this log exists to prevent:

1. **Re-litigating settled decisions.** Six months in, someone proposes flattening
   the studio/line split. Without a record of why it exists, that argument is fought
   from scratch every time — usually by whoever is loudest that week.
2. **Losing the reason a constraint exists.** A rule whose rationale is forgotten
   becomes a rule people route around. Every entry here answers "what breaks if we
   stop doing this?"
3. **Repeating an abandoned approach.** Reversals are recorded as prominently as
   adoptions, with what actually went wrong.

## Relationship to other records

| Record | Answers |
|---|---|
| [CHANGELOG.md](../../CHANGELOG.md) | What changed in this release? |
| [bible/12_amendment_log.md](../../bible/12_amendment_log.md) | What changed in editorial canon, and who signed? |
| [docs/decisions/](../decisions/) | What was decided, given what options? (ADRs — one per decision, immutable once accepted) |
| **This file** | How has the structure evolved, and what did each move teach us? |

An ADR is a *decision at a point in time*. This log is the *narrative across them* —
including the ones that were later found wrong.

## Entry format

```
## AE-NNN — <title>
**Date:** YYYY-MM-DD · **Kind:** adoption | revision | reversal | deprecation | scaling
**Scope:** <which parts of the tree>
**ADR:** <link, or "none — mechanical">
**Trigger:** <what forced this. A concrete event, not "we felt it would be cleaner".>
**Change:** <what is structurally different now>
**Cost:** <migration effort, records touched, work invalidated>
**What it protects:** <what breaks if this is undone>
**Watch for:** <the signal that this decision is going wrong>
```

The **Watch for** field is the important one and the easiest to skip. An
architectural decision without a stated failure signal cannot be evaluated later —
it can only be defended or attacked on taste.

## Architecture versions

The repository's structural contract is versioned independently of its content.

| Version | Shape | Status |
|---|---|---|
| `arch-1` | Studio → production line → episode; records-first evidence layer; prompt cards as records; nine gates | current |

A new `arch-N` is declared when a change invalidates existing records or breaks the
folder contract. Everything smaller is an entry below without a version bump.

---

# Log

## AE-001 — Studio, not show

**Date:** 2026-08-07 · **Kind:** adoption
**Scope:** whole tree
**ADR:** [0001-studio-not-show.md](../decisions/0001-studio-not-show.md)

**Trigger:** The initial brief was a Nigerian documentary series. Building it as a
single show would put Nigeria-specific material (advisory board, language guides,
visual identity) in the same tier as universal material (evidence rules, schemas,
prompt library) — and every later country would either fork the repo or contaminate
Nigeria's namespace.

**Change:** Three tiers. Studio holds what is true for all lines. A production line
holds what is true for one region. An episode holds what is true once. Nigeria is
`productions/ng-nigeria/`, line 01.

**Cost:** One extra path segment on every line-scoped file. Contributors must know
which tier a change belongs to — mitigated by the branch naming convention.

**What it protects:** Adding a country becomes `studio_ops new-line` instead of a
refactor. More importantly, it forces the question "is this rule universal or
regional?" at write time, which is when it is cheap to answer.

**Watch for:** Studio-level documents accumulating Nigeria-specific examples. If
`bible/` starts saying "for instance, in Yoruba…", the tiers are leaking and the
second line will inherit assumptions that do not hold.

---

## AE-002 — Evidence as a record graph, not prose

**Date:** 2026-08-07 · **Kind:** adoption
**Scope:** `sources/`, `standards/schemas/`, script format
**ADR:** [0002-claims-as-records.md](../decisions/0002-claims-as-records.md)

**Trigger:** The known failure mode of AI-assisted history is that generation
outruns verification. A footnote convention does not survive a re-cut; a script with
facts embedded in prose cannot be mechanically checked.

**Change:** Scripts contain `{{CLM-*}}` references, not facts. Claims are records
with confidence registers and evidence arrays. Sources are records with mandatory
critique blocks. CI walks the chain.

**Cost:** Substantially more upfront research overhead per minute of screen time.
Writers cannot draft freely — they draft against a claim registry.

**What it protects:** The ability to answer "where did that come from?" for any
frame, at any point in the future, without the original researcher present.

**Watch for:** Claims being created retroactively to satisfy the validator, with
`evidence` arrays pointing at whatever was nearest. If claim records start appearing
*after* script drafts in the git history, the discipline has inverted and the
validator is being farmed rather than served.

---

## AE-003 — Prompt cards as first-class records

**Date:** 2026-08-07 · **Kind:** adoption
**Scope:** `prompts/`, `standards/schemas/prompt_card.schema.json`
**ADR:** [0003-prompt-cards.md](../decisions/0003-prompt-cards.md)

**Trigger:** Prompts kept as text strings in a doc are unversioned, unreviewable,
untestable, and impossible to attribute an output to six months later.

**Change:** A prompt is a YAML record with structured fields, an inheritance chain
from the line's style block, an evidence basis where it depicts reconstruction, and
an append-only `runs` history recording seed, outcome, cost, and — critically — why
it worked or did not.

**Cost:** Writing a prompt takes longer than typing one. Vendor-specific syntax has
to be rendered rather than written.

**What it protects:** Reproducibility, continuity across shots, the sensitivity gate
having something concrete to review *before* generation, and a prompt library that
improves rather than accumulating.

**Watch for:** Heavy use of `prompt.raw_override`. Every override is a place the
structure did not fit; a rising override rate means the abstraction is wrong for the
tools actually being used.

---

## AE-004 — Templates centralised at studio level

**Date:** 2026-08-07 · **Kind:** adoption
**Scope:** `templates/`
**ADR:** none — mechanical

**Trigger:** The obvious layout puts an episode template inside each production
line. With two lines that is two copies; with five it is five, and they diverge
silently.

**Change:** One canonical `templates/episode/` and `templates/production_line/` at
studio level. `studio_ops` scaffolds from them. Production lines contain only real
work.

**Cost:** A line cannot customise its episode skeleton without either changing the
studio template or accepting drift.

**What it protects:** A structural change to the episode pipeline lands everywhere
at once.

**Watch for:** A line needing a stage the template does not have. That is a signal
to add an optional stage to the template, not to fork it.

---

## AE-005 — Nine gates, distinct owners

**Date:** 2026-08-07 · **Kind:** adoption
**Scope:** `ops/`, `episode.schema.json`

**Trigger:** A small team naturally collapses review into "the showrunner watches
it". That works until the showrunner is the person who wrote the thing.

**Change:** Nine gates — greenlight, source lock, script lock, fact-check,
sensitivity, rights, picture lock, audio lock, technical QC — each with a named role
owner and a checklist. No person signs two gates on the same episode. The Cultural
Advisor's hold cannot be released by the Showrunner alone.

**Cost:** Requires at least four distinct people to ship an episode. This is a real
constraint on a small team and is the item most likely to be quietly abandoned.

**What it protects:** The one structural check on the Showrunner's authority, in the
place where being wrong harms people outside the studio.

**Watch for:** The same name in two gate signatures. `studio_ops validate --canon`
should flag it; if it starts being flagged regularly, the studio has outgrown its
staffing, not its process.

---

<!-- New entries appended below, newest last. Never edit an existing entry —
     supersede it with a new one of kind `revision` or `reversal`. -->
