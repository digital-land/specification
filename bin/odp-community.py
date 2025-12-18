#!/usr/bin/env python3

# create project-organisation.csv from individual project-organisation files ..

import sys
import csv
from operator import getitem


def cohort_key(row):
    return f'{row["start-date"]}/{row["intervention"]}'


# load organisations
organisations = {}
for row in csv.DictReader(open("var/cache/organisation.csv", newline="")):
    organisations[row["organisation"]] = row

# load cohorts
cohorts = {}

for row in csv.DictReader(open("specification/cohort.csv", newline="")):
    cohorts[row['fund'].lower()] = row["cohort"]
    cohorts[cohort_key(row)] = row["cohort"]


members = {}
project = "open-digital-planning"

awards = [award for award in csv.DictReader(open("specification/award.csv", newline=""))]
awards = sorted(awards, key=lambda d: d['start-date'])

for award in awards:

    # ODP membership is based on being funded for these interventions ...
    if award["intervention"] not in ["software", "improvement", "innovation", "integration"]:
        continue

    for organisation in [award["organisation"]] + award["organisations"].split(";"):
        if not organisation:
            continue

        o = organisations[organisation]

        if organisation not in members:
            members[organisation] = {
                "project": project,
                "organisation": organisation,
                "cohort": '',
                "start-date": award["start-date"],
                "end-date": award.get("end-date", "") or o.get("end-date", ""),
                "notes": award["notes"]
            }

        # cohorts are being deprecated, but we use them for now in our PowerBI dashboard ..
        if not members[organisation]["cohort"]:
            cohort = ""
            if award['fund'] in cohorts:
                cohort = cohorts[award['fund']]
            elif organisation in cohorts:
                cohort = cohorts[organisation]
            else:
                key = cohort_key(award)
                if key in cohorts:
                    cohort = cohorts[key]

            if cohort:
                    members[organisation]["cohort"] = cohort


# create project-organisation.csv
fieldnames = ["project", "organisation", "cohort", "start-date", "end-date", "notes"]

w = csv.DictWriter(
    open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction="ignore"
)
w.writeheader()

errors = 0
for organisation, row in sorted(members.items(), key=lambda x: getitem(x[1], 'start-date')):
    if organisation not in ["local-authority:GMCA", "local-authority:LIC"]:
        if not row["cohort"]:
            print("unknown cohort for:", organisation, file=sys.stderr)
            errors += 1

    w.writerow(row)

if errors:
    sys.exit(2)
