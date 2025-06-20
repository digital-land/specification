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

# load cohorts
cohorts = {}
for row in csv.DictReader(open("specification/cohort.csv", newline="")):
    cohorts[row["cohort"]] = row

# load projects and organisations
for row in csv.DictReader(open("specification/project.csv", newline="")):
    project = row["project"]
    path = f"content/project/{project}.md"

    post = frontmatter.load(path)

    for o in post.metadata["organisations"] or {}:

        cohort = o.get("cohort", "")

        dates = [post.metadata["start-date"]]
        if cohort in cohorts:
            dates.append(cohorts[cohort].get("start-date", "") or "")
        start_date = min(dates)

        dates = [post.metadata["end-date"]]
        if cohort in cohorts:
            dates.append(cohorts[cohort].get("end-date", "") or "")
        dates = [x for x in dates if x]
        end_date = min(dates) if dates else ""

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
