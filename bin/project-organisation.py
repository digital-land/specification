#!/usr/bin/env python3

# create project-organisation.csv from individual project-organisation files ..

import sys
import csv


# create project-organisation.csv
fieldnames = ["project", "organisation", "cohort", "start-date", "end-date", "notes"]

w = csv.DictWriter(
    open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction="ignore"
)
w.writeheader()

for csvfile in sys.argv[2:]:
    for row in csv.DictReader(open(csvfile, newline="")):
        w.writerow(row)
