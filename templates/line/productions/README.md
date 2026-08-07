---
title: productions — the line's episodes, films, and shorts
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [showrunner]
---

# productions

One folder per production, created by `studio_ops new-production --line <line>` from
[../../production/](../../production/).

```
productions/
├── S01E01_<slug>/
├── S01E02_<slug>/
└── ...
```

Folder naming is fixed: `S<NN>E<NN>_<slug>`, zero-padded, slug in kebab-case. The
season and episode numbers are part of the folder name so that a directory listing
sorts into broadcast order without a tool.

## Nothing is created here by hand

The scaffolder does three things that hand-copying does not:

1. **Allocates the production ID**, taking the next serial for the (type, scope)
   pair. Hand-allocated IDs collide, and a collided ID corrupts the reference graph
   silently — the references still resolve, to the wrong record.
2. **Builds the `gates` block** from the studio's declared canon pack. A production
   created without a pack has an undefined gate set, which in practice means no gate
   set.
3. **Refuses if the line is not `open`.** All three opening conditions on
   [../line.yaml](../line.yaml) must be true. A production greenlit against a
   `candidate` line has no research lead, no advisory contact, and no survey of what
   archives exist.

The scaffolder is **NOT BUILT** — [../../../docs/status.md](../../../docs/status.md).
Until it is, copying [../../production/](../../production/) by hand is the fallback,
and the three checks above become a human's responsibility rather than the tool's.
Write down which of them you performed.

## What lives at the production and what lives at the line

| At the line | At the production |
|---|---|
| Source records, claims, open questions | Which of them this production uses |
| Character, location, and event profiles | Which of them appear, and in which shots |
| Language entries, orthography, fonts | The VO record sheet for this script |
| Visual identity, lens set, palette, style anchors | Prompt cards that inherit them |
| Advisory register and rulings | The sensitivity findings for this production |
| The corrections log | Corrections raised against this production |

The rule behind the table: anything that could be true of a second production belongs
at the line. Copying a claim, an entity, or a naming decision into a production
folder guarantees the copies diverge, and the divergence is invisible until a
fact-check catches it — or does not, and a viewer does.
