from abc import ABC, abstractmethod


class ActorBehavior(ABC):
    @abstractmethod
    def set_make_order(self, make_order: bool):
        pass

    @abstractmethod
    def set_take_order(self, take_order: bool):
        pass

    @abstractmethod
    def is_make_order(self) -> bool:
        pass

    @abstractmethod
    def is_take_order(self) -> bool:
        pass
