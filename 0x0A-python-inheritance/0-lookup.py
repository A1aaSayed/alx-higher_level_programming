#!/usr/bin/python3
""" lookup function """


def lookup(obj):
    """
    Function that returns a list containing the available
    attributes and methods of an object.
    """
    return [attribute for attribute in dir(obj)]
