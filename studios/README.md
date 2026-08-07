# Studios

A **studio** is a branded content operation running on this platform. It declares one
[canon pack](../packs), adds its own bible and brand, and owns one or more
production lines.

Studios are independent. One studio's decisions, advisory boards, visual identity,
and subject matter never leak into another's.

## Current studios

| Studio | Pack | Lines | Status |
|---|---|---|---|
| [african-history/](african-history) | `documentary-history` | `ng-nigeria` (line 01) | opening |

## Studio structure

```
studios/<code>/
├── README.md
├── studio.yaml            declares the pack, brand, and governance
├── bible/                 the studio's own canon — addendum only, never a re-statement
│   ├── 00_charter.md      mission, scope, audience, independence
│   ├── amendment_log.md
│   └── corrections.md     append-only, public
├── brand/                 identity: type, colour, title cards, thumbnails, labelling
└── lines/
    └── <line-code>/       a production line
```

## What belongs at studio level

- Mission, audience, and editorial independence
- Which pack it runs, and any tightenings on top of it
- Brand identity and channel presentation
- The corrections log
- Studio-wide governance and role assignments

## What does *not* belong at studio level

| Material | Where it goes | Why |
|---|---|---|
| Evidence rules, narrative doctrine, sensitivity procedure | the [pack](../packs) | Genre-level, shared across studios |
| Schemas, prompt library, automation, delivery specs | the [platform](..) | Universal |
| Research, sources, characters, locations, language guides | the **line** | Line-scoped by nature |
| Anything about one production | the production | — |

If a studio bible starts restating pack rules, they will drift apart and nobody will
know which is authoritative. The studio bible is an **addendum**: it says what is
true of *this studio* and nothing else.

## Opening a studio

```bash
# NOT BUILT — these commands do not exist yet. See docs/status.md.
python -m studio_ops new-studio --code <code> --title "<Title>" --pack <pack-code>
```

Then, before the first greenlight:

1. Fill `bible/00_charter.md` — mission, scope, audience, success conditions.
2. Resolve every item in the pack's `studio_must_decide` list. `studio_ops` blocks
   greenlight while any is unresolved.
3. Define brand identity — noting that typeface selection is blocked on knowing every
   language and diacritic the studio's lines will need.
4. Open at least one line.

## Precedence

```
core  >  pack  >  studio bible  >  line addendum  >  production
```

A studio may tighten anything above it. It may loosen nothing. An exemption requires
an amendment at the layer that owns the rule, with that layer's signatures.
