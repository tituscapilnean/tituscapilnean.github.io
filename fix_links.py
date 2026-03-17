#!/usr/bin/env python3
"""Fix broken internal links and image references in migrated Jekyll posts."""

import re
import os
import glob
import yaml
from urllib.parse import unquote

POSTS_DIR = '_posts'

# Jekyll paths that are valid in the built site (besides /posts/ and /tags/)
VALID_PREFIXES = (
    '/categories/',
    '/archives/',
    '/about/',
    '/assets/',
)


def build_known_slugs(posts):
    """Extract all post slugs from filenames (URL-decoded, lowercased)."""
    slugs = set()
    for filepath in posts:
        filename = os.path.basename(filepath)
        # Strip .md and date prefix YYYY-MM-DD-
        m = re.match(r'^\d{4}-\d{2}-\d{2}-(.+)\.md$', filename)
        if m:
            raw = m.group(1)
            decoded = unquote(raw).lower()
            slugs.add(decoded)
            slugs.add(raw.lower())  # also keep encoded form
    return slugs


def build_known_tags(posts):
    """Extract all tags actually used across all posts."""
    tags = set()
    for filepath in posts:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Extract YAML frontmatter
        m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1))
            if isinstance(fm, dict):
                post_tags = fm.get('tags', [])
                if isinstance(post_tags, list):
                    for t in post_tags:
                        if isinstance(t, str):
                            # Chirpy slugifies tags: lowercase, spaces → hyphens
                            tags.add(re.sub(r'\s+', '-', t.lower()))
        except Exception:
            pass
    return tags


def fix_content(content, known_slugs, known_tags):
    # 0. Remove linked-image [![alt](img_url)](link_url) where img is broken WP path
    #    Uses .*? (lazy) because escaped brackets like \[1\] produce double ]]
    content = re.sub(
        r'\[!\[.*?\]\((?:/wp-content/|/wp-includes/|file:///)[^)]*\)\]\([^)]*\)',
        '',
        content,
    )

    # 1. Remove file:/// image references
    content = re.sub(r'!\[[^\]]*\]\(file:///[^)]*\)', '', content)

    # 2. Remove /wp-includes/ image references (smilies, etc.)
    content = re.sub(r'!\[[^\]]*\]\(/wp-includes/[^)]*\)', '', content)

    # 3. Remove /wp-content/ image references
    content = re.sub(r'!\[[^\]]*\]\(/wp-content/[^)]*\)', '', content)
    content = re.sub(r'!\[[^\]]*\]\(\.\./wp-content/[^)]*\)', '', content)

    # 4. Strip markdown links to /wp-content/ (keep text)
    content = re.sub(r'\[([^\]]*)\]\(/wp-content/[^)]*\)', r'\1', content)
    content = re.sub(r'\[([^\]]*)\]\(\.\./wp-content/[^)]*\)', r'\1', content)
    content = re.sub(r'\[([^\]]*)\]\(\.\./\.\./wp-content/[^)]*\)', r'\1', content)

    # 5. Strip links to /wp-includes/
    content = re.sub(r'\[([^\]]*)\]\(/wp-includes/[^)]*\)', r'\1', content)

    # 6. Fix protocol-relative URLs: (//domain/...) → (https://domain/...)
    content = re.sub(r'\]\(//([^)]+)\)', r'](https://\1)', content)

    # 7. Fix bare www.* URLs: (www.X) → (https://www.X)
    content = re.sub(r'\]\(www\.([^)]+)\)', r'](https://www.\1)', content)

    # 8. Fix bare domain URLs with no protocol that htmlproofer treats as internal
    #    e.g. (thenextweb.com) → (https://thenextweb.com)
    content = re.sub(
        r'\]\(([a-z0-9][a-z0-9.-]+\.[a-z]{2,}(?:/[^)]*)?)\)',
        lambda m: f'](https://{m.group(1)})' if not m.group(1).startswith('/') else m.group(0),
        content,
    )

    # 9. Convert relative ../YYYY/MM/slug/ links (same as absolute /YYYY/MM/slug/)
    def convert_relative_wp(m):
        url = m.group(1)
        # ../YYYY/MM/DD/slug/ or ../YYYY/MM/slug/
        m4 = re.match(r'^\.\./20\d\d/\d\d/(\d\d)/([^/?#\s]+?)/?$', url)
        if m4:
            slug = m4.group(2)
            return f'](/posts/{slug}/)'
        m3 = re.match(r'^\.\./20\d\d/\d\d/([^/?#\s]+?)/?$', url)
        if m3:
            slug = m3.group(1)
            return f'](/posts/{slug}/)'
        return m.group(0)

    content = re.sub(r'\]\((\.\./20\d\d/[^)]*)\)', convert_relative_wp, content)

    # 10. Convert absolute /YYYY/MM/slug/ links → /posts/slug/
    def convert_wp_link(m):
        url = m.group(1)
        m4day = re.match(r'^/20\d\d/\d\d/(\d\d)/([^/?#\s]+?)/?(?:[?#].*)?$', url)
        if m4day:
            return f'](/posts/{m4day.group(2)}/)'
        m3 = re.match(r'^/20\d\d/\d\d/([^/?#\s]+?)/?(?:[?#].*)?$', url)
        if m3:
            return f'](/posts/{m3.group(1)}/)'
        return m.group(0)

    content = re.sub(r'\]\((/20\d\d/\d\d[^)]*)\)', convert_wp_link, content)

    # 11. Strip remaining /YYYY/MM/... links (WP attachment sub-pages, etc.)
    def strip_wp_attachment(m):
        text, url = m.group(1), m.group(2)
        if re.match(r'^/20\d\d/', url):
            return text
        return m.group(0)

    content = re.sub(r'\[([^\]]*)\]\((/20\d\d/[^)]+)\)', strip_wp_attachment, content)

    # 12. Fix /tag/X/ → /tags/X/
    content = re.sub(r'\]\(/tag/([^)]+)\)', r'](/tags/\1)', content)

    # 13. Strip .html extension from /posts/slug.html/ links
    content = re.sub(r'\]\(/posts/([^)]+)\.html/?(\))', r'](/posts/\1/\2', content)

    # 14. Validate /posts/slug/ links — strip if the slug doesn't exist
    def validate_post_link(m):
        text, url = m.group(1), m.group(2)
        slug = re.sub(r'^/posts/', '', url).strip('/')
        slug_decoded = unquote(slug).lower()
        if slug_decoded in known_slugs or slug.lower() in known_slugs:
            return m.group(0)
        return text  # post doesn't exist, strip link

    content = re.sub(r'\[([^\]]*)\]\((/posts/[^)#]+)\)', validate_post_link, content)

    # 15. Validate /tags/TAG/ links — strip if no posts use that tag
    def validate_tag_link(m):
        text, url = m.group(1), m.group(2)
        tag = re.sub(r'^/tags/', '', url).strip('/')
        if tag.lower() in known_tags:
            return m.group(0)
        return text  # tag has no posts, strip link

    content = re.sub(r'\[([^\]]*)\]\((/tags/[^)]+)\)', validate_tag_link, content)

    # 16. Strip any remaining absolute internal links to non-Jekyll paths
    def strip_unknown_internal(m):
        text, url = m.group(1), m.group(2)
        if any(url.startswith(p) for p in VALID_PREFIXES):
            return m.group(0)
        if url in ('/', ''):
            return m.group(0)
        if url.startswith('#') or url.startswith('mailto:'):
            return m.group(0)
        if re.match(r'^https?://', url):
            return m.group(0)
        if url.startswith('/'):
            return text
        return m.group(0)

    content = re.sub(r'\[([^\]]*)\]\((/[^)]*)\)', strip_unknown_internal, content)

    return content


def main():
    posts = sorted(glob.glob(os.path.join(POSTS_DIR, '*.md')))
    known_slugs = build_known_slugs(posts)
    known_tags = build_known_tags(posts)
    print(f"Known slugs: {len(known_slugs)}, Known tags: {len(known_tags)}")

    fixed = 0
    for filepath in posts:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        updated = fix_content(original, known_slugs, known_tags)
        if updated != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated)
            fixed += 1

    print(f"Fixed {fixed} / {len(posts)} posts")


if __name__ == '__main__':
    main()
