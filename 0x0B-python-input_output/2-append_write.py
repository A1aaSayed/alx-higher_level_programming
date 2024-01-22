#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Function to append to the end of a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        tell = f.tell()
    return tell
