#!/usr/bin/env python3

import glob
import re
import frontmatter

for path in glob.glob("content/dataset/*.md"):
    post = frontmatter.load(path)

    if post.get("collection") and not post.get("availability"):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        content = re.sub(
            r"^(attribution:.*)$",
            r"\1\navailability: production",
            content,
            count=1,
            flags=re.MULTILINE,
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

