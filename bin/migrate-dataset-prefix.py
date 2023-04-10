#!/usr/bin/env python3

import sys
import glob
import frontmatter


for path in glob.glob("content/dataset/*.md"):
    post = frontmatter.load(path)

    if post["realm"] == "dataset":
        for field in ["prefix", "reference", "entity", "name", "notes"]:
            if field not in [f["field"] for f in post["fields"]]:
                post["fields"].append({"field": field})
        post["fields"] = sorted(post["fields"], key=lambda f: f["field"])

    with open(path, "wb") as f:
        frontmatter.dump(post, f)
        f.write("\n".encode("utf-8"))
