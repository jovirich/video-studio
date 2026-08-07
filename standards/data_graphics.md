# Data graphics, maps, and timelines

Graphics make claims. A map asserts a border; a chart asserts a quantity; a timeline
asserts a sequence and often a causation. They are held to the same evidence
standard as narration and carry claim IDs like any other assertion.

## Universal rules

1. **Every graphic carries its sources**, on the graphic or in a credit visible in
   the same sequence.
2. **Every graphic has a claim ID** for the assertion it makes, recorded on the shot.
3. **Uncertainty is shown, not smoothed.** Ranges as bands, unattested boundaries as
   gradients, unknown intervals as visible gaps.
4. **No truncated value axes** on bar charts. Line charts may truncate with the
   baseline explicitly labelled.
5. **Legible at 360p on a phone.** Test it, do not assume it.
6. **Colour is not the only encoding.** Pattern, position, or label as well —
   roughly 1 in 12 male viewers will not read a red/green distinction.

## Maps

The highest-risk graphic type in historical documentary, because a clean line on a
map is a strong assertion that the evidence almost never supports.

| Rule | Detail |
|---|---|
| **State the projection** | On the map or in the credit. Different projections make different political arguments about relative size. |
| **Historical polities are zones, not outlines** | Draw influence as gradient or hatched zone. A hard border is drawn only where a documented boundary (a treaty line, a wall, a surveyed limit) is being depicted, and it carries that source. |
| **Modern borders are never drawn over pre-colonial periods** | Unless labelled on screen as a modern overlay for orientation. |
| **Period-appropriate place names primary** | Modern name once, parenthetically, for orientation. Per [../bible/09_localization.md](../packs/documentary-history/09_localization.md) §3. |
| **Coastlines and rivers change** | Use period-appropriate hydrography where evidence exists; note where a modern base map is being used as an approximation. |
| **Scale bar and north indicator** | Always. |
| **Animated expansion** | Animating a polity's growth asserts dates for each stage. Each stage needs a claim ID, or the animation is replaced with a static "at its greatest documented extent" frame. |

Base maps and their licences live in [../library/map_bases/](../library/map_bases).

## Timelines

- **Show the resolution of the evidence.** If a date is known to the decade, the
  marker spans the decade. A tick mark on a specific year asserts precision the
  source may not have.
- **Distinguish attested from inferred events** by visual treatment, keyed.
- **Do not imply causation by adjacency.** Two events near each other on a timeline
  read as connected; if they are not, separate them or label the relationship.
- **Multiple calendars** (Gregorian, Hijri, regnal, local) shown where relevant, with
  the conversion basis recorded on the claim.

## Quantitative charts

| Rule | Detail |
|---|---|
| Attested / estimated / modelled | Encoded visually and keyed. Most pre-modern quantities are modelled. |
| Error bars or bands | Wherever the source gives a range. |
| Source and date | In the frame. |
| Sample and method | For any survey or excavation-derived figure. |
| Per-capita and absolute | Do not switch between them mid-sequence without a title change. |
| Log scales | Labelled prominently. Never used to flatten an inconvenient trend. |

## Diagrams and processes

- Reconstructed processes (smelting, weaving, construction, trade routes) carry the
  archaeological or ethnographic basis for each depicted step.
- Where a step is unattested, mark it. A dashed connector and a key entry are enough.

## Accessibility

- Contrast ≥ 4.5:1 for text, ≥ 3:1 for graphical elements against their background.
- Type ≥ 1/20 frame height.
- On-screen duration ≥ 2× the reading time.
- Described in the audio description track if that track is in scope.
- The narration should carry the graphic's point, so the sequence works audio-only.

## Style

Palette, type, stroke weights, and animation timing come from the line's style
folder and [../brand/](../studios/african-history/brand) — a graphic should look like it belongs to the same
show as the shot before it. Chart construction follows the studio's data
visualisation conventions, not a tool's defaults.

## QC

- [ ] Sources present on or beside the graphic
- [ ] Claim ID recorded on the shot
- [ ] Projection stated (maps)
- [ ] Uncertainty encoded, not hidden
- [ ] No truncated bar axis
- [ ] Legible at 360p
- [ ] Colour-independent encoding present
- [ ] Names match entity records
- [ ] Contrast measured
