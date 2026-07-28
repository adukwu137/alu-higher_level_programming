#!/usr/bin/python3
"""
Returns dictionary description for JSON.
"""


def class_to_json(obj):
    """Returns dict description with simple data structure for JSON."""
    return obj.__dict__
