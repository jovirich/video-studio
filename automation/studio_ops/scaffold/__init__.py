"""Scaffolding: ID allocation and record creation.

`ids` and `new_record` are IMPLEMENTED. The remaining scaffolders — `new-studio`,
`new-line`, `new-production`, `new-pack` — are NOT BUILT; see ../../README.md.

The allocator was built first because IDs are permanent and records reference each
other by ID *string*, not by path. A duplicate does not break a reference, it
re-points it, and `validate --sources` — the gate that would catch that — does not
exist yet.

Submodules are exported rather than their symbols, because `new_record` is both a
module and the function inside it, and a package-level re-export would make
`scaffold.new_record` mean whichever import happened to run last. Callers write
`ids.allocate(...)` and `new_record.new_record(...)`.
"""

from __future__ import annotations

from . import ids, new_record

__all__ = ["ids", "new_record"]
