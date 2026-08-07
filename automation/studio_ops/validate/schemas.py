"""Record schema gate.

Validates YAML records and markdown front matter against standards/schemas/.

Maturity: IMPLEMENTED.

Note on honesty: with no real records in the repository, a clean run here proves
that the schemas parse and that the few control records conform. It does not prove
the schemas are right. That requires records, and records require a production.
See docs/status.md.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..config import Config
from ..frontmatter import is_template, read, read_yaml
from ..paths import iter_files
from ..result import Finding, GateReport, Severity, rel

GATE = "schemas"

# Filename or glob -> schema file. Control records first; record-type files are
# routed by their `type` field instead.
FILE_SCHEMAS: dict[str, str] = {
    "studio.yaml": "studio.schema.json",
    "line.yaml": "production_line.schema.json",
    "production.yaml": "episode.schema.json",
    "episode.yaml": "episode.schema.json",
    "manifest.yaml": "asset_manifest.schema.json",
    "pack.yaml": "pack.schema.json",
}

TYPE_SCHEMAS: dict[str, str] = {
    "source": "source_record.schema.json",
    "claim": "claim.schema.json",
    "character": "character.schema.json",
    "location": "location.schema.json",
    "timeline_event": "timeline_event.schema.json",
    "shot": "shot.schema.json",
    "prompt_card": "prompt_card.schema.json",
    "episode": "episode.schema.json",
    "production_line": "production_line.schema.json",
    "asset_manifest": "asset_manifest.schema.json",
    "open_question": "open_question.schema.json",
    "fact_check": "fact_check.schema.json",
    "advisory_ruling": "advisory_ruling.schema.json",
    "correction": "correction.schema.json",
    "style_anchor": "style_anchor.schema.json",
    "continuity_character": "continuity_character.schema.json",
    "continuity_location": "continuity_location.schema.json",
}


def run(cfg: Config) -> GateReport:
    report = GateReport(gate=GATE)
    root = cfg.root
    schema_dir = cfg.layout.schemas

    if not schema_dir.is_dir():
        report.findings.append(
            Finding(GATE, Severity.ERROR, "standards/schemas/ is missing", "standards/schemas")
        )
        return report

    try:
        import jsonschema  # noqa: F401
    except ImportError:
        report.findings.append(
            Finding(
                GATE,
                Severity.ERROR,
                "jsonschema is not installed",
                hint="pip install -e '.[dev]'",
            )
        )
        return report

    store = _load_schemas(schema_dir, report, root)
    if not store:
        return report

    for path in iter_files(root, suffix=".yaml") + iter_files(root, suffix=".yml"):
        if _skip(path, root):
            continue
        data, err = read_yaml(path)
        if err:
            report.files_checked += 1
            report.findings.append(Finding(GATE, Severity.ERROR, err, rel(path, root)))
            continue
        schema_name = _route(path, data or {})
        if not schema_name:
            continue
        report.files_checked += 1
        _validate(path, data or {}, schema_name, store, schema_dir, report, root)

    for path in iter_files(root, suffix=".md"):
        if _skip(path, root):
            continue
        doc = read(path)
        if doc.error:
            report.files_checked += 1
            report.findings.append(Finding(GATE, Severity.ERROR, doc.error, rel(path, root)))
            continue
        if not doc.has_frontmatter:
            continue
        schema_name = TYPE_SCHEMAS.get(str(doc.meta.get("type", "")))
        if not schema_name:
            continue
        report.files_checked += 1
        _validate(path, doc.meta, schema_name, store, schema_dir, report, root)

    return report


def _skip(path: Path, root: Path) -> bool:
    if is_template(path):
        return True
    relpath = rel(path, root)
    # Workflow and tooling config are not records.
    return relpath.startswith((".github/", ".vscode/", "automation/tests/fixtures/"))


def _route(path: Path, data: dict[str, Any]) -> str | None:
    if path.name in FILE_SCHEMAS:
        return FILE_SCHEMAS[path.name]
    if path.name.endswith(".prompt.yaml"):
        return "prompt_card.schema.json"
    declared = str(data.get("type", ""))
    return TYPE_SCHEMAS.get(declared)


def _load_schemas(schema_dir: Path, report: GateReport, root: Path) -> dict[str, dict[str, Any]]:
    store: dict[str, dict[str, Any]] = {}
    for schema_file in sorted(schema_dir.glob("*.schema.json")):
        try:
            store[schema_file.name] = json.loads(schema_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            report.findings.append(
                Finding(
                    GATE,
                    Severity.ERROR,
                    f"schema is not valid JSON: {exc}",
                    rel(schema_file, root),
                    rule="schema-parse",
                )
            )
    return store


def _validate(
    path: Path,
    data: dict[str, Any],
    schema_name: str,
    store: dict[str, dict[str, Any]],
    schema_dir: Path,
    report: GateReport,
    root: Path,
) -> None:
    import jsonschema
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012

    schema = store.get(schema_name)
    if schema is None:
        report.findings.append(
            Finding(
                GATE,
                Severity.WARNING,
                f"no schema named {schema_name} — record not validated",
                rel(path, root),
                rule="schema-missing",
            )
        )
        return

    # Sibling schemas reference each other by bare filename (_common.schema.json#/...).
    registry: Registry = Registry()
    for name, doc in store.items():
        registry = registry.with_resource(
            name, Resource.from_contents(doc, default_specification=DRAFT202012)
        )

    validator = Draft202012Validator(schema, registry=registry)
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        pointer = "/".join(str(p) for p in error.path) or "(root)"
        report.findings.append(
            Finding(
                GATE,
                Severity.ERROR,
                f"{pointer}: {error.message}",
                rel(path, root),
                rule=f"schema:{schema_name}",
                hint=f"Validated against standards/schemas/{schema_name}",
            )
        )
    _ = jsonschema  # keep the import meaningful for readers
