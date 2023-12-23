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
        self.__size = size

    @property
    def size(self):
        """
        Getter method that return the size of the square

        Return:
            int: the size of the square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter method that set the size of the square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate the area of the square

        Return:
            int: The area of the square
        """
        return self.__size ** 2
