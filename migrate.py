#!/usr/bin/env python3
"""
Blog migration script: Archivarix backup → Jekyll Chirpy posts
Sources (Archivarix backups):
    ro  : /opt/homebrew/var/www/tituscapilnean_ro/.content.5jGCYXv6/  (default)
    com : pass --content-dir <path to tituscapilnean.com/.content.XXXX>
Target: the repo this script lives in.

Usage:
    python3 migrate.py              # migrate all pending articles
    python3 migrate.py --stats      # show migration stats only
    python3 migrate.py --url <url>  # migrate a specific article URL
    python3 migrate.py --batch 50   # migrate next N articles
    python3 migrate.py --urls-file urls.txt          # migrate only these URLs
    python3 migrate.py --site com --content-dir DIR --urls-file urls.txt
"""

import sqlite3
import os
import re
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from urllib.parse import unquote
from bs4 import BeautifulSoup
import html2text

# ── Paths ──────────────────────────────────────────────────────────────────
REPO_ROOT        = str(Path(__file__).resolve().parent)
JEKYLL_POSTS     = os.path.join(REPO_ROOT, "_posts")
JEKYLL_ASSETS    = os.path.join(REPO_ROOT, "assets", "img", "posts")

# ── Sites ──────────────────────────────────────────────────────────────────
# ro : dated permalinks  /YYYY/MM/slug/  (Romanian-era blog)
# com: flat permalinks   /slug/          (English blog, 2014-2023)
SITES = {
    'ro':  {'host': 'tituscapilnean.ro',
            'content_dir': '/opt/homebrew/var/www/tituscapilnean_ro/.content.5jGCYXv6',
            'extra_categories': []},
    'com': {'host': 'tituscapilnean.com',
            'content_dir': None,
            'extra_categories': ['English']},
}
SITE             = 'ro'
HOST             = SITES['ro']['host']
ARCHIVARIX_DB    = os.path.join(SITES['ro']['content_dir'], "structure.db")
ARCHIVARIX_HTML  = os.path.join(SITES['ro']['content_dir'], "html")


def configure(site, content_dir=None):
    global SITE, HOST, ARCHIVARIX_DB, ARCHIVARIX_HTML
    cfg = SITES[site]
    content_dir = content_dir or cfg['content_dir']
    if not content_dir:
        sys.exit(f"--content-dir is required for --site {site}")
    SITE, HOST = site, cfg['host']
    ARCHIVARIX_DB = os.path.join(content_dir, "structure.db")
    ARCHIVARIX_HTML = os.path.join(content_dir, "html")

# ── Query: all clean blog post URLs ────────────────────────────────────────
# Slugs may start with a digit ("8-setari-...", "911-au-trecut-8-ani") or with
# "feed" ("feedburner-suge-grav"), so match [a-z0-9]* and exclude only real
# /feed endpoints, not every slug that begins with "feed".
ARTICLES_QUERY = """
SELECT url, filename, request_uri
FROM structure
WHERE hostname='tituscapilnean.ro'
  AND mimetype='text/html'
  AND url NOT LIKE '%?%'
  AND url NOT LIKE '%/comment-page%'
  AND url NOT LIKE '%/page/%'
  AND url NOT LIKE '%/feed/%'
  AND url NOT LIKE '%/feed'
  AND url NOT LIKE '%/trackback%'
  AND request_uri GLOB '/20[0-9][0-9]/[0-9][0-9]/[a-z0-9]*'
  AND request_uri NOT GLOB '/20[0-9][0-9]/[0-9][0-9]/'
  AND (length(request_uri) - length(replace(request_uri, '/', ''))) <= 4
ORDER BY url
"""

# .com posts live at the root: /slug/
COM_ARTICLES_QUERY = """
SELECT url, filename, request_uri
FROM structure
WHERE hostname='tituscapilnean.com'
  AND mimetype='text/html'
  AND url NOT LIKE '%?%'
  AND request_uri GLOB '/[a-z0-9]*'
  AND (length(rtrim(request_uri, '/')) - length(replace(rtrim(request_uri, '/'), '/', ''))) = 1
  AND request_uri NOT GLOB '/wp-*'
ORDER BY url
"""

URL_QUERY = """
SELECT url, filename, request_uri FROM structure
WHERE url=? AND mimetype='text/html'
"""

IMAGE_QUERY = """
SELECT url, filename FROM structure
WHERE url=?
"""


def get_db():
    return sqlite3.connect(ARCHIVARIX_DB)


def get_all_articles(db):
    cur = db.execute(COM_ARTICLES_QUERY if SITE == 'com' else ARTICLES_QUERY)
    return cur.fetchall()


def get_migrated_slugs():
    """Return set of slugs already in _posts (without date prefix)."""
    slugs = set()
    for f in Path(JEKYLL_POSTS).glob("*.md"):
        # Remove YYYY-MM-DD- prefix
        slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', f.stem)
        slugs.add(slug)
    return slugs


def url_to_slug(url):
    """Extract slug from URL like http://tituscapilnean.ro/2009/03/my-post/"""
    parts = url.rstrip('/').split('/')
    return unquote(parts[-1]) if parts else ''


def sanitize_slug(slug):
    """Make a slug safe for use as a filename: keep alphanumerics, hyphens, dots."""
    # Replace special unicode chars and spaces with hyphens
    slug = slug.replace('–', '-').replace('—', '-').replace(' ', '-')
    # Remove chars that are not safe in filenames
    slug = re.sub(r'[^\w\-.]', '', slug, flags=re.UNICODE)
    # Collapse multiple hyphens
    slug = re.sub(r'-{2,}', '-', slug)
    return slug.strip('-')


def url_to_date_and_slug(url):
    """Extract YYYY, MM, slug from URL. Returns decoded + sanitized slug."""
    if SITE == 'com':
        # Flat permalink: year/month come from the page's published date
        m = re.match(r'https?://(?:www\.)?tituscapilnean\.com/([^/]+)/?$', url)
        if m:
            return '', '', sanitize_slug(unquote(m.group(1)))
        return None, None, None
    m = re.match(r'https?://tituscapilnean\.ro/(\d{4})/(\d{2})/([^/]+)/?$', url)
    if m:
        raw_slug = unquote(m.group(3))
        return m.group(1), m.group(2), sanitize_slug(raw_slug)
    return None, None, None


def copy_image(db, src_url, dest_dir):
    """
    Looks up an image URL in Archivarix DB, copies the file to dest_dir.
    Returns the new relative path (for Jekyll) or None on failure.
    """
    row = (db.execute(IMAGE_QUERY, (src_url,)).fetchone()
           or db.execute(IMAGE_QUERY, (src_url.replace('http://', 'https://', 1),)).fetchone())
    if not row:
        return None
    _, img_filename = row
    # Archivarix stores images under binary/, HTML under html/
    src_path = os.path.join(os.path.dirname(ARCHIVARIX_HTML), 'binary', img_filename)
    if not os.path.exists(src_path):
        src_path = os.path.join(ARCHIVARIX_HTML, img_filename)
    if not os.path.exists(src_path):
        return None
    os.makedirs(dest_dir, exist_ok=True)
    # Preserve original filename from URL
    orig_name = src_url.rstrip('/').split('/')[-1].split('?')[0]
    dest_path = os.path.join(dest_dir, orig_name)
    if not os.path.exists(dest_path):
        shutil.copy2(src_path, dest_path)
    return dest_path


def rewrite_image_urls(soup_content, db, year, slug):
    """
    For each img tag in content, attempt to copy image from Archivarix
    and rewrite src to local Jekyll path. Returns list of broken image URLs.
    """
    broken = []
    dest_dir = os.path.join(JEKYLL_ASSETS, year, slug)

    for img in soup_content.find_all('img'):
        src = img.get('src', '')
        if not src:
            continue

        # Normalize relative URLs
        host_re = re.escape(HOST)
        if src.startswith('/wp-content/'):
            full_url = f"http://{HOST}{src}"
        elif re.match(rf'https?://(www\.)?{host_re}/', src):
            full_url = re.sub(rf'^https?://(www\.)?{host_re}', f'http://{HOST}', src)
        else:
            # External image — leave as-is
            continue

        # Try to copy from Archivarix
        new_path = copy_image(db, full_url, dest_dir)
        if new_path:
            # Make Jekyll-relative path
            rel = new_path.replace(REPO_ROOT, "")
            img['src'] = rel
        else:
            broken.append(full_url)

    return broken


def check_embeds(soup_content):
    """
    Find iframes and shortcodes that may be broken embeds.
    Returns list of (type, src) tuples.
    """
    issues = []
    for iframe in soup_content.find_all('iframe'):
        src = iframe.get('src', iframe.get('data-src', ''))
        issues.append(('iframe', src))

    # WordPress shortcode patterns left in content
    text = soup_content.get_text()
    shortcodes = re.findall(r'\[(?:youtube|vimeo|video|audio|embed)[^\]]*\]', text, re.I)
    for sc in shortcodes:
        issues.append(('shortcode', sc))

    return issues


def extract_article(filepath, db, year, month, slug):
    """
    Parse a WordPress HTML file and return dict with Jekyll post data.
    """
    with open(filepath, encoding='utf-8', errors='replace') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # ── Title ──────────────────────────────────────────────────────────────
    og_title = soup.find('meta', property='og:title')
    title = og_title['content'].strip() if og_title else ''
    # Yoast appends the site name to og:title on the .com theme
    title = re.sub(r'\s+[-|–]\s+Titus Capilnean$', '', title)
    if not title:
        h1 = soup.find('h1', class_='entry-title')
        title = h1.get_text(strip=True) if h1 else slug.replace('-', ' ').title()

    # ── Date ───────────────────────────────────────────────────────────────
    pub = soup.find('meta', property='article:published_time')
    if pub and pub.get('content'):
        raw_date = pub['content']
        # Parse ISO 8601 and format for Jekyll
        dt = datetime.fromisoformat(raw_date.replace('Z', '+00:00'))
        date_str = dt.strftime('%Y-%m-%d %H:%M:%S %z')
        date_ymd = dt.strftime('%Y-%m-%d')
    else:
        # Older theme: <time class="entry-date published" datetime="...">
        t = (soup.find('time', class_='published') or soup.find('time', class_='entry-date'))
        if t and t.get('datetime'):
            dt = datetime.fromisoformat(t['datetime'].replace('Z', '+00:00'))
            date_str = dt.strftime('%Y-%m-%d %H:%M:%S %z')
            date_ymd = dt.strftime('%Y-%m-%d')
        elif year:
            # Fallback: use year/month from URL (day=01, time=noon UTC)
            date_str = f"{year}-{month}-01 12:00:00 +0000"
            date_ymd = f"{year}-{month}-01"
        else:
            return None   # flat permalink and no published date: can't place it
    # Normalise to UTC so GitHub Pages never treats the post as future-dated
    if not date_str.endswith('+0000'):
        dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S %z')
        dt = dt.astimezone(__import__('datetime').timezone.utc)
        date_str = dt.strftime('%Y-%m-%d %H:%M:%S +0000')
        date_ymd = dt.strftime('%Y-%m-%d')
    year = date_ymd[:4]

    # ── Categories ─────────────────────────────────────────────────────────
    cats = list(dict.fromkeys([
        c.get_text(strip=True)
        for c in soup.find_all('a', rel='category tag')
    ]))
    if not cats:
        # Older theme: extract from body class (e.g. category-socialmedia)
        body_classes = soup.find('body').get('class', []) if soup.find('body') else []
        cats = [c.replace('category-', '').replace('-', ' ').title()
                for c in body_classes if c.startswith('category-')]
    if not cats:
        art = soup.find('article')
        cats = [c.replace('category-', '').replace('-', ' ').title()
                for c in (art.get('class', []) if art else []) if c.startswith('category-')]
    cats = [c for c in cats if c.lower() != 'uncategorized']
    for extra in reversed(SITES[SITE]['extra_categories']):
        if extra not in cats:
            cats.insert(0, extra)

    # ── Tags ───────────────────────────────────────────────────────────────
    tags_container = soup.find(class_='tags-links')
    if tags_container:
        tags = list(dict.fromkeys([
            t.get_text(strip=True)
            for t in tags_container.find_all('a', rel='tag')
        ]))
    else:
        # Older theme: extract from body class (e.g. tag-twitter)
        body_classes = soup.find('body').get('class', []) if soup.find('body') else []
        tags = list(dict.fromkeys([
            c.replace('tag-', '')
            for c in body_classes if c.startswith('tag-')
        ]))

    # ── Content ────────────────────────────────────────────────────────────
    # Try multiple selectors to support different WP theme generations
    content_div = None
    article_el = soup.find('article')
    if article_el:
        content_div = article_el.find(class_='entry-content')
    if not content_div:
        # Older theme: div.entry (no <article> tag)
        content_div = soup.find('div', class_='entry')
    if not content_div:
        # Fallback: any .entry-content anywhere
        content_div = soup.find(class_='entry-content')

    if not content_div:
        return None

    # Drop related-posts and share widgets (Jetpack, Sociable, Zemanta, YARPP)
    # and Facebook Like iframes before images/embeds are checked
    for el in content_div.find_all(class_=re.compile(r'jp-relatedposts|sharedaddy|yarpp|zemanta|sociable')):
        el.decompose()
    for el in content_div.find_all('iframe', src=re.compile(r'facebook\.com/plugins/like')):
        el.decompose()

    # Rewrite images and collect broken ones
    broken_images = rewrite_image_urls(content_div, db, year, slug)


    # Check for embed issues
    embed_issues = check_embeds(content_div)

    # Remove share buttons, post-nav, related posts clutter
    for el in content_div.find_all(class_=re.compile(
        r'sharedaddy|sd-sharing|jp-relatedposts|wpcnt|'
        r'post-navigation|entry-footer|comments-area'
    )):
        el.decompose()

    # Convert to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0
    h.unicode_snob = True
    h.wrap_links = False
    content_md = h.handle(str(content_div)).strip()

    return {
        'title': title,
        'date': date_str,
        'date_ymd': date_ymd,
        'categories': cats,
        'tags': tags,
        'content': content_md,
        'broken_images': broken_images,
        'embed_issues': embed_issues,
    }


def build_frontmatter(data):
    """Build Jekyll Chirpy-compatible YAML frontmatter."""
    title = data['title'].replace('"', '\\"')

    # Format categories and tags as YAML lists
    if data['categories']:
        cats_yaml = '[' + ', '.join(f'"{c}"' for c in data['categories']) + ']'
    else:
        cats_yaml = '[]'

    if data['tags']:
        tags_yaml = '[' + ', '.join(
            f'"{t.lower().replace(" ", "-")}"' for t in data['tags']
        ) + ']'
    else:
        tags_yaml = '[]'

    lines = [
        '---',
        f'title: "{title}"',
        f'date: {data["date"]}',
        f'categories: {cats_yaml}',
        f'tags: {tags_yaml}',
        'author: titus_capilnean',
    ]

    if data['broken_images']:
        lines.append(f'# BROKEN_IMAGES: {len(data["broken_images"])} image(s) could not be resolved')
        for img in data['broken_images']:
            lines.append(f'#   - {img}')

    if data['embed_issues']:
        lines.append(f'# EMBED_ISSUES: {len(data["embed_issues"])} embed(s) need review')
        for kind, src in data['embed_issues']:
            lines.append(f'#   - [{kind}] {src}')

    lines.append('---')
    return '\n'.join(lines)


def migrate_article(url, filename, db, dry_run=False):
    """
    Migrate a single article. Returns (success, output_path, issues).
    Returns (None, None, None) to signal silently skip (e.g. attachment page).
    """
    year, month, slug = url_to_date_and_slug(url)
    if slug is None:
        # Sub-page/attachment URL — not a blog post, skip silently
        return None, None, None

    html_path = os.path.join(ARCHIVARIX_HTML, filename)
    if not os.path.exists(html_path):
        return False, None, [f"HTML file not found: {html_path}"]

    data = extract_article(html_path, db, year, month, slug)
    if not data:
        return False, None, [f"Could not extract content from: {url}"]

    # Build output filename: YYYY-MM-DD-slug.md
    date_prefix = data['date_ymd']
    out_filename = f"{date_prefix}-{slug}.md"
    out_path = os.path.join(JEKYLL_POSTS, out_filename)

    if dry_run:
        return True, out_path, data['broken_images'] + [s for _, s in data['embed_issues']]

    frontmatter = build_frontmatter(data)
    post_content = f"{frontmatter}\n\n{data['content']}\n"

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(post_content)

    issues = []
    if data['broken_images']:
        issues.append(f"{len(data['broken_images'])} broken image(s)")
    if data['embed_issues']:
        issues.append(f"{len(data['embed_issues'])} embed issue(s)")

    return True, out_path, issues


def effective_slug(url):
    """Return the slug that would be used as a filename for this URL."""
    _, _, slug = url_to_date_and_slug(url)
    return slug  # already sanitized by url_to_date_and_slug


def print_stats(db):
    articles = get_all_articles(db)
    migrated = get_migrated_slugs()
    total = len(articles)

    seen = set()
    done_count = 0
    pending_urls = []
    for url, _, _ in articles:
        slug = effective_slug(url)
        if slug is None:
            continue  # attachment page, skip
        if slug in seen:
            continue  # duplicate URL (with/without trailing slash)
        seen.add(slug)
        if slug in migrated:
            done_count += 1
        else:
            pending_urls.append((url, slug))

    print(f"Total unique articles    : {len(seen)}")
    print(f"Already migrated         : {done_count}")
    print(f"Pending migration        : {len(pending_urls)}")

    from collections import Counter
    year_pending = Counter()
    for url, slug in pending_urls:
        m = re.match(r'https?://[^/]+/(\d{4})/', url)
        if m:
            year_pending[m.group(1)] += 1
    if year_pending:
        print("\nPending by year:")
        for yr in sorted(year_pending):
            print(f"  {yr}: {year_pending[yr]}")


def main():
    parser = argparse.ArgumentParser(description='Migrate Archivarix blog to Jekyll')
    parser.add_argument('--stats', action='store_true', help='Show stats only')
    parser.add_argument('--url', help='Migrate specific URL')
    parser.add_argument('--batch', type=int, default=0, help='Migrate next N articles')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    parser.add_argument('--site', choices=sorted(SITES), default='ro', help='Which backup to read')
    parser.add_argument('--content-dir', help='Archivarix .content.XXXX directory (overrides site default)')
    parser.add_argument('--urls-file', help='Migrate only the URLs listed in this file (one per line)')
    args = parser.parse_args()

    configure(args.site, args.content_dir)
    db = get_db()

    if args.urls_file:
        urls = [l.strip() for l in open(args.urls_file) if l.strip() and not l.startswith('#')]
        ok_n = fail_n = 0
        for i, u in enumerate(urls, 1):
            row = db.execute(URL_QUERY, (u,)).fetchone()
            if not row:
                fail_n += 1
                print(f"[{i}/{len(urls)}] FAIL: {u} — not in DB")
                continue
            ok, path, issues = migrate_article(row[0], row[1], db, dry_run=args.dry_run)
            if ok:
                ok_n += 1
                print(f"[{i}/{len(urls)}] OK: {os.path.basename(path)}" + (f" ({', '.join(issues)})" if issues else ''))
            else:
                fail_n += 1
                print(f"[{i}/{len(urls)}] FAIL: {u} — {issues}")
        print(f"\nDone. Success: {ok_n}, Failures: {fail_n}")
        return

    if args.stats:
        print_stats(db)
        return

    articles = get_all_articles(db)
    migrated = get_migrated_slugs()

    if args.url:
        # Single article mode
        row = next(((u, f, r) for u, f, r in articles if u == args.url), None)
        if not row:
            print(f"URL not found in DB: {args.url}")
            return
        url, filename, _ = row
        ok, path, issues = migrate_article(url, filename, db, dry_run=args.dry_run)
        if ok:
            print(f"{'[DRY RUN] Would write' if args.dry_run else 'Wrote'}: {path}")
            if issues:
                print(f"  Issues: {', '.join(issues)}")
        else:
            print(f"FAILED: {issues}")
        return

    # Batch / full migration — deduplicate by effective slug
    seen_slugs = set()
    pending = []
    for u, f, _ in articles:
        slug = effective_slug(u)
        if slug is None or slug in migrated or slug in seen_slugs:
            continue
        seen_slugs.add(slug)
        pending.append((u, f))
    batch = pending[:args.batch] if args.batch > 0 else pending

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Migrating {len(batch)} of {len(pending)} pending articles...")

    success_count = 0
    fail_count = 0
    issue_count = 0

    for i, (url, filename) in enumerate(batch, 1):
        ok, path, issues = migrate_article(url, filename, db, dry_run=args.dry_run)
        if ok is None:
            # Silently skip attachment/sub-page URLs
            continue
        if ok:
            success_count += 1
            slug = url_to_slug(url)
            status = f"[{i}/{len(batch)}] OK: {slug}"
            if issues:
                status += f" ({', '.join(issues)})"
                issue_count += 1
            print(status)
        else:
            fail_count += 1
            print(f"[{i}/{len(batch)}] FAIL: {url} — {issues}")

    print(f"\nDone. Success: {success_count}, Failures: {fail_count}, With issues: {issue_count}")
    print_stats(db)


if __name__ == '__main__':
    main()
