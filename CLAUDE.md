# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Jekyll-based personal blog using the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy). Hosted at https://tituscapilnean.ro via GitHub Pages. Content covers GTM, AI, blockchain, identity, and geopolitics.

## Commands

```bash
# Development server (with live reload)
bash tools/run.sh

# Production build + html-proofer validation
bash tools/test.sh

# Install Ruby dependencies
bundle install

# Install/build frontend assets
cd assets/lib && npm install && npm run build
```

## Architecture

- **`_posts/`** — Published articles as Markdown with YAML frontmatter (title, date, categories, tags, author)
- **`_drafts/`** — Unpublished drafts
- **`_tabs/`** — Static pages rendered as navigation items (About, Categories, Tags, Timeline)
- **`_data/`** — Site metadata: `authors.yml`, `contact.yml`, `share.yml`
- **`_plugins/posts-lastmod-hook.rb`** — Auto-captures last-modified date from git history
- **`assets/lib/`** — Frontend dependencies (FontAwesome, Mermaid, TocBot, etc.) managed via npm
- **`tools/`** — `run.sh` (dev server), `test.sh` (production build + validation)
- **`.github/workflows/pages-deploy.yml`** — CI/CD: builds with `JEKYLL_ENV=production`, runs html-proofer, deploys to GitHub Pages on push to main

## Post Frontmatter

```yaml
---
title: "Post Title"
date: YYYY-MM-DD HH:MM:SS +0000
categories: [Category]
tags: [tag1, tag2]
author: titus_capilnean   # defined in _data/authors.yml
---
```

## Git Workflow

Always create a feature branch, never commit directly to `main`:

```bash
git checkout -b branch-name
# make changes, commit
gh pr create --title "..." --body "..."
# merge via PR
```

## Archivarix Migration

Migrating ~1,621 blog posts from an Archivarix backup of the original WordPress site.

**Source:** `/opt/homebrew/var/www/tituscapilnean_ro/.content.5jGCYXv6/`
**Script:** `./migrate.py`
**Branch:** `migrate/archivarix-posts` (PR to master — never push migration directly to master)

### Resuming migration

```bash
python3 migrate.py --stats          # check progress
python3 migrate.py --batch 100      # migrate next 100 articles
python3 migrate.py                  # migrate all remaining
python3 migrate.py --url "http://tituscapilnean.ro/2009/03/my-post/"  # single article
python3 migrate.py --batch 10 --dry-run  # preview without writing
```

### What the script does

For each article it:
1. Parses WordPress HTML → extracts title, date, categories, tags, `.entry-content`
2. Copies images from Archivarix `html/` to `assets/img/posts/YEAR/SLUG/` and rewrites `src` paths
3. Flags broken images and iframe/embed issues as YAML comments in the post frontmatter
4. Converts HTML to Markdown with `html2text`
5. Writes `_posts/YYYY-MM-DD-slug.md`

### Post-migration review

Find posts needing manual attention:
```bash
grep -l 'BROKEN_IMAGES\|EMBED_ISSUES' _posts/*.md
```

### Dependencies

```bash
pip3 install beautifulsoup4 html2text
```

## Theme Customization

The Chirpy theme is installed as a gem (`jekyll-theme-chirpy`). To override theme files, copy them from the gem into the corresponding local path. Key config is in `_config.yml`.
