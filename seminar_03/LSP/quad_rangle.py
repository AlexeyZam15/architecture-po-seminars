from abc import ABC, abstractmethod


class QuadRangle(ABC):
    @property
    @abstractmethod
    def area(self) -> int:
        pass
