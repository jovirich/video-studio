---
title: Runbooks
status: active
version: 0.1.0
updated: 2026-08-07
owners: [pipeline-engineer, showrunner]
---

# Runbooks

Operational procedures. A runbook is written for the person who has to act **now**,
possibly at an awkward hour, possibly without the person who normally does this. It
opens with what to do, not with why.

Editorial rules live in [`core/`](../../core/) and [`packs/`](../../packs/). Step-by-step
production procedures live in [../workflows/](../workflows/). This folder is for
operations and for things going wrong.

## The runbooks

| Runbook | Use when | Maturity |
|---|---|---|
| [environment.md](environment.md) | Setting up locally, or the validators behave differently on your machine | **IMPLEMENTED** — the steps run today |
| [asset_storage.md](asset_storage.md) | Ingesting, storing, verifying, or restoring media | **DESIGNED, NOT BUILT** — no code, no proven round trip |
| [restricted_records.md](restricted_records.md) | Material is under restricted access, community control, or contributor anonymity | **DESIGNED** — procedure is binding now; tooling does not exist |
| [takedown_procedure.md](takedown_procedure.md) | A rights holder or community asks for something to come down | **DESIGNED** — binding now |
| [incident_response.md](incident_response.md) | Something has already shipped and is wrong | **DESIGNED** — binding now |

The maturity column matters and is not decoration. `environment.md` describes commands
that work. `asset_storage.md` describes a contract that nothing implements — following
it today means doing the steps by hand and recording them. The three procedural
runbooks are binding regardless of tooling: they describe what humans do, and humans
exist.

## The shape of a runbook here

1. **When to use this** — the trigger, in one line.
2. **Immediate actions** — numbered, imperative, in the order they are done. First
   step is always the one that stops the bleeding.
3. **Who is told, and when** — by role, with a time bound.
4. **Where it is recorded** — the register, by path.
5. **Then, and only then**, the explanation.

If a runbook cannot be executed by someone who has not read the surrounding canon, it
is not finished.

## Two rules that apply to all of them

**Media never enters git.** Git holds the manifest, the records, and the text. Media
lives in the asset store. See [asset_storage.md](asset_storage.md) — this is enforced
socially today, because the conform step that would enforce it mechanically is NOT
BUILT.

**Restricted material never enters git in any form** — not the file, not a transcript,
not an excerpt, not a summary in an issue. See
[restricted_records.md](restricted_records.md). Git history is effectively permanent
and is copied to every clone; there is no such thing as quietly removing something
from it.

## Related

- [../status.md](../status.md) — what actually runs
- [../architecture/refinements_before_episode_one.md](../architecture/refinements_before_episode_one.md) — the known gaps behind these runbooks, and what each blocks
- [../api/README.md](../api/README.md) — the `studio_ops` command surface
- [../../automation/README.md](../../automation/README.md) — the toolkit's own maturity table
</content>
