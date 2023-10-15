from homework_01.in_memory_model.i_model_changed_observer import IModelChangedObserver
from homework_01.in_memory_model.i_model_changer import IModelChanger
from homework_01.model_elements.camera import Camera
from homework_01.model_elements.flash import Flash
from homework_01.model_elements.poligonal_model import PoligonalModel
from homework_01.model_elements.scene import Scene
from homework_01.stuff.angle3d import Angle3D
from homework_01.stuff.color import Color
from homework_01.stuff.point3d import Point3D


class ModelStore(IModelChanger):
    def __init__(self, changed_observers: IModelChangedObserver = None):
        self.models = [PoligonalModel()]
        self.flashes = [Flash(Point3D(), Angle3D(), Color(), 0.5)]
        self.cameras = [Camera(Point3D(), Angle3D())]
        self.scenes = [Scene(0, self.models, self.cameras, self.flashes)]
        self.__changed_observers = changed_observers

    def get_scene(self, id_var: int):
        for i in self.scenes:
            if i.id_var == id_var:
                return i

    def notify_change(self, i_model_changer: IModelChanger):
        pass
