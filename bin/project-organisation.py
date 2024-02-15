#!/usr/bin/env python3

import sys
import csv
import frontmatter
import requests


# create project-organisation.csv
fieldnames = ["project", "organisation", "cohort", "start-date", "end-date", "notes"]

w = csv.DictWriter(
    open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction="ignore"
)
w.writeheader()


# load projects and organisations
for row in csv.DictReader(open("specification/project.csv", newline="")):
    project = row["project"]
    path = f"content/project/{project}.md"

    post = frontmatter.load(path)
    start_date = post.metadata["start-date"]
    end_date = post.metadata["end-date"]
    for o in post.metadata["organisations"] or {}:

        w.writerow(
            {
                "project": project,
                "organisation": o["organisation"],
                "cohort": o.get("cohort", ""),
                "start-date": o.get("start-date", start_date),
                "end-date": o.get("end-date", end_date),
                "notes": o.get("notes", ""),
            }
        )
