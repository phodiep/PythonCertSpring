#!/usr/bin/env python

"""
Circle class -- an example class with a few properties

"""

import math


class Circle(object):
    """
    A class that defines a circle.

    You can get and set either the radius or the diameter with properties.

    setable:

    Circle.radius
    Circle.diameter

    getable:

    Circle.area

    """
    def __init__(self, radius):
        """
        Initialize a new Circle

        :param radius: the radius of the circle

        """
        self.radius = float(radius)

    @property
    def diameter(self):
        return self.radius * 2.0

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return self.radius**2 * math.pi

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __repr__(self):
        return "Circle(%f)"%self.radius

    def __str__(self):
        return "Circle Object with radius: %f"%self.radius

if __name__ == "__main__":
    import doctest
    print doctest.testmod()
