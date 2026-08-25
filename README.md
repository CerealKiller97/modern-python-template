# Modern Python Template

A batteries-included Python project template built on the **Astral stack** — [uv](https://github.com/astral-sh/uv) for packaging, [ruff](https://github.com/astral-sh/ruff) for linting and formatting, and [ty](https://github.com/astral-sh/ty) for type checking — wired together with [Poe the Poet](https://github.com/nat-n/poethepoet) as the task runner.

[![Lint](https://github.com/CerealKiller97/modern-python-template/actions/workflows/lint.yml/badge.svg)](https://github.com/CerealKiller97/modern-python-template/actions/workflows/lint.yml)
[![Tests](https://github.com/CerealKiller97/modern-python-template/actions/workflows/test.yml/badge.svg)](https://github.com/CerealKiller97/modern-python-template/actions/workflows/test.yml)
[![Type checking](https://github.com/CerealKiller97/modern-python-template/actions/workflows/type-coverage.yml/badge.svg)](https://github.com/CerealKiller97/modern-python-template/actions/workflows/type-coverage.yml)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue)](https://www.python.org/downloads/)

## Why this template?

No `pip`, no `poetry`, no juggling `flake8` + `black` + `isort` + `mypy` configs. One toolchain, written in Rust, that's an order of magnitude faster than what it replaces:

| Concern | Tool | Replaces |
|---|---|---|
| Dependency management & venvs | [uv](https://docs.astral.sh/uv/) | pip, pip-tools, poetry, pyenv |
| Linting + import sorting | [ruff](https://docs.astral.sh/ruff/) | flake8, isort, pylint |
| Formatting | [ruff format](https://docs.astral.sh/ruff/formatter/) | black |
| Type checking | [ty](https://github.com/astral-sh/ty) | mypy |
| Task running | [poethepoet](https://poethepoet.natn.io/) | make, tox |

## Getting started

```bash
git clone https://github.com/CerealKiller97/modern-python-template.git
cd modern-python-template
uv sync
```

That installs Python 3.14 (if you don't already have it), creates `.venv`, and resolves every dependency — dev tools included.

## Commands

All tasks are defined in `pyproject.toml` under `[tool.poe.tasks]` and run through `uv run`:

```bash
uv run poe fmt          # format the codebase with ruff
uv run poe lint         # lint + autofix with ruff
uv run poe type-check   # static type checking with ty
uv run poe test         # run tests with pytest + coverage report
```

## Project structure

```
.
├── src/                  # application source
│   └── util/             # example module
├── tests/
│   └── unit/              # unit tests (pytest)
├── ruff.toml              # ruff lint + format config
├── pyproject.toml         # project metadata, deps, poe tasks
└── .github/workflows/     # CI: lint, test, type-check
```

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## License

MIT
