#!/usr/bin/python3
""" Create an empty Rectangle class """


class Rectangle:
    """ Implements an empty class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle with a given width and height

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() > rect_2.area() else rect_2

    def __str__(self):
        """Informal and nicely printable string representation of rectangle"""
        return '\n'.join([str(self.print_symbol) * self.__width
                          for _ in range(self.__height)]
                         if self.__height != 0 and self.__width != 0 else '')

    def __repr__(self):
        """Official string representation of rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Delete Instance of Rectangle"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
