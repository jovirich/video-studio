---
title: Studio bible — African History Studio
status: active
version: 0.1.0
updated: 2026-08-07
owners: [showrunner]
---

# Studio bible

The canon that is true of **this studio and nothing else**.

Maturity: **DESIGNED**. Every document here exists on paper, none has been exercised
against a production, and the bible is **not ratified** — see
[amendment_log.md](amendment_log.md).

## 1. What this is, and what it deliberately is not

This bible is an **addendum**. It carries only the material that is specific to
African History Studio: its mission, its scope, the lines it owns, the corrections it
has published, and any place where it binds itself *more tightly* than the layers
above.

It does not restate evidence rules, narrative doctrine, visual grammar, sound policy,
sensitivity procedure, or localisation policy. Those belong to the
[documentary-history pack](../../../packs/documentary-history/) and are authoritative
there. They are not summarised here, not paraphrased here, and not "kept in sync"
here.

The reason is mechanical rather than stylistic. A restatement is a second copy, a
second copy drifts, and the moment two copies disagree nobody on a deadline knows
which one governs — so they follow whichever is nearer to hand, which is this one,
which is the one nobody updated. A studio bible that restates its pack has quietly
replaced its pack.

**If you are about to write a rule here, apply the placement test in
[CONTRIBUTING.md](../../../CONTRIBUTING.md) § Which layer does your change belong to?
first.** A rule that would still be right for a studio covering a different continent
belongs in the pack. A rule that would still be right for a studio making brand films
belongs in [core](../../../core/).

## 2. Precedence

```
core  >  pack  >  studio bible  >  line addendum  >  production
```

A lower layer may **tighten** anything above it and may **never loosen** it. There is
no exemption mechanism at the point of use: an exemption is an amendment to the layer
that owns the rule, carrying that layer's signatures.

Concretely, for this studio:

| Layer | Where | What it settles |
|---|---|---|
| Core | [core/](../../../core/) | Provenance, AI disclosure, rights, delivery, the gate *framework* |
| Pack | [packs/documentary-history/](../../../packs/documentary-history/) | Evidence tiers, narrative doctrine, visual and sonic language, sensitivity procedure, localisation, the gate *set* |
| Studio bible | here | Mission, scope, audience, editorial independence, standing commitments, corrections |
| Line addendum | [lines/ng-nigeria/](../lines/ng-nigeria/) | Region-scoped research, sources, entities, languages, advisory, style |
| Production | `lines/<line>/productions/<code>/` | One piece and its gate signatures |

The one asymmetry worth memorising: the Showrunner holds final editorial authority at
this layer, **except** over an advisory hold, which is the pack's
([07 §4](../../../packs/documentary-history/07_cultural_sensitivity.md)) and cannot be
released unilaterally at studio level.

## 3. Documents

| Document | Holds | Status |
|---|---|---|
| [00_charter.md](00_charter.md) | Mission, scope, audience, independence, standing commitments, success conditions | **DESIGNED** — mission, audience, and success conditions are `TBD — Showrunner` |
| [amendment_log.md](amendment_log.md) | Append-only record of every change to this bible, with signatures | **DESIGNED** — one entry; studio not ratified |
| [corrections.md](corrections.md) | Public, append-only correction log | **DESIGNED** — empty; nothing has been published to correct |

Numbering follows the pack's convention: `00` is this studio's charter because
[core/00](../../../core/00_platform_charter.md) is the *platform's* charter and the
two are different documents at different layers. The gaps in the pack's numbering
exist so a document can move between layers without renumbering; do not fill them
here.

The studio's identity system is not bible material and lives in
[brand/](../brand/). The registers of actual records — sources, claims, entities,
questions — are line-scoped by nature and live under
[lines/](../lines/), never here.

## 4. Amending this bible

Every change is recorded in [amendment_log.md](amendment_log.md) **before it takes
effect**. An amendment absent from that log has no force and the prior text stands.
The required signatures per section are in that document's § Required signatures; in
summary, nothing changes without the Showrunner and the Cultural Advisor, and
specialist sections add their owner.

Two standing rules:

1. **A bible amendment never rides in a production PR.** It goes on a
   `studio/bible-*` branch and is reviewed on its own merits. A change to canon
   justified by one episode's convenience is exactly how a standard erodes, and it
   erodes invisibly because the diff is buried in a hundred lines of script.
2. **An amendment that loosens a pack or core rule is not an amendment to this
   bible.** It is a request to amend the pack or core. Route it there.

## 5. Ratification

This bible is a **draft** until the Showrunner and Cultural Advisor sign the initial
ratification entry. Until they do:

- no production may be greenlit,
- no line may move to `line_status: open`,
- nothing in [brand/](../brand/) is binding on a designer.

The open items blocking ratification are listed in
[amendment_log.md](amendment_log.md) and tracked as `unresolved` decisions in
[studio.yaml](../studio.yaml).

## 6. Historical content

**There is none, anywhere in this studio, and its absence is deliberate.**

No document under `studios/african-history/` asserts anything about the past. Every
factual field is `TBD — needs research` with an owner and a required evidence tier.
Facts enter this studio only as claim records under a line's `sources/`, created by a
researcher through the chain in
[02_evidence_and_sourcing.md](../../../packs/documentary-history/02_evidence_and_sourcing.md).

A plausible placeholder that survives into a script is the single most likely way this
studio embarrasses itself, and the cheapest moment to prevent it is now, while there
is nothing to preserve.
