# 001 - Setup Track

## Task 1 - Initialize Virtual environment, direnv, pip

Use `python3` for the system interpreter here (on many systems no bare `python`
command exists); after this Task, always invoke the venv interpreter directly. Run:

```bash
python3 -m venv .venv
echo 'source .venv/bin/activate' > .envrc
direnv allow
.venv/bin/python -m pip install --upgrade pip
```

## Task 2 - Project and Package Naming

Ask the user for:

1. **Project name** — the distribution name used in `pyproject.toml` and typically the
   repository/directory name. May contain hyphens (e.g., `data-pipeline`).
2. **Package name** — the importable package directory under `src/`. Must be a valid
   Python identifier: lowercase, underscores instead of hyphens, no leading digits
   (e.g., `data_pipeline`).

If the user has already stated one or both in the conversation, confirm rather than
re-ask. If they provide only one name, propose the other by normalizing it (hyphens ↔
underscores) and confirm. Do not proceed to Task 2 until both names are settled.

Everywhere in the project, `<project_name>` and `<package_name>` mean these confirmed values —
never leave literal placeholders in generated files.

## Task 3 - Rename placeholders

Replace all `<project_name>`, `<package_name>`, `project_name`, and `package_name` placeholders throughout the repository with the normalized name from Task 2.

## Task 4 - Install the package

Install the package in editable mode so the CLI alias actually works:

```bash
.venv/bin/python -m pip install -e .
```

Verify with `.venv/bin/<package_name>` (should print the placeholder message).

## Task 5 - Git init and initial commit

Run:

```bash
git init
git add -A
git commit -m "Initial commit"
```

Before committing, confirm `git status` shows no `.venv/`, `.env`, `out/`, or
`*.egg-info/` entries — if any appear, `.gitignore` is missing or
wrong; fix it before committing.
