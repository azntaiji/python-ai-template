"""Configuration for <package_name>, loaded from the environment and `.env`.

All access to environment variables goes through this module. Other modules
must not call `os.getenv` directly — define a named value here instead so
every configuration knob is documented in one place.
"""

import os

from dotenv import load_dotenv

# Values already present in the environment take precedence over .env.
load_dotenv()


def get_env(name: str, default: str | None = None, *, required: bool = False) -> str | None:
    """Return the value of an environment variable.

    Args:
        name: Environment variable name.
        default: Value returned when the variable is unset.
        required: When True, raise instead of returning None when the
            variable is unset and no default is given.

    Returns:
        The variable's value, or ``default`` when unset.

    Raises:
        RuntimeError: If ``required`` is True and the variable is unset.
    """
    value = os.getenv(name, default)
    if required and value is None:
        raise RuntimeError(
            f"Required environment variable {name!r} is not set; "
            "add it to .env (see .env.example)"
        )
    return value


# Define configuration values below as the project grows, and document each
# variable in .env.example. Examples:
#
# API_KEY = get_env("API_KEY", required=True)
# DATA_DIR = get_env("DATA_DIR", default="data")
