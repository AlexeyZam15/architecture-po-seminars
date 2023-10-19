from abc import ABC, abstractmethod

from seminar_02.task_01.actor import Actor


class QueueBehaviour(ABC):

    @abstractmethod
    def take_in_queue(self, actor: Actor):
        pass

    @abstractmethod
    def take_orders(self):
        pass

    @abstractmethod
    def give_orders(self):
        pass

    @abstractmethod
    def release_from_queue(self):
        pass
