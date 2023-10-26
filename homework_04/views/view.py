from abc import ABC, abstractmethod


class View(ABC):

    @abstractmethod
    def get_fields(self, fields: dict):
        pass

    @abstractmethod
    def show_list(self, list_: list, text: str = ""):
        pass

    @abstractmethod
    def confirmation(self, text: str):
        pass

    @abstractmethod
    def show_text(self, text: str):
        pass

    @abstractmethod
    def intro(self, text: str):
        pass
