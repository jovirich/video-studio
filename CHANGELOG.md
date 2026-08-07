# Changelog

All notable changes to the studio infrastructure are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning is semantic and applies to the *infrastructure*, not to episodes.

- **MAJOR** — a breaking change to schemas, folder contract, or canon that requires
  migrating existing records.
- **MINOR** — new capability: a new prompt vendor, a new validator, a new template.
- **PATCH** — corrections, doc fixes, non-breaking clarifications.

Episode releases are tracked separately in each production line's `slate.md`.

## [Unreleased]

### Added
- Studio / production line / episode three-tier architecture.
- Production Bible (13 documents) as the binding editorial constitution.
- JSON Schema set for episode, character, location, source, claim, shot, prompt
  card, asset, and timeline event records.
- Prompt library covering image, video, audio, text, 3D/scene, restoration,
  performance, and post tooling across 40 vendor folders.
- `studio_ops` Python package: scaffolding, validation, reporting, prompt
  rendering, pipeline and adapter stubs.
- Nigeria production line (`productions/ng-nigeria/`) as line one.
- Six review gates with separate owners and checklists.
- CI validation workflow and issue/PR templates.

### Notes
- No historical content has been authored. Every record is a template or an
  explicitly empty register.

## [0.1.0] — repository bootstrap

Initial infrastructure scaffold.
