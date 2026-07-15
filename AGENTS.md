# AGENTS.md

> Read this file before doing any work in the repository.

## Working Session (read in this order, nothing else)

1. `AGENTS.md` — this file: rules and repository map
2. `STATE.md` — current track, next task, completed tasks
3. The active track file named on the `CURRENT TRACK:` line of `STATE.md`

Do not load other track files. Load the rule files in `docs/` only when their topic comes up (see Conventions below).

Repository map, document roles, and track mechanics live in `docs/REFERENCE.md`. You do not need it for normal Task execution — the active track file names every path you need. Open it only if you're lost about where something lives.

Skim `PLAN.md` (at the repository root, next to this file — not in `docs/`) only when designing new components or making architecture decisions.

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
- Never reason from memory about what a file contains — read it again with the read tool. Do not run commands or open files that no step asks for.
- Repository history from earlier sessions is normal. Do not investigate commits, branches, or remotes beyond what a step explicitly asks.
- Do each step once. If the outcome is correct but the wording could be better, do NOT redo it — imperfect phrasing is acceptable; move on.
- Read an instruction file at most once per session. After that, act on it instead of re-checking it.
- Do not redesign the system unless the Task requires it.
- For each Task: restate it, name the files to change, name the Verify step, make the smallest change that passes, stop.
- Keep source files under 400 lines. If a file grows beyond that, split it.
- Use explicit types where possible.
- For Tasks that change package code, write or update tests before implementation. Setup, configuration, and documentation Tasks need no tests.
- Durable context lives in repository files, not chat history. When implementation diverges from the docs, update the docs immediately. Record material architecture decisions in the "Architecture" section of `PLAN.md` (repository root) before moving on, and read that section before designing new components.
- Ask before destructive actions, broad refactors, adding dependencies, or changing public contracts. Shell commands listed in the active track file are pre-authorized.
- After each Task, report: files changed, tests added/updated, Verify result, open issues.

## How to finish a Task

When the Task's work is done, do these steps in order:

1. Run the Task's **Verify** command from the track file.
2. **If Verify failed**, run:

   ```bash
   python3 scripts/finish_task.py --fail "<one line describing the failure>"
   ```

   Then follow `docs/ERROR_RECOVERY.md`. Stop here.
3. **If Verify passed** and the Task changed files under `src/` or `tests/`:
   bump `version` in `pyproject.toml` AND `__version__` in
   `src/<package_name>/__init__.py` per `docs/VERSIONING_RULES.md` (the two
   must be identical). Otherwise skip.
4. If installation, configuration, or run commands changed: update `README.md`.
   Otherwise skip.
5. Run:

   ```bash
   python3 scripts/finish_task.py --result "<one line describing what the Task produced>"
   ```

   The script updates `STATE.md` for you (records the finished Task,
   advances `NEXT TASK:`, rolls to the next track in "Track Chain" when the
   current one is done) AND makes the git commit for the Task. Never edit
   `STATE.md`, run `git commit`, or modify `scripts/finish_task.py`
   yourself. If the script prints an error, follow `docs/ERROR_RECOVERY.md`
   and stop.

6. Print exactly these five lines with each `<...>` filled in — no extra text before or after — then stop. Copy the Commit value from the `Commit:` line the script printed:

   - Verify: <pass | fail>
   - STATE.md updated: <yes>
   - Version: <new number | no bump needed>
   - README: <updated | no change needed>
   - Commit: <the script's Commit line>