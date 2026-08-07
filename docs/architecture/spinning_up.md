---
title: Spinning up new work
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner]
---

# Spinning up new work

The practical answer to *"I want to make a different kind of video — do I need a new
repository?"*

**No.** Work out which tier your new thing lives at, and run one command.

## Decision tree

```
Is it another piece in an existing strand?
  └─ yes ──► new-production          e.g. another Nigeria episode

Is it a new strand of the same studio's work?
  └─ yes ──► new-line                e.g. Ghana inside African History Studio

Is it a different brand or subject, but the same KIND of video?
  └─ yes ──► new-studio              e.g. a Roman history studio
                                          — reuses documentary-history unchanged

Is it a different KIND of video, with different obligations?
  └─ yes ──► new-pack, then new-studio
                                     e.g. product video, fashion film,
                                          narrative adaptation
```

The only question that ever needs real thought is the last one: **is this genuinely a
different kind of work, or the same kind about a different subject?**

Rome is the same kind of work as Nigeria — evidence chain, reconstruction labelling,
advisory review. It needs a studio, not a pack. A Giftinz product film is a different
kind of work: the risk is a false product claim, not a false historical one, and its
gate set has to be different or it protects nothing.

## Worked examples

### History of Rome — a new studio, no new pack

```bash
# NOT BUILT — these commands do not exist yet. See docs/status.md.
python -m studio_ops new-studio --code roman-history --title "Roman History Studio" \
       --pack documentary-history
python -m studio_ops new-line   --studio roman-history --code it-rome --title "Rome"
```

Reuses the documentary-history pack **unchanged**: source tiers, claim records,
reconstruction labelling, nine gates, the bias register, the oral-history protocol.
Nothing at platform level is touched.

Only the line-level material is new: its own archive landscape, advisory contacts,
language policy (Latin and Greek orthography, epigraphic conventions), and visual
identity. Which is correct — those *are* the things that differ.

### Giftinz product videos — a different kind of work

```bash
# NOT BUILT — these commands do not exist yet. See docs/status.md.
python -m studio_ops new-studio --code giftinz --title "Giftinz" \
       --pack product-marketing
python -m studio_ops new-line   --studio giftinz --code feature-films \
       --title "Feature explainers"
```

Gets [product-marketing](../../packs/product-marketing/): five gates, a hard claim
substantiation gate, a stakeholder approval gate, and a prohibition on generating the
product's own interface. Gets **no** source registry, no fact-check gate, no advisory
hold — because those would be ceremony, not protection, for this work.

Still gets everything from core: provenance on every asset, AI disclosure, rights
clearance, delivery specs, captions, human gates.

A second product line — MyTenant — is another line inside the same studio if the
brand and approvals are shared, or its own studio if they are not.

### A biblical narrative series — narrative pack

```bash
# NOT BUILT — these commands do not exist yet. See docs/status.md.
python -m studio_ops new-pack   --code narrative          # already authored
python -m studio_ops new-studio --code biblical-narrative --pack narrative
python -m studio_ops new-line   --studio biblical-narrative --code genesis
```

Gets [narrative](../../packs/narrative/): story bible lock, continuity lock,
production-level disclosure instead of per-shot marks, and — the part that matters
here — a **required declared interpretive stance**: which tradition, which variant
text, whose reading, and what the production is explicitly not claiming.

That declaration is the difference between an adaptation and an argument nobody
agreed to have.

### Fashion films

```bash
# NOT BUILT — these commands do not exist yet. See docs/status.md.
python -m studio_ops new-studio --code <brand> --pack fashion-film
```

Gets garment verification and representation review, plus a studio-level decision on
synthetic humans that then applies uniformly rather than being renegotiated per shot.

## What every route shares

Whatever the pack, every production on this platform inherits core's guarantees:
traceable, disclosed, cleared, gated, reproducible, accessible. That is the point of
having a platform rather than four repositories.

## What none of them touch

`core/`, `standards/`, `prompts/`, `templates/`, `automation/`, `library/`, `ops/`.

If a new studio, line, or pack forces a change to any of those, that is an
architecture finding — record it in [evolution.md](evolution.md). It means the
abstraction sits in the wrong place, and moving it is cheaper than working around it.

## Authoring a pack when none fits

Only when the *obligations* differ, not when the subject does. Start from
[packs/_TEMPLATE_pack/](../../packs/_TEMPLATE_pack/) and answer three questions:

1. **What is the characteristic way this genre goes wrong?** If you cannot name it,
   you probably need a studio under an existing pack, not a new pack.
2. **What would we regret not having checked?** That list is your gate set. Write it
   before looking at any other pack's gates — inherited gate sets are how ceremony
   accumulates.
3. **What does core already cover?** Do not restate it. A pack with four documents is
   a legitimate pack; product-marketing has four and is complete.

Then `studio_ops validate --pack <code>` checks that every gate has a checklist,
every referenced document exists, and nothing contradicts or loosens core.
