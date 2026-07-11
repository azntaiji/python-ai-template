# Logging Rules

This project uses the stdlib `logging` module with rotating file handlers.
All configuration is centralized in `src/<package_name>/logging_config.py` —
it writes to `out/logs/app.log` (rotates at 5 MB, keeps 5 backups; console
shows INFO and up, the file records DEBUG and up). Individual modules must
never configure handlers or levels themselves.

## Entrypoints

Call `setup_logging()` exactly once, at the top of each application entrypoint
(CLI `main()`, `__main__.py`, a service's start script), before other work:

```python
from <package_name>.logging_config import setup_logging

setup_logging()
```

Library code and importable modules never call it. Duplicate setup calls or
stray `addHandler` calls cause duplicated log lines — if you see repeated
output, look for a second setup call.

## In every module that logs

```python
import logging

logger = logging.getLogger(__name__)
```

Always use `__name__` — it makes records carry the fully qualified module path
so they are traceable and filterable per-subtree. Never hardcode logger names,
share one logger across modules, or reference the root logger.

## Rules

- **No `print()` for diagnostics.** All diagnostic output goes through the
  logger. Replace existing diagnostic `print()` calls with logger calls at the
  right level. `print()` remains fine for program *output* — e.g., a CLI whose
  job is to print results to stdout.
- **Lazy formatting.** Write `logger.info("x=%s", x)` — never f-strings or
  pre-formatted strings inside the call. Lazy arguments are only interpolated
  if the record passes the level filter, so filtered-out messages cost nothing.
- **Exceptions get tracebacks.** In `except` blocks, use
  `logger.exception("...")` (or `logger.error("...", exc_info=True)`). A bare
  `logger.error(str(e))` loses the stack trace.
- **Never commit log files.** `out/` must stay in `.gitignore`; add it if
  missing.

## Log levels

| Level      | Use for                                                         |
|------------|-----------------------------------------------------------------|
| `DEBUG`    | Detailed diagnostic info (variable values, flow tracing)        |
| `INFO`     | Routine operational events (startup, shutdown, task completion) |
| `WARNING`  | Unexpected but recoverable situations                           |
| `ERROR`    | Failures that prevent a specific operation from completing      |
| `CRITICAL` | Failures that may force the application to abort                |

Choose by what a reader of the logs needs, not by how the code feels.

## Review checklist (when cleaning up existing code)

1. Diagnostic `print()` → logger call at the right level.
2. f-strings or pre-formatted strings in logger calls → lazy `%s` args.
3. Handler/level configuration outside `logging_config.py` → remove.
4. Hardcoded or shared logger names → `logging.getLogger(__name__)`.
5. `except` blocks logging without the traceback → `logger.exception`.
6. Missing `setup_logging()` at an entrypoint, or more than one call.
