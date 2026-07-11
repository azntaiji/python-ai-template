# AGENTS.md

> Read this file before doing any work in the repository. The skills named below are installed in the agent environment — consult them by name when their domain comes up; do not improvise alternatives to them.

## Quick Start

1. Read this file — architecture and operating rules
2. Read `PLAN.md` — scope and status
3. Read `STATE.md` — current status

## Architecture

- Flow: `Intent → Command → Event → State`

## Conventions and Working agreements

These apply to all work in this repository, at all times:

- Use `python3` for the system interpreter and always invoke the venv interpreter directly (`.venv/bin/python`, `.venv/bin/python -m pip`) rather than relying on shell activation, since activation does not persist across separate command invocations. Interactive users get activation automatically via direnv when they `cd` into the project.
- Use Python and Python libraries to develop the project unless otherwise specified.
- Write Google-style docstrings for all functions (and for classes and modules where non-trivial).
- **Logging** — follow the **python-logging** skill for anything involving diagnostic output: adding log statements, creating modules, setting up entrypoints, or cleaning up `print()` calls.
- **Versioning** — follow the **python-versioning** skill whenever a change could affect the package version: public API changes, bug fixes, release or pre-release preparation.

## Repository Map

```markdown
.
├── .env
├── .env.example
├── .envrc
├── .gitignore
├── AGENTS.md
├── PLAN.md             **North star** — goal, scope, backlog, done criteria
├── pyproject.toml
├── README.md
├── STATE.md            Current status, active track, next task
├── data/               data and input files
├── docs/               **Implementation tracks** — phased task lists
│   └── AGENT_RULES.md  Operating rules
├── etc/                miscellaneous: misc scripts, scratchpads, extra instructions
├── fixtures/           Test fixtures
├── out/
│   └── logs/           rotating log files
├── scripts/            thin wrappers calling specific modules (IDE run configurations)
├── src/
│   └── <package_name>/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       └── logging.py
└── tests/              Test scripts
```

## Implementation Tracks

As a project grows, `PLAN.md` holds the strategic vision while individual implementation tracks live in `docs/`. This keeps the root plan readable and lets each phase get its own detailed task list.

Tracks are named `docs/NNN-NAME_TRACK.md` with zero-padded, three-digit indices (e.g. `docs/001-SETUP_TRACK.md`). When a track splits into subtracks they use dot notation (e.g. `001.1-...`, `001.2-...`).

### Document Roles

- **`PLAN.md` (root)** — North star. Goal, scope, backlog, and done criteria for the entire project. Read this to understand *what* we're building.
- **`docs/NNN-*_TRACK.md`** — Implementation tracks. Ordered Tasks with acceptance criteria for a specific phase. Read the active one to understand *how* to build the next piece.
- **`STATE.md`** — Pointer. Which track is active, what's the next task, what's done. Read this to know *where* to work next.

The current implementation track is defined in `STATE.md` under "Current Track".

### Working Session (Minimal Context)

To implement a Task, load only these files:

1. `AGENTS.md` — architecture and operating rules
2. `PLAN.md` — scope and status (skim for context)
3. `STATE.md` — current status and next task
4. The active track file (listed in `STATE.md` under "Current Track")

Do not load every track file. Load only the active one.

Before doing work on the current track, read:

1. The active track file (see `STATE.md`)
2. `STATE.md`

### Track Rules

- Implement Tasks in order.
- Do not skip Tasks.
- Do not implement features outside the active track.
- Each Task should change at most 5 files. If more are needed, split the Task.
- Each track file should stay under 300 lines. If a track grows beyond that, break it into multiple track files in the same phase.
- When starting a new phase, create a track file in `docs/`, add it to the track chain in `STATE.md`, and update `PLAN.md` backlog status if needed.

### Post-Task Completion

After implementing a Task, update `STATE.md` to:

1. Mark the completed Task under "Completed Tasks" with a brief summary.
2. Advance "Next Task" to the following Task in the active track.

After updating `STATE.md`:

1. Follow the **python-versioning** skill to increase the `version` in `pyproject.toml` and `__init__.py`, keeping `version` identical in both files.
2. Update `README.md` with the latest installation, configuration, and run commands, including CLI arguments and flags.
3. Commit the changes with a descriptive message.

This ensures a fresh session can resume from the correct task.
