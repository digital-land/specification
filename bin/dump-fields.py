import os
import csv
import json
from datetime import datetime

# Create the 'tmp' directory if it doesn't exist
output_dir = 'tmp'
os.makedirs(output_dir, exist_ok=True)

today = datetime.today()

# Define dictionaries to store field information and their associated datasets
fields_info = {}
field_datasets = {}

fields_csv = 'specification/field.csv'
dataset_fields_csv = 'specification/dataset-field.csv'

print(f"Processing {fields_csv} and {dataset_fields_csv}")

# Read fields.csv and store field information
with open(fields_csv, 'r', newline='') as fields_file:
    fields_reader = csv.DictReader(fields_file)
    for row in fields_reader:
        field_name = row['field']
        fields_info[field_name] = {
            'name': row['name'],
            'description': row['description'],
            'cardinality': row['cardinality'],
            'end-date': row['end-date'],
        }

# Read dataset-field.csv and store field-dataset relationships
with open(dataset_fields_csv, 'r', newline='') as dataset_field_file:
    dataset_field_reader = csv.DictReader(dataset_field_file)
    for row in dataset_field_reader:
        dataset_name = row['dataset']
        field_name = row['field']

        if field_name in field_datasets:
            field_datasets[field_name].append(dataset_name)
        else:
            field_datasets[field_name] = [dataset_name]

# Create a list of fields with associated datasets
fields_list = []
for field_name, field_info in fields_info.items():
    datasets = field_datasets.get(field_name, [])
    field_info['datasets'] = datasets
    fields_list.append({
        'field': field_name,
        'name': field_info['name'],
        'description': field_info['description'],
        'cardinality': field_info['cardinality'],
        'end-date': field_info['end-date'],
        'datasets': datasets
    })

output_dict = {
    "created": today.strftime("%Y-%m-%d"),
    "fields": fields_list
}

output_file = os.path.join(output_dir, 'fields.json')

with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(output_dict, json_file, indent=4)

print(f"Fields have been saved to {output_file}")

