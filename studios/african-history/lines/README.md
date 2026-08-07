# Production lines — African History Studio

A **line** is a coherent body of work: a region, a period strand, or a diaspora
thread. It owns its own research, sources, entities, language policy, advisory board,
and visual identity. It inherits everything else from the studio, the pack, and the
platform.

## Open and opening

| # | Line | Code | Status | Lead |
|---|---|---|---|---|
| 01 | Nigeria | [`ng-nigeria`](ng-nigeria) | `candidate` | TBD |

## Opening conditions

A line moves to `open` only when all three are true. The
[production_line schema](../../../standards/schemas/production_line.schema.json)
enforces it — `line_status: open` fails validation while any is false.

1. **A named research lead with domain competence has agreed to own it.**
2. **At least one advisory contact with standing in that region has agreed to review.**
3. **The archive landscape has been surveyed** and recorded in the line's
   `sources/archive_landscape.md`.

Condition 2 is the one that gets skipped under enthusiasm, and skipping it is the
most reliable way to produce work that insults the people it claims to honour.

## Candidate lines

Not a plan. A record of what has been considered, so that ordering is a decision
rather than an accident of whose history was easiest to research in English.

| Line | Note |
|---|---|
| — | No candidates registered. Add them with the reasoning for their priority, including honest notes on archive accessibility and advisory reach. |

When adding a candidate, record:
- why this line, and why now,
- who could lead it,
- who could advise, and whether they have been approached,
- what the archive landscape looks like, including what is held outside the region,
- what languages the evidence is in.

## Opening a line

```bash
python -m studio_ops new-line --studio african-history --code gh-ghana --title "Ghana"
```

Scaffolds from [templates/line/](../../../templates/line) with `line_status:
candidate` and all opening conditions false. Nothing else in the repository changes.

## Cross-line material

Trade, migration, empire, and diaspora do not respect modern borders. Sources
spanning more than one line use the `STUDIO` scope (`SRC-STUDIO-0001`) and live in
the studio's shared registry rather than in any one line.

Where two lines make claims about the same events, the claims are cross-referenced
and any disagreement is resolved explicitly — not left for a viewer to discover.
