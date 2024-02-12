#!/usr/bin/env python3

# generate the provision dataset from rules in the provison-rule dataset
# TBD: start-date and end-date should come from project-organisation ..


import sys
import csv


organisations = {}
lookups = {
        "role": {},
        "project": {},
        "organisation": {},
}
rules = {}
dataset_organisations = {}


def rule_set(rule, field, a):
    b = lookups[field][rule[field]]
    if rule["include-exclude"] == "include":
        return a | b
    else:
        return a - b



# load organisations
for row in csv.DictReader(open("var/cache/organisation.csv")):
    organisation = row["organisation"].replace(
        "local-authority-eng:", "local-authority:"
    )
    organisations[organisation] = row
    lookups["organisation"][organisation] = set([organisation])

# load project organisations
for row in csv.DictReader(open("specification/project-organisation.csv")):
    lookups["project"].setdefault(row["project"], set())
    lookups["project"][row["project"]].add(row["organisation"])

# load role organisations
for row in csv.DictReader(open("specification/role-organisation.csv")):
    lookups["role"].setdefault(row["role"], set())
    lookups["role"][row["role"]].add(row["organisation"])


# missing rule values
lookups["organisation"][""] = set()
lookups["role"][""] = set()
lookups["project"][""] = set()


# load rules
for row in csv.DictReader(open("content/provision-rule.csv")):
    rules.setdefault(row["dataset"], {})
    rules[row["dataset"]].setdefault(row["priority"], [])
    rules[row["dataset"]][row["priority"]].append(row)

# apply rules to find the organisations for each dataset
for dataset, priorities in sorted(rules.items()):
    dataset_organisations.setdefault(dataset, set())
    for priority, rules in sorted(priorities.items(), reverse=True):
        for rule in rules:
            dataset_organisations[dataset] = rule_set(rule, "organisation", dataset_organisations[dataset])
            dataset_organisations[dataset] = rule_set(rule, "role", dataset_organisations[dataset])
            dataset_organisations[dataset] = rule_set(rule, "project", dataset_organisations[dataset])

# write 
fieldnames = ["dataset", "organisation", "provision-reason", "entry-date", "start-date", "end-date"]
w = csv.DictWriter(
    open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction="ignore"
)
w.writeheader()

for dataset, orgs in dataset_organisations.items():
    for org in sorted(orgs):
        w.writerow({"organisation": org, "dataset": dataset,
                    "start-date": organisations[org].get("start-date", ""),
                    "end-date": organisations[org].get("end-date", ""),
                    })
