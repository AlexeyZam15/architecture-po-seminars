from homework_01.stuff.angle3d import Angle3D
from homework_01.stuff.point3d import Point3D


class Camera:
    def __init__(self, location: Point3D, angle: Angle3D):
        self.location = location
        self.angle = angle

    def rotate(self, angle3d: Angle3D):
        pass

    def move(self, point3d: Point3D):
        pass
