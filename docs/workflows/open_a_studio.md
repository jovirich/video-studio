---
title: Open a studio
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner, showrunner]
---

# Open a studio

A studio is a brand and a body of work with its own mission, its own editorial voice,
and its own production lines. It declares **exactly one canon pack**, and that
declaration determines what every production under it is held to.

**Before you start:** are you sure you need a studio and not a line? A studio is
warranted when the *brand, mission, or approvals* differ. A different region or period
under an existing brand is a **line** — see [open_a_line.md](open_a_line.md). A
different *kind* of video with different obligations needs a **pack** first — see
[author_a_pack.md](author_a_pack.md) and
[../architecture/spinning_up.md](../architecture/spinning_up.md).

**Precondition:** the pack you intend to declare exists and is ratified. Today, no pack
is ratified — see
[../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md)
item 10.

---

## 1. Choose the pack

Read the pack's README and its `gates.yaml`. Two questions:

- **Does its gate set match what you would regret not checking?** If the pack has a
  fact-check gate and your work has no factual claims, that gate becomes ceremony —
  which is worse than no gate, because it trains people that gates are ceremony.
- **Can you staff its signatories?** The documentary-history pack declares nine gates
  and `minimum_distinct_signatories: 4`. That is a hiring and budget commitment, not a
  configuration value. Answer it now, not at 1am before a release.

If no pack fits, stop and go to [author_a_pack.md](author_a_pack.md). Do not adopt a
near-fit and plan to request exemptions; canon that routinely grants exemptions is a
suggestion with paperwork.

## 2. Choose the code

A short, lowercase, hyphenated, ASCII slug: `african-history`, `roman-history`. It
becomes a permanent path segment (`studios/<code>/`) and appears in IDs, so it is not
renameable in practice.

## 3. Scaffold

```bash
python -m studio_ops new-studio --code <code> --title "<Title>" --pack <pack-code>
```

**NOT BUILT.** The stub records what it will do: copy `templates/studio/` to
`studios/<code>/`, write `studio.yaml` with the declared pack, and seed the decision
register from that pack's `studio_must_decide` list.

**Today, by hand:**

1. Create `studios/<code>/` with `bible/`, `brand/`, and `lines/`.
2. Write `studios/<code>/studio.yaml`. Use
   [`studios/african-history/studio.yaml`](../../studios/african-history/studio.yaml)
   as the reference — it is the only extant example. It must carry the studio code,
   title, `pack`, and `pack_version`.
3. Write `bible/00_charter.md` from
   [`studios/african-history/bible/00_charter.md`](../../studios/african-history/bible/00_charter.md).
   Every unresolved field is `TBD — needs research` or `TBD — <role> to decide`. Do not
   write a plausible mission statement to make the file look finished.
4. Create the decision register by reading the pack and listing every decision it
   leaves to the studio.
5. Add a row to [`studios/README.md`](../../studios/README.md).

**Caution:** `validate --schemas` checks `studio.yaml` against `studio.schema.json`, so
its *shape* is validated. Nothing checks that the pack you named actually exists —
`validate --packs` is NOT BUILT. A typo in the `pack:` value produces a structurally
valid record pointing at nothing. Check it by eye against the pack's directory name.

## 4. Make the studio's decisions

The pack decides genre; the studio decides brand. Typically: mission, audience, scope
boundaries, editorial independence, voice policy, music policy, runtime and platform
set, accessibility scope, and licensing posture.

Every one of these that is left `TBD` is a decision that will be made implicitly, under
deadline, by whoever is in the room. Making them now is the entire point of a studio
tier.

## 5. Ratify

Nothing generates until this closes.

1. Fill the charter's unresolved sections.
2. Record a ratification entry in the studio's amendment log with **two signatures** —
   for documentary-history, Showrunner and Cultural Advisor.
3. Set the studio record's status to active.

Exit criterion: the amendment log carries a ratification entry with two signatures and
no open blocking items. See [../../ROADMAP.md](../../ROADMAP.md) Phase 1 for the worked
version.

## 6. Verify

```bash
python -m studio_ops validate --schemas --naming --links --root-hygiene
```

Then confirm by inspection, because no validator does it yet:

- [ ] `studio.yaml` names a pack that exists, spelled correctly
- [ ] No platform file was changed. `git diff --stat` should show nothing under
      `core/`, `standards/`, `prompts/`, `templates/`, or `automation/`
- [ ] The charter names no fact that is not sourced, and no `TBD` was quietly filled
- [ ] Signatories for the pack's gate set are named actual people, or the gap is
      recorded as a blocker

If the studio *did* force a change to a platform file, that is an architecture
finding, not a chore. Record it in
[../architecture/evolution.md](../architecture/evolution.md) — it means the abstraction
sits in the wrong place, and moving it is cheaper than working around it.

## 7. Then

Open the first line: [open_a_line.md](open_a_line.md).
</content>
