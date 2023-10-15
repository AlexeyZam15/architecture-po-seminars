from poligon import Poligon, Point3D
from texture import Texture


class PoligonalModel:
    def __init__(self, textures: list[Texture] = None):
        self.textures = textures
        self.poligons = []
        self.poligons.append(Poligon([Point3D()]))
