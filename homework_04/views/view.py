from abc import ABC, abstractmethod


class View(ABC):

    @abstractmethod
    def get_fields(self, fields: list[str]):
        pass

    @abstractmethod
    def show_list(self, list_: list):
        pass
