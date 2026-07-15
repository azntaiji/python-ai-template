#!/usr/bin/env python3
"""Update STATE.md after a Task finishes. This is the ONLY writer of STATE.md.

Run exactly one of:

    python3 scripts/finish_task.py --result "<one-line result>"   # Verify passed
    python3 scripts/finish_task.py --fail "<one-line reason>"     # Verify failed

--result records the current NEXT TASK as completed, advances NEXT TASK to the
following Task in the current track (rolling to the next file in "Track Chain"
when the track is finished), and resets VERIFY to not-run.

--fail sets VERIFY to fail and records the reason under "Blockers". NEXT TASK
is left unchanged so the next session retries the same Task.

After updating STATE.md, the script also commits all changes with a message
naming the Task — when a .git directory exists (during initial setup it may
not yet; that is fine).

Do not modify this script. Do not edit STATE.md by hand (one exception:
deleting a resolved Blocker line, per docs/ERROR_RECOVERY.md). Do not run
git commit yourself when finishing a Task — this script does it.

Uses only the Python standard library; runs on the system python3 (no venv
required).
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = ROOT / "STATE.md"

ALL_DONE = "(all tracks complete)"

HEADER = (
    "# STATE.md\n"
    "\n"
    "Data only. Updated by `python3 scripts/finish_task.py` — do not edit by hand\n"
    '(see `AGENTS.md`, section "How to finish a Task").\n'
)


class StateError(Exception):
    """Raised when STATE.md or a track file is missing or cannot be parsed."""


def read_key(text: str, key: str) -> str:
    """Return the value of a ``KEY: value`` line in STATE.md.

    Args:
        text: Full STATE.md contents.
        key: The line prefix, e.g. ``"CURRENT TRACK"``.

    Returns:
        The trimmed value after the colon.

    Raises:
        StateError: If no such line exists.
    """
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, re.MULTILINE)
    if not match:
        raise StateError(f'STATE.md has no "{key}:" line.')
    return match.group(1)


def read_section(text: str, heading: str) -> list[str]:
    """Return the non-empty lines of a ``## <heading>...`` section.

    The ``(none)`` placeholder is dropped, so an empty section returns ``[]``.

    Args:
        text: Full STATE.md contents.
        heading: Section heading prefix, e.g. ``"Completed Tasks"``.

    Returns:
        The section's content lines, stripped, in order.

    Raises:
        StateError: If no such section exists.
    """
    match = re.search(
        rf"^## {re.escape(heading)}[^\n]*\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise StateError(f'STATE.md has no "## {heading}" section.')
    lines = [line.strip() for line in match.group(1).splitlines() if line.strip()]
    return [line for line in lines if line != "(none)"]


def track_tasks(track_rel: str) -> list[str]:
    """Return a track file's Task titles (its ``## Task ...`` headings), in order.

    Args:
        track_rel: Track file path relative to the repository root.

    Returns:
        Task titles without the ``## `` prefix, e.g. ``"Task 1 - Git init..."``.

    Raises:
        StateError: If the file is missing or has no Task headings.
    """
    track_path = ROOT / track_rel
    if not track_path.is_file():
        raise StateError(f"Track file not found: {track_rel}")
    titles = re.findall(
        r"^## (Task .+?)\s*$", track_path.read_text(encoding="utf-8"), re.MULTILINE
    )
    if not titles:
        raise StateError(f'No "## Task ..." headings found in {track_rel}')
    return titles


def advance(current_track: str, next_task: str, chain: list[str]) -> tuple[str, str]:
    """Compute the (track, task) pair that follows the just-finished Task.

    Args:
        current_track: Value of the CURRENT TRACK line.
        next_task: Value of the NEXT TASK line (the Task that just finished).
        chain: Track file paths from the Track Chain section, in order.

    Returns:
        The new (CURRENT TRACK, NEXT TASK) values. When the whole chain is
        finished, NEXT TASK is the ALL_DONE marker.

    Raises:
        StateError: If the current Task or track cannot be located.
    """
    tasks = track_tasks(current_track)
    if next_task not in tasks:
        raise StateError(
            f'NEXT TASK "{next_task}" does not match any "## Task" heading in '
            f"{current_track}. Fix the mismatch before finishing."
        )
    index = tasks.index(next_task)
    if index + 1 < len(tasks):
        return current_track, tasks[index + 1]
    if current_track not in chain:
        raise StateError(
            f'CURRENT TRACK "{current_track}" is not listed under "Track Chain".'
        )
    chain_index = chain.index(current_track)
    if chain_index + 1 < len(chain):
        new_track = chain[chain_index + 1]
        return new_track, track_tasks(new_track)[0]
    return current_track, ALL_DONE


def render(
    track: str,
    task: str,
    verify: str,
    completed: list[str],
    blockers: list[str],
    chain_lines: list[str],
) -> str:
    """Build the full new STATE.md contents.

    Args:
        track: New CURRENT TRACK value.
        task: New NEXT TASK value.
        verify: New VERIFY value.
        completed: Completed Tasks lines, newest first.
        blockers: Blockers lines.
        chain_lines: Track Chain lines, verbatim (e.g. ``"1. docs/..."``).

    Returns:
        The complete file text, ending with a newline.
    """

    def section(lines: list[str]) -> str:
        return "\n".join(lines) if lines else "(none)"

    return (
        f"{HEADER}\n"
        f"CURRENT TRACK: {track}\n"
        f"NEXT TASK: {task}\n"
        f"VERIFY: {verify}\n"
        "\n"
        "## Completed Tasks (newest first, one line each)\n"
        "\n"
        f"{section(completed)}\n"
        "\n"
        "## Blockers\n"
        "\n"
        f"{section(blockers)}\n"
        "\n"
        "## Track Chain (execution order)\n"
        "\n"
        f"{section(chain_lines)}\n"
    )


def git_commit(message: str) -> str:
    """Commit all changes with the given message, if a .git directory exists.

    Args:
        message: The commit message (the finished Task's title).

    Returns:
        A one-line description of the outcome, for the printed summary.
        Never raises: git problems are reported in the returned line so a
        failed commit does not undo the STATE.md update.
    """
    if not (ROOT / ".git").is_dir():
        return "no .git yet — commit skipped (the setup track creates it)"

    def run(*args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", "-C", str(ROOT), *args], capture_output=True, text=True
        )

    add = run("add", "-A")
    if add.returncode != 0:
        return f"WARNING: git add failed: {add.stderr.strip()}"
    commit = run("commit", "-m", message)
    if commit.returncode != 0:
        output = (commit.stdout + commit.stderr).strip()
        if "nothing to commit" in output:
            return "nothing new to commit"
        return f"WARNING: git commit failed: {output}"
    rev = run("rev-parse", "--short", "HEAD")
    return f'{rev.stdout.strip()} "{message}"'


def main(argv: list[str] | None = None) -> int:
    """Parse arguments, update STATE.md, and print the outcome.

    Args:
        argv: Command-line arguments (defaults to ``sys.argv[1:]``).

    Returns:
        Process exit code: 0 on success, 1 on error.
    """
    parser = argparse.ArgumentParser(
        description="Update STATE.md after a Task finishes."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--result", metavar="TEXT", help="Verify passed; one-line result of the Task"
    )
    group.add_argument(
        "--fail", metavar="TEXT", help="Verify failed; one-line reason for the failure"
    )
    args = parser.parse_args(argv)

    try:
        if not STATE_PATH.is_file():
            raise StateError("STATE.md not found at the repository root.")
        text = STATE_PATH.read_text(encoding="utf-8")

        current_track = read_key(text, "CURRENT TRACK")
        next_task = read_key(text, "NEXT TASK")
        completed = read_section(text, "Completed Tasks")
        blockers = read_section(text, "Blockers")
        chain_lines = read_section(text, "Track Chain")
        chain = [
            m.group(1)
            for line in chain_lines
            if (m := re.match(r"\d+\.\s*(\S+)", line))
        ]

        if args.fail is not None:
            verify = "fail"
            blockers.append(f"{next_task}: {args.fail}")
            new_track, new_task = current_track, next_task
        else:
            verify = "not-run"
            completed.insert(0, f"{next_task} — {args.result}")
            new_track, new_task = advance(current_track, next_task, chain)

        STATE_PATH.write_text(
            render(new_track, new_task, verify, completed, blockers, chain_lines),
            encoding="utf-8",
        )
    except StateError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        print(
            "STATE.md was NOT updated. Follow docs/ERROR_RECOVERY.md and stop.",
            file=sys.stderr,
        )
        return 1

    commit_message = next_task if args.fail is None else f"{next_task} — Verify failed"
    commit_note = git_commit(commit_message)

    print("STATE.md updated.")
    print(f"  CURRENT TRACK: {new_track}")
    print(f"  NEXT TASK: {new_task}")
    print(f"  VERIFY: {verify}")
    if args.fail is not None:
        print(f"  Blocker recorded: {blockers[-1]}")
    else:
        print(f"  Completed: {completed[0]}")
    print(f"  Commit: {commit_note}")
    if new_task == ALL_DONE:
        print("All tracks in the Track Chain are complete.")
    print("Now print the report lines (AGENTS.md \"How to finish a Task\"), then STOP.")
    print("Do NOT begin the next Task shown above — a fresh session picks it up.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
