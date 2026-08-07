"""Command-line interface.

Every command in this repository's documentation is registered here. Commands that
are not implemented say so and exit non-zero — they never succeed quietly, because a
command that appears to work and does nothing is worse than a missing command.
"""

from __future__ import annotations

import sys
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from . import validate as gates
from .config import Config
from .result import GateState, RunReport, Severity

app = typer.Typer(
    name="studio",
    help="Toolkit for the video-studio platform.",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()

NOT_BUILT_EXIT = 2


def _not_built(command: str, will_do: str, blocked_on: str) -> None:
    console.print(f"[bold yellow]NOT BUILT[/] — `{command}` does not exist yet.")
    console.print(f"  Will do:     {will_do}")
    console.print(f"  Blocked on:  {blocked_on}")
    console.print("  See [cyan]docs/status.md[/] for the full capability ledger.")
    raise typer.Exit(NOT_BUILT_EXIT)


# --------------------------------------------------------------------------
# validate
# --------------------------------------------------------------------------


@app.command()
def validate(
    all_gates: Annotated[bool, typer.Option("--all", help="Run every gate, built or not.")] = False,
    schemas: Annotated[bool, typer.Option("--schemas")] = False,
    naming: Annotated[bool, typer.Option("--naming")] = False,
    links: Annotated[bool, typer.Option("--links")] = False,
    root_hygiene: Annotated[bool, typer.Option("--root-hygiene")] = False,
    reality: Annotated[bool, typer.Option("--reality")] = False,
    sources: Annotated[bool, typer.Option("--sources")] = False,
    canon: Annotated[bool, typer.Option("--canon")] = False,
    prompts: Annotated[bool, typer.Option("--prompts")] = False,
    packs: Annotated[bool, typer.Option("--packs")] = False,
    fmt: Annotated[str, typer.Option("--format", help="table | json")] = "table",
) -> None:
    """Run repository gates.

    Exit codes: 0 clean, 1 findings, 2 a requested gate is NOT BUILT.

    2 is distinct from 0 on purpose: a green build that ran four of nine gates must
    not look like a green build that ran nine.
    """
    selected: list[str] = []
    if all_gates:
        selected = list(gates.ALL_GATES)
    else:
        for flag, name in (
            (schemas, "schemas"),
            (naming, "naming"),
            (links, "links"),
            (root_hygiene, "root-hygiene"),
            (reality, "reality"),
            (sources, "sources"),
            (canon, "canon"),
            (prompts, "prompts"),
            (packs, "packs"),
        ):
            if flag:
                selected.append(name)

    if not selected:
        console.print("[yellow]No gate selected.[/] Use --all or a specific flag.")
        console.print(f"Available: {', '.join(gates.ALL_GATES)}")
        raise typer.Exit(1)

    cfg = Config.load()
    report = gates.run_gates(cfg, selected)

    if fmt == "json":
        print(report.to_json())
    else:
        _render(report, cfg)

    raise typer.Exit(report.exit_code())


def _render(report: RunReport, cfg: Config) -> None:
    console.print(f"\n[dim]repository:[/] {cfg.root}\n")

    summary = Table(show_header=True, header_style="bold")
    summary.add_column("Gate")
    summary.add_column("State")
    summary.add_column("Files", justify="right")
    summary.add_column("Errors", justify="right")
    summary.add_column("Warnings", justify="right")

    for gate_report in report.reports:
        if gate_report.state is GateState.NOT_BUILT:
            state = "[yellow]NOT BUILT[/]"
        elif gate_report.errors:
            state = "[red]FAIL[/]"
        elif gate_report.warnings:
            state = "[yellow]PASS[/]"
        else:
            state = "[green]PASS[/]"
        summary.add_row(
            gate_report.gate,
            state,
            str(gate_report.files_checked or "—"),
            str(len(gate_report.errors)) if gate_report.errors else "—",
            str(len(gate_report.warnings)) if gate_report.warnings else "—",
        )
    console.print(summary)

    for gate_report in report.reports:
        if not gate_report.findings:
            continue
        console.print(f"\n[bold]{gate_report.gate}[/]")
        for finding in gate_report.findings[:50]:
            colour = "red" if finding.severity is Severity.ERROR else "yellow"
            console.print(f"  [{colour}]{finding.severity}[/] {finding.location()}")
            console.print(f"    {finding.message}")
            if finding.hint:
                console.print(f"    [dim]{finding.hint}[/]")
        if len(gate_report.findings) > 50:
            console.print(f"  [dim]... and {len(gate_report.findings) - 50} more[/]")

    console.print(
        f"\n[bold]{report.error_count}[/] errors, "
        f"[bold]{report.warning_count}[/] warnings, "
        f"[bold]{len(report.not_built)}[/] gates NOT BUILT\n"
    )


# --------------------------------------------------------------------------
# scaffolding — NOT BUILT
# --------------------------------------------------------------------------


@app.command("new-studio")
def new_studio(code: str = "", title: str = "", pack: str = "") -> None:
    """Create a studio. NOT BUILT."""
    _not_built(
        "new-studio",
        "Copy templates/studio/ to studios/<code>/, write studio.yaml with the "
        "declared pack, and seed the decision register from that pack's "
        "studio_must_decide list.",
        "templates/studio/ scaffolding and pack.schema.json.",
    )


@app.command("new-line")
def new_line(studio: str = "", code: str = "", title: str = "") -> None:
    """Create a production line. NOT BUILT."""
    _not_built(
        "new-line",
        "Copy templates/line/ to studios/<studio>/lines/<code>/ with "
        "line_status: candidate and all opening conditions false.",
        "templates/line/ scaffolding.",
    )


@app.command("new-production")
def new_production(line: str = "", season: int = 1, number: int = 1, slug: str = "") -> None:
    """Create a production. NOT BUILT."""
    _not_built(
        "new-production",
        "Copy templates/production/ into the line, build the gate block from the "
        "studio's pack gates.yaml, and allocate the production ID.",
        "templates/production/ scaffolding and gates.yaml parsing.",
    )


@app.command("new-pack")
def new_pack(code: str = "", title: str = "") -> None:
    """Author a canon pack. NOT BUILT."""
    _not_built(
        "new-pack",
        "Copy packs/_TEMPLATE_pack/ to packs/<code>/.",
        "Nothing — this is the cheapest scaffolder to build first.",
    )


@app.command("new-record")
def new_record(type_: str = typer.Option("", "--type"), line: str = "") -> None:
    """Allocate an ID and create a record. NOT BUILT."""
    _not_built(
        "new-record",
        "Allocate the next serial for (type, scope), refuse on a gap-and-collision "
        "pattern suggesting a hand-edited ID, and write the record from its template.",
        "The ID allocator. This is the highest-priority scaffolder — hand-allocated "
        "IDs collide, and a collided ID silently corrupts the reference graph.",
    )


# --------------------------------------------------------------------------
# other command families — NOT BUILT
# --------------------------------------------------------------------------

report_app = typer.Typer(help="Derived views over the record graph. NOT BUILT.")
app.add_typer(report_app, name="report")


@report_app.callback(invoke_without_command=True)
def report_root(ctx: typer.Context) -> None:
    if ctx.invoked_subcommand is None:
        _not_built(
            "report",
            "bibliography, shotlist, open-questions, source-coverage, dependents, "
            "pronunciation, chapters, provenance, chain-of-title.",
            "The record graph. No records exist yet.",
        )


promptlib_app = typer.Typer(help="Prompt card rendering and execution. NOT BUILT.")
app.add_typer(promptlib_app, name="promptlib")


@promptlib_app.callback(invoke_without_command=True)
def promptlib_root(ctx: typer.Context) -> None:
    if ctx.invoked_subcommand is None:
        _not_built(
            "promptlib",
            "render a prompt card to a vendor-specific string; run it against an "
            "adapter under the production's cost ceiling.",
            "Per-vendor renderers. This is the main practical payoff of the card "
            "structure and is currently unproven.",
        )


pipeline_app = typer.Typer(help="Asset pipeline. NOT BUILT.")
app.add_typer(pipeline_app, name="pipeline")


@pipeline_app.callback(invoke_without_command=True)
def pipeline_root(ctx: typer.Context) -> None:
    if ctx.invoked_subcommand is None:
        _not_built(
            "pipeline",
            "ingest, manifest, conform, package. The conform step refuses any "
            "timeline clip without a manifest entry — that refusal is the mechanism "
            "behind the platform's traceability guarantee.",
            "The asset store. No round trip has been proved.",
        )


@app.command()
def status(studio: str = "", line: str = "") -> None:
    """Slate and gate status. NOT BUILT."""
    _not_built(
        "status",
        "Walk studios, lines, and productions; report stage, gate signatures, "
        "unresolved decisions, and counts.",
        "Control records to walk. See docs/status.md for the current hand-maintained "
        "capability ledger.",
    )


def main() -> None:
    try:
        app()
    except KeyboardInterrupt:
        sys.exit(130)


if __name__ == "__main__":
    main()
