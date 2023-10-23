from seminar_03.DIP.engine import Engine


class Car:
    def __init__(self, engine: Engine):
        self.__engine = engine

    @property
    def petrol_engine(self):
        return self.__engine

    def start(self):
        self.__engine.start()
