#!/usr/bin/python3
"""MyList Class that inherits from list"""


class MyList(list):
    """Sub-Class from list"""
    def print_sorted(self):
        """Function to print list"""
        print(sorted(self))
