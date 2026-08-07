---
title: Templates
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer]
---

# Templates

The canonical skeletons. Everything a studio, a line, a production, a record, or a
legal instrument starts life as is a copy of something in this directory.

Maturity: **DESIGNED**. The templates exist and are internally consistent. The
scaffolder that copies them is **NOT BUILT** — see [../docs/status.md](../docs/status.md).

## 1. The rule

> **Templates are copied by `studio_ops`. They are never filled in place.**

A template is a file that must survive being used. Filling one in destroys it for
the next production, and the loss is silent — nobody notices until someone needs the
skeleton again and finds one episode's half-finished brief where it used to be.

Two mechanisms enforce this:

| Mechanism | What it catches |
|---|---|
| `_TEMPLATE_<slug>.<ext>` naming | Marks the file as not-real-content to humans, to `git grep`, and to every validator |
| `status: draft` required on every `_TEMPLATE_` file | `studio_ops validate --naming` fails a template whose status is `review` or `locked` — the fingerprint of someone editing the original |

Both are in [../standards/naming_conventions.md](../standards/naming_conventions.md).
The second rule is the one that actually fires in practice.

### Two kinds of file live in a skeleton

A skeleton directory is copied whole, so the files that must land at a fixed path
inside it carry their **final names** — `studio.yaml`, `line.yaml`,
`production.yaml`, the stage `README.md` files, `bible/00_charter.md`,
`10_publish/credits_ai_statement.md`. Renaming them would break the copy.

The `_TEMPLATE_` prefix is for artefacts created **many times inside** a skeleton: a
brief, a narration pass, a shot record, a prompt card, a source record. Those are
copied individually, repeatedly, and are exactly the files someone edits in place by
accident.

Both kinds carry `status: draft`. Only the prefixed ones are checked for it.

If you have already filled a template in place: copy your work to where it belongs,
then `git checkout -- <template>` to restore the skeleton. Do not "clean it back
up" by hand — a template that has been partially reverted carries the ghost of one
production into every later one.

## 2. What is here

| Path | Skeleton for | Copied by |
|---|---|---|
| [studio/](studio/) | A studio — bible, charter, control record | `studio_ops new-studio` |
| [line/](line/) | A production line — research, sources, entities, advisory, style | `studio_ops new-line` |
| [production/](production/) | One episode, film, or short — eleven pipeline stages | `studio_ops new-production` |
| [records/](records/) | One record of each type in [../standards/id_system.md](../standards/id_system.md) | `studio_ops new-record` |
| [legal/](legal/) | Consent, release, and agreement instruments | By hand, then a lawyer |
| [reviews/](reviews/) | Pointer to the canonical gate checklists | — |
| [prompts/](prompts/) | Pointer to the prompt framework and the prompt card template | — |

The three **skeleton types** — studio, line, production — mirror the lower three
tiers of the architecture in [../README.md](../README.md) §1. Each one is a whole
directory, not a file, because what a tier *is* includes the shape of its folders.

The **record templates** are single files. They are per-type because each record
type has its own schema in [../standards/schemas/](../standards/schemas/), and a
template whose front matter does not match its schema is a trap: it validates
nowhere and teaches the wrong shape.

The **legal templates** are the exception to everything else here — they are not
scaffolded, not validated, and not authoritative. See [legal/README.md](legal/README.md).

## 3. Every human decision is a `TBD`

No template in this directory contains an invented fact, name, date, figure, place,
or person — not as an example, not as filler, not in a comment. Every field a human
must decide reads:

```
TBD — <what is needed to resolve it>
```

The trailing clause is not decoration. `TBD` alone tells the next person that
something is missing; `TBD — needs the archive's reference number for the folio`
tells them what to go and do. A `TBD` without a clause is half a placeholder.

This convention is specified in [../standards/metadata_spec.md](../standards/metadata_spec.md)
§ The `TBD` convention, and it is load-bearing:

- `TBD` is **legal** at `status: draft` and `status: review`.
- `TBD` is **illegal** at `status: locked`. Locking is what forces the decision.
- A `TBD` in a `review`-status record must link an open question.

The alternative — a plausible-sounding placeholder that nobody flags because it
reads like a finished sentence — is the single failure this repository is built to
prevent. See [../CONTRIBUTING.md](../CONTRIBUTING.md) § Writing rules.

## 4. Where the gate block comes from

Production and line control records carry a `gates` block. It is **generated**, not
authored: `studio_ops new-production` reads the studio's declared canon pack, opens
that pack's `gates.yaml`, and writes one entry per declared gate with `status:
pending` and the declared owner.

The set in [production/production.yaml](production/production.yaml) is the
documentary-history set from
[../packs/documentary-history/gates.yaml](../packs/documentary-history/gates.yaml),
present so the template is complete and readable. A studio on a different pack gets
a different set, and hand-editing the block to add or remove a gate is how a
production ends up shipping without one.

## 5. Changing a template

A template change affects every production created after it, and none created
before. That asymmetry is the reason template edits go through the `studio/*`
branch prefix and never ride along in an episode PR — see
[../CONTRIBUTING.md](../CONTRIBUTING.md) § Branching.

Checklist for a template PR:

1. The file still carries `status: draft` and its `_TEMPLATE_` prefix.
2. Every new field is either `TBD — <what is needed>` or a genuine structural default.
3. If the template has a schema, it still validates: `python -m studio_ops validate --schemas`.
4. Every link still resolves: `python -m studio_ops validate --links`.
5. The comment explains *why the field exists and what goes wrong without it* — not
   what the field is called. A field whose comment restates its name has no comment.
