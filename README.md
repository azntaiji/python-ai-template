# <project_name>

## Overview

<!-- One paragraph: what <project_name> does and who it is for.
     Fill this in during the setup track. -->

## Requirements

- Python 3.11+
- direnv (optional — auto-activates the venv in interactive shells)

## Installation

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e .
```

For development (adds pytest):

```bash
.venv/bin/python -m pip install -e ".[dev]"
```

## Configuration

Copy `.env.example` to `.env` and fill in the values. `.env` is gitignored —
never commit it.

```bash
cp .env.example .env
```

## Usage

```bash
.venv/bin/<package_name>
```

<!-- Document CLI arguments and flags here as they are added. The post-task
     checklist in STATE.md requires keeping this section current. -->

## Development

- Run tests: `.venv/bin/pytest`
- Logs are written to `out/logs/app.log` (rotating; not committed)
- Agents and contributors: start with `AGENTS.md`

## Contact

Contact me: zach@azntaiji.com
