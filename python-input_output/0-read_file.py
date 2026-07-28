#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to standard output."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
