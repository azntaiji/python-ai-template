# 001 - Setup Track

## Read first

`AGENTS.md`, `STATE.md`. Do not read other track files.

## Done when

- [ ] All five Tasks below are marked complete in `STATE.md`
- [ ] `.venv/bin/<package_name>` prints the placeholder CLI message
- [ ] `git log` shows one commit per completed Task
- [ ] No literal placeholder strings remain anywhere in the repository

## Task 1 - Git init and initial commit

**Files:** none (repository state only)

**Steps:**

1. If a `.git` directory already exists, skip `git init` and go to step 3.
2. Run `git init`.
3. Run `git status` and confirm no `.venv/`, `.env`, `out/`, or `*.egg-info/`
   entries appear. If any appear, `.gitignore` is missing or wrong — fix it
   before committing.
4. Run:

```bash
git add -A
git commit -m "Initial commit"
```

**Verify:** `git log --oneline` shows at least one commit.

## Task 2 - Initialize virtual environment and pip

Use `python3` for the system interpreter here (on many systems no bare `python`
command exists); after this Task, always invoke the venv interpreter directly.

**Files:** `.envrc` (created, only if direnv is installed)

**Steps:**

1. Run:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
```

2. Optional, for interactive shell convenience only. If `direnv` is installed
   (check with `command -v direnv`), run:

```bash
echo 'source .venv/bin/activate' > .envrc
direnv allow
```

   If `direnv` is not installed, skip this step entirely — do not install it
   and do not record a Blocker. Agents and scripts never rely on it; they
   invoke `.venv/bin/python` directly.

**Verify:** `.venv/bin/python --version` prints Python 3.11 or newer.

## Task 3 - Project and Package Naming

**Files:** none (this Task only settles names; Task 4 applies them)

Ask the user for:

1. **Project name** — the distribution name used in `pyproject.toml` and typically the
   repository/directory name. May contain hyphens (e.g., `data-pipeline`).
2. **Package name** — the importable package directory under `src/`. Must be a valid
   Python identifier: lowercase, underscores instead of hyphens, no leading digits
   (e.g., `data_pipeline`).

If the user has already stated one or both in the conversation, confirm rather than
re-ask. If they provide only one name, propose the other by normalizing it (hyphens ↔
underscores) and confirm. If no user is available to answer, use the repository
directory name as the project name and derive the package name from it by replacing
hyphens with underscores.

Record both names in `STATE.md` under "Completed Tasks" when marking this Task done.
Do not proceed to Task 4 until both names are settled.

Everywhere in the project, `<project_name>` and `<package_name>` mean these confirmed
values — never leave literal placeholders in generated files.

**Verify:** Both names are recorded in `STATE.md`, and the package name is a valid
Python identifier.

## Task 4 - Rename placeholders

Using the two names confirmed in Task 3:

**Files:** all files containing placeholders, plus the `src/package_name/` directory

**Steps:**

1. Rename the directory `src/package_name/` to `src/<package_name>/`
   (the confirmed package name).
2. In every file in the repository, replace:
   - `<project_name>` and `project_name` → the project name (hyphens allowed)
   - `<package_name>` and `package_name` → the package name (underscores)

**Verify:**

```bash
grep -rn "package_name\|project_name" . --exclude-dir=.venv --exclude-dir=.git
```

must return no matches.

## Task 5 - Install the package

Install the package in editable mode so the CLI alias actually works:

**Files:** none (environment state only)

**Steps:**

```bash
.venv/bin/python -m pip install -e .
```

**Verify:** `.venv/bin/<package_name>` prints the placeholder CLI message and
exits without error.
