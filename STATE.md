# STATE.md

<!-- The agent edits ONLY the lines marked EDIT and the two lists (Completed
     Tasks, Blockers). Do not reword anything else. Do not add freeform notes
     anywhere in this file. -->

## HOW TO FINISH A TASK (do this before you stop — no exceptions)

You are NOT done until this whole block is done. Do them in order:

1. Run the Task's **Verify** command from the track file. Set `VERIFY:` under "Task Status" to `pass` or `fail`.
2. If `VERIFY: fail` → STOP. Add a line under "Blockers". Do NOT touch "Completed Tasks". See docs/ERROR_RECOVERY.md.
3. If `VERIFY: pass`:
   a. Cut the line under "Next Task". Paste it at the TOP of "Completed Tasks", appending " — <one-line result>".
   b. Set "Next Task" to the next Task title in the current track file. If the track has no more Tasks, set "Current Track" to the next file in "Track Chain" and "Next Task" to its "Task 1 - ..." title.
   c. Reset "Task Status": set `STARTED: no` and `VERIFY: not-run`.
4. If the Task changed files under `src/` or `tests/`, bump `version` in `pyproject.toml` AND `__version__` in `src/<package_name>/__init__.py` per docs/VERSIONING_RULES.md (the two must be identical). Setup, docs, and configuration Tasks do NOT bump.
5. Update `README.md` if installation, configuration, or run commands changed.
6. If a `.git` directory exists, commit all changes with a message naming the Task. If it does not exist yet, skip this (the setup track creates it).
7. Print the completion checklist (below) with every box filled, then STOP.

### Completion checklist — print this verbatim with each box checked

- [ ] Verify command was run; result recorded in "Task Status"
- [ ] Finished task moved to top of "Completed Tasks"
- [ ] "Next Task" advanced (or track rolled to next in chain)
- [ ] Version bumped if src/ or tests/ changed (else: N/A)
- [ ] README updated if run/config/install changed (else: N/A)
- [ ] Committed with a message naming the task (or: no .git yet)

If any box is unchecked, you are not done — go back and finish it.

## Current Track

docs/001-SETUP_TRACK.md          <!-- EDIT: track file path -->

## Next Task

Task 1 - Git init and initial commit   <!-- EDIT: exact task title from the track file -->

## Task Status

STARTED: no       <!-- EDIT: flip to "yes" the moment you begin the Task -->
VERIFY: not-run   <!-- EDIT: "pass" or "fail" after running the Verify step -->

## Completed Tasks

<!-- Newest at the top. One line each: "Task N - title — one-line result" -->
(none)

## Blockers

(none)

## Track Chain

1. docs/001-SETUP_TRACK.md  ← active
