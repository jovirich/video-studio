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
def new_record_cmd(
    type_: Annotated[str, typer.Option("--type", help="Record type. Omit to list them.")] = "",
    scope: Annotated[str, typer.Option("--scope", help="ID scope, e.g. NG or STUDIO")] = "",
    slug: Annotated[str, typer.Option("--slug")] = "",
    episode: Annotated[str, typer.Option("--episode", help="S01E01 or EXP001")] = "",
    dry_run: Annotated[bool, typer.Option("--dry-run")] = False,
) -> None:
    """Allocate an ID and create a record from its template.

    Refuses on any duplicate ID within the (type, scope) being allocated. That
    refusal is the point: records reference each other by ID string, so a collision
    resolves to whichever file wins, and corrupts the reference graph silently.
    """
    from .scaffold import new_record as scaffold

    if not type_:
        console.print("[bold]Record types[/]")
        for name, spec in sorted(scaffold.RECORD_TYPES.items()):
            console.print(f"  {name:24} {spec.id_type}-*")
        raise typer.Exit(1)
    if not scope:
        console.print("[red]--scope is required[/] (e.g. NG, or STUDIO)")
        raise typer.Exit(1)

    cfg = Config.load()
    try:
        path = scaffold.new_record(
            cfg,
            type_,
            scope.upper(),
            slug=slug or None,
            episode=episode or None,
            dry_run=dry_run,
        )
    except scaffold.ScaffoldError as exc:
        console.print(f"[red]{exc}[/]")
        raise typer.Exit(1) from exc

    verb = "would create" if dry_run else "created"
    console.print(f"[green]{verb}[/] {path}")


@app.command("modes")
def modes() -> None:
    """List execution modes and the backends registered against each.

    Mode is an implementation detail behind the adapter interface — not a tier, and
    not visible to a production. Swapping it changes one config value and no record.
    """
    from .adapters import registered_adapters

    table = Table(show_header=True, header_style="bold")
    table.add_column("Backend")
    table.add_column("Mode")
    table.add_column("Phases")
    table.add_column("Spends")
    table.add_column("Notes")
    for name, cls in sorted(registered_adapters().items()):
        caps = cls.capabilities()
        table.add_row(
            name,
            str(caps.execution_mode),
            "two" if caps.two_phase else "one",
            "yes" if caps.spends_money else "no",
            (caps.notes or "")[:60],
        )
    console.print(table)
    console.print(
        "\n[dim]local[/]        offline model or deterministic test backend, no external call"
        "\n[dim]interactive[/]  pipeline prepares a job; an operator generates; the file is ingested"
        "\n[dim]api[/]          automated vendor call — needs verified terms, credentials, a ceiling\n"
    )


@app.command("prepare-job")
def prepare_job_cmd(
    shot: Annotated[str, typer.Option("--shot", help="Path to the shot record")],
    card: Annotated[str, typer.Option("--card", help="Path to the prompt card")],
    manifest: Annotated[str, typer.Option("--manifest", help="Path to the production manifest")],
    continuity: Annotated[
        list[str], typer.Option("--continuity", help="Continuity record path; repeatable")
    ] = [],  # noqa: B006
    out: Annotated[str, typer.Option("--out", help="Where the asset should land")] = "out",
    job_dir: Annotated[str, typer.Option("--job-dir")] = "jobs",
    vendor: Annotated[str, typer.Option("--vendor")] = "",
    seed: Annotated[str, typer.Option("--seed")] = "",
) -> None:
    """Assemble a complete generation job for interactive execution.

    Offline and free: nothing is rendered by a vendor and no adapter runs. Produces a
    `.job.yaml` and an operator-facing `.md` brief carrying the same obligations, so
    an operator never has to reconstruct constraints from four separate files.
    """
    from pathlib import Path

    from .pipeline import generate as gen

    if not continuity:
        console.print(
            "[red]--continuity is required.[/] A job assembled without continuity "
            "records carries the prompt but none of the constraints, which is the "
            "under-specified brief this format exists to prevent."
        )
        raise typer.Exit(1)

    cfg = Config.load()
    try:
        path = gen.prepare_job(
            cfg,
            shot_path=Path(shot),
            card_path=Path(card),
            manifest_path=Path(manifest),
            work_dir=Path(out),
            continuity_paths=[Path(c) for c in continuity],
            job_dir=Path(job_dir),
            vendor=vendor or None,
            seed=seed or None,
        )
    except (gen.RoundTripError, OSError) as exc:
        console.print(f"[red]{exc}[/]")
        raise typer.Exit(1) from exc

    console.print(f"[green]job[/]   {path}")
    console.print(f"[green]brief[/] {path.with_suffix('.md')}")
    console.print("\n[dim]Hand the brief to the operator. Ingest the returned file with[/]")
    console.print("[dim]  studio_ops ingest --job <job> --file <delivered>[/]")


@app.command("ingest")
def ingest_cmd(
    job: Annotated[str, typer.Option("--job", help="The job file that was fulfilled")],
    file: Annotated[str, typer.Option("--file", help="The delivered asset")],
    vendor: Annotated[str, typer.Option("--vendor", help="What ACTUALLY produced it")] = "",
    model: Annotated[str, typer.Option("--model")] = "",
    model_version: Annotated[str, typer.Option("--model-version")] = "",
    seed: Annotated[str, typer.Option("--seed")] = "",
    cost: Annotated[float, typer.Option("--cost-usd")] = 0.0,
) -> None:
    """Ingest an operator-generated file: hash it, record it, add it to the manifest.

    The hash is computed from the delivered bytes and is never taken on report. An
    operator can hand back the wrong file; they cannot hand back a file whose hash
    disagrees with its contents, because nobody asks them for it.
    """
    from pathlib import Path

    from .pipeline import generate as gen
    from .pipeline import manifest as manifest_mod

    if not vendor or not model:
        console.print(
            "[red]--vendor and --model are required.[/] They name what ACTUALLY "
            "produced the file. 'interactive' is how it arrived, not what made it, and "
            "a manifest entry that cannot say what made an asset is not a provenance "
            "record."
        )
        raise typer.Exit(1)

    cfg = Config.load()
    try:
        trip = gen.fulfil_job(
            cfg,
            job_path=Path(job),
            delivered=Path(file),
            vendor=vendor,
            model=model,
            model_version=model_version or model,
            seed=seed or None,
            cost_usd=cost,
        )
    except (gen.RoundTripError, manifest_mod.ManifestError, OSError) as exc:
        console.print(f"[red]{exc}[/]")
        raise typer.Exit(1) from exc

    console.print(f"[green]ingested[/] {trip.asset_id}")
    console.print(f"  sha256      {trip.sha256}")
    console.print(f"  store path  {trip.entry['store_path']}")
    console.print(f"  shot        {trip.shot_id or '—'}")
    console.print(
        "\n[dim]Hash computed from the delivered bytes, not taken on report. "
        "Vendor, model, and seed are as you stated them and are recorded as "
        "unverifiable.[/]"
    )


@app.command("check-ids")
def check_ids() -> None:
    """Audit the whole repository for duplicate IDs.

    Worth running before any research pass and after any hand-edit of a record. A
    collided ID is silent and, because IDs are permanent, unrecoverable.
    """
    from .scaffold import ids

    cfg = Config.load()
    collisions = ids.find_collisions(cfg.root)
    if not collisions:
        console.print("[green]No duplicate IDs.[/]")
        return
    for record_id, paths in sorted(collisions.items()):
        console.print(f"[red]{record_id}[/] claimed by {len(paths)} files:")
        for path in paths:
            console.print(f"    {path}")
    raise typer.Exit(1)


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
        console.print("Subcommands: [cyan]render[/]")
        raise typer.Exit(1)


@promptlib_app.command("render")
def promptlib_render(
    card: Annotated[str, typer.Argument(help="Path to a *.prompt.yaml")],
    vendor: Annotated[str, typer.Option("--vendor")] = "",
    style: Annotated[str, typer.Option("--style", help="Continuity record to inherit")] = "",
    fmt: Annotated[str, typer.Option("--format", help="text | json")] = "text",
) -> None:
    """Render a card to its vendor string. Offline, and costs nothing.

    The same card renders differently per vendor — that portability is the practical
    payoff of treating a prompt as a record rather than a string.
    """
    from pathlib import Path

    from .pipeline.generate import style_block_from_continuity
    from .promptlib import render as render_mod

    block = style_block_from_continuity([Path(style)]) if style else {}
    try:
        rendered = render_mod.render_file(Path(card), vendor or None, style_block=block)
    except render_mod.PromptCardError as exc:
        console.print(f"[red]{exc}[/]")
        raise typer.Exit(1) from exc

    if fmt == "json":
        import json

        print(json.dumps(rendered.to_dict(), indent=2))
        return

    console.print(f"[dim]{rendered.card_id} -> {rendered.vendor}[/]")
    console.print()
    console.print(rendered.prompt)
    if rendered.negative:
        console.print()
        console.print(f"[dim]negative:[/] {', '.join(rendered.negative)}")
    if rendered.parameters:
        console.print(f"[dim]parameters:[/] {rendered.parameters}")


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
