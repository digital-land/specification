#!/usr/bin/env python3

#  convert csv files to .md files with front-matter

import sys
import csv
import glob
import frontmatter
from pathlib import Path
from itertools import chain
from decimal import Decimal

datasets = {}


for path in glob.glob("content/dataset/*.md"):
    post = frontmatter.load(path)
    row = post.metadata
    datasets[row["dataset"]] = row


# initial range ..
ranges = [
    [Decimal(1), Decimal(999)],  # early assignments
]

for dataset, row in datasets.items():
    ranges.append(
        [
            Decimal(row.get("entity-minimum", "") or 0),
            Decimal(row.get("entity-maximum", "") or 0),
        ]
    )

ranges = sorted(ranges)
lowest = ranges[0][0] - 1
highest = ranges[-1][1] + 1
flat = chain((lowest,), chain.from_iterable(ranges), (highest,))
gaps = [[x + 1, y - 1] for x, y in zip(flat, flat) if x + 1 < y]

for gap in gaps:
    if gap[1] - gap[0] > 0:
        print(gap[0], gap[1], gap[1] - gap[0])

print(highest)
