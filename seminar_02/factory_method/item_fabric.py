from abc import ABC, abstractmethod

from seminar_02.factory_method.i_game_item import IGameItem


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self) -> IGameItem:
        pass
