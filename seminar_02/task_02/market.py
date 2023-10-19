from seminar_02.task_01.actor import Actor
from seminar_02.task_02.market_behaviour import MarketBehaviour
from seminar_02.task_02.queue_behaviour import QueueBehaviour


class Market(MarketBehaviour, QueueBehaviour):

    def __init__(self):
        self.__queue: list[Actor] = []

    def accept_to_market(self, actor: Actor):
        print(actor.name, "пришёл в магазин")
        self.take_in_queue(actor)

    def release_from_market(self, actors: list[Actor]):
        for actor in actors:
            print(actor.name, "вышел из магазина")
            self.__queue.remove(actor)

    def take_in_queue(self, actor: Actor):
        print(actor.name, "встал в очередь")
        self.__queue.append(actor)

    def take_orders(self):
        for actor in self.__queue:
            if not actor.is_make_order:
                actor.set_make_order(True)
                print(actor.name, "сделал свой заказ")

    def give_orders(self):
        for actor in self.__queue:
            if actor.is_make_order:
                actor.set_take_order(True)
                print(actor.name, "получил свой заказ")

    def release_from_queue(self):
        released_actors = []
        for actor in self.__queue:
            if actor.is_take_order:
                released_actors.append(actor)
                print(actor.name, "вышел из очереди и готов уходить")
        self.release_from_market(released_actors)

    def update(self):
        self.take_orders()
        self.give_orders()
        self.release_from_queue()
