#!/usr/bin/python3
"""Module for Square Class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Instantiation with size

        Args:
            size: size of the square
        """
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """compute area of the square"""
        return self.__size ** 2

    def __str__(self):
        """print the square size"""
        return (f'[Square] {self.__size}/{self.__size}')
