# Абстрактный класс Actor, который хранит в себе параметры актора, включая состояние готовности сделать заказ и факт
#    получения заказа. Дополнение: для большего понимания, можно сделать методы-геттеры для имени и прочих “персональных
#    данных” abstract

from abc import ABC, abstractmethod

from seminar_02.task_01.actor_behavior import ActorBehavior


class Actor(ActorBehavior, ABC):
    def __init__(self, name: str):
        self._name = name
        self._is_take_order = False
        self._is_make_order = False

    def __str__(self):
        return self._name

    @abstractmethod
    def name(self):
        return self._name

    @property
    def is_make_order(self) -> bool:
        return self._is_make_order

    @is_make_order.setter
    def is_make_order(self, make_order: bool):
        self._is_make_order = make_order

    @property
    def is_take_order(self) -> bool:
        return self._is_take_order

    @is_take_order.setter
    def is_take_order(self, take_order: bool):
        self._is_take_order = take_order
