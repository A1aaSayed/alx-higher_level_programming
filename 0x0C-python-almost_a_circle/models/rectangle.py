#!/usr/bin/python3
"""Module for Rectangle lass"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        self.__height = value

    @property
    def __x(self):
        """get the __x of the rectangle"""
        return self.__x

    @__x.setter
    def __x(self, value):
        """set the __x of the rectangle"""
        self.__x = value

    @property
    def __y(self):
        """get the __y of the rectangle"""
        return self.__y

    @__y.setter
    def __y(self, value):
        """set the __y of the rectangle"""
        self.__y = value
