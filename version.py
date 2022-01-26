#!/usr/bin/env python3
"""
Use `git` executable on PATH to print current commit hash of working directory
"""
import sys
import subprocess


def get_version():
    try:
        return (
            subprocess.check_output(["git", "show", "-s", "--format=%h"])[:-1].decode("utf-8")
        )
    except subprocess.CalledProcessError:
        print("Unable to get current commit hash from git show")
        sys.exit(1)


if __name__ == "__main__":
    print(get_version())
