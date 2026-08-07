---
title: Stakeholder approval gate checklist
status: active
version: 0.1.0
updated: 2026-08-07
owners: [showrunner]
---

# Stakeholder approval — checklist

| | |
|---|---|
| **Gate key** | `stakeholder_approval` |
| **Owner** | `showrunner` |
| **Stage** | `08_review` |
| **Blocks** | `09_delivery` |
| **Packs** | product-marketing, fashion-film |
| **Completed copy** | `08_review/checklists/stakeholder_approval.md` in the production folder |

The gate documentary deliberately lacks. It exists here because these packs make work
**for** someone who is not in the production, and that person's approval has to attach
to a specific artefact rather than to a feeling about the direction.

The entire failure mode of this gate is approval on the wrong object. "Yes, love it"
said over a shoulder at a rough cut is not an approval of the delivered version, and
it will be quoted as though it were.

## What this signature certifies

> *product-marketing:* Product owner, brand owner, and legal (where the category
> requires it) have each seen and signed this cut. Approval is on a specific version,
> never on "the general direction".
>
> *fashion-film:* Designer and brand owner have seen and signed this specific version.
> Model contracts cover every use in this cut, including AI processing where applied.

## Checks

### Approval attaches to a version

- [ ] A version identifier exists for the cut being approved, and it appears in each approver's written response
- [ ] Every approver saw **this** version, not an earlier one, and not a description of the changes since
- [ ] Approvals are in writing and are retained. A verbal approval is a recollection
- [ ] Every approver saw it with final audio, final captions, and final on-screen text — the elements most often changed after approval and least often re-approved
- [ ] Where an approver saw only a subset of deliverables, the record says which; approval of the 16:9 master is not approval of the vertical cut

### Who has to sign

- [ ] *(product-marketing)* Product owner — has confirmed the product is depicted as it ships
- [ ] *(product-marketing)* Brand owner — has confirmed brand assets are current versions and usage is correct
- [ ] *(product-marketing)* Legal — where the category requires it, and the requirement was determined at brief approval rather than guessed at now
- [ ] *(fashion-film)* Designer — has confirmed the garments are represented as they are
- [ ] *(fashion-film)* Brand owner
- [ ] Every approver named at brief approval has signed, and any approver added since is recorded with the reason they were added

### Contracts and consents — *(fashion-film)*

- [ ] Every model appearing in the cut has a contract covering **this** use: media, territory, term, and deliverable variants
- [ ] **Model contracts explicitly cover AI processing and generation.** A contract that does not name it does not cover it
- [ ] No real model's likeness has been generated beyond the scope of their contract
- [ ] No generated body is presented as a specific real model
- [ ] Retouching that changes body shape is logged as a post-process step on the asset, and complies with the studio's disclosure policy

### Change control after approval

- [ ] Any change made after an approval has been re-approved by everyone whose approval it could affect
- [ ] The list of post-approval changes is recorded, however small. "Just a text fix" is the change most likely to introduce an unapproved claim

## Do not sign if

- **Any approval is on "the general direction".** That is not an approval; it is
  encouragement.
- **An approver saw a cut without final on-screen text, captions, or audio.** Those
  carry claims, and they are where the changes happen after everyone stopped watching.
- **The cut changed after an approval and was not re-approved.** The version
  identifier exists precisely so this is answerable rather than remembered.
- **A model contract does not name AI processing** *(fashion-film)*. Silence is not
  permission, and this is the single most likely contractual gap in this pack.
- **Legal was required at brief approval and has not signed.**
- **You signed `brief_approval` on this production.** Both are owned by `showrunner`
  in these packs, which conflicts with
  [../../core/04_review_gate_framework.md](../../core/04_review_gate_framework.md) §5 —
  see [../roles.md](../roles.md) §5.1.

## Signature

| Field | Value |
|---|---|
| Role | `showrunner` |
| Person | |
| Date | |
| Version approved | |
| Approvers and dates | |
| Gate status | `signed` / `blocked` |
| Blockers, if blocked | |
| Note | |
