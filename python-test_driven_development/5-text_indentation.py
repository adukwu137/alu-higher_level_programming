#!/usr/bin/python3
"""
Module containing text_indentation function.
Prints a text with 2 new lines after each of: ., ? and :
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.
    Trims leading and trailing spaces on printed lines.

    Args:
        text: String to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    length = len(text)
    while c < length and text[c] == ' ':
        c += 1

    while c < length:
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < length and text[c] == ' ':
                c += 1
            continue
        c += 1
