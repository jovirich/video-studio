---
# ---------------------------------------------------------------------------
# CHARACTER — a person or collective actor.
# Schema: ../../standards/schemas/character.schema.json
# Copy to <line>/characters/profiles/CHR-XX-0000_<slug>.md with a
# toolkit-allocated ID. Do not fill this template in place.
#
# THIS RECORD HOLDS NO HISTORICAL FACTS. Every substantive statement is a claim
# reference. The prose body explains and contextualises; it never asserts
# anything absent from `claims`. That is what makes cross-production consistency
# mechanical instead of remembered.
# ---------------------------------------------------------------------------
id: CHR-XX-0000
type: character
line: xx-line-code
title: TBD — the on-screen name form (see `naming` below)
status: draft
version: "0.1.0"
updated: "2026-08-07"
owners: [research-lead]
sensitivity: review-required
# advisory_ref: ADV-XX-0000

# individual | lineage | office | collective | institution |
# contemporary_contributor
#
# `office` is a title held by successive individuals. Treating an office as one
# person compresses generations into a biography and produces confident
# nonsense — the visible version is a two-hundred-year reign; the invisible and
# more damaging version is attributing one holder's actions to another.
# Choosing `individual` by default is the error this field exists to prevent.
actor_kind: TBD

naming:
  # The form the production speaks and captions. An editorial decision.
  on_screen: TBD — the name form used on screen
  # Why this form and not another. Endonym, exonym, colonial form, regnal form,
  # honorific, transliteration — each is a different claim about whose account
  # is being used, and choosing silently is still choosing.
  on_screen_reason: TBD — why this form
  language_of_form: TBD
  orthography: TBD — which standard, and who decided
  # Required before any VO session mentions this entity.
  ipa: TBD — narrow enough to be actionable, including tone where the language is tonal
  # The reference recording is the AUTHORITY; the IPA is the aide-memoire. IPA
  # transmits badly through a booth — read by someone who does not use it daily,
  # under time pressure — and small errors in it are invisible until playback.
  pronunciation_ref: TBD — asset store path of a recording by a speaker of the language
  alternative_forms:
    - form: TBD
      # endonym | exonym | colonial | historical | regnal | honorific |
      # transliteration | variant
      kind: TBD
      used_by: TBD — who uses this form, and in what context
      note: TBD
  # Rendered accurately, not translated into approximate European equivalents.
  # "King" for a title that is not one is a substitution that imports a whole
  # political structure the source never described.
  titles: []

dating:
  earliest: TBD
  latest: TBD
  display: TBD — how the dates are spoken on screen
  calendar: TBD
  basis: TBD — how the dating was arrived at
  confidence: TBD
  claims: []

affiliations:
  - org: ORG-XX-0000
    relation: TBD — the nature of the affiliation
    claims: []

locations: []                   # TBD — LOC-XX-0000

# EVERYTHING the production asserts about this actor. If it is not here, the
# production does not say it.
claims: []

open_questions: []              # TBD — QST-XX-0000

depiction:
  # A decision, not a capability statement.
  may_be_depicted: false
  depiction_constraints: TBD — what may and may not be shown, and under what conditions

  # What a depiction would be grounded in: portraits, descriptions, regalia in
  # collections, contemporary accounts of appearance.
  #
  # EMPTY MEANS NO EVIDENCE-BASED DEPICTION IS POSSIBLE. The honest response is
  # to compose around the person — frame past them, hold them in silhouette,
  # keep them out of focus — rather than let a model invent a face. The model's
  # face will be confident, plausible, and attributable to nothing.
  appearance_evidence: []

  # Synthesising a historical figure's voice is prohibited outright. Consent is
  # impossible, so the question does not arise. `true` is only ever correct for
  # a living contributor, and the schema then requires consent_ref.
  voice_permitted: false

  living: false
  # consent_ref: CLR-XX-0000    # REQUIRED by the schema when living is true, and
                                # when voice_permitted is true
  descendant_community_contact: TBD — who was consulted, or why nobody was

# Fixed reference images that hold this actor's appearance consistent across
# shots, sequences, productions, and seasons. Without them, a model produces a
# different person every run, each internally plausible, and continuity depends
# on whoever is generating that week remembering last month.
style_anchors: []               # TBD — STA-XX-0000

appears_in: []                  # populated as productions reference this record
notes: TBD
---

# TBD — on-screen name

> Copy this file; do not fill it in place.

## Who this is

TBD — an orientation for a reader coming to this record cold. Every substantive
statement here points at a claim in the front matter; nothing is asserted that is
not in that list.

## Naming decision

TBD — the forms that exist, who uses each, and why the production speaks the one it
does. Written out because this decision is re-litigated at every VO session, every
caption pass, and every metadata write, and each re-litigation is an opportunity to
quietly reverse it.

## Depiction

TBD — what the evidence supports showing, what it does not, and how sequences are
composed around the gap.

## Sensitivity

TBD — advisory rulings affecting this record, and any conditions attached to them.

## Open questions

TBD — `QST-XX-0000`, with what would resolve each.
