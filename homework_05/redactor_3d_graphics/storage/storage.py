from storage_functions import StorageInterface
from model3d import Model3D


class Storage(StorageInterface):
    def __init__(self, models3d: list[Model3D]):
        self.models3d = models3d

    def convert(self, model3d: Model3D):
        pass

    def render(self, model3d: Model3D):
        pass

    def load(self, filename: int):
        for model3d in self.models3d:
            if model3d.file_name == filename:
                return model3d

    def save(self, file_name: int, model3d):
        for i, v in enumerate(self.models3d):
            if v.file_name == file_name:
                self.models3d[i] = model3d

    def create(self) -> Model3D:
        pass
