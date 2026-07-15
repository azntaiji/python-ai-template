# PLAN.md

## Goal

A lightweight personal blog served by Flask: markdown files dropped into `blogs/` are rendered as HTML pages, with Obsidian-style YAML frontmatter supplying per-post metadata (title, date, author, tags) and a TOML file supplying site-wide settings. Local development deployment only.

## Scope

### In scope

- Flask as the Python web framework; local dev server started by the package CLI (`.venv/bin/zach_taiji_blog`).
- Tailwind CSS via the Play CDN — zero build step, no Node toolchain.
- Markdown posts stored in the `blogs/` directory at the project root; the URL slug is the filename without `.md`.
- Obsidian-style YAML frontmatter parsed for metadata: title, published date, author, tags.
- Tags collected from all posts' frontmatter appear as menu items in the navbar, each linking to a tag listing page.
- A `site.toml` configuration file controlling: blog title, additional custom menu links, footer copyright text, and footer social-platform links (GitHub, X, Instagram, etc.).
- Extended markdown beyond the standard syntax: `==text==` highlighting, footnotes, `^sup^`/`~sub~`, tables, fenced code blocks.

### Out of scope

- Containerization or remote deployment.
- Elaborate theming — the theme stays bare-bones, but templates use Jinja2 block inheritance from a single `base.html` so future theming is possible.
- Databases, caching layers, comments, search, RSS, drafts/preview, authentication.

## Architecture

- Names: project=zach-taiji-blog, package=zach_taiji_blog (decided 2026-07-11)
- Flask app-factory pattern: `create_app(blogs_dir, site_config_path)` in `src/zach_taiji_blog/app.py`; the CLI entry point (`zach_taiji_blog.cli:main`) starts the dev server. Reason: factories keep the app testable with temporary content directories. (2026-07-11)
- Markdown rendering via the `markdown` package plus `pymdown-extensions` (`pymdownx.mark`, `pymdownx.caret`, `pymdownx.tilde`) and the built-in `footnotes`, `tables`, `fenced_code`, `sane_lists` extensions. Reason: covers the required extended syntax with mature, zero-config libraries. (2026-07-11)
- Frontmatter parsed with `python-frontmatter`. Reason: handles Obsidian-style YAML frontmatter directly and separates metadata from body. (2026-07-11)
- Posts are re-read from `blogs/` on every request — no cache or database. Reason: single local user; edits to markdown appear on refresh. (2026-07-11)
- `site.toml` parsed with stdlib `tomllib` into frozen dataclasses in `src/zach_taiji_blog/site_config.py`; missing file falls back to defaults. Reason: no extra dependency, typed access in templates. (2026-07-11)
- Tailwind loaded from the Play CDN with the typography plugin (`https://cdn.tailwindcss.com?plugins=typography`); post bodies use the `prose` class. Reason: zero build step, decent default markdown styling. (2026-07-11)
- Templates live in `src/zach_taiji_blog/templates/`; site config and nav tags are injected by a Flask context processor so every page gets them. (2026-07-11)
- Default paths (`BLOGS_DIR=blogs`, `SITE_CONFIG_PATH=site.toml`) are exposed through `config.py` env vars per the scaffold convention. (2026-07-11)

## Backlog

1. [~] Project setup — docs/001-SETUP_TRACK.md
2. [~] Content renderer (markdown + extended syntax) — docs/002.1-CONTENT_RENDERER_TRACK.md
3. [~] Content posts (frontmatter, post loading) — docs/002.2-POST_LOADER_TRACK.md
4. [~] Content posts (sample posts) — docs/002.3-SAMPLE_POSTS_TRACK.md
5. [~] Site configuration (site.toml loader) — docs/003-CONFIG_TRACK.md
6. [~] Webapp scaffold (Flask dependency, path settings, templates) — docs/004.1-WEBAPP_SCAFFOLD_TRACK.md
7. [~] Webapp routes (app factory, CLI server, app tests) — docs/004.2-WEBAPP_ROUTES_TRACK.md
8. [~] Frontend layout (Tailwind navbar, footer, post styling) — docs/005-FRONTEND_TRACK.md

## Done Criteria

- `.venv/bin/zach_taiji_blog` starts a local server and `http://127.0.0.1:5000/` lists every post in `blogs/`, newest first.
- Each post page renders its markdown as HTML, including `==highlight==`, footnotes, tables, and fenced code blocks.
- The navbar shows the blog title, one link per frontmatter tag, and the custom menu links from `site.toml`; the footer shows the copyright text and social links from `site.toml`.
- `/tag/<tag>` lists only posts carrying that tag; unknown post slugs return a rendered 404 page.
- `.venv/bin/pytest` passes with no failures.
- `README.md` documents installation, configuration (`site.toml`, env vars), and run commands.
