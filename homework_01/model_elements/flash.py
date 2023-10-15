from homework_01.stuff.angle3d import Angle3D
from homework_01.stuff.color import Color
from homework_01.stuff.point3d import Point3D


class Flash:
    def __init__(self, location: Point3D, angle: Angle3D, color: Color, power: float):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, angle3d: Angle3D):
        pass

    def move(self, point3d: Point3D):
        pass
