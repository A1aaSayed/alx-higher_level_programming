#!/usr/bin/python3
"""function that write a string to file (UTF8)"""


def write_file(filename="", text=""):
    """function that write a string to file (UTF8)"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        tell = f.tell()

    return tell
