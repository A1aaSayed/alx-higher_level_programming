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
        return self.width
    
    @size.setter
    def size(self, value):
        """set the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """override str"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attribute_names = ['id', 'size', 'x', 'y']
        for name, value in zip(attribute_names, args):
            setattr(self, name, value)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)
