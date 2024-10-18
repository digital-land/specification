#!/usr/bin/env python3
import os
import sys
import argparse
import frontmatter
import shutil
import re

from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Create a new version of a specification"
    )

    parser.add_argument(
        "--specification",
        type=str,
        help="Specification name (e.g., 'tree-preservation')",
        required=True,
    )

    parser.add_argument(
        "--version",
        choices=["major", "minor", "patch"],
        help="The type of version bump (major, minor, or patch)",
        required=True,
    )

    args = parser.parse_args()

    print(f"Specification: {args.specification}")
    print(f"Version: {args.version}")

    base_directory = Path(__file__).parent.parent.resolve()
    specification_directory = base_directory / "content" / "specification"

    spec_file = f"{specification_directory}/{args.specification}.md"
    if os.path.exists(spec_file):
        print(f"Specification file: {spec_file}")
        with open(spec_file, "r", encoding="utf-8") as file:
            post = frontmatter.load(file)
            current_version = post["version"]

        new_version = get_new_version(current_version, args.version)
        print(f"Current version: {current_version}")
        print(f"New {args.version} version: {new_version}")
        move_current_version(args.specification, current_version, spec_file)
        update_current_version(spec_file, new_version)
    else:
        print(f"Specification file not found: {spec_file}")
        sys.exit(-1)


def get_new_version(current_version, version_type):
    version_parts = current_version.split(".")
    if version_type == "major":
        new_version = f"{int(version_parts[0]) + 1}.0.0"
    elif version_type == "minor":
        new_version = f"{version_parts[0]}.{int(version_parts[1]) + 1}.0"
    elif version_type == "patch":
        new_version = f"{version_parts[0]}.{version_parts[1]}.{int(version_parts[2]) + 1}"
    else:
        print(f"Invalid version type: {version_type}")
        sys.exit(-1)

    return new_version


def move_current_version(specification, current_version, spec_file):
    version_with_prefix = f"v{current_version}"
    version_directory = Path(spec_file).parent / specification / version_with_prefix
    if not version_directory.exists():
        version_directory.mkdir(parents=True)
        print(f"Created directory: {version_directory}")
    new_spec_file = version_directory / Path(spec_file).name
    if not new_spec_file.exists():
        shutil.copyfile(spec_file, new_spec_file)
        print(f"Copied {spec_file} to {new_spec_file}")


def update_current_version(spec_file, new_version):
    with open(spec_file, "r", encoding="utf-8") as file:
        content = file.read()

    frontmatter_match = re.search(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not frontmatter_match:
        raise ValueError("No frontmatter found in the file")

    frontmatter = frontmatter_match.group(1)
    updated_frontmatter = re.sub(r"(?m)^version:\s*.*$", f"version: {new_version}", frontmatter)

    updated_content = content.replace(frontmatter, updated_frontmatter, 1)

    with open(spec_file, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print(f"Updated version in {spec_file}")


if __name__ == "__main__":
    main()
