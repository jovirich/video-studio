"""An anchor's filename must name the card VERSION, not just the card.

Pins the defect that nearly cost Character A's anchor. Both A's and B's prompt cards
were rewritten — a lateral distinctive feature became a midline one — while sitting at
`version: 0.1.0`. Every candidate file named only the card ID, so a file made before
the rewrite was indistinguishable from one made after it. Four superseded candidates
were sitting in the incoming folder under the correct card ID and came within one step
of being ingested as the canonical anchor.

An anchor propagates into every shot that inherits it. It is the one artefact where
"which version of the spec produced this?" has to be answerable from the filename
alone, because by the time it is wrong, seventeen shots are wrong with it.

Runs against the real EXP-001 records rather than a fixture: the fixture would have
been written to match the code, and the code was what was wrong.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from studio_ops.config import Config
from studio_ops.pipeline.generate import prepare_job

PRODUCTION = Path("studios/african-history/lines/ng-nigeria/productions/EXP001_laboratory-scene")
CARD = PRODUCTION / "04_prompts/PC-NG-EXP001-0002_anchor-b-face.prompt.yaml"
CONTINUITY = Path("studios/african-history/lines/ng-nigeria/continuity/characters")


def test_anchor_filename_carries_the_card_version(tmp_path: Path) -> None:
    cfg = Config.load()
    root = cfg.root

    job_path = prepare_job(
        cfg,
        card_path=root / CARD,
        manifest_path=root / PRODUCTION / "manifest.yaml",
        work_dir=tmp_path,
        continuity_paths=[root / CONTINUITY / "CNC-NG-0002_character-b.md"],
        job_dir=tmp_path / "jobs",
        is_anchor=True,
        candidates=4,
    )
    job = yaml.safe_load(job_path.read_text(encoding="utf-8"))

    card = yaml.safe_load((root / CARD).read_text(encoding="utf-8"))
    version = str(card["version"])

    assert f"_v{version}_" in job["output_filename"], (
        f"anchor filename {job['output_filename']!r} does not name card version {version!r}"
    )
    for name in job["candidate_filenames"]:
        assert f"_v{version}_" in name, f"candidate {name!r} does not name the card version"


def test_every_candidate_filename_is_distinct(tmp_path: Path) -> None:
    """Four candidates must be four files.

    The four files that had to be quarantined were 627x627 — exactly half of the
    1254x1254 composite the surface actually returned. They were the cells of ONE
    generation, cropped apart and renamed, which made a single sampling event look
    like four independent draws.
    """
    cfg = Config.load()
    root = cfg.root
    job_path = prepare_job(
        cfg,
        card_path=root / CARD,
        manifest_path=root / PRODUCTION / "manifest.yaml",
        work_dir=tmp_path,
        continuity_paths=[root / CONTINUITY / "CNC-NG-0002_character-b.md"],
        job_dir=tmp_path / "jobs",
        is_anchor=True,
        candidates=4,
    )
    job = yaml.safe_load(job_path.read_text(encoding="utf-8"))
    names = list(job["candidate_filenames"])
    assert len(names) == 4
    assert len(set(names)) == 4, f"candidate filenames collide: {names}"
