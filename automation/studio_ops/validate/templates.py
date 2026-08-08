"""Template gate — a template must produce a record that can pass its own schema.

Built because it blocked a production step. Creating Character A's face anchor from
`_TEMPLATE_style_anchor.md` produced a file that failed `style_anchor.schema.json` five
ways at once: three required fields the template never mentions (`file`, `sha256`,
`description`), six fields the schema forbids, and an `anchor_kind` whose documented
values were not the enum's values.

Neither artefact was wrong on its own. The schema was valid JSON Schema; the template
was valid front matter. They had simply drifted apart, and nothing compared them —
because the comparison only happens when somebody creates a record of that type, and
nobody had ever created a style anchor.

Five of thirteen templates were in that state. Each one is a wall that the first person
to use it walks into.

WHAT THIS CHECKS, AND WHAT IT DELIBERATELY DOES NOT
---------------------------------------------------
It compares KEYS, not values: every schema-required key is present in the template, and
no template key is one the schema forbids.

It cannot check values, because a template's values are placeholders. `TBD` is the
correct content for a template field and illegal in a real record (finding G6), so
running full schema validation over a template would fail every template forever and
the gate would be switched off within a week. Keys are the part that can be checked
honestly, and keys are where the drift was.

A template with no `type`, or a `type` with no schema, is reported as UNCHECKED rather
than passed. `_TEMPLATE_research_brief.md` is genuinely in that state and says so in
its own header; it is not a defect, but it is not evidence of correctness either.

Maturity: IMPLEMENTED.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..config import Config
from ..frontmatter import read
from ..result import Finding, GateReport, Severity, rel

GATE = "templates"

TEMPLATE_DIR = Path("templates") / "records"
SCHEMA_DIR = Path("standards") / "schemas"

# Maps a record's `type` to its schema file where the two are not the same word.
# Kept deliberately small: a long list here means the naming convention has failed.
TYPE_SCHEMA_ALIASES: dict[str, str] = {
    "source": "source_record",
}


def run(cfg: Config) -> GateReport:
    report = GateReport(gate=GATE)
    root = cfg.root
    template_dir = root / TEMPLATE_DIR

    if not template_dir.is_dir():
        return report

    for path in sorted(template_dir.glob("_TEMPLATE_*.md")):
        report.files_checked += 1
        doc = read(path)
        meta: dict[str, Any] = doc.meta or {}
        where = rel(path, root)

        record_type = meta.get("type")
        if not isinstance(record_type, str) or not record_type:
            report.findings.append(
                Finding(
                    GATE,
                    Severity.WARNING,
                    "UNCHECKED — the template declares no `type`, so no schema can be found",
                    where,
                    rule="template-unchecked",
                    hint=(
                        "Not necessarily wrong: some record types have no schema yet. But "
                        "this template is not evidence that anything agrees with anything."
                    ),
                )
            )
            continue

        schema_name = TYPE_SCHEMA_ALIASES.get(record_type, record_type)
        schema_path = root / SCHEMA_DIR / f"{schema_name}.schema.json"
        if not schema_path.is_file():
            report.findings.append(
                Finding(
                    GATE,
                    Severity.WARNING,
                    f"UNCHECKED — no schema for type {record_type!r}",
                    where,
                    rule="template-unchecked",
                    hint=(
                        f"Expected {SCHEMA_DIR}/{schema_name}.schema.json. Write the schema, "
                        "or add an alias if it exists under a different name."
                    ),
                )
            )
            continue

        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            report.findings.append(
                Finding(GATE, Severity.ERROR, f"unreadable schema: {exc}", where)
            )
            continue

        properties = set(schema.get("properties") or {})
        required = set(schema.get("required") or [])
        keys = set(meta)

        missing = sorted(required - keys)
        if missing:
            report.findings.append(
                Finding(
                    GATE,
                    Severity.ERROR,
                    f"template omits required field(s): {', '.join(missing)}",
                    where,
                    rule="template-missing-required",
                    hint=(
                        "Anyone creating this record from the template gets a file that "
                        "fails validation immediately, with no indication that the "
                        "template was at fault rather than their editing."
                    ),
                )
            )

        if schema.get("additionalProperties") is False:
            forbidden = sorted(keys - properties)
            if forbidden:
                report.findings.append(
                    Finding(
                        GATE,
                        Severity.ERROR,
                        f"template has field(s) the schema forbids: {', '.join(forbidden)}",
                        where,
                        rule="template-forbidden-field",
                        hint=(
                            "Usually the schema was tightened and the template was not "
                            "updated with it. Decide which is right — the field may belong "
                            "in the schema — but they cannot both stand."
                        ),
                    )
                )

        _check_enums(report, meta, schema, where)

    return report


def _check_enums(
    report: GateReport, meta: dict[str, Any], schema: dict[str, Any], where: str
) -> None:
    """Flag a template placeholder that is not one of its field's permitted values.

    Narrow on purpose. A template placeholder is normally free text and must stay that
    way, but an enum field is the one case where the template can and should carry a
    real value — and where a stale one actively misleads. The style-anchor template
    documented nine `anchor_kind` values, of which four were not in the enum at all.
    """
    for field, spec in (schema.get("properties") or {}).items():
        enum = spec.get("enum")
        if not enum or field not in meta:
            continue
        value = meta[field]
        if isinstance(value, str) and value not in enum and not _is_placeholder(value):
            report.findings.append(
                Finding(
                    GATE,
                    Severity.ERROR,
                    f"{field}: template value {value!r} is not one of {enum}",
                    where,
                    rule="template-stale-enum",
                    hint="The enum changed and the template kept the old vocabulary.",
                )
            )


def _is_placeholder(value: str) -> bool:
    """`TBD` in a template is correct, and stays correct (finding G6)."""
    return value.strip().upper().startswith("TBD")
