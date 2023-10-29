from abc import ABC, abstractmethod


class ViewInterface(ABC):

    @abstractmethod
    def view_model3d(self):
        pass

    @abstractmethod
    def load_model3d(self) -> str:
        pass

    @abstractmethod
    def save_model3d(self) -> str:
        pass
