#!/usr/bin/python3
"""Module for Square lass"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the square"""
        return self.__width
    
    @size.setter
    def size(self, value):
        """set the size of the square"""
        self.__width = value
        self.__height = value
