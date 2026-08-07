---
title: characters — people, offices, lineages, collectives
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [research-lead, cultural-advisor]
---

# characters

`CHR-*` profiles for every actor the line depicts — individual, lineage, office,
collective, institution, or contemporary contributor.

```
characters/
└── profiles/   CHR-XX-0000_<slug>.md
```

Template: [../../records/_TEMPLATE_character.md](../../records/_TEMPLATE_character.md).

## These records hold no facts

Every substantive statement about an actor is a **claim reference**. The prose body
of a profile explains and contextualises; it never asserts anything absent from the
`claims` list.

This is what makes cross-production consistency mechanical rather than remembered.
Two productions referencing the same claim say the same thing by construction. Two
productions each summarising a person in their own words diverge, and the divergence
surfaces as a viewer noticing that season one and season three disagree.

## `actor_kind` is the field that prevents a specific, common error

An **office** is a title held by successive individuals. Treating an office as one
person compresses centuries into a biography and produces confident nonsense —
"he ruled for two hundred years" is the visible version; the invisible version is
attributing one holder's actions to another.

The same applies to a **lineage** and to a **collective**. Choosing `individual` by
default is the error; the field exists to make the choice deliberate.

## Naming is an editorial decision with a recorded reason

`naming.on_screen` is the form the line speaks. `on_screen_reason` says why that
form and not another. Endonym, exonym, colonial form, regnal form, honorific,
transliteration — each is a different claim about whose account is being used, and
choosing silently is still choosing.

`ipa` and `pronunciation_ref` are required before any VO session mentions the entity.
The reference recording — by a speaker of the language — is the authority; the IPA is
the aide-memoire. A mispronounced endonym is the most reliable signal available to
the people the material belongs to that nobody was consulted.

## Depiction

`depiction.may_be_depicted` is a decision, not a capability statement. The supporting
fields are what make it defensible:

- `appearance_evidence` — what the depiction is grounded in. **Empty means no
  evidence-based depiction is possible**, and the honest response is to compose
  around the person rather than let a model invent a face.
- `voice_permitted` — synthesising a historical figure's voice is prohibited
  outright. Consent is impossible, so the question does not arise.
- `living: true` requires `consent_ref`. The schema enforces it.
- `descendant_community_contact` — because a depiction of an ancestor is a matter for
  the people who have one, not only for the studio.

Sensitivity `held` on any profile freezes work on it until the Cultural Advisor
writes a ruling. Any contributor may raise the hold; only the Advisor releases it.
