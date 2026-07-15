# Pi-specific Resume Prompt (every session after kickoff)

Paste everything below the line as the prompt, unchanged, at the start of each working session. `STATE.md` tells the agent where to pick up; nothing project-specific goes in this prompt.

---

You have four tools: read, write, edit, bash. Every action you take MUST use one of these tools. Do not output raw file contents — use write or edit. Do not describe shell commands — use bash to run them.

Read `AGENTS.md` and `STATE.md`. Do not read `PLAN.md` or any other track file — everything you need for the Task is in the one track file named below.

Open the track file named under "Current Track" in `STATE.md`. Execute the one Task named under "Next Task", exactly as written in that track file. Do exactly ONE Task only — do not begin the next Task even if you have context left.

When the Task's work is done, do the **"HOW TO FINISH A TASK"** block at the top of `STATE.md`, in order — run Verify, move the finished Task, advance "Next Task", bump the version / update `README.md` / commit if required.

Then, before you stop, output this checklist verbatim with every box filled:

- [ ] Verify command was run; result recorded in STATE.md "Task Status"
- [ ] Finished task moved to top of "Completed Tasks"
- [ ] "Next Task" advanced (or track rolled to next in chain)
- [ ] Version bumped if src/ or tests/ changed (else: N/A)
- [ ] README updated if run/config/install changed (else: N/A)
- [ ] Committed with a message naming the task (or: no .git yet)

If any box is unchecked, you are not done — go back and finish it. Then report files changed, Verify result, and open issues, and stop. Do NOT begin the next Task. A fresh session will pick it up.
