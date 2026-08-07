---
title: Music beds
status: draft
version: 0.1.0
updated: 2026-08-07
owners: [audio-lead, rights-and-clearances]
---

# Music beds

Licensed underscore, texture, drones, and stings available to any studio on the
platform.

**Maturity: DESIGNED.** Empty. No cue has been licensed or placed.

## What goes in here

Cross-studio, subject-neutral musical material: beds, textures, drones, transitions,
and utility stings that carry no cultural specificity and no studio's identity.

Not here:

| Not here | Where instead |
|---|---|
| Original score for a production or line | that production's audio folder |
| Anything idiomatic to a specific tradition or region | a line — and see below |
| A studio's sonic identity, theme, or motif | `studios/<code>/brand/` |
| Temp music | nowhere. Temp music that is not licensed must not reach a cut it can survive in. |

**Material idiomatic to a living tradition does not belong in a shared library at
all.** Not because of the licence, but because the questions it raises — who granted
it, on what basis they held the right to grant it, whether the tradition's custodians
were involved — are answered at the level of the line and the advisory relationship,
never once at the platform for everybody. Core/02 §2 gives traditional music its own
category for exactly this reason, and it is the one category where the licensor is
frequently not the person entitled to license.

## The licence requirement

The grant must permit **inclusion in a distributed finished film**, in the media,
territories, and term the productions using it will actually reach.

**"Royalty free" does not answer this question.** It describes a payment model — you
pay once instead of per use — and says nothing about scope. A royalty-free cue can
still be limited to a territory, limited to online distribution, limited in term,
prohibited from broadcast, prohibited from being sublicensed to a distributor, or
subject to an attribution requirement that a delivered film has no obvious place to
carry. Treat the phrase as marketing copy that has not yet been read.

The questions the row must answer:

| Question | Why it bites |
|---|---|
| Does the grant cover **synchronisation** into an audiovisual work? | A licence to *use* audio is not automatically a sync licence. |
| Does it cover **broadcast and streaming**, specifically? | Frequently a separate tier, exactly as with fonts. |
| **Composition and recording rights** — who holds each? | They are separate rights and are recorded separately, per core/02 §2. One party often holds both; that is a fact to record, not to assume. |
| Territory, term, and expiry date | A term expressed as a duration loses its start date. Record the expiry. |
| Does it permit **sublicensing to a distributor**? | A distributor will require the studio to grant onward. A licence that cannot be passed on caps the delivery. |
| Is there an **attribution requirement**, and in what exact wording? | Carried verbatim in the credits and the published credit list. |
| Does it permit **editing** — cutting, looping, pitching, layering? | Editorial use is editing by definition. Some grants restrict it. |

Every cue carries a row in
[../../rights/permissions/clearance_log.md](../../rights/permissions/clearance_log.md)
under category *Music*, with a `CLR-STUDIO-*` ID, before it is placed here.

## Cue sheets

Every production maintains `10_publish/cue_sheet.csv` from episode one, even where the
score is entirely original — core/02 §6. A bed used from this library produces a cue
sheet row in every production that uses it, and that row cites the clearance ID here.

Retrofitting a cue sheet for a distributor at short notice is, in core's words, a
well-known and entirely avoidable emergency. The library's job is to make the row
trivial to produce: the clearance record already holds the composition and recording
holders, the territory, and the term.

## Naming

```
mus_<mood-or-function>_<bpm>_<duration>s_v<NN>.wav

mus_bed-tension_072_180s_v01.wav
mus_drone-low_000_240s_v02.wav
```

Lowercase, ASCII, hyphens within a field, underscores between fields, per
[../../standards/naming_conventions.md](../../standards/naming_conventions.md).
`000` for BPM where the material has no pulse. The slug describes **function**, never
the tradition, region, or period it evokes — a bed named for a place is a bed that
will be used because of the name rather than because of the sound, and it puts a
subject-matter claim into a platform-level folder.

Delivery-grade audio only. Record the format in the manifest; a bed that has to be
sample-rate converted at the mix is a bed that will be converted differently by
different people.

## Manifest and storage

Audio binaries are gitignored ([../../.gitignore](../../.gitignore)); the manifest is
not. Per cue: filename, SHA-256, duration, sample rate and bit depth, BPM and key where
meaningful, composition holder, recording holder, clearance ID, territory, term expiry,
attribution wording, and whether stems exist.

Stems matter more than they look. A bed with stems can be re-balanced under a mix and
re-versioned for an M&E deliverable; a stereo bounce cannot, and the difference is only
discovered at the dub.
