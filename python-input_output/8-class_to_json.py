#!/usr/bin/python3
"""
This module contains a function that returns dictionary description for JSON.
"""


def class_to_json(obj):
    """Returns dict description with simple data structure for JSON serialization."""
    return obj.__dict__
