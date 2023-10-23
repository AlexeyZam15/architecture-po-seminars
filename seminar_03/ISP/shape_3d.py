from abc import ABC, abstractmethod

from seminar_03.ISP.shape import Shape


class Shape3d(Shape, ABC):
    @property
    @abstractmethod
    def value(self) -> float:
        pass
