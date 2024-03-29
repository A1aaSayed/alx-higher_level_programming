#!/usr/bin/python3
"""Rectangle Class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """Instantiation with width and height

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
