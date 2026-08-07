---
title: Incident response
status: active
version: 0.1.0
updated: 2026-08-07
owners: [showrunner, pipeline-engineer, rights-and-clearances]
---

# Incident response

**Maturity: DESIGNED.** Binding now; no tooling.

For when something has **already shipped** and is wrong. Everything caught before
publication is a gate doing its job — that is [../workflows/README.md](../workflows/README.md),
not this file.

## The first sixty seconds

Whatever the incident:

1. **Stop the spread.** Unlist, pause the scheduled post, halt the cutdown, revoke the
   key. Whatever prevents the next copy.
2. **Do not edit anything to make it look better.** Not the published file, not the
   record, not the commit history. Preserve the artefact as it stood. The studio must
   be able to say exactly what it published.
3. **Tell one named human** — the owner in the table below — by the fastest channel
   available, not by opening an issue and hoping.
4. **Write down the time you found out.** Everything downstream is measured from it.

Step 1 before step 3 is deliberate. **Anyone may take protective action without
permission, and nobody is ever penalised for taking it and being wrong.** A studio
where the intern needs approval to unlist a video is a studio that publishes for three
more hours.

## Severity

| Sev | Meaning | Response |
|---|---|---|
| **S1** | Ongoing harm to a person or community: leaked restricted record, unconsented likeness, sacred material published, live credential leak | Immediate action, out-of-hours, whoever is awake |
| **S2** | Rights breach, or a factual error that is load-bearing for an episode's argument | Same working day |
| **S3** | A contained factual error, a wrong caption, a missing credit | Next working day |

When unsure, treat it as one level higher. Downgrading later is free.

---

## Factual error found post-publish

**Owner: Research Lead.** Escalates to Showrunner if the error is load-bearing.

**Immediately**

1. Do not silently re-cut. A quiet fix is a second, worse error — it converts a mistake
   into a concealment, and the internet keeps the original.
2. Establish the scope from the records, not from memory: which `CLM-*` is wrong, which
   sources it rested on, which sequences reference it, which cutdowns, trailers,
   localisations, thumbnails, descriptions, and the sources page inherited it.
3. Determine what the honest state is now. Usually the claim does not vanish — it drops
   register (`established` → `probable` or `contested`), or its evidence turns out
   dependent rather than independent.

**Then**

4. Amend the claim record: `status: retracted` or `superseded`, with
   `retraction_reason` and `superseded_by`. The ID persists forever. Never delete a
   claim — the retracted record is how the studio remembers it was wrong, which is
   worth more than a clean-looking registry.
5. Re-check every sibling claim that shared the failed source. One bad source rarely
   supports one claim.
6. Issue the correction, proportionate to reach:

   | Error | Correction |
   |---|---|
   | Load-bearing for the episode's argument | Re-cut and re-publish, with an on-screen correction card, plus a corrections-log entry and a pinned public note |
   | Materially wrong, not load-bearing | Corrections-log entry, updated description and sources page, pinned note |
   | Minor — a caption, a date within a stated range | Corrections-log entry and an updated sources page |

7. Record it in the production's corrections log **publicly**. The published corrections
   log is not damage control; it is the artefact that makes the accuracy claims
   credible in the first place. A studio with an empty corrections log after a season
   is a studio that is not looking.
8. Ask the process question at the retrospective: which gate should have caught this,
   and what would have had to be different? A fact-check gate that passed a wrong claim
   has a checklist problem, not a diligence problem.

---

## Rights breach

**Owner: Rights & Clearances.** S2, or S1 if the material is a person's likeness or
voice.

**Immediately**

1. Unlist or take down the affected deliverable. Do not wait for legal advice to stop
   distributing.
2. Pull the asset from every unpublished cut, cutdown, and localisation in flight.
3. Check the clearance log. **If the asset is not in it, it was uncleared by
   definition** — that settles the question of what happened, and the remaining work is
   scope, not investigation.

**Then**

4. Tell the Showrunner and the Pipeline Engineer the same day. Tell the rights holder
   directly, in writing, before they have to chase — an unprompted contact changes the
   conversation materially.
5. Decide: licence it retroactively, replace the shot, or cut the sequence. Retroactive
   licensing is often available and is usually cheapest; it is not available for
   unconsented likeness or voice.
6. Log it as a takedown case even if nobody asked — see
   [takedown_procedure.md](takedown_procedure.md). The register is of *events*, not of
   complaints.
7. Sweep for the same cause elsewhere. A breach almost always has a mechanism — a
   vendor whose terms changed, a stock library misread, an asset conformed without a
   manifest entry — and the mechanism has touched other assets.
8. If the cause was a vendor terms change, re-check the model terms register for every
   tool, not just that one, and record the date checked.

---

## Sensitivity breach

**Owner: Cultural Advisor.** S1. Treat as ongoing harm until ruled otherwise.

**Immediately**

1. **Take it down.** Not unlist-and-discuss — down. Sacred, funerary, restricted, or
   an unconsented depiction of a named person or a living family's ancestor.
2. Raise an advisory hold on the asset, the sequence, and every related prompt card.
   Any contributor may do this and it takes effect immediately.
3. Stop all generation touching the same subject matter, including work on other
   productions, until the ruling.

**Then**

4. Notify the Cultural Advisor within hours, and the advisory contact for the community
   concerned. Not the Showrunner first — the Showrunner cannot release the hold, and
   routing through them wastes the hours that matter.
5. **Do not defend it in public before the ruling.** The instinct to explain the
   editorial reasoning immediately is the wrong one; it converts a mistake into a
   position.
6. The Cultural Advisor rules in writing. The ruling — not the Showrunner's judgement
   about it — determines what happens next: permanent removal, re-cut, an on-screen
   acknowledgement, an apology, or return of material.
7. Where the community asks that something not be shown, **the default is to comply.**
   An overriding public-interest argument is made in writing, ruled on, and disclosed on
   screen — it is not assumed.
8. Record: the line's advisory register (the ruling), the takedown register (the event),
   the corrections log (anything public). Amend the affected prompt cards and shot
   records so the same prompt cannot be re-run to the same result.
9. At the retrospective, ask the structural question: did the sensitivity gate run at
   all three of its points — greenlight, before generation, and picture lock? A breach
   usually means it ran once, at the end, when the imagery already existed.

---

## Leaked restricted record

**Owner: Cultural Advisor jointly with Pipeline Engineer.** S1, always.

Includes: a restricted file committed to git; a transcript pasted into an issue, a PR,
or a chat; restricted audio sent to a hosted model endpoint; an anonymised
contributor's identity disclosed; a filename that discloses subject matter.

**Immediately**

1. **Assume it is permanent.** Git history is copied to every clone; a hosted endpoint
   has already received the bytes; a chat message has already been indexed. Act on that
   assumption from the first minute rather than working toward it.
2. Make the repository private and stop pushes, if the leak is in git and the repository
   is public.
3. Revoke the credential or endpoint access involved, if a third-party service received
   the material.
4. Do **not** force-push a history rewrite as the first move. It does not remove copies
   already pulled, it invalidates everyone's clone, and it destroys the evidence of what
   was exposed and for how long. History rewriting is a later, deliberate step taken
   after the exposure is characterised.

**Then**

5. Characterise it, in writing, within 24 hours: exactly what was exposed, from when to
   when, who could have accessed it, whether it was public or internal, whether a
   third-party service retained it, and whether the vendor's terms permitted training on
   it.
6. **Tell the affected contributor, custodian, or community.** Promptly, honestly, in
   their language, without minimising, and before they hear it elsewhere. The studio does
   not get to decide on their behalf that a leak was minor.
7. Ask them what they want done. Options include destruction, removal from the record,
   withdrawal of the material entirely, or public acknowledgement. Their answer governs.
8. Then remediate the technical side: history rewrite where it still helps, key
   rotation, access-list review, and moving the material to the restricted volume it
   should have been on.
9. Record the incident and its cause. The cause is almost always structural — a
   researcher with no local model, a restricted file inside the repo tree, an asset store
   configured under the repository root — and the fix belongs to the structure.

See [restricted_records.md](restricted_records.md) for the standing rules this incident
means were breached.

---

## Credential leak

**Owner: Pipeline Engineer.** S1 if it grants spend or data access; S2 otherwise.

Includes: a committed `.env`, an API key in a prompt card, a service-account JSON, a
key pasted into an issue, a token in a screenshot or a screen share.

**Immediately**

1. **Rotate the credential.** First action, before assessment, before telling anyone,
   before working out whether anyone saw it. Rotation is cheap; assessment is slow.
2. Revoke the old key at the vendor, do not merely replace it locally.
3. Check for use: vendor usage logs, spend, and anything anomalous since the earliest
   possible exposure time — which is the commit date, not the discovery date.
4. If the key had spend authority, set or confirm the vendor-side cap while assessing.

**Then**

5. Remove the file from the working tree and confirm the ignore rules cover it. The CI
   secret scan already fails on a tracked `.env`, `*.pem`, `*.key`, or
   `service_account*.json` — check why it did not fire, because either it was bypassed
   or the pattern has a gap, and both are findings.
6. Decide on history rewriting deliberately. For a credential, the rewrite matters less
   than the rotation — a rotated key in history is inert.
7. Tell the Showrunner if spend or data was involved. Tell the vendor if their terms
   require it.
8. Record it in the production's or the platform's incident notes with the cause. "Key
   in `.env` that was committed because the ignore rule was added later" is a fixable
   cause; "human error" is not.

---

## Where things are recorded

| Incident | Record | Public? |
|---|---|---|
| Factual error | Production corrections log; the claim record's `retraction_reason` | **Yes** — the corrections log is published |
| Rights breach | [Clearance log](../../rights/permissions/clearance_log.md); [takedown register](../../rights/permissions/takedown_log.md) | Outcome only, if the material was public |
| Sensitivity breach | Line advisory register; takedown register; corrections log | Ruling and outcome, per the ruling |
| Leaked restricted record | Restricted incident log, held under restricted access | **No.** Publishing the detail re-discloses the material. Acknowledge the fact where the affected party wishes it. |
| Credential leak | Platform incident notes | No |

The takedown register's fields and the append-only rule are in
[takedown_procedure.md](takedown_procedure.md) § The register.

## After any incident

Two questions at the next retrospective, both structural:

1. **Which gate should have caught this, and why did it not?** If no gate covers it,
   that is a gate-set finding for the pack owner, not a note to be more careful.
2. **What made the wrong thing easy?** Every incident above has a configuration that
   made it likely: no local model available, the asset store inside the repo tree, a
   sensitivity review that ran once at the end instead of three times, a credential
   with no spend cap. Fix the configuration. Diligence does not scale and does not
   survive a deadline; structure does.

Findings that change the architecture go in
[../architecture/evolution.md](../architecture/evolution.md). Findings that change
canon go in the amendment log of the layer that owns the rule.
</content>
