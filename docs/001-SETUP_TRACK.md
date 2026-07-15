# 001 - Setup Track

## Read first (use the read tool)

1. read `AGENTS.md`
2. read `STATE.md`
3. read the track file named on the `CURRENT TRACK:` line of `STATE.md`

Do not read other track files.

## Done when

- [ ] All five Tasks below are marked complete in `STATE.md`
- [ ] `.venv/bin/<package_name>` prints the placeholder CLI message
- [ ] `git log` shows at least one commit per completed Task
- [ ] No literal placeholder strings remain outside `docs/001-SETUP_TRACK.md` (this file keeps its generic wording — see Task 4)

## Task 1 - Git init and initial commit

**Files:** none (repository state only)

**Steps:**

1. If a `.git` directory already exists, skip `git init` and go to step 3.
2. Run `git init`.
3. Run `git status` and confirm no `.venv/`, `.env`, `out/`, or `*.egg-info/` entries appear. If any appear, `.gitignore` is missing or wrong — fix it before committing.
4. Run:

```bash
git add -A
git commit -m "Initial commit"
```

If `git commit` reports "nothing to commit", the initial commit already exists from an interrupted session — this is not an error; go to Verify.

**Verify:** run

```bash
git log --oneline
```

Expected: Prints at least one commit.

## Task 2 - Initialize virtual environment and pip

Use `python3` for the system interpreter here (on many systems no bare `python` command exists); after this Task, always invoke the venv interpreter directly.

**Files:** `.envrc` (created, only if direnv is installed)

**Steps:**

1. Run:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
```

2. Optional, for interactive shell convenience only. If `direnv` is installed (check with `command -v direnv`), run:

```bash
echo 'source .venv/bin/activate' > .envrc
direnv allow
```

If `direnv` is not installed, skip this step entirely — do not install it and do not record a Blocker. Agents and scripts never rely on it; they invoke `.venv/bin/python` directly.

**Verify:** run

```bash
.venv/bin/python --version
```

Expected: Prints Python 3.11 or newer.

## Task 3 - Project and Package Naming

**Files:** `PLAN.md`

**Steps:**

1. If the Architecture section of `PLAN.md` (at the repository root, NOT `docs/PLAN.md`) contains a `Names:` line, use those two names and skip to step 2. Otherwise ask the user for:

- **Project name** — the distribution name used in `pyproject.toml` and typically the repository/directory name. May contain hyphens (e.g., `data-pipeline`).
- **Package name** — the importable package directory under `src/`. Must be a valid Python identifier: lowercase, underscores instead of hyphens, no leading digits (e.g., `data_pipeline`).

If the user has already stated one or both in the conversation, confirm rather than re-ask. If they provide only one name, propose the other by normalizing it (hyphens ↔ underscores) and confirm. If no user is available to answer, use the repository directory name as the project name and derive the package name from it by replacing hyphens with underscores.

2. If the Architecture section of `PLAN.md` does not already contain the `Names:` line, add it now with the edit tool, on its own bullet (e.g., `- Names: project=data-pipeline, package=data_pipeline (decided 2026-07-15)`). Do not proceed to Task 4 until both names are settled.

Everywhere in the project, `<project_name>` and `<package_name>` mean these confirmed values — never leave literal placeholders in generated files.

**Verify:** run

```bash
grep -n "Names:" PLAN.md
```

Expected: Prints one line containing both names, and the package name is a valid Python identifier (lowercase, underscores, no leading digits).

When finishing this Task, use the result line `names settled: project=<project name>, package=<package name>` so the names are also recorded in `STATE.md`.

## Task 4 - Rename placeholders

Using the two names confirmed in Task 3:

**Files:** `src/package_name/` (directory rename), `pyproject.toml`, `README.md`, `AGENTS.md`, `PLAN.md`, `src/<package_name>/__init__.py`, `src/<package_name>/cli.py`, `src/<package_name>/config.py`, `src/<package_name>/logging_config.py`

**Steps:**

1. Rename the directory: run `mv src/package_name/ src/<package_name>/` (the confirmed package name).
2. In each of the following files, edit to replace every occurrence of `project_name` → the confirmed project name, and every occurrence of `package_name` → the confirmed package name: `pyproject.toml`, `README.md`, `AGENTS.md`, `PLAN.md`, and all `.py` files under `src/<package_name>/`. Use the edit tool with replace-all for each file. Do not touch `STATE.md` or `scripts/finish_task.py` — they contain no placeholders.

Do NOT rename placeholders in `docs/` rule files (`LOGGING_RULES.md`, `VERSIONING_RULES.md`, `REFERENCE.md`), `.env.example`, or the track template at `docs/000-TRACK_TEMPLATE.md` — those use <package_name> as a generic documentation convention.

**Verify:** run

```bash
grep -rn "package_name\|project_name" \
  src/ tests/ scripts/ pyproject.toml PLAN.md README.md STATE.md AGENTS.md
```

Expected: 0 matches.

## Task 5 - Install the package

Install the package in editable mode so the CLI alias actually works:

**Files:** none (environment state only)

**Steps:**

```bash
.venv/bin/python -m pip install -e .
```

**Verify:** run

```bash
.venv/bin/<package_name>
```

Expected: Prints the placeholder CLI message and exits with status 0.
