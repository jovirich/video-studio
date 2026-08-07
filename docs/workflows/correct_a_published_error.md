---
title: Correct a published error
status: active
version: 0.1.0
updated: 2026-08-07
owners: [research-lead, showrunner]
---

# Correct a published error

For a **factual** error found after publication. If the issue is a rights breach, a
sensitivity breach, a leaked restricted record, or a credential leak, go to
[../runbook/incident_response.md](../runbook/incident_response.md) instead — those have
immediate protective actions this workflow does not.

If the error arrived as a request from outside the studio, log it as a takedown case
first: [../runbook/takedown_procedure.md](../runbook/takedown_procedure.md). Then come
back here.

> **The rule that governs this entire procedure: do not silently re-cut.** A quiet fix
> converts a mistake into a concealment, and the original is already downloaded,
> mirrored, and quoted. The published corrections log is not damage control — it is the
> artefact that makes the accuracy claims credible in the first place. A studio with an
> empty corrections log after a season is a studio that is not looking.

---

## 1. Establish scope from the records, not from memory

The whole point of claims-as-records is that this step is mechanical.

1. Identify the wrong claim: `CLM-*`.
2. List its supporting sources from its `evidence` array.
3. List everything that references the claim — narration, on-screen text, graphics,
   maps, chapter titles, the episode description, the thumbnail text, the sources page,
   every cutdown, trailer, localisation, and dub.

```bash
python -m studio_ops report dependents --claim <CLM-ID>
```

**NOT BUILT.** Today: grep the production's script and on-screen text for the claim ID,
then check the sources page and every derived deliverable by hand. Write the list down —
step 6 works from it, and the derived deliverables are where a correction is most often
forgotten.

## 2. Establish what the honest state is now

Usually the claim does not vanish. It moves.

| What went wrong | Usual outcome |
|---|---|
| A source was misread or mistranslated | Claim amended; register may hold |
| The evidence turned out dependent, not independent | Register drops: `established` → `probable` |
| Scholarship has moved | Register may become `contested`, with both positions named |
| The source itself was unreliable about this thing | Claim retracted; sibling claims on that source re-checked |
| A figure was falsely precise | Restate as a range; record whether it is attested, estimated, or modelled |

**Change the register down; do not adjust the claim up to fit what shipped.** That
temptation is strongest at exactly this moment, because the alternative is a re-cut.

## 3. Re-check the siblings

Every other claim resting on the same source. One bad source rarely supports one claim,
and the second error found by a viewer after you announced the first is much more
expensive than the first.

## 4. Amend the records

1. Set the claim's `status` to `superseded` (with `superseded_by`) or `retracted` (with
   `retraction_reason`).
2. Create the replacement claim with a **new ID** if the statement changed materially.
3. If the source is at fault, amend its record — its critique block should now say what
   it turned out not to be reliable about, which is the most useful thing that source
   record will ever contain.
4. **Never delete a record.** IDs are permanent and a retracted record is a tombstone.
   Deleting it destroys the audit trail that justifies keeping the whole system, and it
   makes the correction itself unverifiable.

## 5. Choose the response, proportionate to reach

| Error | Response |
|---|---|
| Load-bearing for the production's argument | Re-cut and re-publish, with an on-screen correction card. Plus everything below. |
| Materially wrong, not load-bearing | Corrections-log entry, updated description and sources page, pinned public note |
| Minor — a caption, a date inside a stated range, a name form | Corrections-log entry and an updated sources page |

The test is not embarrassment. It is: **would a viewer who learned this feel informed,
or misled?** If misled, it goes on screen.

## 6. Re-open the gates

A published error means a gate certified something that was not true. Re-opening is the
mechanism that makes that visible.

1. Request a re-open with a stated reason. The gate owner decides.
2. On re-open the gate returns to `pending`, **the prior signature is retained in
   history**, and every downstream gate signed on the basis of it also returns to
   `pending`.
3. Work back through the cascade for real. A corrected claim usually means fact-check,
   picture lock (if the visuals change), audio lock (if narration is re-recorded),
   rights (if an asset changes), and technical QC.

Apply the fix to **every** derived deliverable from step 1. Cutdowns and localisations
inherit the error and are the ones that get missed.

## 7. Publish the correction

- Corrections-log entry: what was wrong, what is right, the evidence, the date, who
  made the correction.
- Updated sources page, regenerated from the amended records — not hand-edited, or it
  will disagree with them.
- A pinned public note where the error was public.
- Tell anyone who reported it, and tell them what changed. People who report errors and
  hear nothing stop reporting errors.
- Where a contributor, community, or custodian is affected, tell them directly, in
  their language, before they find it.

## 8. Fix the cause

Two questions at the retrospective, and both are structural:

1. **Which gate should have caught this, and why did it not?** A fact-check gate that
   passed a wrong claim has a checklist problem, not a diligence problem.
2. **What made the wrong thing easy?** Independence not asserted because the schema does
   not require it. On-screen text not fact-checked because only narration was. A map
   drawn from a claim nobody linked. These are configuration failures, and diligence
   does not scale.

Then act at the layer that owns the cause: a checklist change is a pack change; a
schema change is a standards change; a structural change goes in
[../architecture/evolution.md](../architecture/evolution.md). None of them rides along
in a production PR.

## 9. Verify

```bash
python -m studio_ops validate --schemas --naming --links --root-hygiene
python -m studio_ops validate --sources        # NOT BUILT — walk the chain by hand
```

- [ ] Amended and retracted records carry reasons, and no record was deleted
- [ ] Every derived deliverable from step 1 is fixed or explicitly out of scope
- [ ] The re-opened gates are re-signed, by people permitted to sign them
- [ ] The corrections log is public, and the sources page matches the records
- [ ] The cause has an owner at the right layer
</content>
