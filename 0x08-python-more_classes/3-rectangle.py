#!/usr/bin/python3
""" Create an empty Rectangle class """


class Rectangle:
    """ Implements an empty class """
    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle with a given width and height

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method that return the width of the rectangle

        Return:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method that set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
        Getter method that return the height of the rectangle

        Return:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method that set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle

        Return:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle

        Return:
            int: The perimeter of the rectangle
        """
        return (0 if self.__width == 0 or self.__height == 0
                else 2 * (self.__width + self.__height))

    def __str__(self):
        """prints in stdout the square"""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])\
        if self.__width != 0 and self.__height != 0 else ''
