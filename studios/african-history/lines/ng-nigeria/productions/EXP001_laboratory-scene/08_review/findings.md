---
title: EXP-001 findings
status: draft
maturity: NOT STARTED
version: 0.1.0
updated: "2026-08-07"
owners: [pipeline-engineer, showrunner]
---

# EXP-001 — findings

**This is the deliverable.** The twenty shots are the instrument; this document is
the output.

Empty. The production has not started.

## How to use this document

Record breakages **as they happen**, in the moment, at production pace. Reconstructing
them at the end loses exactly the small frictions that compound into a schedule — the
field nobody could interpret, the command that had to be run twice, the ten minutes
spent deciding where a file goes.

A short findings list means the production was made too carefully. Go back and run it
the way a real one would be run.

## Entry format

```
### F-NNN — <one line>

**Area:** research | claims | continuity | prompting | generation | conform |
          gates | tooling | cost | schedule | rights | sensitivity
**Stage:** which pipeline stage
**Severity:** blocker | friction | annoyance | observation

**What happened**
<Concretely. Include the command, the field, the shot number.>

**What it implies**
<About the architecture, not about the person. "The prompt card has no field for X"
is a finding; "I forgot to fill in X" is only a finding if the form invited it.>

**Action:** fix-tooling | amend-canon | amend-schema | change-workflow |
            accept-limitation | open
```

Mirror each entry into `production.yaml` under `findings.breakages`.

## The seven questions

Answer each explicitly at the end, with evidence, whether or not anything broke.

### 1. Did the claim chain survive contact with real research?

`TBD`

The failure signal is in the git history, not in anyone's memory: **do claim records
appear before or after the script drafts that reference them?** If after, the
discipline inverted and the validator is being farmed rather than served. Check the
log; do not ask.

### 2. Did continuity hold across ~20 shots?

`TBD`

Per character and per location: which mechanism, how far it held, where it broke.
Record angle and lighting conditions at the point of failure — "it drifted" is not a
finding, "it drifted past 40° off-axis under low key" is.

If two characters were used: did the mechanism hold them **separately**, or did they
converge?

### 3. Was the prompt card worth its overhead?

`TBD`

Report the `raw_override` rate. ADR 0003 names a rising rate as its own falsification
condition — if most cards used it, the structure does not fit the tools and should be
revised rather than defended.

Also: how long did a card take to write, against how long a bare prompt would have?

### 4. Could the gates be staffed?

`TBD`

How many distinct people actually signed? Did anyone sign work they produced? The
laboratory relaxation permits a shortfall **only if it is recorded here** — so record
it, with the number.

### 5. Did the manifest get filled?

`TBD`

Did any asset reach the edit without a provenance entry? If yes, the traceability
guarantee is currently documentation rather than a property of the system, and
`pipeline conform` moves to the top of the build queue.

### 6. What did a finished second cost?

`TBD`

In money and in hours, separately. Include rejected generations — they are most of
the cost and they are what a naive estimate omits. This number is what makes a season
budget real instead of aspirational.

### 7. Which schema fields were dead weight?

`TBD`

**List every field nobody filled, and every field filled `TBD` and never read again.**

This repository is over-built by design and this experiment is the instrument for
cutting it back. A field that survived twenty shots without being used is a candidate
for deletion, and proposing its removal is as valuable as reporting a bug. Be
ruthless — the cost of an unused field is not storage, it is the attention of every
person who fills it out forever.

## Findings

<!-- F-001 onward, appended as they occur. -->

*None recorded. Production has not started.*

## Actions arising

| ID | Finding | Action | Owner | Landed |
|---|---|---|---|---|
| — | — | — | — | — |

Architecture-level actions go to
[`docs/architecture/evolution.md`](../../../../../../../docs/architecture/evolution.md).
Canon changes go to the relevant amendment log. Tooling changes go to
[`docs/status.md`](../../../../../../../docs/status.md) with a maturity update.
