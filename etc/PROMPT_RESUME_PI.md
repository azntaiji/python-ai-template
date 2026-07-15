# Pi-specific Resume Prompt (every session after kickoff)

Use this prompt when you are using the Pi coding agent harness specifically. Paste everything below the line as the prompt, unchanged, at the start of each working session. `STATE.md` tells the agent where to pick up; nothing project-specific goes in this prompt.

---

You have four tools: read, write, edit, bash. Every action you take MUST use one of these tools. Do not output raw file contents — use write or edit. Do not describe shell commands — use bash to run them.

Read `AGENTS.md` and `STATE.md`. Do not read `PLAN.md` or any other track file — everything you need for the Task is in the one track file named below.

Open the track file named on the `CURRENT TRACK:` line of `STATE.md`. Execute the one Task named on the `NEXT TASK:` line, exactly as written in that track file. Do exactly ONE Task only — do not begin the next Task even if you have context left.

When the Task's work is done, follow the **"How to finish a Task"** section of `AGENTS.md`, in order — run Verify, rewrite `STATE.md` in one call to the write tool, then bump the version / update `README.md` / commit if required.

Then, before you stop, print this report with each `<...>` filled in:

- Verify: <pass | fail>
- STATE.md rewritten: <yes>
- Version: <new number | no bump needed>
- README: <updated | no change needed>
- Commit: <message | no .git yet>

Then report files changed and open issues, and stop. Do NOT begin the next Task. A fresh session will pick it up.
