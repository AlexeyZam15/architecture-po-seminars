from abc import ABC, abstractmethod


class Shape(ABC):
    @property
    @abstractmethod
    def perimeter(self):
        pass
