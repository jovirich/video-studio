# Delivery specifications

Authoritative technical spec. Checked at the technical QC gate by
`studio_ops validate --delivery --episode <code>` (stub) and by human QC against
[../ops/checklists/technical_qc.md](../ops/checklists/technical_qc.md).

Values marked `TBD` require a Showrunner or Pipeline Engineer decision before S01E01.

## Picture

| Parameter | Archival master | Web master |
|---|---|---|
| Resolution | 3840 × 2160 | 3840 × 2160 and 1920 × 1080 |
| Frame rate | 24.000p | 24.000p |
| Codec | ProRes 422 HQ (or DNxHR HQX) | H.264 High / H.265 Main10 |
| Chroma | 4:2:2 | 4:2:0 |
| Bit depth | 10-bit | 8-bit (H.264) / 10-bit (H.265) |
| Colour space | Rec.709 | Rec.709 |
| Transfer | Gamma 2.4 | Gamma 2.4 |
| Scan | Progressive | Progressive |
| Bitrate | codec-native | UHD ≥ 35 Mbps, 1080p ≥ 12 Mbps |
| Container | MOV | MP4 |
| HDR | `TBD — out of scope unless decided` | — |

**Generated-clip conform.** Generation tools output at their own native rates
(commonly 24, 25, or 30 fps) and durations. Every clip is conformed to 24p, and the
conform method (`retime`, `frame-blend`, `optical-flow`, `native`) is recorded on
the asset record. Optical-flow retiming introduces artefacts that survive grading
and is checked for at picture lock.

## Legal levels and safe areas

| | |
|---|---|
| Video levels | Legal range, 64–940 (10-bit). No illegal blacks or superwhites in the master. |
| Title safe | 90% |
| Action safe | 93% |
| Vertical safe zone | 9:16 centre crop marked in storyboard; no critical information outside it |
| Square safe zone | 1:1 centre crop marked in storyboard |

## Audio

| Parameter | Value |
|---|---|
| Sample rate | 48 kHz |
| Bit depth | 24-bit (masters), 16-bit acceptable for web deliverable |
| Channels | Stereo minimum. 5.1 `TBD — decide if in scope`. |
| Integrated loudness | −14 LUFS (streaming), −23 LUFS ±0.5 (EBU R128 broadcast variant) |
| True peak | ≤ −1.0 dBTP |
| Loudness range | 6–12 LU |
| Dialogue/VO short-term | −18 to −12 LUFS |
| Noise floor | ≤ −60 dBFS on narration recordings |
| Master format | Broadcast WAV (BWF) with metadata |

### Required stems

`vo`, `testimony`, `music`, `ambience`, `sfx`, `me` (music + effects).
All at full length, sample-accurate to the master, single file each.

### Interview/testimony capture spec

48 kHz / 24-bit, uncompressed, primary + backup recorder, lavalier + boom where
possible, room tone recorded for every location, timecode or clap sync.

## Captions and subtitles

| Parameter | Value |
|---|---|
| Formats | SRT and VTT mandatory; TTML where the platform requires styling |
| Encoding | UTF-8, NFC normalised, no BOM |
| Max lines | 2 |
| Max chars/line | 42 |
| Duration | 1.0–7.0 s |
| Reading speed | ≤ 20 characters per second |
| Gap between cues | ≥ 2 frames |
| Speaker ID | Required where more than one speaker |
| Non-speech | `[sound]` bracketed, for accessibility captions |
| Positioning | Bottom centre default; repositioned to avoid on-screen text |

## On-screen text

| | |
|---|---|
| Minimum size | 1/20 of frame height for body text |
| Contrast | ≥ 4.5:1 against the shot behind it, measured, not eyeballed |
| Duration | Readable at 2× the reading time of the text |
| Fonts | Line-specified; must cover every diacritic used ([../bible/09_localization.md](../bible/09_localization.md) §2) |
| Layers | Kept separate in the NLE project so a textless master is a render, not a rebuild |

## Reconstruction mark

Spec in [../brand/labelling_system.md](../brand/labelling_system.md). Constraints:
persistent for the full duration of the labelled shot, inside title safe, contrast
≥ 3:1, legible at 360p, never obscured by a caption.

## Metadata

Embedded on delivery:
- Title, episode code, version, studio, year
- Copyright notice
- Language
- Content Credentials (C2PA) where the platform supports it
- The episode's provenance manifest hash, so a delivered file can be tied to the
  exact record set that produced it

## Delivery package

```
S01E01_v01/
├── master/            archival master + textless master
├── web/               H.264/H.265 renders
├── audio/             full mix + all stems
├── captions/          per language, SRT + VTT
├── artwork/           thumbnails, title card, key art
├── documents/         cue_sheet.csv, chain_of_title.pdf, credits.md,
│                      provenance_summary.md, sources.md, corrections.md
└── manifest.yaml      the episode manifest, frozen at delivery
```

`studio_ops pipeline package --episode <code>` assembles this (stub —
see [../automation/README.md](../automation/README.md) § Implementation status).
