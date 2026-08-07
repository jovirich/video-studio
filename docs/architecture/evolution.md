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
| [bible/12_amendment_log.md](../../core/05_amendment_log.md) | What changed in editorial canon, and who signed? |
| [docs/decisions/](../decisions) | What was decided, given what options? (ADRs — one per decision, immutable once accepted) |
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
| `arch-1` | Studio → production line → episode; records-first evidence layer; prompt cards as records; nine gates | superseded by `arch-2` |
| `arch-2` | **Platform → studio → line → production**; core canon + genre canon packs; gate *set* declared by pack | current |

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

**What it protects:** Adding a country becomes `studio_ops new-line` instead of a *(NOT BUILT)*
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

## AE-006 — Platform and canon packs; `arch-1` → `arch-2`

**Date:** 2026-08-07 · **Kind:** revision · **Supersedes:** AE-001 in part
**Scope:** whole tree — `bible/` split, `productions/` relocated, two tiers added
**ADR:** [0005-platform-and-canon-packs.md](../decisions/0005-platform-and-canon-packs.md)

**Trigger:** A direct question during the initial build: *"What if we want to create
other things outside this studio? I thought we'd set up a platform that could make
different types of videos. Do we need to recreate the whole repo?"*

Under `arch-1` the honest answer was **yes, largely**. The repository root *was* a
historical-documentary studio. `bible/` mixed universal rules (AI disclosure, rights,
delivery) with genre rules (source tiers, narrative doctrine, cultural sensitivity),
so a narrative short or a brand film would have inherited an evidence chain it could
not satisfy and a gate set that made no sense for it. The only routes were to fork
the repo or to bolt exemptions onto canon — and canon that routinely grants
exemptions stops being canon.

AE-001's diagnosis was right; its abstraction was one tier too shallow. It separated
*region* from *studio* but left *genre* fused to the platform.

**Change:**

1. **Two tiers inserted.** Platform → studio → line → production.
2. **`bible/` split three ways by what each rule is actually true of:**
   - universal → [`core/`](../../core/) (provenance and AI disclosure, rights,
     distribution, gate framework, amendment log)
   - genre → [`packs/documentary-history/`](../../packs/documentary-history/)
     (editorial standards, evidence, narrative, visual, sound, sensitivity,
     localisation, methodology)
   - studio → [`studios/african-history/bible/`](../../studios/african-history/bible/)
     (charter, corrections, amendments)
3. **Canon packs introduced.** A studio declares one pack; the pack supplies the
   editorial rules *and the gate set*. Core defines what a gate is; the pack says
   which gates exist. `_TEMPLATE_pack/` scaffolds new genres.
4. **Precedence made explicit:** `core > pack > studio > line > production`. A lower
   layer may tighten, never loosen.
5. **Relocations:** `productions/ng-nigeria/` → `studios/african-history/lines/ng-nigeria/`;
   `sources/permissions/` → `rights/`; `research/methodology/` → the pack;
   `brand/` → the studio; `templates/episode/` → `templates/production/`.
6. **Platform de-branded.** Nothing in `core/`, `standards/`, `prompts/`,
   `templates/`, or `automation/` names African history.

**Cost:** Roughly 30 files moved and all cross-links rewritten, done in one pass
before any production existed. One extra path segment on line-scoped files. Four
tiers is more to learn than three, and with one studio it reads as over-engineering.
Nigeria's paths got longer for no immediate benefit.

Doing this after episode one would have cost an order of magnitude more, because
every claim ID, asset path, and locked record would have moved with it.

**What it protects:** The platform can host genres with incompatible obligations
without either compromising. A brand film gets no fake fact-check gate; a history
documentary cannot skip a real one. Adding a genre is `new-pack`, not a fork.

**Watch for:** Three signals, in order of seriousness.

1. **Studio names appearing in platform-level files.** If `core/`, `standards/`, or
   `prompts/` starts referencing African history, the tiers are leaking and the
   second studio will inherit assumptions that do not hold. Grep for it.
2. **A second pack that is 80% copy of the first.** That means the shared material
   belonged in core, and the split was made in the wrong place.
3. **Packs requesting core exemptions.** One is a signal core is over-reaching; a
   pattern means core was written from documentary assumptions rather than universal
   ones.

**Reflection:** This is the change AE-001 should have been. It was caught because
someone asked what the architecture could not do, rather than admiring what it could
— which is the only question that finds this class of error before it is expensive.

---

## AE-007 — Architecture freeze; continuity registry; laboratory production

**Date:** 2026-08-07 · **Kind:** scaling (constraint, not expansion)
**Scope:** whole tree — a stop on further structural work, plus two additions
**ADR:** none — this is a decision about *pace*, not about shape

**Trigger:** A review of the repository at roughly 400 files concluded that the
conceptual design was sound and that the immediate risk had inverted: *"the immediate
risk isn't bad architecture — it's over-engineering before we prove generation
quality."* The instruction was to freeze expansion, reconcile documentation with
implementation, add a continuity system, and prepare for an experimental production.

That reading is correct and the evidence for it is in this repository's own status
ledger. Every architectural claim here is **DESIGNED**. Nothing is **TESTED**. The
schemas have never validated a real record; the continuity mechanisms have never been
drift-tested; no gate has ever been signed. Continuing to add structure would have
increased the amount of untested design without increasing confidence in any of it.

**Change:**

1. **Freeze.** No new tiers, no new packs, no new canon documents until EXP-001
   reports. The freeze is on *structure*, not on tooling — building the scaffolders
   and adapters is exactly what the freeze exists to make room for.
2. **Continuity registry** — `CNC-*` and `CNL-*` records, deliberately separate from
   the `CHR-*` / `LOC-*` evidence records. The entity record answers to sources; the
   continuity record answers to what the model actually produces. Fusing them would
   let wardrobe decisions sit beside claims and would make it impossible to depict one
   person at two life stages.
3. **Laboratory production kind.** `kind: laboratory`, `EXP<NNN>` codes, and a
   `findings` block. EXP-001 scaffolded. Its deliverable is a findings report, not a
   film, and its `10_publish` stage stays permanently empty.
4. **`validate --reality`** — a gate enforcing that documentation naming an
   unimplemented command says so. It found 63 violations on its first run.

**Cost:** Two new record types and a validator, against a mandate to stop adding.
That tension is real and was weighed: the continuity registry addresses the specific
failure the whole architecture exists to prevent, and the reality gate makes an
existing rule enforceable rather than adding a new one. Neither adds a tier.

The freeze itself costs optionality — questions that would have been answered by
writing another document now wait for evidence.

**What it protects:** The ratio of tested to untested design. A repository where
every part is specified and no part is exercised is not an asset; it is a large
untested hypothesis, and the longer it grows the more expensive it is to discover the
hypothesis was wrong.

**Watch for:** Three signals that the freeze is failing.

1. **A new canon document appearing before EXP-001 reports.** The freeze is
   self-enforced and there is no validator for it. If governance markdown starts
   accumulating again, the discipline has lapsed.
2. **EXP-001 producing a short findings list.** That means it was run too carefully to
   be informative, not that the pipeline is sound. The experiment is only useful at
   production pace.
3. **EXP-001 being quietly upgraded into a publishable piece.** The moment it is shown
   to anyone, its purpose inverts — nobody records honest failures about something
   they are about to release.

**Reflection:** The instruction to freeze arrived from outside this repository, and
it should have arrived from inside it. Nothing in the tooling measures the ratio of
designed to tested capability, so nothing pushed back as that ratio worsened. The
status ledger records the state but does not raise an alarm about it. Whether that
should become a gate is itself a question for after EXP-001 — deciding it now would
be another instance of the error.

---

<!-- New entries appended below, newest last. Never edit an existing entry —
     supersede it with a new one of kind `revision` or `reversal`. -->
