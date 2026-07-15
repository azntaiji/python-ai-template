# Session 0 (alternative) — Frontier Planning Prompt

Use this INSTEAD of `PROMPT_0_KICKOFF.md` when you have a frontier model
(large context, full repository access) do the planning. It fills in
`PLAN.md` AND writes the implementation track files that local models will
later execute.

Replace EVERY angle-bracket value below, then paste everything below the
line as the prompt.

Afterwards, no separate local kickoff is needed: start the local model with
`PROMPT_RESUME.md` — `STATE.md` already points at Task 1 of the setup track.

---

You are a frontier model planning a Python project in this repository. The
plans you write will be EXECUTED by local LLMs with small context windows
(8k–32k tokens), one Task per session, with no memory between sessions.
Everything an executor needs must be written down explicitly.

Read first, in order: `AGENTS.md`, `PLAN.md`, `STATE.md`,
`docs/000-TRACK_TEMPLATE.md`, `docs/001-SETUP_TRACK.md`.

Project context:

- Goal: <one or two sentences: what this project delivers>
- In scope: <bullet list>
- Out of scope: <bullet list>
- Names line for PLAN.md (copy verbatim into the Architecture section):

      - Names: project=<project-name-with-hyphens>, package=<package_name_with_underscores> (decided <today's date>)

- Additional context: <constraints, data sources, APIs, preferences — or "none">

Do these three jobs, then stop:

## Job 1 — Fill in PLAN.md

Replace every `—` placeholder: Goal, Scope (in/out), Done Criteria. In the Architecture section, add the Names line verbatim, plus one bullet per
material architecture decision you are making in Job 2 (decision, reason, date). In the Backlog, keep item 1 (setup) as is, then list the remaining phases in build order — one line each, matching the tracks you create below.

## Job 2 — Write the implementation tracks

For each backlog phase after setup, create `docs/NNN-NAME_TRACK.md` (002, 003, ...) from `docs/000-TRACK_TEMPLATE.md`. Do NOT modify `docs/001-SETUP_TRACK.md`.

Authoring rules — these exist because the executor is a small model:

- Follow the template structure exactly: Read first / Done when / Tasks, each Task with **Files:**, **Steps:**, **Verify:**.
- Each Task changes at most 5 files. Each Step is one command or one edit, imperative, with exact paths — no "as appropriate", no "etc."
- **Step verbs must map to tool calls.** The executor has four tools: `read`, `write`, `edit`, `bash`. Use exactly one of these verbs per step:
  - **Create** `path` with: → `write` tool (new file, full contents follow)
  - **Write (overwrite)** `path`: → `write` tool (replace entire existing file)
  - **Edit** `path`: → `edit` tool (partial change; provide old/new blocks — see below)
  - **Run:** → `bash` tool (fenced ```bash``` block follows)
  - **Rename** `old` → `new` → `bash` tool (mv command)
- **Edit steps must provide anchored old/new blocks.** The `edit` tool works by exact string matching. Never say "replace the X section with" or "add Y at the end" — always provide the literal old text and the literal new text. Format:

      Edit `path`:

      old:
      ```
      exact current text to find
      ```

      new:
      ```
      replacement text
      ```

  If the step creates a new file from scratch, use **Create** (the `write` tool), not **Edit**. If the step replaces an entire file, use **Write (overwrite)**, not **Edit**.
- Every **Verify:** is an exact shell command plus the expected output. The executor runs it literally.
- Each track must be self-contained: restate any fact the executor needs (file locations, function signatures from earlier tracks, env variables) instead of assuming it is remembered. When naming `PLAN.md` or `STATE.md`, say they are at the repository root — only tracks and rule files live in `docs/`. The executor reads only `AGENTS.md`, `PLAN.md`, `STATE.md`, and the one active track file.
- Use the real confirmed project and package names everywhere — never literal `<package_name>`-style placeholders.
- Keep **each track under 150 lines**; split into `NNN.1-`, `NNN.2-` subtracks if a phase needs more.
- Order Tasks so every Task builds only on already-completed Tasks, and the first Task of each track builds only on the previous track's "Done when" state.

## Job 3 — Update STATE.md and the Backlog

- In `STATE.md`, list every track under "Track Chain" in execution order. Leave `CURRENT TRACK:` as `docs/001-SETUP_TRACK.md` and `NEXT TASK:` as Task 1 — do not start any Task.
- In `PLAN.md`'s Backlog, mark each item whose track file now exists as `[~]` and reference its file.

Do not modify `AGENTS.md`, `docs/001-SETUP_TRACK.md`, the rule files, `scripts/finish_task.py`, or anything under `src/`. Do not execute any Task.

Finally, report: the backlog phases you chose, the track files you created with a one-line summary each, and any open questions — then stop.
