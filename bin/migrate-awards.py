#!/usr/bin/env python3

import csv

project_organisations = {}

fund_cohort = {
}


def _cohort(row):
    return row["cohort"] or fund_cohort.get(row.get("fund", ""), "")


def _key(row, organisation=None):
    organisation = organisation or row["organisation"]
    project = row["project"]
    cohort = _cohort(row)
    return f'{project}:{organisation}:{cohort}'


def add_award(organisation, row):
    if row["start-date"] > "2024-10-01":
        if row["intervention"] in ["software", "integration", "improvement"]:
            row["project"] = "open-digital-planning"
            _key= f'{row["project"]}:{organisation}'
            if _key not in project_organisations:
                print(f'- organisation: {organisation}')
                print(f'  cohort: {row["fund"]}')


if __name__ == "__main__":


    for row in csv.DictReader(open("specification/project-organisation.csv", newline="")):
        project_organisations[_key(row)] = row
        

    for row in csv.DictReader(open("specification/award.csv", newline="")):
        add_award(row["organisation"], row)
        partners = filter(None, row["organisations"].split(";"))
        for partner in partners:
            add_award(partner, row)
