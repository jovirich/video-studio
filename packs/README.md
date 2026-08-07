# Canon packs

A **canon pack** is a genre's editorial rulebook. It supplies everything
[core](../core) deliberately leaves open: evidence standards, narrative doctrine,
visual and sonic language, sensitivity procedure, localisation policy, and the set of
review gates.

A studio declares exactly one pack in its `studio.yaml`. That declaration determines
what its productions are held to.

## Why packs exist

The platform makes video. Different kinds of video have genuinely different, and
sometimes incompatible, obligations:

| | Historical documentary | Brand film | Narrative fiction |
|---|---|---|---|
| Factual claims need source records | **yes, mandatory** | for claims about the product only | no |
| Fact-check gate | **yes** | partial | no |
| Cultural advisory authority | **yes, with hold power** | situational | situational |
| Reconstruction labelling | **yes** | n/a | n/a — the whole thing is fiction |
| Continuity bible | light | none | **heavy** |
| Client approval gate | no | **yes** | no |

Forcing a brand film through an evidence chain produces theatre, not rigour. Letting
a history documentary skip one produces something worse. The pack layer lets each be
correct without either contaminating the other.

## Available packs

| Pack | For | Gates | Status |
|---|---|---|---|
| [documentary-history/](documentary-history) | Historical documentary with heavy generative assistance | 9 | active |
| [_TEMPLATE_pack/](_TEMPLATE_pack) | Skeleton for authoring a new pack | — | template |

## What a pack may and may not do

**May:**
- Add rules core does not have
- Tighten a core rule
- Define its own gate set, checklists, and owners
- Define its own record types and schemas, in `pack/schemas/`
- Require additional fields on platform record types

**May not:**
- Loosen or contradict any core rule
- Remove technical QC from its gate set
- Permit anything in [core §01 §2 prohibitions](../core/01_provenance_and_ai_disclosure.md)
- Redefine platform identifier grammar or naming conventions

A pack that needs core loosened must amend core, with core's signatures and an impact
statement covering every existing studio. That bar is deliberately high.

## Authoring a new pack

```bash
python -m studio_ops new-pack --code brand-film --title "Brand and corporate film"
```

Scaffolds from `_TEMPLATE_pack/`. Then, in order:

1. Write `pack.yaml` — identity, owner, which core version it targets.
2. Write `gates.yaml` — the gate set. Start from the question *what would we regret
   not checking?*, not from another pack's list.
3. Write the canon documents. Only the ones the genre actually needs — a pack with
   three documents is a legitimate pack.
4. Write the checklists each gate references.
5. Add any pack-specific schemas.
6. Run `studio_ops validate --pack <code>` — checks that every declared gate has a
   checklist, every referenced document exists, and no rule contradicts core.

## Pack structure

```
packs/<code>/
├── README.md            what this pack is for, and what it deliberately omits
├── pack.yaml            identity, owner, core version targeted
├── gates.yaml           the gate set
├── NN_*.md              canon documents
├── checklists/          one per gate
├── schemas/             pack-specific record types (optional)
├── templates/           pack-specific templates (optional)
└── methodology/         working protocols (optional)
```

## Versioning

Packs are semver'd independently of core.

- **MAJOR** — a change requiring existing productions to be re-reviewed
- **MINOR** — a new rule, gate, or document
- **PATCH** — clarification

A studio pins a pack version in `studio.yaml`. Upgrading is deliberate, and a major
upgrade mid-production is refused by the scaffolder — you finish the season on the
version you started it on.
