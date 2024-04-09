#!/usr/bin/python3

# 2-rectangle.py
# created by Osaro. e

""" The class Rectangle """


class Rectangle:
    """ In the rectangle class i've added two more methods (Area and perimeter)
    both used to perform calculations on the Rectangle object """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'
        return rectangle_str.rstrip()
    def __repr(self):
        return f"Rectangle(width={self.__width}, height={self.__height})"
