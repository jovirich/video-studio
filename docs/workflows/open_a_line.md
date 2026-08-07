---
title: Open a line
status: active
version: 0.1.0
updated: 2026-08-07
owners: [showrunner, research-lead, cultural-advisor]
---

# Open a line

A production line is a coherent strand of a studio's work — a region, a series, a
season strand. It owns its research, sources, entities, language policy, advisory
board, and visual identity, and inherits everything above it.

Opening a line is not a scaffolding task. It is mostly a **relationships and staffing**
task, and the folder is the easy part. A line moves from `candidate` to `open` only
when its opening conditions are all true, and those conditions are about people.

---

## 1. Register the line as a candidate

```bash
python -m studio_ops new-line --studio <studio> --code <code> --title "<Title>"
```

**NOT BUILT.** The stub records what it will do: copy `templates/line/` to
`studios/<studio>/lines/<code>/` with `line_status: candidate` and all opening
conditions `false`.

**Today, by hand:** create `studios/<studio>/lines/<code>/` and write `line.yaml`
against
[`standards/schemas/production_line.schema.json`](../../standards/schemas/production_line.schema.json),
with `line_status: candidate` and every opening condition explicitly `false`. Add the
line to
[`studios/african-history/lines/README.md`](../../studios/african-history/lines/README.md)
or its equivalent.

The code is a permanent path segment and the basis of the ID scope
(`ng-nigeria` → `SRC-NG-*`). Choose it once. See
[`standards/id_system.md`](../../standards/id_system.md).

**A candidate line does no research and creates no records.** It exists so the
commitment is visible and so the opening conditions have somewhere to live.

## 2. Name a research lead with real competence in the material

Not a generalist with search access. Someone with historiographical competence in the
line's subject, who knows the scholarly disputes, and who can read or commission
reading in the languages the evidence is actually in.

This is first because everything else depends on it, and because it is the condition
most often deferred and then never met.

## 3. Recruit and contract the advisory board

Per [`07_cultural_sensitivity.md`](../../packs/documentary-history/07_cultural_sensitivity.md)
§5. The advisory register names:

- each advisor, their standing and expertise, and **what they are and are not competent
  to rule on**,
- the communities and traditions covered, and **the gaps not yet covered**,
- terms: fee, credit, review rights, right to withdraw.

Two rules with teeth:

- **Advisors are paid.** An advisor who is not paid is not an advisor; they are a
  favour being taken advantage of, and they will eventually and rightly stop answering.
- **A line does not begin production on material outside its advisory coverage.** If no
  one on the register is competent on a tradition an episode needs, the episode waits.
  This is why the register records the gaps as explicitly as the coverage.

## 4. Survey the archive landscape

Before assessing what you can reach, map where evidence could exist: archives in-region
and ex-region, museum and university collections, excavation reports and site archives,
oral tradition holders and the institutions that recorded them, scholarship including
work not in English, and material culture in private and community hands.

Record it as the line's `sources/archive_landscape.md`, and **record explicitly what is
inaccessible and why** — held abroad, undigitised, restricted, lost, uncatalogued. The
distribution of what survives is itself historically informative and frequently belongs
on screen.

The accessible-first temptation is strong and systematically biases toward the
coloniser's record, because that is the record that was catalogued, digitised, and
translated. The survey is how you see that happening.

Method: [`methodology/research_protocol.md`](../../packs/documentary-history/methodology/research_protocol.md)
Stage 2.

## 5. Set language and naming policy

Which languages appear on screen, which orthography, which name form for each people
and place and why, diacritic handling, and pronunciation. Then **select typefaces with
full diacritic coverage** — this blocks all brand design, and discovering a missing
combining mark after a title sequence is designed is expensive.

## 6. Define the visual identity

Palette, lens set, grade, show LUT, and the style-anchor set. Every prompt card in the
line inherits from this, so an undefined identity means every card improvises and
continuity is impossible.

## 7. Set up the line's folders

```
studios/<studio>/lines/<code>/
  line.yaml
  research/           open questions, briefs
  sources/            registry/records/ (SRC-*), registry/claims/ (CLM-*), archive_landscape.md
  entities/           characters, locations, organisations, objects, timeline events
  language/           style guides, pronunciation
  advisory/           register, rulings
  style/              style block, anchors
  productions/
```

**Records live here, at the line level** — not in the pack, which holds method only.
See [`packs/documentary-history/sourcing/README.md`](../../packs/documentary-history/sourcing/README.md).

**Before creating the first record, read this:** `new-record` is NOT BUILT, so IDs
would be allocated by hand, and hand-allocated IDs collide silently and corrupt the
reference graph — records reference each other by ID string, not by path, and the gate
that would detect it (`validate --sources`) is also NOT BUILT. Either build the
allocator first, or keep a single append-only ID ledger and update it *before* creating
each record. See
[../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md)
item 2.

## 8. Open it

Set `line_status: open` only when every opening condition is `true`. The schema is
intended to refuse `open` otherwise.

Checklist before flipping it:

- [ ] Research Lead named and engaged
- [ ] Advisory board contracted; register populated, including its gaps
- [ ] Archive landscape survey written, including what could not be reached
- [ ] Language and orthography policy set
- [ ] Typefaces selected with full diacritic coverage
- [ ] Visual identity defined: palette, lens set, grade, LUT
- [ ] Voice policy set and narration cast
- [ ] ID allocation solved — allocator built, or ledger in place

```bash
python -m studio_ops validate --schemas
```

## 9. Then

[run_a_production.md](run_a_production.md).
</content>
