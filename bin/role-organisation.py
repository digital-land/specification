#!/usr/bin/env python3

# generate the role-organisation dataset from role-organisation-rule dataset


import sys
import csv


organisations = {}
lookups = {
        "organisation": {},
        "dataset": {},
        "local-authority-type": {},
}
role_rules = {}
role_organisations = {}


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
    lookups["dataset"].setdefault(row["dataset"], set())
    lookups["dataset"][row["dataset"]].add(organisation)
    if row.get("local-authority-type", ""):
        lookups["local-authority-type"].setdefault(row["local-authority-type"], set())
        lookups["local-authority-type"][row["local-authority-type"]].add(organisation)


lookups["organisation"][""] = set()
lookups["dataset"][""] = set()
lookups["local-authority-type"][""] = set()

# load rules
for row in csv.DictReader(open("content/role-organisation-rule.csv")):
    role_rules.setdefault(row["role"], {})
    role_rules[row["role"]].setdefault(row["priority"], [])
    role_rules[row["role"]][row["priority"]].append(row)


# apply rules to find the organisations for each dataset
for role, priorities in sorted(role_rules.items()):
    role_organisations.setdefault(role, set())
    for priority, rules in sorted(priorities.items(), reverse=True):
        for rule in rules:
            role_organisations[role] = rule_set(rule, "organisation", role_organisations[role])
            role_organisations[role] = rule_set(rule, "dataset", role_organisations[role])
            role_organisations[role] = rule_set(rule, "local-authority-type", role_organisations[role])

# write 
fieldnames = ["role", "organisation", "entry-date", "start-date", "end-date"]
w = csv.DictWriter(
    open(sys.argv[1], "w", newline=""), fieldnames=fieldnames, extrasaction="ignore"
)
w.writeheader()

for role, orgs in role_organisations.items():
    for org in sorted(orgs):
        w.writerow({"organisation": org, "role": role,
                    "start-date": organisations[org]["start-date"],
                    "end-date": organisations[org]["end-date"],
                    })
