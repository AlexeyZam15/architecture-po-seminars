from abc import ABC, abstractmethod

from seminar_02.task_01.actor import Actor


class MarketBehaviour(ABC):
    @abstractmethod
    def accept_to_market(self, actor: Actor):
        pass

    @abstractmethod
    def release_from_market(self, actors: list[Actor]):
        pass

    @abstractmethod
    def update(self):
        pass
