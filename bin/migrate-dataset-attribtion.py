#!/usr/bin/env python3

import sys
import glob
import frontmatter

attribution =  {
    "ancient-woodland": "natural-england",
    "ancient-woodland-status": "natural-england",
    "area-of-outstanding-natural-beauty": "natural-england",
    "conservation-area": "historic-england",
    "green-belt": "os-open-data",
    "heritage-coast": "natural-england",
    "battlefield": "historic-england",
    "heritage-at-risk": "historic-england",
    "park-and-garden": "historic-england",
    "scheduled-monument": "historic-england",
    "world-heritage-site": "historic-england",
    "world-heritage-site-buffer-zone": "historic-england",
    "protected-wreck-site": "historic-england",
    "building-preservation-notice": "historic-england",
    "certificate-of-immunity": "historic-england",
    "listed-building": "historic-england",
    "local-authority-district": "ons-boundary",
    "local-planning-authority": "ons-boundary",
    "national-park": "ons-boundary",
    "open-space": "os-open-data",
    "parish": "ons-boundary",
    "ramsar": "natural-england",
    "region": "ons-boundary",
    "site-of-special-scientific-interest": "natural-england",
    "special-area-of-conservation": "natural-england",
    "special-protection-area": "natural-england",
}


for path in glob.glob("content/dataset/*.md"):
    post = frontmatter.load(path)

    dataset = post["dataset"]

    if not post.get("attribution", ""):
        post["attribution"] = attribution.get(dataset, "crown-copyright")

    if not post.get("licence", ""):
        post["licence"] = "ogl3"

    with open(path, "wb") as f:
        frontmatter.dump(post, f)
        f.write("\n".encode("utf-8"))
