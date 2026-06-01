#!/usr/bin/env python3

# reformat markdown files which may have been hand-edited
# with the intention of making further changes simpler to see in a diff

# - ensure files are encoded in utf-8
# - indent frontmatter consistently
# - replace None values with an empty string ''
# - normalise strings, preserving markdown formatting

# Depends on PyYAML >= 6.0.0

import glob
import re
import sys
import yaml

FRONTMATTER_RE = re.compile(r"^---[ \t]*\n(.*?)\n---[ \t]*\n?(.*)", re.DOTALL)


class _NormalisedDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow=flow, indentless=False)


def _str_representer(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_NormalisedDumper.add_representer(str, _str_representer)


def _dump(data):
    return yaml.dump(
        data,
        Dumper=_NormalisedDumper,
        default_flow_style=False,
        indent=2,
        sort_keys=True,
        allow_unicode=True,
        width=4096,
    )


def normalise_frontmatter(text):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return text

    fm_text, body = match.group(1), match.group(2)
    data = yaml.safe_load(fm_text)

    if not isinstance(data, dict):
        return text

    normalised_fm = _dump(data)
    return f"---\n{normalised_fm}---\n{body}"


if __name__ == "__main__":
    for path in glob.glob("content/*/*.md"):
        with open(path) as f:
            content = f.read()
        normalised = normalise_frontmatter(content)
        with open(path, "w") as f:
            f.write(normalised)
