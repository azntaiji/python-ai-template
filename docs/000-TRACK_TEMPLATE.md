# NNN - <Track Name>

<!-- Copy this file to docs/NNN-NAME_TRACK.md when starting a new phase.
     Fill every section. Delete these comments. Keep the file under 150 lines. -->

## Read first (use the read tool)

1. read `AGENTS.md`
2. read `STATE.md`
3. read the track file named on the `CURRENT TRACK:` line of `STATE.md`

Do not read other track files.

## Done when

- [ ] <observable end state, e.g. "`.venv/bin/pytest` passes with N tests">
- [ ] All Tasks below are marked complete in `STATE.md`
- [ ] `STATE.md` points to the next track in the Track Chain

## Task 1 - <imperative title>

**Files:** <the files this Task changes — 5 at most>

**Steps:**

<!-- Use exactly one of these verbs per step so the agent knows which tool to call:

  Create `path` with:         → write tool (new file, full contents follow)
  Write (overwrite) `path`:   → write tool (replace entire existing file)
  Edit `path`:                → edit tool (partial change; provide old/new blocks)
  Run:                        → bash tool (fenced ```bash``` block follows)
  Rename `old` → `new`        → bash tool (mv command)

  For Edit steps, always provide anchored old/new blocks:

    Edit `pyproject.toml`:

    old:
    ```
    exact text to find
    ```

    new:
    ```
    replacement text
    ```
-->

1. <one command or one edit per step>
2. <...>

**Verify:** run

<exact command to run as a single fenced code block>

Expected: <a literal expected-output line>

## Task 2 - <imperative title>

**Files:** <...>

**Steps:**

1. <...>

**Verify:** run

<...>

Expected: <...>
