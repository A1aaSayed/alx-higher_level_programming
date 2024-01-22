#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Function to append to the end of a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        before_append = f.tell()
        f.write(text)
        after_append = f.tell()
        tell = after_append - before_append

    return tell
