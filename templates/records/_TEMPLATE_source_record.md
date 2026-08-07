---
# ---------------------------------------------------------------------------
# SOURCE RECORD — one item of evidence.
# Schema: ../../standards/schemas/source_record.schema.json
# Copy to <line>/sources/records/SRC-XX-0000_<slug>.md with a toolkit-allocated
# ID. Do not fill this template in place.
#
# Dates are QUOTED throughout. Unquoted, YAML resolves an ISO date to a date
# object, and the schema types these fields as strings — so an unquoted date
# fails validation with a message that reads like a schema bug.
# ---------------------------------------------------------------------------
id: SRC-XX-0000
type: source
line: xx-line-code
title: TBD — how this item is referred to internally; short enough for an index
status: draft
version: "0.1.0"
updated: "2026-08-07"
owners: [research-lead]
sensitivity: review-required
# advisory_ref: ADV-XX-0000     # required when sensitivity is `held`

# T1 primary/archival · T2 peer-reviewed secondary · T3 reputable general
# T4 oral testimony · T5 NEVER CITABLE (leads only; model output is T5)
# The tier is a property of the item, not of how much you trust it. A weak T1 is
# still T1; a superb T3 is still T3.
tier: TBD

# manuscript | inscription | archival_document | government_record |
# correspondence | chronicle | excavation_report | material_object | photograph |
# film | audio_recording | map | dataset | monograph | journal_article |
# edited_volume | thesis | catalogue_entry | encyclopedia_entry | journalism |
# oral_testimony | oral_tradition | interview | other
source_type: TBD

bibliographic:
  author: []                    # TBD
  editor: []
  translator: []                # TBD — a translation is an edition; name whose
  container_title: TBD
  publisher: TBD
  publisher_place: TBD
  issued: TBD                   # as printed; not normalised into a false precision
  volume: TBD
  issue: TBD
  page: TBD
  edition: TBD                  # TBD — editions differ, sometimes materially
  doi: TBD
  isbn: TBD
  url: TBD
  # accessed: "YYYY-MM-DD"      # add when a URL is actually consulted
  original_language: TBD

# Where the thing physically is, and who controls access. This is what makes a
# citation checkable by someone who is not you.
custody:
  repository: TBD — the holding institution
  collection: TBD
  reference_number: TBD — the catalogue or shelfmark, exactly as the repository writes it
  location_country: TBD
  custodian_contact: TBD
  # open | by-appointment | restricted | embargoed | community-controlled | unknown
  access: unknown
  access_conditions: TBD — what a researcher must agree to; conditions on access are conditions on the work
  digitised: false
  local_copy: TBD — asset store path of the scan or recording, if one exists

# ===========================================================================
# CRITIQUE — the block that makes this a record rather than a citation.
# ===========================================================================
# A CITATION WITHOUT A CRITIQUE IS AN UNFINISHED RECORD.
#
# A citation tells you where something is. It does not tell you whether the
# person who wrote it was there, what they wanted, what they would never have
# written down, or what happened to the text between then and now. Those
# questions decide what the source can carry — and unanswered, they get
# re-litigated informally in every meeting where the source comes up, with a
# different answer each time depending on who is in the room.
#
# The schema requires the first three. The other three are required by anyone
# who intends the record to be useful.
critique:
  # Who made this, when, for whom. A district officer's report, a court
  # chronicle, and a missionary's letter are three different instruments even
  # when they describe the same afternoon.
  creator_context: TBD — who made this, when, and for what audience

  # What were they ACTUALLY in a position to observe or record? Present at the
  # event, or writing at a remove of decades? Working from an informant, and if
  # so, whose? This is the question that most often changes what a source can
  # support, and it is the one most often skipped because the text sounds
  # authoritative either way.
  position_to_know: TBD — what this creator could actually observe or know

  # What interest shaped what was recorded and how. Every source has one; the
  # answer is never "none". A tax register wants revenue. A chronicle wants a
  # lineage legitimated. An excavation report wants a further grant. Naming the
  # interest is not discrediting the source — it is knowing which of its claims
  # cost the author something to make.
  interests: TBD — the interest that shaped what was recorded and how

  # Copying, translation, restoration, selective preservation, archival
  # rearrangement. What you are reading is rarely what was written: it has been
  # through hands, and each pair had priorities. An archive's arrangement is
  # itself an argument about what belongs with what.
  transmission: TBD — how this reached you, and what each step did to it

  # What this source would NOT have recorded, and what its absence therefore
  # does and does not prove.
  #
  # The field most often left thin, and the most consequential. An absence in a
  # source is evidence of absence ONLY IF the source would have recorded the
  # thing had it happened. Establishing that is research. Assuming it is an
  # argument from silence wearing a footnote — and it is the mechanism behind a
  # large fraction of confidently wrong history.
  silences: TBD — what this source is structurally unable to tell you

  # Scholarly challenges to this source's reliability. If a specialist has
  # argued this document is a later fabrication, a misattribution, or a
  # compilation, that argument belongs here rather than in the mind of the one
  # researcher who happens to have read it.
  known_disputes: TBD — challenges to this source's reliability, or `none found, searched <where>`

# Required by the schema when source_type is oral_testimony, oral_tradition, or
# interview. Commented out for other source types; delete this block if it does
# not apply.
#
# oral_protocol:
#   holder: TBD — the person; may be an anonymised reference where safety requires
#   holder_standing: TBD — their relationship to the knowledge: lineage, office,
#                    # training. THIS is what makes testimony evidence rather
#                    # than an anecdote, and it is the field that distinguishes
#                    # a knowledge holder from a passer-by with an opinion.
#   transmission_context: TBD — how they came to hold it, and from whom
#   language: TBD
#   recorded_by: TBD
#   recorded_on: "YYYY-MM-DD"
#   consent_ref: CLR-XX-0000   # required; see ../legal/interview_consent.md
#   restrictions: TBD — what may not be published, broadcast, or shown, and to whom
#   translation_by: TBD — named translator; an uncredited translation is an
#                    # editorial act presented as a transcription

rights:
  # cleared | pending | not-required | refused | unknown
  status: unknown
  clearance_ref: TBD — CLR-XX-0000
  credit_line: TBD — the EXACT wording the rights holder requires; paraphrasing it breaches the licence
  restrictions: TBD — territory, term, media, and any no-alteration term

# Populated as claims are written. A T5 record's list must be empty — the schema
# enforces it, so a never-citable source cannot be made to support anything.
supports_claims: []

notes: TBD — anything a researcher coming to this record cold would need
---

# TBD — source title

> Copy this file; do not fill it in place.

## Summary

TBD — what this item is, in a few sentences: its physical form, extent, condition,
and what parts of it are relevant to this line.

## How it was found

TBD — the finding aid, the citation trail, or the person who pointed at it. Recorded
because the next researcher looking for adjacent material starts from here, and
because a source found through a single secondary work is not independent of that
work.

## Reading notes

TBD — what was read, what was skimmed, and what has not been examined. Being honest
about the last one is what stops a partially-read source being cited as if it were
fully read.

## Passages relied on

| Locator | Passage | Translation | Supports |
|---|---|---|---|
| TBD — page, folio, timecode | TBD — in the original language where relevant | TBD — and the translator | TBD — `CLM-XX-0000` |

## Independence

TBD — what this source is demonstrably **not** derived from, and how that was
established.

Two sources sharing an upstream origin are one source. A chronicle and a later
summary of that chronicle corroborate nothing — the second lends the first a weight
it never earned, and the claim built on both looks twice as well supported as it is.
Independence is asserted deliberately, in the claim's `independent_of` field. It is
never inferred from two different titles on a shelf.
