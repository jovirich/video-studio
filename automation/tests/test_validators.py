"""Tests for the implemented validation gates.

These build fixture trees containing deliberate violations. A validator that runs
cleanly on an empty repository has proved nothing; these assert that each rule
actually fires, and that clean input produces no finding.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from studio_ops.config import Config
from studio_ops.paths import Layout
from studio_ops.result import GateState, RunReport
from studio_ops.validate import links, naming, reality, root_hygiene, schemas
from studio_ops.validate import not_built as nb


def make_cfg(tmp_path: Path) -> Config:
    (tmp_path / "core").mkdir(exist_ok=True)
    (tmp_path / "packs").mkdir(exist_ok=True)
    return Config(root=tmp_path, layout=Layout(root=tmp_path))


def rules(report) -> set[str]:
    return {f.rule for f in report.findings if f.rule}


# ---------------------------------------------------------------- root hygiene


def test_root_hygiene_accepts_whitelisted_files(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    (tmp_path / "README.md").write_text("x", encoding="utf-8")
    (tmp_path / "ROADMAP.md").write_text("x", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text("x", encoding="utf-8")
    (tmp_path / "video-studio.code-workspace").write_text("{}", encoding="utf-8")

    assert root_hygiene.run(cfg).passed


def test_root_hygiene_rejects_stray_file(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    (tmp_path / "SPRINT_12_DELIVERY.md").write_text("x", encoding="utf-8")

    report = root_hygiene.run(cfg)

    assert not report.passed
    assert "root-whitelist" in rules(report)
    # The suggestion must name a destination, not just refuse.
    assert any("docs/archive/sprints/" in (f.hint or "") for f in report.findings)


def test_root_hygiene_rejects_unexpected_directory(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    (tmp_path / "scratch").mkdir()

    assert "root-dirs" in rules(root_hygiene.run(cfg))


# ---------------------------------------------------------------------- naming


@pytest.mark.parametrize(
    ("filename", "expected_rule"),
    [
        ("my notes.md", "no-spaces"),
        ("Ìbàdàn.md", "ascii-only"),
        ("script_final.md", "numeric-versions"),
        ("shot_latest.md", "numeric-versions"),
        ("backup_of_thing.md", "numeric-versions"),
        ("07-08-2026_meeting.md", "iso-dates"),
    ],
)
def test_naming_rejects(tmp_path: Path, filename: str, expected_rule: str) -> None:
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / filename).write_text("x", encoding="utf-8")

    assert expected_rule in rules(naming.run(cfg))


def test_naming_accepts_conforming_names(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "2026-08-07_advisory-ruling.md").write_text("x", encoding="utf-8")
    (docs / "beat_sheet_v03.md").write_text("x", encoding="utf-8")
    (docs / "SRC-NG-0042_kano-record.md").write_text("x", encoding="utf-8")

    assert naming.run(cfg).passed


def test_naming_catches_template_filled_in_place(tmp_path: Path) -> None:
    """The most common real mistake: filling a template instead of copying it."""
    cfg = make_cfg(tmp_path)
    templates = tmp_path / "templates"
    templates.mkdir()
    (templates / "_TEMPLATE_source_record.md").write_text(
        "---\nstatus: locked\n---\nfilled in\n", encoding="utf-8"
    )

    assert "template-not-filled" in rules(naming.run(cfg))


# ----------------------------------------------------------------------- links


def test_links_detects_dead_link(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "a.md").write_text("see [b](b.md)\n", encoding="utf-8")

    report = links.run(cfg)

    assert "dead-link" in rules(report)
    assert report.findings[0].line == 1


def test_links_accepts_resolvable_and_external(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "b.md").write_text("target\n", encoding="utf-8")
    (docs / "a.md").write_text(
        "[b](b.md) [ext](https://example.com) [anchor](#section) [dir](../core)\n",
        encoding="utf-8",
    )

    assert links.run(cfg).passed


def test_links_tolerates_media_paths(tmp_path: Path) -> None:
    """Media is intentionally absent from git; a link into it is a spec, not a bug."""
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "a.md").write_text("[shot](../05_assets/stills/x.png)\n", encoding="utf-8")

    assert links.run(cfg).passed


def test_links_warns_on_absolute_path(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "a.md").write_text("[x](/core/README.md)\n", encoding="utf-8")

    report = links.run(cfg)

    assert "relative-links" in rules(report)
    assert report.passed  # a warning, not a blocker


# --------------------------------------------------------------------- schemas


SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.local/thing.schema.json",
    "type": "object",
    "properties": {"type": {"const": "source"}, "tier": {"enum": ["T1", "T2"]}},
    "required": ["type", "tier"],
}


def write_schema(tmp_path: Path) -> None:
    d = tmp_path / "standards" / "schemas"
    d.mkdir(parents=True)
    (d / "source_record.schema.json").write_text(json.dumps(SCHEMA), encoding="utf-8")


def test_schemas_accepts_valid_record(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    write_schema(tmp_path)
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "rec.yaml").write_text("type: source\ntier: T1\n", encoding="utf-8")

    assert schemas.run(cfg).passed


def test_schemas_rejects_invalid_enum(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    write_schema(tmp_path)
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "rec.yaml").write_text("type: source\ntier: T9\n", encoding="utf-8")

    assert not schemas.run(cfg).passed


def test_schemas_reports_malformed_yaml(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    write_schema(tmp_path)
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "rec.yaml").write_text("type: source\n  bad: [\n", encoding="utf-8")

    report = schemas.run(cfg)
    assert any("invalid YAML" in f.message for f in report.findings)


def test_schemas_skips_templates(tmp_path: Path) -> None:
    """Templates are meant to be incomplete; validating them would be noise."""
    cfg = make_cfg(tmp_path)
    write_schema(tmp_path)
    (tmp_path / "templates").mkdir()
    (tmp_path / "templates" / "_TEMPLATE_source.yaml").write_text(
        "type: source\ntier: TBD\n", encoding="utf-8"
    )

    assert schemas.run(cfg).passed


# ------------------------------------------------------------------- not built


def test_unbuilt_gate_fails_loudly(tmp_path: Path) -> None:
    """A stub must never pass silently — that would manufacture false confidence."""
    cfg = make_cfg(tmp_path)

    report = nb.run(cfg, "canon")

    assert report.state is GateState.NOT_BUILT
    assert not report.passed
    assert "NOT BUILT" in report.findings[0].message
    assert report.findings[0].hint  # must say what it is blocked on


def test_unbuilt_gate_exits_2_not_1(tmp_path: Path) -> None:
    """Exit code 2 must be reachable.

    Regression: not_built emitted Severity.ERROR, and `exit_code` tests errors
    before not-built, so every unbuilt gate returned 1 — indistinguishable from a
    real finding, and code 2 was dead. The CI workflow's own comment asserted a
    behaviour that never happened.
    """
    cfg = make_cfg(tmp_path)

    run = RunReport()
    run.add(nb.run(cfg, "canon"))

    assert run.error_count == 0
    assert run.exit_code() == 2


def test_real_finding_outranks_unbuilt_gate(tmp_path: Path) -> None:
    """A real failure must not be hidden behind a missing gate."""
    cfg = make_cfg(tmp_path)
    (tmp_path / "STRAY.md").write_text("x", encoding="utf-8")

    run = RunReport()
    run.add(root_hygiene.run(cfg))
    run.add(nb.run(cfg, "canon"))

    assert run.exit_code() == 1


# ---------------------------------------------------------------------- reality


def test_reality_flags_unmarked_unbuilt_command(tmp_path: Path) -> None:
    """Prose naming an unbuilt command without saying so reads as working software."""
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "a.md").write_text(
        "Scaffold it:\n\n    python -m studio_ops new-record --type source\n",
        encoding="utf-8",
    )

    assert "unmarked-unbuilt" in rules(reality.run(cfg))


def test_reality_accepts_marked_mention(tmp_path: Path) -> None:
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "a.md").write_text(
        "```bash\n# NOT BUILT - see docs/status.md\n"
        "python -m studio_ops new-record --type source\n```\n",
        encoding="utf-8",
    )

    assert reality.run(cfg).passed


def test_reality_ignores_implemented_commands(tmp_path: Path) -> None:
    """validate --naming works today and needs no caveat."""
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "a.md").write_text(
        "Run `studio_ops validate --naming` before you push.\n", encoding="utf-8"
    )

    assert reality.run(cfg).passed


def test_reality_exempts_the_status_ledger(tmp_path: Path) -> None:
    """docs/status.md is the source of truth about maturity, not a consumer of it."""
    cfg = make_cfg(tmp_path)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "status.md").write_text(
        "`studio_ops new-record` and `studio_ops report`.\n", encoding="utf-8"
    )

    assert reality.run(cfg).passed
