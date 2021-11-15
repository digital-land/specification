#!/usr/bin/env python3

import frontmatter
import sys

for path in sys.argv:
    post = frontmatter.load(path)
    row = post.metadata
    row["text"] = post.content
    w.writerow()
