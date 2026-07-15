# 003 - Config Track

Site-wide configuration for the `zach_taiji_blog` package: a `site.toml` file at the project root and a typed loader module. Parsing uses stdlib `tomllib` (Python 3.11+) — no new dependencies. Code lives in `src/zach_taiji_blog/`, tests in `tests/`. Always use the venv interpreter: `.venv/bin/python`, `.venv/bin/pytest`.

Prerequisite state from track 002.x: the package installs in editable mode and `.venv/bin/pytest -q` passes with 8 tests.

## Read first (use the read tool)

1. read `AGENTS.md`
2. read `STATE.md`
3. read the track file named on the `CURRENT TRACK:` line of `STATE.md`

Do not read other track files.

## Done when

- [ ] `site.toml` exists at the project root and parses
- [ ] `.venv/bin/pytest -q` passes with at least 11 tests
- [ ] All Tasks below are marked complete in `STATE.md`
- [ ] `STATE.md` points to the next track in the Track Chain

## Task 1 - Create site.toml

**Files:** `site.toml`

**Steps:**

1. Create `site.toml` at the project root with exactly:

```toml
[site]
title = "Zach Taiji's Blog"

[[menu]]
label = "GitHub"
url = "https://github.com/azntaiji"

[footer]
copyright = "© 2026 Zach Taiji. All rights reserved."

[[footer.social]]
name = "github"
url = "https://github.com/azntaiji"

[[footer.social]]
name = "x"
url = "https://x.com/azntaiji"
```

**Verify:** run
```bash
.venv/bin/python -c "import tomllib; d = tomllib.load(open('site.toml', 'rb')); print(d['site']['title'], len(d['footer']['social']))"
```

Expected: prints `Zach Taiji's Blog`.

## Task 2 - Create the site config loader

**Files:** `src/zach_taiji_blog/site_config.py`, `tests/test_site_config.py`, `fixtures/sample_site.toml`

**Steps:**

1. Create `src/zach_taiji_blog/site_config.py` with exactly:

```python
"""Site-wide configuration loaded from a TOML file."""

import logging
import tomllib
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class MenuItem:
    """A custom navbar link."""

    label: str
    url: str


@dataclass(frozen=True)
class SocialLink:
    """A footer link to a social platform."""

    name: str
    url: str


@dataclass(frozen=True)
class SiteConfig:
    """All site-wide settings read from site.toml."""

    title: str = "Blog"
    menu: tuple[MenuItem, ...] = ()
    footer_copyright: str = ""
    socials: tuple[SocialLink, ...] = ()


def load_site_config(path: Path) -> SiteConfig:
    """Load site settings from a TOML file.

    Args:
        path: Path to the TOML file (normally site.toml at project root).

    Returns:
        The parsed SiteConfig; every missing file, table, or key falls back
        to the dataclass defaults.
    """
    if not path.is_file():
        logger.warning("Site config %s not found; using defaults", path)
        return SiteConfig()
    with path.open("rb") as fh:
        data = tomllib.load(fh)
    footer = data.get("footer", {})
    return SiteConfig(
        title=str(data.get("site", {}).get("title", "Blog")),
        menu=tuple(
            MenuItem(label=str(m["label"]), url=str(m["url"]))
            for m in data.get("menu", [])
        ),
        footer_copyright=str(footer.get("copyright", "")),
        socials=tuple(
            SocialLink(name=str(s["name"]), url=str(s["url"]))
            for s in footer.get("social", [])
        ),
    )
```

2. Create `fixtures/sample_site.toml` with exactly:

```toml
[site]
title = "Fixture Blog"

[[menu]]
label = "About"
url = "/about"

[footer]
copyright = "© 2026 Fixture"

[[footer.social]]
name = "github"
url = "https://github.com/example"
```

3. Create `tests/test_site_config.py` with exactly:

```python
"""Tests for zach_taiji_blog.site_config."""

from pathlib import Path

from zach_taiji_blog.site_config import SiteConfig, load_site_config

FIXTURE = Path("fixtures/sample_site.toml")


def test_load_full_config() -> None:
    cfg = load_site_config(FIXTURE)
    assert cfg.title == "Fixture Blog"
    assert [(m.label, m.url) for m in cfg.menu] == [("About", "/about")]
    assert cfg.footer_copyright == "© 2026 Fixture"
    assert [(s.name, s.url) for s in cfg.socials] == [
        ("github", "https://github.com/example")
    ]


def test_missing_file_returns_defaults(tmp_path: Path) -> None:
    assert load_site_config(tmp_path / "absent.toml") == SiteConfig()


def test_empty_file_returns_defaults(tmp_path: Path) -> None:
    empty = tmp_path / "empty.toml"
    empty.write_text("")
    cfg = load_site_config(empty)
    assert cfg.title == "Blog"
    assert cfg.menu == ()
    assert cfg.socials == ()
```

**Verify:** run from the project root

```bash
.venv/bin/pytest -q
```

Expected: output ends with `11 passed`.
