# African History Studio — task runner.
# Windows users: `make` may not be present. Every target below has an equivalent
# VS Code task in .vscode/tasks.json (Ctrl+Shift+P → "Tasks: Run Task").

.DEFAULT_GOAL := help
PY := python

.PHONY: help setup validate validate-fast lint format typecheck test status \
        new-episode new-line bibliography shotlist clean audit-root

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

setup: ## Create venv and install the toolkit in editable mode
	$(PY) -m venv .venv
	.venv/Scripts/pip install -e ".[dev]" || .venv/bin/pip install -e ".[dev]"

validate: ## Run every repository gate (what CI runs)
	$(PY) -m studio_ops validate --all

validate-fast: ## Schemas and naming only — the pre-commit subset
	$(PY) -m studio_ops validate --schemas --naming

lint: ## Ruff
	ruff check automation

format: ## Ruff format
	ruff format automation

typecheck: ## mypy
	mypy automation/studio_ops

test: ## pytest
	pytest

status: ## Slate + gate status for the default line
	$(PY) -m studio_ops status --line ng-nigeria

new-episode: ## make new-episode LINE=ng-nigeria S=1 E=1 SLUG=working-title
	$(PY) -m studio_ops new-episode --line $(LINE) --season $(S) --number $(E) --slug $(SLUG)

new-line: ## make new-line CODE=gh-ghana NAME="Ghana"
	$(PY) -m studio_ops new-line --code $(CODE) --name $(NAME)

bibliography: ## Build the bibliography for an episode: make bibliography EP=S01E01
	$(PY) -m studio_ops report bibliography --episode $(EP)

shotlist: ## Export the shot list for an episode: make shotlist EP=S01E01
	$(PY) -m studio_ops report shotlist --episode $(EP)

audit-root: ## Fail if unwhitelisted files have accumulated at repo root
	$(PY) -m studio_ops validate --root-hygiene

clean: ## Remove Python build and cache artefacts
	rm -rf build dist *.egg-info .pytest_cache .mypy_cache .ruff_cache
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
