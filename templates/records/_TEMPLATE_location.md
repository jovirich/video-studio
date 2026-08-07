---
# ---------------------------------------------------------------------------
# LOCATION — a place appearing in the line.
# Schema: ../../standards/schemas/location.schema.json
# Copy to <line>/locations/profiles/LOC-XX-0000_<slug>.md with a
# toolkit-allocated ID. Do not fill this template in place.
#
# HOLDS NO HISTORICAL FACTS — only references to claims. Coordinates are for map
# production, not for asserting a historical extent. Extent is a claim.
# ---------------------------------------------------------------------------
id: LOC-XX-0000
type: location
line: xx-line-code
title: TBD — the on-screen name form
status: draft
version: "0.1.0"
updated: "2026-08-07"
owners: [research-lead]
sensitivity: review-required
# advisory_ref: ADV-XX-0000

# settlement | city | polity_territory | region | landscape_feature |
# watercourse | route | structure | site | archaeological_site | sacred_site |
# burial_site | market | port | modern_administrative
place_kind: TBD

naming:
  on_screen: TBD — the name form used on screen
  on_screen_reason: TBD — why this form and not another
  # Primary on screen for historical sequences.
  period_name: TBD
  # Given ONCE for orientation, and never silently substituted. Substituting it
  # tells the viewer the place has one real name and it is the current one.
  modern_name: TBD
  ipa: TBD
  pronunciation_ref: TBD — asset store path of a recording by a speaker of the language
  alternative_forms:
    - form: TBD
      kind: TBD                 # endonym | exonym | colonial | historical |
                                # transliteration | variant
      note: TBD

geography:
  modern_country: TBD
  # latitude / longitude are omitted rather than zeroed: 0,0 is a real place in
  # the Gulf of Guinea, and a zeroed coordinate that reaches a map render puts a
  # marker there. Add the numbers when they are real.
  #   latitude: <number>
  #   longitude: <number>
  #
  # exact | approximate | regional | unlocated | withheld
  # A map render reads this to decide whether it may draw a point, a zone, or
  # nothing. Defaulting it to `exact` is how a map acquires a confidence the
  # record never had.
  coordinate_precision: unlocated
  precision_note: TBD — what the precision is based on
  # elevation_m: <number>
  terrain: TBD
  # Coastlines, river courses, and lake extents change. Where a modern base map
  # approximates a historical one, say so — otherwise the base map silently
  # asserts a geography that did not exist at the period depicted.
  hydrology_note: TBD

site_status:
  extant: false
  excavated: false
  protected_status: TBD
  # public | permit-required | restricted | community-controlled | unknown
  access: unknown
  # True for sites where publishing coordinates would invite looting, trespass,
  # or desecration. The schema then REQUIRES coordinate_precision `withheld`, so
  # the two cannot drift apart.
  #
  # Not hypothetical caution: a documentary is a discovery mechanism for people
  # who were not looking, and a site named and located on a popular platform has
  # a measurably worse year afterwards.
  location_withheld: false

claims: []                      # everything the production asserts about this place
open_questions: []              # TBD — QST-XX-0000

depiction:
  may_be_depicted: false
  depiction_constraints: TBD — what may and may not be shown

  # What a reconstruction must be BUILT FROM: excavation reports, standing
  # structures, contemporary descriptions, photographs, surveys.
  material_evidence: []

  # Features NOT evidenced — roof forms, upper storeys, interiors, surface
  # finishes, decoration.
  #
  # The field that does the real work. A generative tool will supply every one
  # of these confidently and attributably to nothing. Naming them in advance is
  # what turns "the model decided" into "we decided not to show it" — compose
  # around them: frame past the roofline, hold the interior in shadow, keep the
  # unattested detail out of focus.
  unattested_elements:
    - TBD — a feature the evidence does not cover

  # Ambience asserts what a place sounded like. It is reconstruction, and it is
  # the one reconstruction that routinely ships without anyone having decided it
  # was one, because nobody thinks of a sound bed as a claim.
  period_ambience: TBD — what the soundscape is grounded in

style_anchors: []               # TBD — STA-XX-0000
appears_in: []
notes: TBD
---

# TBD — on-screen name

> Copy this file; do not fill it in place.

## Where and what this is

TBD — orientation for a reader coming to this record cold. Every substantive
statement points at a claim in the front matter.

## What the maps may and may not show

TBD — the extent claims that exist, their confidence, and what a map of this place is
therefore permitted to draw. A hard boundary line asserts a precision that most
sources do not support; a graded zone asserts less and is usually more accurate.

## What a reconstruction may show

TBD — the evidenced features, the unattested ones, and how shots are composed around
the second list.

## Access and sensitivity

TBD — who controls access, what permissions filming or publication would require, and
any advisory ruling affecting how this place is shown or located.
