#!/usr/bin/env python3

# generate the provision dataset from rules in the provison-rule dataset
# TBD: start-date and end-date should come from project-organisation ..


import sys
import csv


organisations = {
    "role": {},
    "project": {},
    "organisation": {},
}
sets = {
    "role": {},
    "project": {},
    "organisation": {},
}
values = {}
dataset_rules = {}
rules = {}
dataset_organisations = {}
organisation_datasets = {}


def rule_set(rule, field, a):
    if rule["include-exclude"] == "include":
        return a | b
    else:
        return a - b


def apply_rule(dataset, rule, field):
    value = rule[field]
    if not value:
        return
    s = sets[field][value]

    if rule["include-exclude"] == "exclude":
        dataset_organisations[dataset] = dataset_organisations[dataset] - s
    else:
        dataset_organisations[dataset] = dataset_organisations[dataset] | s
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
    for row in csv.DictReader(open(path)):
        organisations[field].setdefault(row[field], {})
        organisations[field][row[field]][row["organisation"]] = row
        sets[field].setdefault(row[field], set())
        sets[field][row[field]].add(row["organisation"])
        sets[field][""] = set()

load_organisations("organisation", "var/cache/organisation.csv")
load_organisations("project", "specification/project-organisation.csv")
load_organisations("role", "specification/role-organisation.csv")

# load rules
for row in csv.DictReader(open("content/provision-rule.csv")):
    rules[row["reference"]] = row
    dataset_rules.setdefault(row["dataset"], {})
    dataset_rules[row["dataset"]].setdefault(row["priority"], [])
    dataset_rules[row["dataset"]][row["priority"]].append(row)

# apply rules to find the organisations for each dataset
for dataset, priorities in sorted(dataset_rules.items()):
    dataset_organisations.setdefault(dataset, set())
    for priority, priority_rules in sorted(priorities.items(), reverse=True):
        for rule in priority_rules:
            for field in ["project", "role", "organisation"]:
                apply_rule(dataset, rule, field)


# write 
fieldnames = ["organisation", "dataset", "specification", "provision-reason", "provision-rule", "field", "value", "cohort", "entry-date", "start-date", "end-date", "notes"]
w = csv.DictWriter(
    open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction="ignore"
)
w.writeheader()

for organisation, datasets in sorted(organisation_datasets.items()):
    for dataset, reason in sorted(datasets.items()):
        field = reason["field"]
        value = reason["value"]
        rule = reason["rule"]

        if organisation in dataset_organisations[dataset] and organisation in sets[field][value]:

            dates = [organisations["organisation"][organisation].get("start-date", "") or ""]
            dates.append(organisations[field][value][organisation].get("start-date", "") or "")
            dates.append(rule.get("start-date", "") or "")
            start_date = max(dates)

            dates = [organisations["organisation"][organisation].get("end-date", "") or ""]
            dates.append(organisations[field][value][organisation].get("end-date", "") or "")
            dates.append(rule.get("end-date", "") or "")
            dates = [x for x in dates if x]
            end_date = min(dates) if dates else ""

            cohort = organisations[field][value][organisation].get("cohort", "")
            notes = organisations[field][value][organisation].get("notes", "")

            w.writerow({
                "dataset": dataset,
                "organisation": organisation,
                "specification": rule["specification"],
                "provision-rule": rule["reference"],
                "provision-reason": rule["provision-reason"],
                "field": field,
                "value": value,
                "cohort": cohort,
                "start-date": start_date,
                "end-date": end_date,
                "notes": notes,
            })
