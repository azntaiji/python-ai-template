# AGENTS.md

> Read this file before doing any work in the repository.

## Working Session (read in this order, nothing else)

1. `AGENTS.md` — this file: rules and repository map
2. `STATE.md` — current track, next task, completed tasks
3. The active track file named on the `CURRENT TRACK:` line of `STATE.md`

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

## How to finish a Task

When you begin a Task, first edit `STATE.md` to set `STARTED: yes`.

When the Task's work is done, do these steps in order:

1. Run the Task's **Verify** command from the track file.
2. **If Verify failed**: edit `STATE.md` — set `VERIFY: fail` and add one line
   under "Blockers" describing the failure. Do not touch "Completed Tasks".
   Follow `docs/ERROR_RECOVERY.md`. Stop here.
3. **If Verify passed**: rewrite `STATE.md` in ONE call to the write tool.
   Copy the current file, then apply exactly these changes:
   - `NEXT TASK:` → the next Task title in the current track file.
     If the track has no more Tasks, also set `CURRENT TRACK:` to the next
     file in "Track Chain", and `NEXT TASK:` to that track's Task 1 title.
   - `STARTED: no` and `VERIFY: not-run` (ready for the next session).
   - Add the finished Task as the FIRST line under "Completed Tasks",
     as `Task N - title — one-line result`. If the section says `(none)`,
     replace that with the new line.
   - Change nothing else. Keep "Blockers" and "Track Chain" as they were.

   Worked example — finishing Task 1 of a 2-task track:

   ```
   BEFORE                                AFTER
   CURRENT TRACK: docs/001-X_TRACK.md    CURRENT TRACK: docs/001-X_TRACK.md
   NEXT TASK: Task 1 - Git init          NEXT TASK: Task 2 - Init venv
   STARTED: yes                          STARTED: no
   VERIFY: not-run                       VERIFY: not-run
   ## Completed Tasks                    ## Completed Tasks
   (none)                                Task 1 - Git init — repo initialized
   ```

4. If the Task changed files under `src/` or `tests/`: bump `version` in
   `pyproject.toml` AND `__version__` in `src/<package_name>/__init__.py`
   per `docs/VERSIONING_RULES.md` (the two must be identical). Otherwise skip.
5. If installation, configuration, or run commands changed: update `README.md`.
   Otherwise skip.
6. If a `.git` directory exists: commit all changes with a message naming the
   Task. Otherwise skip (the setup track creates it).
7. Print this report with each `<...>` filled in, then stop:

   - Verify: <pass | fail>
   - STATE.md rewritten: <yes>
   - Version: <new number | no bump needed>
   - README: <updated | no change needed>
   - Commit: <message | no .git yet>