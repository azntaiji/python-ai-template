# 005 - Frontend Track

Bare-bones Tailwind styling for the `zach_taiji_blog` templates in `src/zach_taiji_blog/templates/`. Tailwind loads from the Play CDN with the typography plugin (`https://cdn.tailwindcss.com?plugins=typography`) — no build step, no Node. Keep styling minimal; the Jinja2 block structure stays open for future theming. Always use the venv interpreter: `.venv/bin/python`, `.venv/bin/pytest`.

Prerequisite state from track 004.x (restated so nothing else must be read):

- The five templates `base.html`, `index.html`, `post.html`, `tag.html`, `404.html` exist in `src/zach_taiji_blog/templates/` (unstyled).
- Every template receives `site` (fields `title`, `menu` with `.label`/`.url`, `footer_copyright`, `socials` with `.name`/`.url`) and `nav_tags` (list of tag strings) from a context processor.
- Route names: `index`, `post_page` (arg `slug`), `tag_page` (arg `tag`).
- `Post` objects expose `slug`, `title`, `html`, `author`, `date`, `tags`.
- `blogs/hello-world.md` exists; `.venv/bin/pytest -q` passes with 15 tests.

## Read first (use the read tool)

1. read `AGENTS.md`
2. read `STATE.md`
3. read the track file named on the `CURRENT TRACK:` line of `STATE.md`

Do not read other track files.

## Done when

- [ ] `base.html` loads Tailwind from the Play CDN; post bodies use the `prose` class
- [ ] `.venv/bin/pytest -q` still passes with 15 tests
- [ ] All Tasks below are marked complete in `STATE.md`
- [ ] `STATE.md` shows the project's tracks all complete

## Task 1 - Tailwind base layout

**Files:** `src/zach_taiji_blog/templates/base.html`

**Steps:**

1. Write (overwrite) `src/zach_taiji_blog/templates/base.html` with:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}{{ site.title }}{% endblock %}</title>
  <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
</head>
<body class="min-h-screen flex flex-col bg-white text-gray-900">
  <header class="border-b border-gray-200">
    <div class="max-w-3xl mx-auto px-4 py-4 flex flex-wrap items-baseline gap-x-6 gap-y-2">
      <a href="{{ url_for('index') }}" class="text-xl font-bold">{{ site.title }}</a>
      <nav class="flex flex-wrap gap-x-4 gap-y-1 text-sm">
        {% for tag in nav_tags %}
        <a href="{{ url_for('tag_page', tag=tag) }}" class="text-gray-600 hover:text-gray-900">#{{ tag }}</a>
        {% endfor %}
        {% for item in site.menu %}
        <a href="{{ item.url }}" class="text-gray-600 hover:text-gray-900">{{ item.label }}</a>
        {% endfor %}
      </nav>
    </div>
  </header>
  <main class="max-w-3xl mx-auto px-4 py-8 w-full grow">
    {% block content %}{% endblock %}
  </main>
  <footer class="border-t border-gray-200">
    <div class="max-w-3xl mx-auto px-4 py-4 flex flex-wrap justify-between gap-2 text-sm text-gray-500">
      <p>{{ site.footer_copyright }}</p>
      <p class="flex gap-4">
        {% for s in site.socials %}
        <a href="{{ s.url }}" class="hover:text-gray-900">{{ s.name }}</a>
        {% endfor %}
      </p>
    </div>
  </footer>
</body>
</html>
```

**Verify:** run

```bash
grep -c "cdn.tailwindcss.com" src/zach_taiji_blog/templates/base.html
```

Expected: prints `1`, and `.venv/bin/pytest -q` output ends with `15 passed`.

## Task 2 - Style the index and tag listings

**Files:** `src/zach_taiji_blog/templates/index.html`,
`src/zach_taiji_blog/templates/tag.html`

**Steps:**

1. Write (overwrite) `src/zach_taiji_blog/templates/index.html` with:

```html
{% extends "base.html" %}
{% block content %}
<ul class="space-y-6">
  {% for post in posts %}
  <li>
    <a href="{{ url_for('post_page', slug=post.slug) }}" class="text-lg font-semibold hover:underline">{{ post.title }}</a>
    <p class="text-sm text-gray-500">
      {% if post.date %}<time>{{ post.date.isoformat() }}</time>{% endif %}
      {% if post.author %}&middot; {{ post.author }}{% endif %}
      {% for tag in post.tags %}&middot; #{{ tag }}{% endfor %}
    </p>
  </li>
  {% else %}
  <li class="text-gray-500">No posts yet.</li>
  {% endfor %}
</ul>
{% endblock %}
```

2. Write (overwrite) `src/zach_taiji_blog/templates/tag.html` with:

```html
{% extends "base.html" %}
{% block title %}#{{ tag }} - {{ site.title }}{% endblock %}
{% block content %}
<h1 class="text-2xl font-bold mb-6">Posts tagged #{{ tag }}</h1>
<ul class="space-y-4">
  {% for post in posts %}
  <li>
    <a href="{{ url_for('post_page', slug=post.slug) }}" class="font-semibold hover:underline">{{ post.title }}</a>
    {% if post.date %}<span class="text-sm text-gray-500"><time>{{ post.date.isoformat() }}</time></span>{% endif %}
  </li>
  {% else %}
  <li class="text-gray-500">No posts with this tag.</li>
  {% endfor %}
</ul>
{% endblock %}
```

**Verify:** run

```bash
.venv/bin/pytest -q
```

Expected: output ends with `15 passed`.

## Task 3 - Style the post page and 404 page

**Files:** `src/zach_taiji_blog/templates/post.html`,
`src/zach_taiji_blog/templates/404.html`

**Steps:**

1. Write (overwrite) `src/zach_taiji_blog/templates/post.html` with:

```html
{% extends "base.html" %}
{% block title %}{{ post.title }} - {{ site.title }}{% endblock %}
{% block content %}
<article>
  <h1 class="text-3xl font-bold mb-2">{{ post.title }}</h1>
  <p class="text-sm text-gray-500 mb-1">
    {% if post.date %}<time>{{ post.date.isoformat() }}</time>{% endif %}
    {% if post.author %}&middot; by {{ post.author }}{% endif %}
  </p>
  <p class="text-sm mb-8">
    {% for tag in post.tags %}
    <a href="{{ url_for('tag_page', tag=tag) }}" class="text-gray-600 hover:text-gray-900">#{{ tag }}</a>
    {% endfor %}
  </p>
  <div class="prose prose-gray max-w-none">{{ post.html | safe }}</div>
</article>
{% endblock %}
```

2. Write (overwrite) `src/zach_taiji_blog/templates/404.html` with:

```html
{% extends "base.html" %}
{% block title %}Not found - {{ site.title }}{% endblock %}
{% block content %}
<h1 class="text-3xl font-bold mb-4">404 - Page not found</h1>
<p><a href="{{ url_for('index') }}" class="underline hover:text-gray-600">Back to home</a></p>
{% endblock %}
```

**Verify:** run

```bash
.venv/bin/python -c "from zach_taiji_blog.app import create_app; c = create_app().test_client(); print('prose' in c.get('/post/hello-world').text)"
```

Expected: prints `True`, and `.venv/bin/pytest -q` output ends with `15 passed`.

## Task 4 - Final README pass and manual check

**Files:** `README.md`

**Steps:**

1. Read `README.md`. If it does not already mention the Tailwind Play CDN, edit `README.md` to add a note in the run instructions section stating that styling comes from the Tailwind Play CDN (an internet connection is needed for styled pages; content still renders without one) and that no CSS build step exists.
2. Manual check (do not automate): run `.venv/bin/zach_taiji_blog`, open `http://127.0.0.1:5000/` in a browser, click a post, a navbar tag, and a footer link, then stop the server with Ctrl+C.

**Verify:** run

```bash
grep -c "cdn.tailwindcss.com\|Play CDN" README.md
```

Expected: prints a number of 1 or more, and `.venv/bin/pytest -q` output ends with `15 passed`.
