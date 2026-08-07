---
title: Operations framework
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner]
---

# Operations

`core/` defines what a gate **is**. A canon pack declares **which** gates a
production has and who owns them. `ops/` holds everything that sits between those
two statements and an actual human doing the work: who the roles are, who is
accountable for what, what the production lifecycle looks like, what the standing
risks are, what a production costs, and — the bulk of the directory — the checklist
bodies themselves.

Nothing here is genre-specific and nothing here names a studio. If a rule in this
directory only makes sense for historical documentary, it belongs in
[../packs/documentary-history/](../packs/documentary-history), not here.

## 1. Contents

| Path | What it holds |
|---|---|
| [roles.md](roles.md) | Every role slug in the repository: what it owns, what it decides alone, what it cannot decide, which gates it may sign |
| [raci.md](raci.md) | Responsibility matrix across the eleven pipeline stages and the five cross-cutting concerns |
| [workflow_states.md](workflow_states.md) | The production lifecycle — entry and exit conditions per stage, which gate closes each one, and what re-opening costs |
| [risk_register.md](risk_register.md) | The register template, plus the standing platform-level risks that are structural rather than speculative |
| [budget_template.md](budget_template.md) | Production budget template, including the cost lines this kind of work reliably forgets |
| [checklists/](checklists) | One file per gate, across all four packs |

## 2. Why the checklists live here and not in the packs

A gate's *declaration* is pack data. A gate's *checklist* is a document, and two
of them — technical QC and rights — are required by core in every pack
([../core/04_review_gate_framework.md](../core/04_review_gate_framework.md) §8,
[../core/02_rights_and_licensing.md](../core/02_rights_and_licensing.md) §10).

If each pack carried its own copy, there would be four copies of the technical QC
checklist, and within a year they would differ. They would differ *quietly*, because
nothing in the repository compares them, and the first anyone would learn of it is a
delivery that passed QC under one pack's copy and would have failed under another's.
A shared platform guarantee cannot be verified against four divergent checklists.

So the bodies live once, at `ops/checklists/<key>.md`, and every pack's
`gates.yaml` points at the same file:

```yaml
- key: technical_qc
  owner: pipeline-engineer
  checklist: ../../ops/checklists/technical_qc.md
```

Several checklists are genuinely shared across packs — `greenlight`, `script_lock`,
`sensitivity_review`, `picture_audio_lock`, `brief_approval`, `stakeholder_approval`.
Each of those files opens with a **pack applicability** note stating which packs
reference it and which items apply only under which pack. A pack that needs a
materially different checklist for a shared key does not edit the shared file; it
authors a new one under a new key and points its own `gates.yaml` at that. Forking is
allowed. Forking by accident is not.

## 3. Blank checklist vs. completed checklist

These are two different files and confusing them is how a gate ends up signed against
nothing.

| | Blank | Completed |
|---|---|---|
| What | The fixed-in-advance body of checks | One production's filled-in, signed copy |
| Where | `ops/checklists/<key>.md` | Inside the production folder, under the stage the gate closes: `<stage>/checklists/<key>.md` |
| Declared by | The pack's `gates.yaml` `checklist:` field | The production record's `gates.<key>.checklist` field ([../standards/schemas/episode.schema.json](../standards/schemas/episode.schema.json)) |
| Changes | Only via a pack or platform review | Once, at signing, then frozen |

[../core/04_review_gate_framework.md](../core/04_review_gate_framework.md) §7 requires
three artefacts for a signed gate: the signature on the production record, the
completed checklist committed in git, and the commit itself so the state of the
material at signing time is recoverable. A signature without a committed completed
checklist is not a signed gate and the validator treats it as `pending`.

> **Known drift.** Core §7 currently says the completed checklist is committed "at the
> path the gate declares", which was written when checklists lived inside the pack.
> The gate now declares the *blank*. Resolving that wording is a core edit and
> therefore a Platform Owner change — `TBD — amend core/04 §7 to distinguish the two
> paths, with the Platform Owner's signature on the change`.

## 4. Anatomy of a checklist

Every file in [checklists/](checklists) has the same four parts, in the same order,
because a reviewer under deadline reads them in that order:

1. **What the signature certifies** — one sentence, derived from the `certifies:`
   text in the pack's `gates.yaml`. It is the sentence the signatory is putting their
   name to, and the only thing anyone will quote back at them later.
2. **The checkbox list** — the fixed checks. Not "does this feel right?"
3. **Do not sign if** — the disqualifying conditions, stated positively so that they
   are recognisable in the moment rather than reconstructable afterwards. This section
   exists because the failure mode of a checklist is not a reviewer answering "no"; it
   is a reviewer answering "mostly" and ticking the box.
4. **Signature block** — role, person, date, and the note field.

Checkboxes are for *this production's* completed copy. In the blank they are all
unticked, and they stay unticked in `ops/` forever. A ticked box in a blank checklist
means someone edited the template in place; `studio_ops validate --naming` catches
that pattern for `_TEMPLATE_`-prefixed files, but not here, so it is a review
responsibility.

## 5. How ops relates to the rest of the platform

| Layer | Supplies | Ops does not |
|---|---|---|
| [../core/](../core) | What a gate is, gate states, the cascade rule, separation of duties, the universal gate | Redefine any of it. Ops describes and operationalises; it never loosens. |
| [../packs/](../packs) | Which gates exist, who owns them, what each certifies, what it blocks | Decide a pack's gate set. Ops writes bodies for the keys packs declare. |
| [../standards/](../standards) | The numbers a checklist checks against — delivery specs, caption limits, loudness targets, naming, IDs | Restate the numbers. Checklists link to the standard rather than copying it, so there is one place to change a target. |
| studio / line | Who actually holds each role, and the line's advisory register | Name people. Ops names roles. |

The last row is the one that gets violated first. See
[roles.md](roles.md) §1 for why records reference role slugs and never people.

## 6. Maturity

| Capability | Status |
|---|---|
| Role definitions, RACI, workflow states | **DESIGNED** |
| Checklist bodies for all four packs' gates | **DESIGNED** — no gate has ever been signed against one |
| Risk register (platform-level rows) | **DESIGNED** |
| Budget template | **DESIGNED** — every figure in it is `TBD` |
| `studio_ops validate --packs` (would check every declared checklist resolves) | **NOT BUILT** |
| Separation-of-duties check in `validate --canon` | **NOT BUILT** |

Nothing in this directory is TESTED. The first thing that could be is the dry-run
production in [../ROADMAP.md](../ROADMAP.md) Phase 3: one short piece taken through
every gate by actual people under time, which is the only way to learn which of these
checks are load-bearing and which are ceremony. The full ledger is
[../docs/status.md](../docs/status.md).
