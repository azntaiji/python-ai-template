# AGENTS.md

> Read this file before doing any work in the repository.

## Working Session (read in this order, nothing else)

1. `AGENTS.md` — this file: rules and repository map
2. `STATE.md` — current track, next task, post-task checklist
3. The active track file named in `STATE.md` under "Current Track"

Do not load other track files. Load the rule files in `docs/` only when their topic comes up (see Conventions below).

Repository map, document roles, and track mechanics live in `docs/REFERENCE.md`. You do not need it for normal Task execution — the active track file names every path you need. Open it only if you're lost about where something lives.

Skim `PLAN.md` only when designing new components or making architecture decisions.

## Tools

You have four tools. Map every instruction to one of these:

| Verb in tracks       | Tool   |
|----------------------|--------|
| "Read …"             | read   |
| "Create file … with" | write  |
| "In file …, replace" | edit   |
| fenced ```bash```    | bash   |

If a step doesn't map to one of these, stop and report a Blocker.

## Conventions

These apply to all work in this repository, at all times:

- Use `python3` for the system interpreter and always invoke the venv interpreter directly (`.venv/bin/python`, `.venv/bin/python -m pip`) rather than relying on shell activation, since activation does not persist across separate command invocations. (Interactive users who have direnv installed get activation automatically when they `cd` into the project; agents must never depend on this.)
- Use Python and Python libraries to develop the project unless otherwise specified.
- Write Google-style docstrings for all functions (and for classes and modules where non-trivial).
- **Logging** — before adding any diagnostic output, read `docs/LOGGING_RULES.md` and follow it.
- **Versioning** — before changing the package version, read `docs/VERSIONING_RULES.md` and follow it.
- **Errors** — when a command or verification fails, follow `docs/ERROR_RECOVERY.md`.

### Track Rules

- Implement Tasks in order. Do not skip Tasks.
- Do not implement features outside the active track.
- Each Task should change at most 5 files. If more are needed, split the Task.
- Each track file should stay under 150 lines. If a track grows beyond that, break it into multiple track files in the same phase.
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

After implementing a Task, follow the "HOW TO FINISH A TASK" block at the top of `STATE.md`. This ensures a fresh session can resume from the correct task.