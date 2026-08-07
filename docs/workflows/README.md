---
title: Workflows
status: active
version: 0.1.0
updated: 2026-08-07
owners: [platform-owner, showrunner, pipeline-engineer]
---

# Workflows

End-to-end procedures, written as numbered steps you can follow while doing the thing.

| Workflow | Use when | Tooling |
|---|---|---|
| [open_a_studio.md](open_a_studio.md) | A new brand or subject, same kind of video | `new-studio` — **NOT BUILT** |
| [open_a_line.md](open_a_line.md) | A new strand inside an existing studio | `new-line` — **NOT BUILT** |
| [run_a_production.md](run_a_production.md) | Brief through publish, gate by gate | `new-production`, `report *`, `pipeline *` — all **NOT BUILT** |
| [author_a_pack.md](author_a_pack.md) | A genuinely different **kind** of video, with different obligations | `new-pack` — **NOT BUILT** |
| [correct_a_published_error.md](correct_a_published_error.md) | Something shipped and is wrong | none |

Which of the first four you need is one decision, and the decision tree is in
[../architecture/spinning_up.md](../architecture/spinning_up.md). The only question
that takes real thought: **is this a different kind of work, or the same kind about a
different subject?** Rome is the same kind of work as Nigeria — it needs a studio, not
a pack.

## Every command here is NOT BUILT

Read this before following any procedure in this folder.

Of the entire `studio_ops` surface, four validators execute:
`validate --schemas --naming --links --root-hygiene`. **Every scaffolder, every
report, every pipeline command, and the prompt renderer are NOT BUILT** and exit
non-zero with a description of what they will do and what they are blocked on.

So each workflow shows the command as specified, and immediately below it the manual
equivalent to do today:

> ```bash
> python -m studio_ops new-line --studio african-history --code gh-ghana
> ```
> **NOT BUILT.** Today: copy `templates/line/` by hand, set `line_status: candidate`,
> set every opening condition to `false`, then run `validate --schemas`.

The manual equivalent is not a workaround to be embarrassed about. It is the
specification of what the scaffolder must do, written by the person who had to do it —
which is the correct order. Where a manual step is materially risky (ID allocation, in
particular), the workflow says so and says what to do instead.

Per-command maturity and exit codes: [../api/README.md](../api/README.md).

## The rules that apply to all of them

| Rule | Where it comes from |
|---|---|
| Nothing generates before script lock | The pack's gate set — generating for an unlocked script means writing toward the footage you happen to have |
| The sensitivity gate runs three times: greenlight, before generation, picture lock | Once a striking image exists, the argument about whether it should exist is much harder |
| No person signs two gates on one production | [core/04](../../core/04_review_gate_framework.md) §5 |
| Media never in git; restricted material never in git in any form | [../runbook/asset_storage.md](../runbook/asset_storage.md), [../runbook/restricted_records.md](../runbook/restricted_records.md) |
| A studio-level change never rides along in a production PR | [../../CONTRIBUTING.md](../../CONTRIBUTING.md) § Branching |
| `TBD — needs research` beats a plausible placeholder, always | [../../packs/documentary-history/02_evidence_and_sourcing.md](../../packs/documentary-history/02_evidence_and_sourcing.md) §9 |

## Related

- [../runbook/](../runbook/) — operations and things going wrong
- [../onboarding/first_week.md](../onboarding/first_week.md) — read before your first change
- [../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md) — what is weak in these procedures right now
</content>
