---
title: First week
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner, showrunner]
---

# First week

A day-by-day path into this repository. It assumes a few hours a day alongside other
work, and it assumes you will be tempted to skip to day 4 and start writing something.
Do not — the order is the point, and it is explained below.

**Before anything else, two rules.** They take one minute and they are the two that
cause real damage when broken.

> **1. Never invent a fact to fill a template.** Write `TBD — needs research` and open
> an open question. A plausible placeholder that survives to air is the single most
> likely way this project embarrasses itself.
>
> **2. Never claim more maturity than exists.** DESIGNED / IMPLEMENTED / TESTED /
> NOT BUILT. A bare ✅ is banned. Nothing in this repository is currently TESTED.

## Why this order

You will read the honest status ledger on **day 1**, before the architecture. That is
deliberate. The architecture documents describe a system in the present tense — "the
validator walks the chain", "the pipeline refuses the clip" — and almost none of it
runs yet. Read them first and you will build a mental model of a working system and
then spend a month being surprised. Read [../status.md](../status.md) first and every
present-tense verb afterwards reads correctly as a specification.

Then: the shape of the thing (day 2), the rules that shape it (day 3), the tooling
(day 4), and only then a change of your own (day 5).

---

## Day 1 — What this is, and what is actually true

**Read, in this order:**

| # | Document | Look for |
|---|---|---|
| 1 | [../../README.md](../../README.md) | The four tiers, and §9 — read §9 twice |
| 2 | [../status.md](../status.md) | The per-capability ledger. This is the honest document. |
| 3 | [glossary_quickstart.md](glossary_quickstart.md) | Fifteen terms |
| 4 | [../../ROADMAP.md](../../ROADMAP.md) | Phases advance on exit criteria, not dates. Note that Phase 3 exists to find failures on work nobody will see. |

**Run:**

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows; source .venv/bin/activate elsewhere
pip install -e ".[dev]"

python -m studio_ops --help
python -m studio_ops validate --all
pytest
```

Full setup notes, including the Windows drive-letter casing trap that will otherwise
waste an afternoon: [../runbook/environment.md](../runbook/environment.md).

**What you should notice.** `validate --all` does not come back clean. Several gates
report **NOT BUILT** rather than passing silently, and `--links` reports errors for
files that were specified and never written. Both are the system telling the truth. A
validator that returned "OK" because it does nothing would be worse than no validator,
because it manufactures confidence.

**Understand by end of day:** this repository is a *platform*, not a show; it contains
no historical claims at all, deliberately; and about four things in it currently
execute.

---

## Day 2 — The shape, and the placement test

**Read:**

| # | Document | Look for |
|---|---|---|
| 1 | [../architecture/README.md](../architecture/README.md) | The four tiers and the five clauses of the `arch-2` contract |
| 2 | [../architecture/evolution.md](../architecture/evolution.md) | AE-001 and AE-006. Read them as a pair. |
| 3 | [../decisions/0005-platform-and-canon-packs.md](../decisions/0005-platform-and-canon-packs.md) | The four bad options it rejected |
| 4 | [../architecture/spinning_up.md](../architecture/spinning_up.md) | The one question that needs real thought |

AE-001 and AE-006 together are the most useful thing in the repository for a newcomer:
the first decision was right and its abstraction was one tier too shallow, and the log
says so plainly instead of quietly rewriting history. That tone is the house style, and
you are expected to write the same way about your own work.

### The placement test

The most common review correction, by a wide margin, is a change made at the wrong
layer. Ask, in order, and stop at the first yes:

| Ask | If yes, it belongs in |
|---|---|
| Would this rule still be right for a production with **no historical claims at all**? | [`core/`](../../core/) |
| Is it right for a whole **genre** of work? | [`packs/`](../../packs/) |
| Is it right for **one studio's** brand and mission? | `studios/<code>/bible/` |
| Is it about **one region or strand**? | `studios/<code>/lines/<line>/` |
| Is it about **one piece**? | that production's folder |

Precedence is `core > pack > studio > line > production`. A lower layer may add
constraints and tighten upper ones. **It may never loosen one.** If you need an
exemption, you amend the layer that owns the rule, with that layer's signatures — you
do not add a local override.

Two corollaries worth memorising:

- **Platform-level files never name a studio or its subject matter.** If you write "for
  instance, in Nigeria…" in `core/`, `standards/`, or `prompts/`, the change belongs a
  layer down. (The repository does not currently pass its own version of this check —
  see [../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md)
  item 12. Do not make it worse.)
- **A studio-level change never rides along in a production PR.** Open a separate
  `studio/*` branch and link it. Canon changes get their own review.

**Exercise.** For each, name the layer before reading the answer:

1. "Captions are required on every deliverable." → core: true of any video.
2. "Oral testimony carries the `traditional` register." → pack: true of documentary
   history, meaningless for a brand film.
3. "Narration is recorded in a warm, close voice." → studio: a brand decision.
4. "Yoruba diacritics use the following font stack." → line.
5. "This episode's cold open runs 40 seconds." → production.
6. "Every generated asset records its seed." → core. Reproducibility is a platform
   guarantee, not a genre preference.

---

## Day 3 — The rules, and why each one has teeth

**Read:**

| # | Document | Look for |
|---|---|---|
| 1 | [../../core/00_platform_charter.md](../../core/00_platform_charter.md) | §5 guarantees and §6 refusals |
| 2 | [../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) | §2 (absolute prohibitions) and §8 (the question to ask of any generative choice) |
| 3 | [../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) | What a gate is; §5 separation of duties |
| 4 | [../../packs/documentary-history/02_evidence_and_sourcing.md](../../packs/documentary-history/02_evidence_and_sourcing.md) | The whole thing. It is the load-bearing document. |
| 5 | [../../packs/documentary-history/methodology/using_ai_in_research.md](../../packs/documentary-history/methodology/using_ai_in_research.md) | The T5 rule |
| 6 | [../../CONTRIBUTING.md](../../CONTRIBUTING.md) | Branching, commit format, file placement |

The four rules that will actually bite you:

| Rule | What breaks without it |
|---|---|
| **No fact in a script without a claim ID** | You cannot answer "where did that come from?" eighteen months later, and the answer is required in public on every episode's sources page. |
| **A language model is never a source (T5)** | Generation outruns verification, and the show becomes fiction with a serious voiceover. This is the rule most likely to erode under deadline, which is why it is in the schema as well as in prose. |
| **No person signs two gates on the same production** | The only structural check on the Showrunner's authority disappears, exactly where being wrong harms people outside the studio. |
| **Media never in git; restricted material never in git in any form** | A 4 GB render is in every clone forever; a restricted transcript committed once is disclosed permanently. Neither is undoable. |

And the one about honesty in your own writing: use DESIGNED / IMPLEMENTED / TESTED /
NOT BUILT in documents, commit messages, and conversation. "Built" and "finished" are
ambiguous; these are not. Update [../status.md](../status.md) in the *same commit* that
changes a capability's maturity — it is not a separate chore.

---

## Day 4 — The tooling, and where it stops

**Read:**

| # | Document | Look for |
|---|---|---|
| 1 | [../api/README.md](../api/README.md) | Per-command maturity, exit codes, the JSON shape |
| 2 | [../../automation/README.md](../../automation/README.md) | The three design principles |
| 3 | [`automation/studio_ops/paths.py`](../../automation/studio_ops/paths.py) | The folder contract, in one place |
| 4 | [`automation/studio_ops/result.py`](../../automation/studio_ops/result.py) | `Finding`, `GateReport`, `GateState` |
| 5 | [`automation/tests/test_validators.py`](../../automation/tests/test_validators.py) | What a real test looks like here |

**Run and read the output properly:**

```bash
python -m studio_ops validate --all --format json
python -m studio_ops validate --root-hygiene
python -m studio_ops new-record --type source --line ng-nigeria   # NOT BUILT — read what it says
```

That last command is the most informative thing you will run this week. It does not
fail obscurely; it tells you what it *will* do, what it is blocked on, and why it is
the highest-priority thing to build. That is the house standard for an unimplemented
command.

**Understand:** four gates run (`--schemas --naming --links --root-hygiene`); every
scaffolder, report, prompt renderer, and pipeline command is NOT BUILT; findings are
data (`Finding` objects), and rendering is separate; and validation never touches the
network, so a red build always means the repository is wrong.

Then read [../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md)
end to end. It is the list of what is genuinely weak, written by people who built it,
and it is the fastest route to understanding where the real edges are.

---

## Day 5 — Make a change

**Read first:** [../workflows/README.md](../workflows/README.md), and the specific
workflow for whatever you are about to do.

Then take one of these. They are ordered by how much of the system they make you touch,
and each is genuinely useful rather than busy-work.

| # | Task | Teaches |
|---|---|---|
| 1 | Fix a broken internal link found by `validate --links`, in a file whose correct target clearly exists. Do not create files to satisfy links. | The link gate, relative paths, the `arch-1` → `arch-2` move's leftovers |
| 2 | Add one term you had to look up to [../glossary.md](../glossary.md), in the right section. | House voice; the difference between a general and a specific meaning |
| 3 | Add a `--delivery` flag to `cli.py` — the gate is already in `validate.UNBUILT` but has no flag, so it is only reachable through `--all`. | The CLI surface, `ALL_GATES`, and the NOT BUILT convention |
| 4 | Add a test to `test_validators.py` for a naming rule that is implemented but untested. Check the existing parametrised cases first. | The fixture-tree pattern; why a clean run proves nothing |
| 5 | Take one vendor cheat sheet, verify it against the vendor's current documentation, and add a `docs_checked` date to its front matter. Change what is wrong. | The prompt library; that ~49 sheets are DESIGNED and unverified |
| 6 | Write an ADR for something you saw decided implicitly this week. Use [../decisions/0000-template.md](../decisions/0000-template.md). Fill in *Negative consequences* and *Validation* properly. | The decision record discipline. Hardest and most valuable of the six. |

**Before you open the PR:**

```bash
python -m studio_ops validate --schemas --naming --links --root-hygiene
pytest
ruff check automation && ruff format --check automation && mypy automation/studio_ops
```

Commit format: `<area>(<scope>): <imperative summary>`, e.g.
`docs(onboarding): fix dead link to the gate framework`.

Branch: `fix/<short-description>` for a small fix, `studio/<area>` for anything
touching canon, schemas, prompts, or automation. Never mix the two.

---

## The one rule you must not break

> **Never invent a fact to fill a template.**

Not a date, not a name, not a figure, not a plausible-sounding institution, not a
"representative example". Write:

```
TBD — needs research
```

and open an open question recording what you searched and where.

The reason is mechanical, not moral. This repository is a set of templates and
schemas, and templates invite completion — an empty field looks like an error, and a
filled one looks finished. A placeholder that reads plausibly is never questioned
again, and it will be read by the next person as a claim, then by a script as a fact,
then by a viewer as history. `TBD` is ugly, which is precisely its function: it does
not survive review by being unobtrusive.

The same rule governs your own work about your own work: an unbuilt command is
NOT BUILT, not "in progress". A gap you can name is a research artefact. A gap you
filled is a defect nobody can find.
</content>
