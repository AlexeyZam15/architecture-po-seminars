from homework_01.model_elements.camera import Camera
from homework_01.model_elements.flash import Flash
from poligonal_model import PoligonalModel


class Scene:

    def __init__(self, id_var: int, models: list[PoligonalModel], cameras: list[Camera], flashes: list[Flash] = None):
        if not models:
            raise Exception("Должна быть хотя бы 1 модель")
        if not cameras:
            raise Exception("Должна быть хотя бы 1 камера")
        self.id_var = id_var
        self.models = models
        self.flashed = flashes
        self.cameras = cameras

    @staticmethod
    def method1(type1):
        return type1

    @staticmethod
    def method(type1, type2):
        return type1
