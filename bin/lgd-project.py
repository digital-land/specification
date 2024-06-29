import sys
import csv

print("""---
description: ''
end-date: ''
entry-date: ''
name: Localgov Drupal
parent-project: ''
project: localgov-drupal
project-status: in-progress
provision-reason: 
documentation-url: https://localgovdrupal.org/community/our-councils
start-date: ''
specifications:
organisations:""")

for row in csv.DictReader(open(sys.argv[1], newline="")):
    print(f'- organisation: {row["organisation"]}')
    print(f'  cohort: {row["cohort"]}')

print("---")
