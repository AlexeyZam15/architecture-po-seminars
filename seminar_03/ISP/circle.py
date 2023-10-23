import math

from seminar_03.ISP.shape import Shape


class Circle(Shape):
    def __init__(self, radius: int):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.__radius
