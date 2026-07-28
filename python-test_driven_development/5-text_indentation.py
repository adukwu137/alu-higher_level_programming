#!/usr/bin/python3
"""
Module containing text_indentation function.
Prints text with two new lines after '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints text with two new lines after '.', '?', and ':'.

    Args:
        text: String to print and format

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in [".", "?", ":"]:
            if text[c] in [".", "?", ":"]:
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
