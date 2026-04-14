#!/usr/bin/env python3

import glob
import frontmatter

for path in glob.glob("content/*/*.md"):
    post = frontmatter.load(path)

    for key, value in post.metadata.items():
        if value is None:
            post.metadata[key] = ""

    with open(path, "wb") as f:
        frontmatter.dump(post, f)
        f.write("\n".encode("utf-8"))
