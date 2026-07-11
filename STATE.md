# STATE.md

## Current Track

docs/001-SETUP_TRACK.md

## Next Task

Task 1 - Git init and initial commit

## Completed Tasks

(none)

## Blockers

(none)

## Track Chain

1. docs/001-SETUP_TRACK.md  ← active
2. (add the next track here when created)

## After finishing a Task (do all of these, in order)

1. Run the Task's Verify step. If it fails, the Task is NOT complete — see
   docs/ERROR_RECOVERY.md.
2. Move the finished Task to "Completed Tasks" above, with a one-line summary.
3. Set "Next Task" to the next Task in the Current Track file. If none remain,
   set "Current Track" to the next file in "Track Chain" and "Next Task" to its
   Task 1.
4. Bump `version` in `pyproject.toml` AND `__version__` in
   `src/<package_name>/__init__.py` per docs/VERSIONING_RULES.md. The two values
   must be identical.
5. Update `README.md` if installation, configuration, or run commands changed.
6. If a `.git` directory exists, commit all changes with a message naming the
   Task. If it does not exist yet, skip this step (the setup track creates it).
