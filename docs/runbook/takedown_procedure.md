---
title: Takedown procedure
status: active
version: 0.1.0
updated: 2026-08-07
owners: [rights-and-clearances, showrunner, cultural-advisor]
---

# Takedown procedure

**Maturity: DESIGNED.** Binding now; no tooling. Required by
[`core/02_rights_and_licensing.md`](../../core/02_rights_and_licensing.md) §9.

Covers any request that published material be removed, altered, credited differently,
or withdrawn — whether it comes from a rights holder, a community, a contributor, a
descendant, an institution, or a member of the public.

A takedown request is not an accusation to be defended against. It is frequently the
studio's first notice that something is wrong, and it is cheaper to be told than to be
found out.

## How the studio is reached

All of these are valid entry points, and none may be refused for arriving by the wrong
one. A request that reaches any contributor by any route becomes a takedown request
the moment it is recognised as one.

| Route | Published where |
|---|---|
| Takedown address — a monitored mailbox owned by Rights & Clearances | On every episode's public page, in the description, and on the studio site |
| Episode sources page | Alongside the citation list, with the same address |
| A `[sensitivity]` issue in this repository | Available to any contributor; also raises an advisory hold |
| Any contributor, by any means — in person, by phone, at a screening | Whoever receives it **logs it that day**. Not "passes it on". |

`TBD` — the takedown address itself is a Phase 1 decision and must exist before the
first publication. An episode published without a route for objection is an episode
that has decided not to hear one.

Requests are accepted in any language the line works in. A request in a language the
studio does not read is translated at the studio's cost, not returned.

## Response SLA

Time runs from **first receipt by anyone at the studio**, not from when it reaches the
right person.

| Stage | Bound | Who |
|---|---|---|
| Acknowledge receipt, by name, with a case reference | **2 working days** | Rights & Clearances |
| Assess and classify (see below) | **5 working days** | Rights & Clearances + the relevant gate owner |
| Substantive response with a decision and reasons | **15 working days** | The decision owner for that class |
| Interim protective action where harm is plausible and ongoing | **Immediately, before assessment** | Anyone. See below. |

The 15-day clock does not pause because a decision is difficult. If the studio needs
longer, it says so before day 15, with a date and a reason.

### Interim action comes first

Where the request alleges sacred, funerary, or restricted material; a depiction of an
identifiable living person or a named ancestor of a living family; or an unconsented
likeness or voice — **restrict the material immediately**, before assessing anything.
Unlist or take down the video, pull the asset from every unpublished cut, and stop all
derivative work.

This is not an admission. It is the default because the cost is asymmetric: an unlisted
video for eleven days costs the studio views, and a wrongly-published depiction of
restricted material costs someone else something that cannot be given back.

Anyone may take this action. Nobody is penalised for taking it and being wrong. That
guarantee is what makes it actually happen.

## Classify, then route

| Class | Example | Decides | Default posture |
|---|---|---|---|
| **Rights claim** | A rights holder says an archival still was used without licence; a music claim; a font or LUT licence breach | Rights & Clearances | Verify against the clearance log. If it is not in the log, it was uncleared by definition — remove or licence it. |
| **Community objection** | A community says material is sacred, restricted, funerary, or was obtained without the right consent | **Cultural Advisor** | Comply. Where the studio believes there is an overriding public-interest reason, it is argued in writing, ruled on by the Cultural Advisor, and disclosed on screen. |
| **Contributor withdrawal** | An interviewee withdraws consent, or asks for anonymity | Research Lead + Cultural Advisor | Follow [restricted_records.md](restricted_records.md) § Withdrawal. |
| **Factual error** | A claim is wrong | Research Lead | Follow [incident_response.md](incident_response.md) § Factual error. A correction, not usually a takedown. |
| **Personal / privacy** | An identifiable living person objects to their depiction or naming | Showrunner + Cultural Advisor | Remove or obscure pending assessment. |
| **Bad faith or out of scope** | No basis; a demand for editorial control over accurate, cleared, sourced material | Showrunner | Still answered, in writing, with reasons, within SLA. |

Where a request spans classes — most substantial ones do — the **most protective**
class governs the interim action and every named decider is involved in the outcome.

## Escalation

```
Received by anyone
      │  logged same day
      ▼
Rights & Clearances ── acknowledges (2d), classifies (5d)
      │
      ├── rights ──────────► Rights & Clearances decides
      ├── community ───────► Cultural Advisor decides ── the Showrunner CANNOT overrule
      ├── contributor ─────► Research Lead + Cultural Advisor
      └── editorial ───────► Showrunner
                                  │
                       unresolved │ or requester disputes the outcome
                                  ▼
                  Showrunner + Cultural Advisor + Platform Owner,
                  jointly, in writing, with the advisory contact for
                  the community concerned present where relevant
                                  │
                                  ▼
                        External counsel, where legal
                        exposure or a formal notice is involved
```

The one asymmetry that matters: **on a community objection the Cultural Advisor's
ruling stands, and the Showrunner cannot unilaterally release it.** This is the single
structural check on the Showrunner's editorial authority and exists because the cost of
being wrong here is borne by people outside the studio. Escalation may seek a different
ruling from the advisor; it may not go around them.

## What is preserved for the record

Removing material from publication does not mean removing it from the record. The
studio must be able to say later, precisely, what it published, when it stopped, and
why.

| Preserved | Where | Note |
|---|---|---|
| The request itself, verbatim, with date and route | Takedown register | Redact the requester's personal details in any published summary; keep the full version restricted |
| The published artefact as it stood | Asset store, marked `withdrawn`, retained | **Not deleted.** You cannot answer "what exactly did you publish?" from a deleted file. |
| The manifest and gate signatures at publication | Git — already immutable | This is why gates leave a commit |
| Assessment, classification, and reasoning | Takedown register | Including reasoning for a refusal |
| The decision, the date, who made it | Takedown register + the line's advisory register where a ruling was involved | |
| Corrections issued and how they were surfaced | The production's corrections log | Public where the error was public |
| Claims and source records affected | The records themselves — `retracted` with a reason, never deleted | IDs persist as tombstones |

Two exceptions to preservation, and only two:

1. **Restricted material disclosed in error** — the default is destruction at the
   holder's direction, not retention. The *record* of the incident is preserved; the
   material is not. See [restricted_records.md](restricted_records.md).
2. **Material a court or a binding agreement requires be destroyed.** Record the
   instruction, then comply.

## The register

[`rights/permissions/takedown_log.md`](../../rights/permissions/takedown_log.md) — the
studio's single register of every request and its outcome. Owned by Rights &
Clearances. It is empty, which is correct: nothing has been published.

One row per request, append-only, never edited after the outcome is recorded:

| Field | Notes |
|---|---|
| `case` | `TD-YYYY-NNN`, allocated on receipt, never reused |
| `received` | ISO date, of **first** receipt by anyone |
| `route` | How it arrived |
| `requester` | Name or organisation; `withheld` where anonymity was asked for, with the detail held restricted |
| `subject` | Production, asset ID, claim ID, or sequence |
| `class` | Per the table above |
| `interim_action` | What was restricted, when, by whom, or `none` and why |
| `acknowledged` / `assessed` / `responded` | Dates, so SLA performance is visible rather than asserted |
| `decision` | Comply, partially comply, refuse — with reasons |
| `decided_by` | Role and person |
| `records_affected` | `SRC-*`, `CLM-*`, `AST-*` retracted or amended |
| `outcome_communicated` | Date, and whether the requester accepted it |

Review the register at every season retrospective. A pattern in it is a finding about
the process, not about the requesters — three community objections against one line is
a coverage gap in the advisory register, and the fix is upstream of any individual
case.
</content>
