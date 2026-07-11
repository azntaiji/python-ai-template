# Agent Rules (AGENT_RULES.md)

## Scope

- Work on one bounded task at a time. Change only the files named in the task.
- Do not redesign the system unless the task requires it.

## Task Process

1. Restate the task.
2. Name the files to change.
3. Name the acceptance test.
4. Make the smallest change that can pass the test.
5. Stop.

## Coding

- Keep modules small. No god modules.
- Aim for source files under 400 lines. If a file grows beyond that, split it.
- Use explicit types where possible.

## Testing

- Write or update tests before implementation.

## Context Control

- Use repo files for durable context. Do not rely on long chat history.
- Summarize progress into `STATE.md` after each task.
- When implementation diverges from docs, update the docs immediately.
- Record material architecture decisions in `PLAN.md` before moving on.

## Safety

- Ask before destructive actions, broad refactors, adding dependencies, or changing public contracts.
- Ask before networked or shell actions if not already authorized.

## Output

For each completed task, report: files changed, tests added/updated, acceptance result, open issues, next suggested task.
