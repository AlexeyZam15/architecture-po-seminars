"""
Содержит абстрактный класс представления.
"""
from abc import ABC, abstractmethod


class View(ABC):
    """
    Абстрактный класс представления
    """

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
    def intro(self):
        pass

    @abstractmethod
    def authorization(self, authorization_function):
        pass

    @abstractmethod
    def search_tickets(self, fields: dict):
        pass

    @abstractmethod
    def show_data(self, data: dict[dict]):
        pass
