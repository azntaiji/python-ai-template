import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("out/logs")

def setup_logging(level: int = logging.DEBUG) -> None:
    """Call once at application startup (e.g., in __main__.py or CLI entrypoint)."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    root = logging.getLogger()
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