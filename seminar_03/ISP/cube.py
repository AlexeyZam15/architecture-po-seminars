from seminar_03.ISP.shape_3d import Shape3d


class Cube(Shape3d):

    def __init__(self, side: int):
        self.__side = side

    @property
    def side(self):
        return self.__side

    @property
    def perimeter(self):
        return self.__side * 12

    @property
    def value(self) -> float:
        return self.__side ** 3
