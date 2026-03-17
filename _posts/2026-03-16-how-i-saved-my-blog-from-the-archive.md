---
title: "How I Saved 17 Years of Blog Posts from a Dead Hosting Account"
date: 2026-03-16 12:00:00 +0000
categories: ["Meta", "Technology"]
tags: ["blogging", "migration", "archivarix", "jekyll", "ai", "python"]
author: titus_capilnean
---

I started blogging in 2009. Back then it was WordPress, on shared hosting, writing in Romanian about PR, advertising events, and whatever was happening in the Bucharest social media scene. Over the years the blog evolved — I wrote in English, moved to London, San Francisco, Austin, and Denver, and the blog followed me through all of it. Marketing, startups, crypto, identity, AI, politics, food.

At some point my hosting disappeared. I don't remember exactly when or why — either I forgot to renew, or the provider shut down, or some combination of both. The domain still pointed somewhere but the content was gone.

Or so I thought.

## The Archivarix Rescue

Sometime before the server died, I had the presence of mind to run [Archivarix](https://archivarix.com/), a CMS that creates a complete offline archive of a website. It saves every URL — the HTML, images, CSS, JavaScript — into a local SQLite database paired with a folder of hashed files. Think of it as a personal Wayback Machine, but one that runs on your own server.

I had a compressed `.tar` of that archive sitting in `/opt/homebrew/var/www/tituscapilnean_ro` doing nothing useful.

Inside: **1,364 HTML files**, each a fully-rendered WordPress page. Plus 1,247 images. Everything was cross-referenced in a `structure.db` SQLite file that mapped URLs to filenames.

## The New Setup

Meanwhile, I had been slowly rebuilding the blog on GitHub Pages using [Jekyll](https://jekyllrb.com/) with the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy). I had manually migrated about 100 articles — mostly the ones I remembered writing and considered worth keeping.

But there were 17 years of posts sitting in that Archivarix archive. Around 1,300 unique articles. Most of them from the early years, in Romanian, covering things I barely remembered writing.

## The Migration

Rather than migrating by hand (which would have taken weeks), I wrote a Python migration script with Claude Code. The workflow:

1. **Query the SQLite DB** for all clean article URLs matching the pattern `YYYY/MM/slug`
2. **Parse the WordPress HTML** with BeautifulSoup to extract title, date, categories, tags, and the `.entry-content` div (with a fallback to `div.entry` for older theme versions)
3. **Copy images** from the Archivarix `html/` directory to `assets/img/posts/YEAR/SLUG/`, rewriting `src` paths in the content
4. **Flag broken images and embeds** as YAML comments at the top of each post — so I can find and fix them later
5. **Convert HTML to Markdown** with `html2text`
6. **Write Jekyll-format `.md` files** with proper frontmatter

The trickiest parts:

- **URL encoding**: Romanian has diacritics (`ș`, `ț`, `ă`, `â`, `î`) that WordPress URL-encodes as `%c8%99`, `%c8%9b`, etc. These needed to be decoded before using as filenames.
- **Two theme generations**: My early 2009–2010 posts used an older WordPress theme that didn't use the `<article>` HTML5 tag, but instead a `div.entry`. The script needed to handle both.
- **Attachment sub-pages**: WordPress creates per-image attachment pages at URLs like `/2009/09/post-slug/image-filename/`. These slipped through my initial filter. I fixed the SQL query to only include 3-segment paths (year/month/slug).
- **Duplicates**: Some articles appeared twice in the DB — once with and once without a trailing slash. Deduplication by effective slug solved this.

The final result: **1,297 unique articles** migrated, 718 of which have flagged issues (mostly broken images whose files weren't captured in the archive, or old YouTube/Vimeo embeds that no longer resolve).

## What Was Lost

Not everything survived. Some articles were saved in a password-protected state — the Archivarix archive captured the login form page, not the content. A handful of very early posts returned empty `entry-content` divs, likely due to caching or server errors at crawl time.

For the broken images and embeds: old screenshots of Romanian ad campaigns from 2009, event photos, embedded YouTube videos of things that have probably been taken down. The text is intact, which is what matters most.

## The Weird Part

Reading through articles I wrote 15 years ago is strange. The 2009–2012 posts are in Romanian and read like a very enthusiastic student discovering that the internet was changing media and advertising. I was right about some things (mobile, social ads, email marketing) and spectacularly wrong about others. There are event recaps for conferences that no longer exist, companies that went bankrupt, campaigns that won awards nobody remembers.

But it's all there. The through-line from "what is Twitter?" in 2009 to AI agents in 2026 is now visible. The blog didn't just survive — it became a complete record.

## The Tools

If you ever need to do something similar:

- **[Archivarix](https://archivarix.com/)** — offline website archiver, creates a browsable CMS from static files
- **[BeautifulSoup](https://beautiful-soup-4.readthedocs.io/)** — Python HTML parsing
- **[html2text](https://github.com/Alir3z4/html2text/)** — HTML to Markdown conversion
- **[Jekyll Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy)** — clean, fast static blog
- **Claude Code** — the AI coding assistant that helped write the migration script, debug the edge cases, and write this article

The migration script lives in the repo at `migrate.py` if you want to see how it works or adapt it for your own WordPress rescue operation.

---

*718 posts still have broken images or embed issues. I'll fix them gradually. If you're reading a post with a broken image — now you know why.*
