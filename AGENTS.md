# AGENTS.md

> Read this file before doing any work in the repository.

## Working Session (read in this order, nothing else)

1. `AGENTS.md` — this file: rules and repository map
2. `PLAN.md` — goal and scope (skim)
3. `STATE.md` — current track, next task, post-task checklist
4. The active track file named in `STATE.md` under "Current Track"

Do not load other track files. Load the rule files in `docs/` only when their
topic comes up (see Conventions below).

## Conventions

These apply to all work in this repository, at all times:

- Use `python3` for the system interpreter and always invoke the venv interpreter directly (`.venv/bin/python`, `.venv/bin/python -m pip`) rather than relying on shell activation, since activation does not persist across separate command invocations. (Interactive users who have direnv installed get activation automatically when they `cd` into the project; agents must never depend on this.)
- Use Python and Python libraries to develop the project unless otherwise specified.
- Write Google-style docstrings for all functions (and for classes and modules where non-trivial).
- **Logging** — before adding any diagnostic output, read `docs/LOGGING_RULES.md` and follow it.
- **Versioning** — before changing the package version, read `docs/VERSIONING_RULES.md` and follow it.
- **Errors** — when a command or verification fails, follow `docs/ERROR_RECOVERY.md`.

## Repository Map

```markdown
.
├── .env                Local secrets (not committed; copy from .env.example)
├── .env.example
├── .envrc              Optional; created by the setup track (Task 2) if direnv is installed
├── .gitignore
├── AGENTS.md
├── PLAN.md             **North star** — goal, scope, architecture, backlog, done criteria
├── pyproject.toml
├── README.md
├── STATE.md            Current track, next task, post-task checklist
├── data/               Data and input files
├── docs/               **Implementation tracks** and rule files
│   ├── 000-TRACK_TEMPLATE.md   Template for new track files
│   ├── 001-SETUP_TRACK.md
│   ├── ERROR_RECOVERY.md
│   ├── LOGGING_RULES.md
│   └── VERSIONING_RULES.md
├── etc/                Miscellaneous: misc scripts, scratchpads, extra instructions
├── fixtures/           Test fixtures
├── out/
│   └── logs/           Rotating log files (created at runtime; not committed)
├── scripts/            Thin wrappers calling specific modules (IDE run configurations)
├── src/
│   └── <package_name>/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       └── logging_config.py
└── tests/              Test scripts
```

## Implementation Tracks

`PLAN.md` holds the strategic vision while individual implementation tracks live in `docs/`. This keeps the root plan readable and lets each phase get its own detailed task list.

Tracks are named `docs/NNN-NAME_TRACK.md` with zero-padded, three-digit indices (e.g. `docs/001-SETUP_TRACK.md`). When a track splits into subtracks they use dot notation (e.g. `001.1-...`, `001.2-...`).

### Document Roles

- **`PLAN.md` (root)** — North star. Goal, scope, architecture decisions, backlog, and done criteria for the entire project. Read this to understand *what* we're building.
- **`docs/NNN-*_TRACK.md`** — Implementation tracks. Ordered Tasks with acceptance criteria for a specific phase. Read the active one to understand *how* to build the next piece.
- **`STATE.md`** — Pointer. Which track is active, what's the next task, what's done. Read this to know *where* to work next.

### Track Rules

- Implement Tasks in order. Do not skip Tasks.
- Do not implement features outside the active track.
- Each Task should change at most 5 files. If more are needed, split the Task.
- Each track file should stay under 300 lines. If a track grows beyond that, break it into multiple track files in the same phase.
- Create new track files from `docs/000-TRACK_TEMPLATE.md`. When starting a new phase: create the track file in `docs/`, add it to "Track Chain" in `STATE.md`, and update the `PLAN.md` backlog status if needed.

## Operating Rules

- Work on one bounded Task at a time. Change only the files the Task names.
- Do not redesign the system unless the Task requires it.
- For each Task: restate it, name the files to change, name the Verify step, make the smallest change that passes, stop.
- Keep source files under 400 lines. If a file grows beyond that, split it.
- Use explicit types where possible.
- For Tasks that change package code, write or update tests before implementation. Setup, configuration, and documentation Tasks need no tests.
- Durable context lives in repository files, not chat history. When implementation diverges from the docs, update the docs immediately. Record material architecture decisions in the "Architecture" section of `PLAN.md` before moving on, and read that section before designing new components.
- Ask before destructive actions, broad refactors, adding dependencies, or changing public contracts. Shell commands listed in the active track file are pre-authorized.
- After each Task, report: files changed, tests added/updated, Verify result, open issues.

## Post-Task Completion

After implementing a Task, complete the checklist at the bottom of `STATE.md`
("After finishing a Task"). This ensures a fresh session can resume from the
correct task.
