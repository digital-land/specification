import os
import glob
import frontmatter

def extract_ranges_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        dataset = frontmatter.load(file)

        if 'entity-maximum' in dataset and dataset['entity-maximum'] != '' and 'entity-minimum' in dataset and dataset['entity-minimum'] != '':
            return {
                'name': dataset.get('name', 'Unknown'),
                'maximum': int(dataset['entity-maximum']),
                'minimum': int(dataset['entity-minimum'])
            }

    return None


def find_unused_ranges(sorted_ranges):
    unused_ranges = []
    prev_maximum = float('-inf')

    for range_info in sorted_ranges:
        minimum = range_info['minimum']
        maximum = range_info['maximum']

        if minimum > prev_maximum + 1:
            unused_ranges.append((prev_maximum + 1, minimum - 1))

        prev_maximum = max(prev_maximum, maximum)

    return unused_ranges


def main():
    dataset_folder = 'content/dataset'
    markdown_files = glob.glob(os.path.join(dataset_folder, '*.md'))

    ranges = []

    for file_path in markdown_files:
        range_info = extract_ranges_from_file(file_path)
        if range_info:
            ranges.append(range_info)

    # Sort ranges by minimum value
    sorted_ranges = sorted(ranges, key=lambda x: x['minimum'])

    # Print to the terminal
    print("Entity ranges from datasets")
    print("==============================================================")
    for range_info in sorted_ranges:
        print(f"{range_info['name']}: {range_info['minimum']} - {range_info['maximum']}")

    # print a gap
    for _ in range(3):
        print()
    
    # Find and print any unused ranges
    print("Unused ranges")
    print("==============================================================")
    unused_ranges = find_unused_ranges(sorted_ranges)
    for unused_range in unused_ranges:
        print(f"Unused Range: {unused_range[0]} - {unused_range[1]}")


if __name__ == "__main__":
    main()
