"""Tests for the ID allocator and the record scaffolder.

Fixture trees carry deliberate violations — duplicated IDs, a filename that
disagrees with the field inside it, a gap where a serial was skipped. An allocator
that returns 0001 on an empty directory has proved nothing; what has to be proved is
that it *refuses* on a corrupt namespace, because a duplicate ID does not break a
reference, it silently re-points it.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import pytest

from studio_ops.config import Config
from studio_ops.paths import Layout
from studio_ops.scaffold import ids, new_record
from studio_ops.scaffold.ids import IdCollisionError, IdError
from studio_ops.scaffold.new_record import (
    DestinationError,
    RecordExistsError,
    ScaffoldError,
    UnknownRecordTypeError,
)

STUDIO = "african-history"
LINE = "ng-nigeria"

# Opens with a banner comment inside the front matter, exactly as the real record
# templates do. A front-matter reader that splits on the bare substring `---` stops
# at that banner and never sees the `id:` field beneath it.
SOURCE_TEMPLATE = """---
# ---------------------------------------------------------------------------
# SOURCE RECORD — one item of evidence.
# ---------------------------------------------------------------------------
id: SRC-XX-0000
type: source
line: xx-line-code
title: TBD — how this item is referred to internally
status: draft
version: "0.1.0"
updated: "2026-01-01"
owners: [research-lead]
---

# TBD — source title

Body prose, with a table rule that must survive the split:

| a | b |
|---|---|
"""

SHOT_TEMPLATE = """# =============================================================================
# SHOT RECORD
# =============================================================================
id: SHT-XX-S00E00-0000
type: shot
line: xx-line-code
status: draft
version: "0.1.0"
updated: "2026-01-01"           # quoted: unquoted, YAML makes this a date object
owners: [visual-director]

episode: S00E00
sequence: SEQ-XX-S00E00-001
order: 1
"""


# ------------------------------------------------------------------- fixtures


def make_cfg(tmp_path: Path) -> Config:
    (tmp_path / "core").mkdir(exist_ok=True)
    (tmp_path / "packs").mkdir(exist_ok=True)
    return Config(root=tmp_path, layout=Layout(root=tmp_path))


def make_line(tmp_path: Path, scope: str = "NG", code: str = LINE) -> Path:
    line = tmp_path / "studios" / STUDIO / "lines" / code
    line.mkdir(parents=True, exist_ok=True)
    (line / "line.yaml").write_text(
        f"id: LINE-{scope}\ntype: production_line\ncode: {code}\nid_scope: {scope}\n",
        encoding="utf-8",
    )
    (tmp_path / "studios" / STUDIO / "bible").mkdir(parents=True, exist_ok=True)
    return line


def make_production(line: Path, episode: str = "EXP001", slug: str = "laboratory-scene") -> Path:
    production = line / "productions" / f"{episode}_{slug}"
    production.mkdir(parents=True, exist_ok=True)
    (production / "production.yaml").write_text(
        f"id: EP-NG-{episode}\ntype: episode\ncode: {episode}\nline: {LINE}\n",
        encoding="utf-8",
    )
    return production


def make_templates(tmp_path: Path) -> None:
    records = tmp_path / "templates" / "records"
    records.mkdir(parents=True, exist_ok=True)
    (records / "_TEMPLATE_source_record.md").write_text(SOURCE_TEMPLATE, encoding="utf-8")
    storyboard = tmp_path / "templates" / "production" / "03_storyboard"
    storyboard.mkdir(parents=True, exist_ok=True)
    (storyboard / "_TEMPLATE_shot.yaml").write_text(SHOT_TEMPLATE, encoding="utf-8")


def write_md(path: Path, record_id: str) -> Path:
    """A markdown record whose ID lives only in its front matter."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"---\nid: {record_id}\ntype: source\nline: {LINE}\n---\n\n# body\n", encoding="utf-8"
    )
    return path


def write_yaml(path: Path, record_id: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"id: {record_id}\ntype: shot\nline: {LINE}\n", encoding="utf-8")
    return path


# -------------------------------------------------------------------- parse_id


@pytest.mark.parametrize(
    ("raw", "id_type", "scope", "episode", "serial"),
    [
        ("SRC-NG-0042", "SRC", "NG", None, 42),
        ("SRC-STUDIO-0007", "SRC", "STUDIO", None, 7),
        ("PC-STUDIO-0009", "PC", "STUDIO", None, 9),
        ("SHT-NG-S01E01-0142", "SHT", "NG", "S01E01", 142),
        ("SHT-NG-EXP001-0142", "SHT", "NG", "EXP001", 142),
        ("SEQ-NG-EXP001-004", "SEQ", "NG", "EXP001", 4),
        ("RSK-PLAT-0001", "RSK", "PLAT", None, 1),
        ("PCL-GFT-0014", "PCL", "GFT", None, 14),
    ],
)
def test_parse_id_decomposes(
    raw: str, id_type: str, scope: str, episode: str | None, serial: int
) -> None:
    parsed = ids.parse_id(raw)

    assert parsed is not None
    assert (parsed.id_type, parsed.scope, parsed.episode, parsed.serial) == (
        id_type,
        scope,
        episode,
        serial,
    )
    assert ids.format_id(id_type, scope, serial, episode) == raw


@pytest.mark.parametrize(
    "raw",
    [
        "LINE-NG",  # a control record, not a serial-allocated one
        "STU-AFH",
        "EP-NG-EXP001",
        "src-ng-0042",
        "SRC-NG-42",
        "SRC-NG-00042",
        "not an id at all",
        "",
    ],
)
def test_parse_id_rejects_non_ids(raw: str) -> None:
    assert ids.parse_id(raw) is None


# ------------------------------------------------------------------ allocation


def test_allocation_from_an_empty_registry_returns_the_first_serial(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)

    assert ids.allocate(cfg, "SRC", "NG") == "SRC-NG-0001"


def test_allocation_skips_existing_serials(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    records = tmp_path / "studios" / STUDIO / "lines" / LINE / "sources" / "records"
    write_md(records / "SRC-NG-0001_a.md", "SRC-NG-0001")
    write_md(records / "SRC-NG-0002_b.md", "SRC-NG-0002")

    assert ids.scan_existing(tmp_path, "SRC", "NG") == {1, 2}
    assert ids.allocate(cfg, "SRC", "NG") == "SRC-NG-0003"


def test_allocation_ignores_other_types_and_scopes(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    write_md(docs / "a.md", "SRC-GH-0009")
    write_md(docs / "b.md", "CLM-NG-0009")
    write_md(docs / "c.md", "SRC-STUDIO-0009")

    assert ids.allocate(cfg, "SRC", "NG") == "SRC-NG-0001"


def test_next_serial_never_fills_a_gap() -> None:
    """Filling a gap re-issues a serial a tombstone may still hold."""
    assert ids.next_serial(set()) == 1
    assert ids.next_serial({1, 2, 5}) == 6
    assert ids.find_gaps({1, 2, 5}) == [3, 4]


def test_ids_are_found_in_markdown_front_matter_as_well_as_yaml(tmp_path: Path) -> None:
    write_md(tmp_path / "docs" / "record.md", "SHT-NG-EXP001-0004")
    write_yaml(tmp_path / "docs" / "record.yaml", "SHT-NG-EXP001-0009")

    assert ids.scan_existing(tmp_path, "SHT", "NG") == {4, 9}


def test_a_banner_comment_does_not_hide_the_id(tmp_path: Path) -> None:
    """The real templates open front matter with `# -----`.

    A reader that splits on the bare substring `---` stops at that banner, finds no
    `id:`, and hands out a serial that is already live.
    """
    path = tmp_path / "docs" / "banner.md"
    path.parent.mkdir(parents=True)
    path.write_text(SOURCE_TEMPLATE.replace("SRC-XX-0000", "SRC-NG-0031"), encoding="utf-8")

    assert ids.scan_existing(tmp_path, "SRC", "NG") == {31}


def test_a_filename_that_lies_does_not_fool_the_scanner(tmp_path: Path) -> None:
    """Filenames drift; the field is the identity."""
    cfg = make_cfg(tmp_path)
    records = tmp_path / "studios" / STUDIO / "lines" / LINE / "sources" / "records"
    write_md(records / "SRC-NG-0044_copied-from-another-record.md", "SRC-NG-0002")

    assert ids.scan_existing(tmp_path, "SRC", "NG") == {2}
    assert ids.allocate(cfg, "SRC", "NG") == "SRC-NG-0003"


def test_templates_are_not_scanned(tmp_path: Path) -> None:
    """Placeholder IDs belong to no scope; counting them would burn real serials."""
    cfg = make_cfg(tmp_path)
    templates = tmp_path / "templates" / "records"
    write_md(templates / "_TEMPLATE_source_record.md", "SRC-NG-0500")

    assert ids.allocate(cfg, "SRC", "NG") == "SRC-NG-0001"


# ---------------------------------------------------------------- the refusals


def test_a_duplicate_id_across_two_files_raises(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    records = tmp_path / "studios" / STUDIO / "lines" / LINE / "sources" / "records"
    write_md(records / "SRC-NG-0002_first.md", "SRC-NG-0002")
    write_md(records / "SRC-NG-0002_second.md", "SRC-NG-0002")

    with pytest.raises(IdCollisionError) as excinfo:
        ids.allocate(cfg, "SRC", "NG")

    assert "SRC-NG-0002" in str(excinfo.value)
    # Both offenders must be named, or the message is not actionable.
    assert "SRC-NG-0002_first.md" in str(excinfo.value)
    assert "SRC-NG-0002_second.md" in str(excinfo.value)
    assert set(excinfo.value.duplicates) == {"SRC-NG-0002"}


def test_the_gap_and_collision_pattern_is_named(tmp_path: Path) -> None:
    """Both together mean somebody typed IDs, not that two branches raced."""
    cfg = make_cfg(tmp_path)
    records = tmp_path / "studios" / STUDIO / "lines" / LINE / "sources" / "records"
    write_md(records / "SRC-NG-0001_a.md", "SRC-NG-0001")
    write_md(records / "b.md", "SRC-NG-0004")
    write_md(records / "c.md", "SRC-NG-0004")

    with pytest.raises(IdCollisionError) as excinfo:
        ids.allocate(cfg, "SRC", "NG")

    assert excinfo.value.gaps == [2, 3]
    assert "0002, 0003" in str(excinfo.value)
    assert "hand-edited" in str(excinfo.value)


def test_a_collision_elsewhere_does_not_block_an_unrelated_namespace(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    write_md(docs / "a.md", "CLM-NG-0003")
    write_md(docs / "b.md", "CLM-NG-0003")

    assert ids.allocate(cfg, "SRC", "NG") == "SRC-NG-0001"
    assert set(ids.find_collisions(tmp_path)) == {"CLM-NG-0003"}


def test_allocation_rejects_a_scope_that_is_not_one(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)

    with pytest.raises(IdError):
        ids.allocate(cfg, "SRC", "ng-nigeria")


# -------------------------------------------------------------- episode scoped


def test_episode_scoped_allocation_uses_the_laboratory_code(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)

    assert ids.allocate(cfg, "SHT", "NG", "EXP001") == "SHT-NG-EXP001-0001"
    assert ids.allocate(cfg, "SEQ", "NG", "S01E01") == "SEQ-NG-S01E01-001"


def test_episode_scoped_serials_are_shared_across_episodes(tmp_path: Path) -> None:
    """standards/id_system.md allocates per (TYPE, SCOPE); EPISODE is not in the key.

    So a shot serial is unique across a whole line, and a mistyped production code
    cannot resolve to a real other shot.
    """
    cfg = make_cfg(tmp_path)
    write_yaml(tmp_path / "docs" / "a.yaml", "SHT-NG-S01E01-0007")

    assert ids.allocate(cfg, "SHT", "NG", "EXP001") == "SHT-NG-EXP001-0008"


def test_an_episode_scoped_type_refuses_without_a_production_code(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)

    with pytest.raises(IdError, match="episode-scoped"):
        ids.allocate(cfg, "SHT", "NG")


def test_a_line_scoped_type_refuses_a_production_code(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)

    with pytest.raises(IdError, match="not episode-scoped"):
        ids.allocate(cfg, "SRC", "NG", "S01E01")


def test_a_studio_scoped_prompt_card_takes_no_episode(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)

    assert ids.allocate(cfg, "PC", "STUDIO") == "PC-STUDIO-0001"


def test_an_unknown_production_code_form_is_refused(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)

    with pytest.raises(IdError, match="laboratory form"):
        ids.allocate(cfg, "SHT", "NG", "SEASON1")


# -------------------------------------------------------------- record writing


def test_new_record_writes_to_the_destination_for_its_type(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    line = make_line(tmp_path)
    make_templates(tmp_path)

    path = new_record.new_record(cfg, "source", "NG", slug="kano-chronicle")

    assert path == line / "sources" / "records" / "SRC-NG-0001_kano-chronicle.md"
    assert path.is_file()
    text = path.read_text(encoding="utf-8")
    assert "id: SRC-NG-0001" in text
    assert f"line: {LINE}" in text
    # The body must survive intact, banner comment and markdown table rule alike.
    assert "# TBD — source title" in text
    assert "|---|---|" in text


def test_the_written_updated_field_is_quoted(tmp_path: Path) -> None:
    """Unquoted, YAML resolves an ISO date to a date object and every schema fails it."""
    cfg = make_cfg(tmp_path)
    make_line(tmp_path)
    make_templates(tmp_path)

    path = new_record.new_record(cfg, "source", "NG")
    today = dt.date.today().isoformat()

    assert f'updated: "{today}"' in path.read_text(encoding="utf-8")


def test_a_trailing_comment_on_a_stamped_field_is_kept(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    line = make_line(tmp_path)
    make_production(line)
    make_templates(tmp_path)

    path = new_record.new_record(cfg, "shot", "NG", episode="EXP001")
    text = path.read_text(encoding="utf-8")

    assert "YAML makes this a date object" in text
    assert "episode: EXP001" in text


def test_new_record_places_a_shot_inside_its_production(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    line = make_line(tmp_path)
    production = make_production(line, "EXP001")
    make_templates(tmp_path)

    path = new_record.new_record(cfg, "shot", "NG", episode="EXP001")

    assert path == production / "03_storyboard" / "shots" / "SHT-NG-EXP001-0001.yaml"
    assert "id: SHT-NG-EXP001-0001" in path.read_text(encoding="utf-8")


def test_a_second_record_takes_the_next_serial(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    make_line(tmp_path)
    make_templates(tmp_path)

    first = new_record.new_record(cfg, "source", "NG", slug="one")
    second = new_record.new_record(cfg, "source", "NG", slug="two")

    assert first.name.startswith("SRC-NG-0001")
    assert second.name.startswith("SRC-NG-0002")


def test_new_record_refuses_to_overwrite(tmp_path: Path) -> None:
    """The squatter carries no `id:`, so the allocator hands out the serial anyway."""
    cfg = make_cfg(tmp_path)
    line = make_line(tmp_path)
    make_templates(tmp_path)
    squatter = line / "sources" / "records" / "SRC-NG-0001_taken.md"
    squatter.parent.mkdir(parents=True)
    squatter.write_text("somebody's work\n", encoding="utf-8")

    with pytest.raises(RecordExistsError):
        new_record.new_record(cfg, "source", "NG", slug="taken")

    assert squatter.read_text(encoding="utf-8") == "somebody's work\n"


def test_dry_run_writes_nothing(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    line = make_line(tmp_path)
    make_templates(tmp_path)

    path = new_record.new_record(cfg, "source", "NG", slug="probe", dry_run=True)

    assert path == line / "sources" / "records" / "SRC-NG-0001_probe.md"
    assert not path.exists()
    assert not (line / "sources").exists()


def test_new_record_refuses_an_unknown_type(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    make_line(tmp_path)

    with pytest.raises(UnknownRecordTypeError, match="continuity_character"):
        new_record.new_record(cfg, "vibe", "NG")


def test_new_record_refuses_a_slug_the_naming_gate_would_reject(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    make_line(tmp_path)
    make_templates(tmp_path)

    with pytest.raises(ScaffoldError, match="kebab-case"):
        new_record.new_record(cfg, "source", "NG", slug="Kano Chronicle_final")


def test_new_record_refuses_an_unregistered_scope(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    make_line(tmp_path, scope="NG")
    make_templates(tmp_path)

    with pytest.raises(DestinationError, match="id_scope"):
        new_record.new_record(cfg, "source", "GH")


def test_new_record_refuses_an_unknown_production(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    line = make_line(tmp_path)
    make_production(line, "EXP001")
    make_templates(tmp_path)

    with pytest.raises(DestinationError, match="EXP002"):
        new_record.new_record(cfg, "shot", "NG", episode="EXP002")


def test_a_studio_scoped_type_with_no_defined_home_says_so(tmp_path: Path) -> None:
    """Refusing beats inventing a directory the repository does not describe."""
    cfg = make_cfg(tmp_path)
    make_line(tmp_path)
    make_templates(tmp_path)

    with pytest.raises(DestinationError, match="no home"):
        new_record.new_record(cfg, "source", "STUDIO")


def test_every_registered_type_names_a_template_that_exists() -> None:
    """A destination table is only data-driven if the data is checked."""
    repo = Path(__file__).resolve().parents[2]
    missing = [
        spec.template
        for spec in new_record.RECORD_TYPES.values()
        if not (repo / spec.template).is_file()
    ]

    assert not missing
