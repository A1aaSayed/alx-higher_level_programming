#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """
    Adds two integers or floats together

    Args:
        a (int): An integer or float
        b (int): An integer or float

    Return:
        The addition of a and b as an integer.

    Raises: TypeError: If a or b is not an integer or float.
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError('a must be an integer')
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
