"""Strip `index.html` from generated links so the site serves directory URLs.

Every page in this project is authored as `<name>/index.qmd`, so the output is
already `<name>/index.html` and a web server resolves `/about/` on its own.
Quarto, however, writes the file name into every link it generates itself -
the navbar, the brand logo, listing cards, the sitemap and the Open Graph
tags - which puts `/about/index.html` in the address bar as soon as a visitor
clicks anything.

This runs as a `post-render` step and rewrites those links in place. External
URLs are left alone: only a reference *ending* in `index.html` is touched.
"""

import os
import re
import sys

OUT_DIR = os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "docs")

# href/src ending in index.html, with an optional #fragment or ?query kept.
ATTR = re.compile(r'\b(href|src)="([^"]*?)index\.html([#?][^"]*)?"')
# <loc>/<url> entries in sitemap.xml and absolute URLs in meta tags.
BARE = re.compile(r'(https?://[^"\'<>\s]*?/)index\.html\b')


def strip_attr(m):
    attr, prefix, tail = m.group(1), m.group(2), m.group(3) or ""
    # A link into a *different* site that happens to end in index.html is not
    # ours to rewrite.
    if re.match(r"^[a-z]+://", prefix):
        return '%s="%s%s"' % (attr, prefix, tail)
    return '%s="%s%s"' % (attr, prefix or "./", tail)


def clean(text):
    return BARE.sub(r"\1", ATTR.sub(strip_attr, text))


def main():
    if not os.path.isdir(OUT_DIR):
        sys.exit("output directory not found: %s" % OUT_DIR)

    touched = 0
    for root, _dirs, files in os.walk(OUT_DIR):
        for name in files:
            if not name.endswith((".html", ".xml")):
                continue
            path = os.path.join(root, name)
            with open(path, encoding="utf-8") as fh:
                before = fh.read()
            after = clean(before)
            if after != before:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(after)
                touched += 1

    print("clean-urls: rewrote %d file(s) in %s" % (touched, OUT_DIR))


if __name__ == "__main__":
    main()
