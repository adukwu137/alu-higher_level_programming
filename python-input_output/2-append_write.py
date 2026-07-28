#!/usr/bin/python3
"""
Appends a string to a text file.
"""


def append_write(filename="", text=""):
    """Appends a string to a UTF-8 text file and returns added char count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
