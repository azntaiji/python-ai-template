# REFERENCE.md

## Repository Map

```markdown
.
├── .env                Local secrets (not committed; copy from .env.example)
├── .env.example
├── .envrc              Optional; created by setup Task 2 if direnv is installed (not committed)
├── .gitignore
├── AGENTS.md
├── PLAN.md             **North star** — goal, scope, architecture, backlog, done criteria
├── pyproject.toml
├── README.md
├── STATE.md            Current track, next task, post-task checklist
├── data/               Data and input files
├── docs/               **Implementation tracks** and rule files
│   ├── 000-TRACK_TEMPLATE.md   Template for new track files
│   ├── 001-SETUP_TRACK.md
│   ├── ERROR_RECOVERY.md
│   ├── LOGGING_RULES.md
│   ├── REFERENCE.md
│   └── VERSIONING_RULES.md
├── etc/                Miscellaneous: misc scripts, scratchpads, extra instructions
│   ├── PROMPT_0_FRONTIER.md
│   ├── PROMPT_0_KICKOFF.md
│   └── PROMPT_RESUME.md
├── fixtures/           Test fixtures
├── out/
│   └── logs/           Rotating log files (created at runtime; not committed)
├── scripts/            Thin wrappers calling specific modules (IDE run configurations)
├── src/
│   └── <package_name>/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       └── logging_config.py
└── tests/              Test scripts
```

## Implementation Tracks

`PLAN.md` holds the strategic vision while individual implementation tracks live in `docs/`. This keeps the root plan readable and lets each phase get its own detailed task list.

Tracks are named `docs/NNN-NAME_TRACK.md` with zero-padded, three-digit indices (e.g. `docs/001-SETUP_TRACK.md`). When a track splits into subtracks they use dot notation (e.g. `001.1-...`, `001.2-...`).

### Document Roles

- **`PLAN.md` (root)** — North star. Goal, scope, architecture decisions, backlog, and done criteria for the entire project. Read this to understand *what* we're building.
- **`docs/NNN-*_TRACK.md`** — Implementation tracks. Ordered Tasks with acceptance criteria for a specific phase. Read the active one to understand *how* to build the next piece.
- **`STATE.md`** — Pointer. Which track is active, what's the next task, what's done. Read this to know *where* to work next.
