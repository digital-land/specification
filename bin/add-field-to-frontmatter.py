import os
import frontmatter
import argparse


def update_frontmatter(directory_name, new_attribute, new_value):
    directory = "content/" + directory_name
    print(directory)
    # Iterate through all files in the given directory
    for filename in os.listdir(directory):
        # Check if the file has a .md extension
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            # Read the markdown file
            with open(file_path, 'r', encoding='utf-8') as file:
                post = frontmatter.load(file)

            # Add the new attribute to the frontmatter
            post[new_attribute] = new_value
            print(post)

            # Write the updated frontmatter back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(frontmatter.dumps(post))
            print(f"Updated {filename}")


def main():
    parser = argparse.ArgumentParser(description='Update frontmatter of markdown files.')
    parser.add_argument('directory_name', type=str, help='Directory containing markdown files')
    parser.add_argument('attribute', type=str, help='New frontmatter attribute to add')
    parser.add_argument('--value', type=str, default='', help='Value of the new attribute (default: empty string)')

    args = parser.parse_args()

    update_frontmatter(args.directory_name, args.attribute, args.value)


if __name__ == '__main__':
    main()
