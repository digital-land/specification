#!/usr/bin/env python3

# generate the provision dataset following the provison-rule dataset


import sys
import csv
from datetime import datetime


today = datetime.today().strftime("%Y-%m-%d")

fields = {
    "organisation": "var/cache/organisation.csv",
    "project": "specification/project-organisation.csv",
    "cohort": "specification/project-organisation.csv",
    "role": "specification/role-organisation.csv",
}

sets = {}
organisations = {}
values = {}
dataset_rules = {}
rules = {}
dataset_organisations = {}
organisation_datasets = {}


def rule_set(rule, field, a, b):
    if rule["include-exclude"] == "include":
        return a | b
    else:
        return a - b


def apply_rule(dataset, rule, field):
    value = rule[field]
    if not value:
        return

    s = sets[field][value]

    dataset_organisations[dataset] = rule_set(rule, field, dataset_organisations[dataset], s)

    for organisation in s:
        organisation_datasets.setdefault(organisation, {})
        organisation_datasets[organisation].setdefault(dataset, [])
        organisation_datasets[organisation][dataset] = {
            "rule": rule,
            "field": field,
            "value": value,
        }


# load organisations
def load_organisations(field, path):
    organisations[field] = {}
    sets[field] = {}
    for row in csv.DictReader(open(path)):
        organisations[field].setdefault(row[field], {})
        organisations[field][row[field]][row["organisation"]] = row
        sets[field].setdefault(row[field], set())
        sets[field][row[field]].add(row["organisation"])
        sets[field][""] = set()


for field, path in fields.items():
    load_organisations(field, path)

# load rules
for row in csv.DictReader(open("content/provision-rule.csv")):
    # skip rules with the same start and end date
    if row["start-date"] and row["end-date"] and row["end_date"] <= row["start_date"]:
        continue

    rules[row["provision-rule"]] = row
    dataset_rules.setdefault(row["dataset"], {})
    dataset_rules[row["dataset"]].setdefault(row["priority"], [])
    dataset_rules[row["dataset"]][row["priority"]].append(row)

# apply rules to find the organisations for each dataset
for dataset, priorities in sorted(dataset_rules.items()):
    dataset_organisations.setdefault(dataset, set())
    for priority, priority_rules in sorted(priorities.items(), reverse=True):
        for rule in priority_rules:
            for field in ["project", "cohort", "role", "organisation"]:
                apply_rule(dataset, rule, field)


# write
fieldnames = [
    "organisation",
    "dataset",
    "specification",
    "provision-reason",
    "provision-rule",
    "role",
    "project",
    "cohort",
    "entry-date",
    "start-date",
    "end-date",
    "notes",
]
w = csv.DictWriter(
    open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction="ignore"
)
w.writeheader()

for organisation, datasets in sorted(organisation_datasets.items()):
    for dataset, reason in sorted(datasets.items()):

        field = reason["field"]
        value = reason["value"]
        rule = reason["rule"]

        if (
            organisation in dataset_organisations[dataset]
            and organisation in sets[field][value]
        ):

            o = organisations["organisation"][organisation]
            f = organisations[field][value][organisation]

            dates = [
                o.get("start-date", "") or "",
                f.get("start-date", "") or "",
                rule.get("start-date", "") or "",
            ]
            start_date = max(dates)

            dates = [
                o.get("end-date", "") or "",
                f.get("end-date", "") or "",
                rule.get("end-date", "") or "",
            ]
            dates = [x for x in dates if x]

            end_date = min(dates) if dates else ""

            if start_date and end_date and end_date < start_date:
                continue

            cohort = f.get("cohort", "")
            notes = f.get("notes", "")

            role = value if field == "role" else ""
            project = value if field == "project" else ""

            row = {
                "dataset": dataset,
                "organisation": organisation,
                "specification": rule["specification"],
                "provision-rule": rule["provision-rule"],
                "provision-reason": rule["provision-reason"],
                "project": project,
                "role": role,
                "cohort": cohort,
                "start-date": start_date,
                "end-date": end_date,
                "notes": notes,
            }

            w.writerow(row)
