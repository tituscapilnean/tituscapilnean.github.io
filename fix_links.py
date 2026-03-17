#!/usr/bin/env python3
"""Fix broken internal links and image references in migrated Jekyll posts."""

import re
import os
import glob

POSTS_DIR = '_posts'

# Jekyll paths that are valid in the built site
VALID_PREFIXES = (
    '/posts/',
    '/tags/',
    '/categories/',
    '/archives/',
    '/about/',
    '/assets/',
)


def fix_content(content):
    # 0. Remove linked-image pattern [![alt](img_url)](link_url) where img is broken WP path
    #    Catches: [![text](/wp-content/...)](any_url) and [![text](/wp-includes/...)](any_url)
    #    Uses .*? (lazy) for alt text because escaped brackets like \[1\] produce double ]]
    content = re.sub(
        r'\[!\[.*?\]\((?:/wp-content/|/wp-includes/|file:///)[^)]*\)\]\([^)]*\)',
        '',
        content,
    )

    # 1. Remove file:/// image references entirely
    content = re.sub(r'!\[[^\]]*\]\(file:///[^)]*\)', '', content)

    # 2. Remove /wp-includes/ image references (smilies, etc.)
    content = re.sub(r'!\[[^\]]*\]\(/wp-includes/[^)]*\)', '', content)

    # 3. Remove any remaining /wp-content/ image references
    content = re.sub(r'!\[[^\]]*\]\(/wp-content/[^)]*\)', '', content)
    content = re.sub(r'!\[[^\]]*\]\(\.\./wp-content/[^)]*\)', '', content)

    # 4. Strip markdown *links* (not images) to /wp-content/ — keep text, remove href
    content = re.sub(r'\[([^\]]*)\]\(/wp-content/[^)]*\)', r'\1', content)
    content = re.sub(r'\[([^\]]*)\]\(\.\./wp-content/[^)]*\)', r'\1', content)
    content = re.sub(r'\[([^\]]*)\]\(\.\./\.\./wp-content/[^)]*\)', r'\1', content)

    # 5. Strip links to /wp-includes/
    content = re.sub(r'\[([^\]]*)\]\(/wp-includes/[^)]*\)', r'\1', content)

    # 6. Fix protocol-relative URLs: [text](//domain/...) → [text](https://domain/...)
    content = re.sub(r'\]\(//([^)]+)\)', r'](https://\1)', content)

    # 7. Fix bare www.* URLs missing protocol: [text](www.X) → [text](https://www.X)
    content = re.sub(r'\]\(www\.([^)]+)\)', r'](https://www.\1)', content)

    # 8. Convert old WordPress date-format post links → /posts/slug/
    def convert_wp_link(m):
        url = m.group(1)

        # /YYYY/MM/DD/slug/ — 4-segment with 2-digit day
        m4day = re.match(r'^/20\d\d/\d\d/(\d\d)/([^/?#\s]+?)/?(?:[?#].*)?$', url)
        if m4day:
            slug = m4day.group(2)
            return f'](/posts/{slug}/)'

        # /YYYY/MM/slug/ — 3-segment
        m3 = re.match(r'^/20\d\d/\d\d/([^/?#\s]+?)/?(?:[?#].*)?$', url)
        if m3:
            slug = m3.group(1)
            return f'](/posts/{slug}/)'

        return m.group(0)  # leave unchanged (attachment pages etc handled below)

    content = re.sub(r'\]\((/20\d\d/\d\d[^)]*)\)', convert_wp_link, content)

    # 9. Strip remaining /YYYY/MM/... links that weren't converted (WP attachment sub-pages)
    #    e.g. /2011/07/post-slug/image-name/ — keep the link text, drop the href
    def strip_wp_attachment_link(m):
        text = m.group(1)
        url = m.group(2)
        if re.match(r'^/20\d\d/', url):
            return text  # strip link, keep visible text
        return m.group(0)

    content = re.sub(r'\[([^\]]*)\]\((/20\d\d/[^)]+)\)', strip_wp_attachment_link, content)

    # 10. Fix /tag/X/ → /tags/X/
    content = re.sub(r'\]\(/tag/([^)]+)\)', r'](/tags/\1)', content)

    # 11. Strip links to WordPress-only pages that don't exist in Jekyll
    wp_only = [
        '/contact/', '/contact',
        '/despre-titus/', '/despre-titus',
        '/portofoliu-web-si-design/', '/portofoliu-web-si-design',
        '/scrie-pe-titusblog/', '/scrie-pe-titusblog',
        '/feed', '/feed/',
    ]
    for path in wp_only:
        # [text](/contact/) → text
        content = re.sub(
            r'\[([^\]]*)\]\(' + re.escape(path) + r'\)',
            r'\1',
            content,
        )

    # 12. Strip any remaining absolute internal links that don't point to valid Jekyll paths
    #     e.g. /2011/07/... that survived the above, /category/, /page/, etc.
    def strip_unknown_internal(m):
        text = m.group(1)
        url = m.group(2)
        # Keep known valid Jekyll paths
        if any(url.startswith(p) for p in VALID_PREFIXES):
            return m.group(0)
        # Keep root link
        if url in ('/', ''):
            return m.group(0)
        # Keep anchors
        if url.startswith('#'):
            return m.group(0)
        # Keep mailto
        if url.startswith('mailto:'):
            return m.group(0)
        # Keep external URLs
        if re.match(r'^https?://', url):
            return m.group(0)
        # Strip everything else that starts with /
        if url.startswith('/'):
            return text
        return m.group(0)

    content = re.sub(r'\[([^\]]*)\]\((/[^)]*)\)', strip_unknown_internal, content)

    return content


def main():
    posts = sorted(glob.glob(os.path.join(POSTS_DIR, '*.md')))
    fixed = 0
    for filepath in posts:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        updated = fix_content(original)
        if updated != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated)
            fixed += 1

    print(f"Fixed {fixed} / {len(posts)} posts")


if __name__ == '__main__':
    main()
