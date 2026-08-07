---
title: Studio skeleton
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [showrunner]
---

# Studio skeleton

The canonical folder for one studio — a brand with an editorial standard and a slate.
Copied by `studio_ops new-studio --code <code> --pack <pack>` into `studios/<code>/`.

Maturity: **DESIGNED**. The scaffolder is **NOT BUILT**
([../../docs/status.md](../../docs/status.md)).

```
<studio>/
├── studio.yaml          the control record — pack, governance, lines, decisions
├── bible/               what this studio holds that core and the pack do not
│   ├── 00_charter.md    mission, audience, scope, success conditions
│   ├── amendment_log.md every change to the bible, with its reasoning
│   └── corrections.md   the public corrections log
├── brand/               identity, labelling system, typography
└── lines/               the production lines
```

## 1. A studio's one structural decision

**A studio declares exactly one canon pack**, and that declaration determines what
every production under it is held to: the evidence standard, the narrative doctrine,
the visual and sonic language, the sensitivity procedure, and the actual gate set.

```yaml
pack: <pack-code>
pack_version: "0.1.0"
```

The pack is not a preference and not a starting point to be diverged from. Forcing a
brand film through a historical evidence chain produces theatre; letting a history
documentary skip one produces something worse. If a studio needs a materially
different standard, it needs a different pack — authored at
[../../packs/](../../packs/), with that layer's review — not an exemption from this
one.

Upgrading a pack's major version mid-season is refused by the scaffolder, because a
production part-way through a nine-gate sequence cannot have the sequence changed
underneath it.

## 2. What belongs in the bible, and what does not

The most common review correction. Use the test in
[../../CONTRIBUTING.md](../../CONTRIBUTING.md) § Which layer does your change belong to:

| If the rule would be right for… | It belongs in |
|---|---|
| A production with no factual claims at all | [../../core/](../../core/) |
| A whole genre of work | [../../packs/](../../packs/) |
| **This studio's brand and mission** | **`bible/`** |
| One region or strand | the line |
| One piece | that production |

Precedence: `core > pack > studio > line > production`. A studio may **add**
constraints and **tighten** inherited ones. It may never loosen one.

Concretely: the bible is where a studio says what it is *for*, who it is *for*, what
it will not make, and what would count as having succeeded. It is not where the
studio restates the pack in its own words — a restatement drifts from the original,
and when they disagree nobody knows which governs.

## 3. The decisions that block first greenlight

`studio.yaml` carries a `decisions` list, seeded from the pack's
`studio_must_decide` set plus the studio's own. `studio_ops` blocks greenlight while
any is `unresolved`.

These are the choices that are cheap now and expensive later — a music policy, a
naming and orthography standard, a narration voice policy, a licensing posture. Each
one, deferred, becomes a precedent set accidentally by whoever made the first
production, and then a precedent that is awkward to reverse.

The template ships with every decision `unresolved`, which is the honest state of a
studio that has not made them.

## 4. Governance

`distinct_signatories_available` is the field worth reading twice. No person signs
two gates on the same production
([../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §5),
and the pack sets a minimum number of distinct signatories.

**With fewer people than that minimum, the studio cannot ship.** Not "will find it
awkward" — the constraint is core, not a pack's choice, and it is the first thing a
small team quietly abandons under a deadline. Recording the real number here makes
that a visible staffing fact rather than something discovered at the first delivery.

## 5. Public artefacts

A studio publishes a methodology page, a correction intake address, a takedown
contact, and a corrections log. All four are `TBD` in the template and all four are
required before publication.

The corrections log in particular is published from the start, not created after the
first error. A studio that only produces one once it has been corrected has told its
audience something about how it expected this to go.
