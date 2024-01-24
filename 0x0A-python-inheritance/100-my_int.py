#!/usr/bin/python3
"""Module"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        """equal method"""
        return super().__ne__(other)
    def __ne__(self, other):
        """negative method"""
        return super().__eq__(other)
