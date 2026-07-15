# When a step fails

1. Re-read the failing command's error output. Do not retry unchanged more than once.
2. If a command is not found (e.g. `direnv`, `git`, `python3`): run `python3 scripts/finish_task.py --fail "missing tool: <name>"` and stop. Do not substitute a different tool.
3. If a file referenced by the track does not exist: run `python3 scripts/finish_task.py --fail "missing file: <path>"` and stop. Do not create the file by guessing its content.
4. If a Verify step's output differs from what the track specifies: the Task is NOT complete. Do not mark it complete. Fix the cause or record a Blocker.
5. Never add a Task to "Completed Tasks" in `STATE.md` without running its Verify step.
6. When a Blocker is resolved, delete its line from "Blockers" in `STATE.md` and resume at the Task that was interrupted. (This is the one permitted hand edit of `STATE.md`; everything else goes through `scripts/finish_task.py`.)
