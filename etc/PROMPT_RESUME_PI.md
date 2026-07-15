# Pi-specific Resume Prompt (every session after kickoff)

Use this prompt when you are using the Pi coding agent harness specifically. Paste everything below the line as the prompt, unchanged, at the start of each working session. `STATE.md` tells the agent where to pick up; nothing project-specific goes in this prompt.

---

You have four tools: read, write, edit, bash. Every action you take MUST use one of these tools. Do not output raw file contents — use write or edit. Do not describe shell commands — use bash to run them.

Read `AGENTS.md` and `STATE.md`. Do not read `PLAN.md` (a separate planning file at the repository root) and do not read any track file except the one named below — everything you need for the Task is in that one file.

Open the track file named on the `CURRENT TRACK:` line of `STATE.md`. Then:

1. Execute the one Task named on the `NEXT TASK:` line, exactly as written in that track file. Do exactly ONE Task only — do not begin the next Task even if you have context left.
2. When the Task's work is done, follow the **"How to finish a Task"** section of `AGENTS.md`, in order — run Verify, bump the version / update `README.md` if required, then run `python3 scripts/finish_task.py` (it updates `STATE.md` AND makes the git commit; never edit `STATE.md` or run `git commit` yourself).
3. Before you stop, print exactly these five lines with each `<...>` filled in — no extra text before or after. Copy the Commit value from the `Commit:` line the script printed:

- Verify: <pass | fail>
- STATE.md updated: <yes>
- Version: <new number | no bump needed>
- README: <updated | no change needed>
- Commit: <the script's Commit line>

Then stop. Do NOT begin the next Task. A fresh session will pick it up.
