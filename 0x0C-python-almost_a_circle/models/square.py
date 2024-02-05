#!/usr/bin/python3
"""Module for Square lass"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """get the size of the square"""
        return self.__width
    
    @size.setter
    def size(self, value):
        """set the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """override str"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'
