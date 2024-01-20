#!/usr/bin/python3
"""MyList Class"""


class MyList(list):
    """Sub class from list"""
    def print_sorted(self):
        """Function to print list"""
        print(sorted(self))
