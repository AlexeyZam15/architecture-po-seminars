from abc import ABC, abstractmethod

from homework_05.redactor_3d_graphics.storage.model3d import Model3D


class StorageInterface(ABC):

    @abstractmethod
    def convert(self, model3d: Model3D) -> Model3D:
        pass

    @abstractmethod
    def render(self, model3d: Model3D) -> Model3D:
        pass

    @abstractmethod
    def load(self, filename: str) -> Model3D:
        pass

    @abstractmethod
    def save(self, file_name: str, model3d: Model3D):
        pass

    @abstractmethod
    def create(self) -> Model3D:
        pass
