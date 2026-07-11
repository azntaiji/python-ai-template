# Versioning Rules

This project follows Semantic Versioning 2.0.0, expressed in PEP 440-compatible
form so Python build tools accept the version strings verbatim.

## Where the version lives

Exactly two places, and they must always match:

1. `pyproject.toml` — the `[project].version` field
2. `src/<package_name>/__init__.py` — the `__version__` attribute

Update both in the same change, then verify they match:

```bash
.venv/bin/python - << 'EOF'
import pathlib, re, tomllib

v1 = tomllib.load(open("pyproject.toml", "rb"))["project"]["version"]
text = pathlib.Path("src/<package_name>/__init__.py").read_text()
v2 = re.search(r"""__version__\s*=\s*["'](.+?)["']""", text).group(1)
assert v1 == v2, f"version mismatch: pyproject.toml={v1} __init__.py={v2}"
print("OK:", v1)
EOF
```

## Deciding the increment (`MAJOR.MINOR.PATCH`)

- **MAJOR** — breaking changes: removing/renaming public functions, classes, or
  modules; non-backward-compatible signature changes; dropping Python version
  support; changing default behavior consumers depend on. Reset MINOR and PATCH
  to 0.
- **MINOR** — backward-compatible new functionality: new public functions,
  classes, or modules; new optional parameters; new CLI commands or options;
  deprecations (without removal); non-trivial performance improvements. Reset
  PATCH to 0.
- **PATCH** — backward-compatible fixes: bug fixes with no public-API change,
  documentation corrections, internal refactors, dependency pin updates,
  test-only changes.

**Mixed releases:** the highest-priority increment wins (MAJOR > MINOR >
PATCH). One breaking change among a dozen bug fixes still means a MAJOR bump.

**Pre-1.0.0:** while the version is `0.Y.Z`, the API is not considered stable.
Breaking changes may be released as MINOR bumps (`0.Y` → `0.(Y+1)`), with the
same highest-increment-wins logic within that relaxed scheme.

Tasks that change no code (docs, configuration, planning) do not bump the
version.

## Pre-release versions

Use PEP 440 canonical forms — never the hyphenated SemVer forms
(`1.2.0-alpha.1`), which tools normalize and would break the two-file match:

| Stage             | Format     | Example    | Meaning                              |
|-------------------|------------|------------|--------------------------------------|
| Alpha             | `X.Y.ZaN`  | `1.2.0a1`  | Early development; API may change    |
| Beta              | `X.Y.ZbN`  | `1.2.0b1`  | Feature-complete; may have bugs      |
| Release candidate | `X.Y.ZrcN` | `1.2.0rc1` | Believed ready, pending validation   |

- Increment `N` within a stage (`1.2.0a1` → `1.2.0a2`); reset `N` to 1 when
  advancing stage (alpha → beta → rc).
- Promoting to stable drops the suffix (`1.2.0rc2` → `1.2.0`).
- The base `X.Y.Z` is the version being worked *toward*, chosen with the
  increment rules above relative to the last stable release.

## Workflow when bumping

1. Review the changes since the last version and classify each as
   MAJOR / MINOR / PATCH.
2. Select the increment: highest priority wins; apply the pre-1.0.0 relaxation
   if the current version is `0.Y.Z`.
3. Update both files to the identical new string.
4. Run the verification snippet above.
5. State the chosen increment and the reasoning. MAJOR bumps must never be
   silent — flag them for the user.
