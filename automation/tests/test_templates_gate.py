"""Tests for the template gate, and for the honesty of NOT-BUILT blockers.

Both pin the same failure mode: a statement that was true when written, stayed in the
repository after it stopped being true, and was believed.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from studio_ops.config import Config
from studio_ops.validate import not_built, templates


def _root() -> Path:
    return Config.load().root


def test_every_template_agrees_with_its_schema() -> None:
    """The gate over the real repository, which is the only run that matters.

    Five of thirteen templates failed this when it was first written. Each one was a
    wall for whoever created the first record of that type — which is exactly when a
    person is least able to tell a broken template from their own mistake.
    """
    report = templates.run(Config.load())
    assert report.files_checked > 0, "gate found no templates — the glob is wrong"
    assert [f.message for f in report.errors] == []


def test_style_anchor_template_produces_a_valid_record_shape() -> None:
    """The specific template that blocked Character A's face anchor."""
    root = _root()
    from studio_ops.frontmatter import read

    meta = read(root / "templates/records/_TEMPLATE_style_anchor.md").meta or {}
    schema = json.loads(
        (root / "standards/schemas/style_anchor.schema.json").read_text(encoding="utf-8")
    )
    assert set(schema["required"]) <= set(meta)
    assert set(meta) <= set(schema["properties"])
    assert meta["anchor_kind"] in schema["properties"]["anchor_kind"]["enum"]


def test_not_built_blockers_do_not_name_files_that_exist() -> None:
    """A gate that blames a missing file must be blaming a file that is missing.

    The `packs` gate claimed to be blocked on `pack.schema.json` not having been
    written. The schema was 13KB and five packs validated against it. Anyone reading
    that would have written a second one.
    """
    root = _root()
    for gate, planned in not_built.PLANNED.items():
        for candidate in planned.missing_paths:
            path = root / candidate
            assert not path.exists(), (
                f"gate {gate!r} claims it is blocked on {candidate!r}, but that file "
                f"now exists. Either implement the gate or correct the claim."
            )


def test_every_named_file_in_a_blocker_is_declared() -> None:
    """Prose and structure must not drift apart either.

    A path named in `blocked_on` prose as missing, but absent from `missing_paths`,
    is unchecked — which is how the original claim survived. The exception is a file
    the prose names as a SOURCE rather than as the thing that is missing, which is
    why this asserts declaration rather than absence.
    """
    # Only repo-relative PATHS are checkable. A bare filename in prose ("pack.schema.json
    # exists") is a reference to a file, not a claim about where it lives, and
    # resolving it against the root would report a false absence.
    pattern = re.compile(r"\b[\w.-]+(?:/[\w.-]+)+\.(?:json|py|yaml|yml)\b")
    for gate, planned in not_built.PLANNED.items():
        for candidate in pattern.findall(planned.blocked_on):
            root = _root()
            if (root / candidate).exists():
                continue  # named as an existing input, not as the blocker
            assert candidate in planned.missing_paths, (
                f"gate {gate!r} names missing file {candidate!r} in prose but does not "
                f"declare it in missing_paths, so nothing checks it"
            )
