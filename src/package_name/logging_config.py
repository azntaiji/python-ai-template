"""Centralized logging configuration — see docs/LOGGING_RULES.md.

All handler and level configuration lives here; other modules only do
`logger = logging.getLogger(__name__)`.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("out/logs")

def setup_logging(level: int = logging.DEBUG) -> None:
    """Configure root logging with rotating file and console handlers.

    Call once at application startup (e.g., in __main__.py or a CLI
    entrypoint). Safe to call again: repeat calls are no-ops, so handlers
    are never duplicated.

    Args:
        level: Root logger level; handlers filter further (file DEBUG+,
            console INFO+).
    """
    root = logging.getLogger()
    if root.handlers:
        return

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    root.setLevel(level)

    # Rotate at 5 MB, keep 5 backups
    file_handler = RotatingFileHandler(
        LOG_DIR / "app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(name)s | %(levelname)-8s | %(message)s")
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter("%(levelname)-8s | %(message)s")
    )

    root.addHandler(file_handler)
    root.addHandler(console_handler)