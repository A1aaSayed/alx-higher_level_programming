#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """
        Initialize the square with a given size

        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Calculate the area of the square

        Return:
            int: The area of the square
        """
        return self.__size ** 2
