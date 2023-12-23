#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a given size

        Args:
            size (int): size of the square
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """prints in stdout the square"""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print('#' * self.__size)

    @property
    def position(self):
        """
        Getter method that return the position of the square

        Return:
            tuple: the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method that set the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
