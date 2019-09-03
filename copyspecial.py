#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import sys
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "Zachary Kline with help from ---"


# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dir):
    """Returns a list of absolute paths of the special files
    in the given directory"""
    listed = os.listdir(dir)
    path_list = []
    for files in listed:
        if re.findall(r'__(\w+)__', files):
            path_list.append(files)
        else:
            continue
    return path_list


def copy_to(paths, dir):
    """given a list of paths, copies those files into the given directory"""
    """shutil.copy() seems to be the right way to go about the copying,
    I guess I should also check if there is a directory."""
    # if the directory doesn't exist it will make a new directory for the files
    if not os.path.exists(dir):
        os.mkdir(dir)
    for path in paths:
        new_file = os.path.basename(path)
        shutil.copy(path, os.path.join(dir, new_file))


def zip_to(paths, zippath):
    """given a list of paths, zip those files up into the given zipfile"""
    # Use subprocess to rub the command line version of this
    cmd = ['zip', '-j', zippath]
    cmd.extend(paths)
    print('Command I\'m going to do: {}'.format(cmd))
    subprocess.call(cmd)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directory to search')
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    if not args:
        parser.print_usage()
        sys.exit(1)

    todir = args.todir
    tozip = args.tozip
    from_dir = args.from_dir

    special_paths = get_special_paths(from_dir)

    if todir:
        copy_to(special_paths, todir)
    elif tozip:
        zip_to(special_paths, tozip)
    else:
        for path in special_paths:
            print(path)
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
