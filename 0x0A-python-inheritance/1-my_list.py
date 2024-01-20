#!/usr/bin/python3
"""Implementation for MyList class"""


class MyList(list):
    """Sub-Class from list"""
    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
