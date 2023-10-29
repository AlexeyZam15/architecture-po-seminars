from ..storage.storage_functions import StorageInterface
from ..view.view_inferface import ViewInterface


class Edit:
    def __init__(self, storage: StorageInterface, view: ViewInterface):
        self.__storage = storage
        self.__view = view
        self.__current_model3D = None

    def convert(self):
        self.__current_model3D = self.__storage.convert(self.__current_model3D)
        self.__storage.save(self.__view.save_model3d(), self.__current_model3D)

    def render(self):
        self.__storage.render(self.__current_model3D)

    def load(self):
        self.__current_model3D = self.__storage.load(self.__view.load_model3d())

    def create(self):
        self.__current_model3D = self.__storage.create()
        self.save()

    def save(self):
        self.__storage.save(self.__view.save_model3d(), self.__current_model3D)
