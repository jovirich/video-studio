---
title: Restricted records
status: active
version: 0.1.0
updated: 2026-08-07
owners: [cultural-advisor, research-lead, rights-and-clearances]
---

# Restricted records

**Maturity: DESIGNED.** The procedure is binding now. No tooling enforces it; every
step here is done by a human, and that is the current state of the control.

Referenced by
[`packs/documentary-history/02_evidence_and_sourcing.md`](../../packs/documentary-history/02_evidence_and_sourcing.md)
§8 and
[`methodology/oral_history_protocol.md`](../../packs/documentary-history/methodology/oral_history_protocol.md)
§7.

## What counts as restricted

Any material in one or more of these states. When in doubt, it is restricted until the
Cultural Advisor says otherwise — the asymmetry is deliberate, because the cost of
wrongly restricting is a delay and the cost of wrongly releasing is unrecoverable.

| Category | Examples | Set by |
|---|---|---|
| **Restricted access** | Archive material under an embargo, a custodian agreement forbidding reproduction, an unpublished scan licensed for consultation only | The custodian. Recorded in the source record's `custody.access` as `restricted` or `embargoed` and in `custody.access_conditions`. |
| **Community control** | Knowledge restricted by initiation, office, gender, or age; sacred, ritual, funerary, or initiatory material; community-held knowledge an individual cannot license alone | The community's decision-making body, via the advisory register. `custody.access: community-controlled`. |
| **Contributor anonymity** | An interview where the holder chose anonymised or withheld attribution; testimony whose subject matter creates risk for the speaker | The contributor, on the consent form. Revisitable by them at any time. |

Two clarifications that come up constantly:

- **Wide availability is not consent.** Restricted material that circulates freely
  online is still restricted. [`07_cultural_sensitivity.md`](../../packs/documentary-history/07_cultural_sensitivity.md)
  §3 states this as a standing prohibition.
- **An individual's consent may not be sufficient.** Where knowledge belongs to a
  community rather than a person, the studio does not decide for itself that one
  person's permission was enough.

## The absolute rule

> **Restricted material never enters git. In any form.**

Not the file. Not a transcript. Not an excerpt or a quotation. Not a paraphrase in a
claim record. Not a description in an issue, a PR comment, a commit message, or a
research note. Not a filename that discloses the content.

Git history is permanent in effect and is copied in full to every clone. There is no
quiet removal: rewriting history requires a force-push, invalidates everyone's clone,
and does not touch the copies already pulled, the forks, or any mirror. Treat anything
committed as published to everyone who has ever cloned the repository.

What *does* go in git is the **pointer**: a source record with an ID, a tier, a
`custody.access` value, `access_conditions`, a critique block written at a level of
generality that discloses nothing, and — critically — a `sensitivity` value that marks
the record itself as restricted. A reader of the repository learns that the evidence
exists, who controls it, and what it supports. They do not learn what it says.

## Who holds the key

| Question | Answer |
|---|---|
| Who decides whether material is restricted, and at what level? | **Cultural Advisor**, for community and sensitivity grounds. Their ruling is written and recorded in the line's advisory register. |
| Who holds custodian and embargo conditions? | **Rights & Clearances**, in the clearance record. |
| Who holds the storage credentials for the restricted volume? | **Pipeline Engineer**, plus exactly one named backup. Two people, no more, both named in the line's control record. |
| Who may grant access to a specific restricted item? | The **Cultural Advisor** for community-controlled material; **Rights & Clearances** for custodian-restricted material. Both, where both apply. |
| Who cannot override any of this? | The **Showrunner.** An advisory hold is released only by a written Cultural Advisor ruling — [`core/04`](../../core/04_review_gate_framework.md) §6 and the pack's §4. |

Access is granted **per item, per person, for a stated purpose, with an end date.**
Not per role, not standing, not "the research team". Every grant is recorded: item,
person, purpose, granted by, date, expiry.

## Processing: local models only

Restricted material is **never sent to a third-party model endpoint.** No
transcription, no translation, no summarisation, no OCR, no "just to see what it
says", no clean-up pass.

| Task | Permitted route |
|---|---|
| Transcription | A local or self-hosted model on the machine holding the material, or a human under NDA |
| Translation | A named human translator under agreement, credited; a local model as a first pass only, and only where the consent explicitly covers AI processing |
| Summarisation, structuring | Locally, or by hand |
| Anything at all on a hosted API | **Prohibited**, regardless of the vendor's no-training claim, unless there is a signed no-training contract *and* the source's permission covers it — both, not either |

Consent that does not state the AI-processing scope is **not valid for this studio's
purposes**. This is not a formality: a contributor who agreed to be recorded in 2026
did not thereby agree to have their voice pass through a vendor's endpoint. See
[`oral_history_protocol.md`](../../packs/documentary-history/methodology/oral_history_protocol.md)
§2 and
[`methodology/using_ai_in_research.md`](../../packs/documentary-history/methodology/using_ai_in_research.md).

The practical consequence is that a researcher working with restricted material needs
a local model on their own machine before the interview, not after it. Arrange it at
Stage 1 of the research protocol.

## Storage

| Rule | Detail |
|---|---|
| Separate volume | A restricted volume distinct from the general asset store. Different credentials, different bucket or disk, different access list. Not a subfolder with a warning in the name. |
| Encrypted at rest | Full-volume or per-object. The key is held by the two named holders. |
| Not synced | Excluded from any general sync, backup-to-cloud, or desktop indexing tool. Consumer sync clients are the most common accidental-disclosure vector in small teams. |
| Backed up under the same rule as everything else | Two copies, two locations, one offline — but both copies live under the restricted regime, and the offline copy is physically secured. See [asset_storage.md](asset_storage.md). |
| Access logged | Who opened what, when. Manually, in the line's restricted-access log, until tooling exists. |
| Filenames disclose nothing | `SRC-NG-0088_restricted_v01.wav`, not the subject matter. Filenames leak through backups, screenshots, and file pickers. |

## Retention

Shorter of:

- the pack's default — life of the studio plus seven years, or
- the term stated on the consent form or the custodian agreement.

**The contributor's or custodian's term always wins**, including when it is
inconvenient. A retention period that expires is acted on: the material is destroyed,
the destruction is recorded against the source record, and the record itself remains
as a tombstone.

The default for restricted knowledge that was disclosed unintentionally is *not
retention*. Per the oral history protocol §7: stop, do not transcribe further, flag
the recording, raise it with the Cultural Advisor, and the default is that it is not
used and the recording is returned or destroyed at the holder's direction. **A
recording that exists is a recording that can leak. The only reliable protection is
not keeping it.**

## Withdrawal

A contributor may withdraw. Some of what follows is possible and some is not, and the
consent form must have said so honestly at the time — a form that implied full
retraction after release was misleading when it was signed.

**On receiving a withdrawal request:**

1. **Acknowledge within two working days**, in the contributor's language, naming a
   person who is handling it. Do not begin by explaining what cannot be undone.
2. **Stop all use immediately.** The material comes out of every unlocked cut, every
   draft, every research pack, and every prompt input, that day. This does not wait
   for a decision.
3. **Tell**, within the same two days: Research Lead, Cultural Advisor, Rights &
   Clearances, Showrunner.
4. **Establish scope with the contributor.** Withdrawal of the recording? Of
   attribution only? Of specific passages? Of future use but not the published
   episode? Ask; do not assume the maximum or the minimum.
5. **Apply it**, in this order of what is achievable:

   | State | What withdrawal does |
   |---|---|
   | Not yet used | Full. Material destroyed, source record `retracted` with reason, claims re-derived or dropped. |
   | In an unlocked cut | Full. Removed and re-cut. |
   | In a locked cut, not published | Full. Re-open the affected gates — the cascade in `core/04` §4 is the mechanism, and this is exactly what it is for. |
   | Published | Partial and honest. Pull or re-cut the published version, remove attribution, remove from all future cutdowns, trailers, and localisations. What cannot be undone: copies already downloaded, mirrored, or reposted. Say so plainly. |
   | Anonymity requested after named publication | Re-cut to remove the name, update the sources page, contact platforms hosting copies. Do not promise erasure you cannot deliver. |

6. **Re-derive the affected claims.** Every claim whose evidence array cites the
   withdrawn source is re-checked against the corroboration requirements. If a claim's
   register no longer holds, it drops — it is not quietly left standing. If the
   sequence cannot survive the honest register, the sequence is cut.
7. **Record it.** The source record's status becomes `retracted` with
   `retraction_reason`. The record and its ID remain permanently — that is how the
   studio remembers, and it is what lets a future reader understand why a claim
   changed. Log the request, the response, and the outcome in the line's advisory
   register and, where the material was published, in the corrections log.
8. **Pay anything outstanding.** A withdrawal does not cancel a fee for work already
   given.

Withdrawal is not an adversarial process and is not to be argued down. A contributor
who withdraws is exercising a right the studio granted in writing, and how that goes
determines whether anyone in that community talks to the studio again.
</content>
