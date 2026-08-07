---
title: Author a canon pack
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner]
---

# Author a canon pack

A canon pack is the genre rulebook a studio adopts. It supplies what
[`core/`](../../core/) deliberately omits: evidence standards, narrative doctrine,
visual and sonic language, sensitivity procedure, localisation, and — the part that
does the most work — **the gate set**.

## First: are you sure?

Author a pack only when the **obligations** differ, not when the subject does.

| Situation | Answer |
|---|---|
| Roman history instead of Nigerian | A studio on `documentary-history`. Same obligations, different subject. |
| A product explainer instead of a documentary | A pack. The risk is a false product claim, not a false historical one, and the gate set must differ or it protects nothing. |
| A biblical narrative series | A pack. Continuity and a declared interpretive stance replace an evidence chain. |
| The same work but the fact-check gate is inconvenient | Not a pack. That is an exemption wearing a costume. |

Three questions, from [../architecture/spinning_up.md](../architecture/spinning_up.md):

1. **What is the characteristic way this genre goes wrong?** If you cannot name it in
   one sentence, you need a studio under an existing pack, not a new pack.
2. **What would we regret not having checked?** That list is your gate set. Write it
   before looking at any other pack's gates.
3. **What does core already cover?** Do not restate it.

Four packs already exist: `documentary-history` (active), `product-marketing`,
`narrative`, and `fashion-film` (draft). Read the closest one — then close it before
writing your gate set.

---

## 1. Scaffold

```bash
python -m studio_ops new-pack --code <code> --title "<Title>"
```

**NOT BUILT.** The stub notes this is the cheapest scaffolder to build first — it is
blocked on nothing.

**Today:** copy [`packs/_TEMPLATE_pack/`](../../packs/_TEMPLATE_pack/) to
`packs/<code>/`. Then check that you copied it rather than filling it in place — the
naming validator catches a `_TEMPLATE_` file whose status is no longer draft, which is
the most common real mistake in this workflow.

## 2. Name the failure mode

Open the README with it. `documentary-history` opens with *"the imagery is cheap and
the truth is expensive"*, and every rule in the pack is visibly aimed at that one
sentence. A pack whose failure mode is vague produces rules that are vague, and vague
rules are the ones that get waived.

## 3. Write the gate set first, from scratch

This is the step people invert, and inverting it is how ceremony accumulates.

Answer "what would we regret not having checked?" on a blank page. Then, for each
answer, write a gate in `gates.yaml`:

```yaml
- key: <snake_case>
  title: <Title>
  owner: <role-slug>          # a role, not a committee
  stage: <pipeline stage>
  blocks: [<stages or gates that cannot proceed>]
  checklist: checklists/<key>.md
  required: true
  certifies: >
    One sentence in the present tense, specific enough that a reader can tell
    whether it is true.
```

Rules from [core/04](../../core/04_review_gate_framework.md), and none is optional:

- **Named owner** — a role, not a committee. Someone is accountable.
- **Written checklist**, fixed in advance. Not "does this feel right?"
- **Recorded signature** — role, person, date, on the production record.
- **Blocking.** A review that is advisory is feedback, which is valuable and is not a
  gate.
- **Technical QC is universal.** Every pack has it, whatever the genre. Everything else
  is negotiable.

Then count. If your gate set needs more distinct signatories than the studios adopting
it can staff, you have written a document that will be abandoned rather than followed.
Declare the number honestly — `documentary-history` sets
`minimum_distinct_signatories: 4` — and let a studio decide with its eyes open.

## 4. Write the documents

Only the ones your genre needs. **A pack with four documents is a legitimate pack;**
`product-marketing` has four and is complete. Padding a pack to match another pack's
document count is how a second pack becomes 80% a copy of the first, which is the
signal that the shared material belonged in core.

Keep the numbering aligned with the convention: `00`, `06`, `08`, and `10` are core's,
and the gaps are kept so numbers stay stable if a document ever moves between layers.

Write one checklist per declared gate, in `checklists/`.

## 5. Declare the pack

`pack.yaml`: code, title, version, `core_version` the pack conforms to, the document
list, and the gate-set path. Use
[`packs/documentary-history/pack.yaml`](../../packs/documentary-history/pack.yaml) as
the reference.

**Caution:** `validate --schemas` checks `pack.yaml` against `pack.schema.json`, so its
shape is validated. What is *not* checked is whether the documents and checklists it
names exist — that is `validate --packs`, which is NOT BUILT. Step 6 is therefore done
by hand. See
[../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md)
item 9.

## 6. Check it does not loosen core

Precedence is `core > pack > studio > line > production`. **A pack may tighten a core
rule. It may never loosen one.**

```bash
python -m studio_ops validate --packs
```

**NOT BUILT** — it would check that every declared gate has a checklist that exists,
that every document in `pack.yaml` exists, and that nothing contradicts core.

**Today, by hand:**

- [ ] Every gate in `gates.yaml` has a checklist file that exists
- [ ] Every document listed in `pack.yaml` exists
- [ ] Technical QC is present
- [ ] No rule weakens [core/01 §2](../../core/01_provenance_and_ai_disclosure.md) —
      the absolute prohibitions
- [ ] No rule weakens [core/04 §5](../../core/04_review_gate_framework.md) —
      separation of duties
- [ ] The pack names no studio and no subject matter

If your genre genuinely cannot satisfy a core rule, **that is a finding about core, not
a reason for an exemption.** One such request suggests core over-reaches; a pattern
means core was written from documentary assumptions wearing a universal name. Record it
in [../architecture/evolution.md](../architecture/evolution.md) and amend core with
core's signatures.

## 7. Register and validate

1. Add a row to [`packs/README.md`](../../packs/README.md) and to the table in
   [`core/00_platform_charter.md`](../../core/00_platform_charter.md) §3.
2. Run:

   ```bash
   python -m studio_ops validate --schemas --naming --links --root-hygiene
   ```

   `--links` matters here specifically. The three draft packs each shipped a README
   listing documents that had not been written, and every one was a dead link until
   someone went back and fixed them. A link is a promise. If a document is not written,
   name it in plain text and do not link to it.

## 8. Prove it

A pack is DESIGNED until a studio produces one finished piece under it, end to end.
That is [ROADMAP](../../ROADMAP.md) Phase 6c, and it is the real test of whether
`core/` is universal.

Then: [open_a_studio.md](open_a_studio.md) declaring the new pack.

**Watch for the failure signal:** a second pack that is largely a copy of the first
means the shared material belonged in core and the split was made in the wrong place.
Record it in the evolution log rather than living with it.
</content>
