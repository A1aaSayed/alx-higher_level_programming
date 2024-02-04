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
    def x(self):
        """get the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""
        self.__x = value

    @property
    def y(self):
        """get the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""
        self.__y = value
