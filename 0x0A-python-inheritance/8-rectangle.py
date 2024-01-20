#!/usr/bin/python3
"""Rectangle Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height
