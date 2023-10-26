from datetime import datetime


class Ticket:
    __FIELDS = {"цена": "price", "место": "place", "номер": "ticket_number", "дата": "ticket_datetime"}

    def __init__(self, price: float, place: int, ticket_number: int, date_time: datetime):
        self.__price = price
        self.__place = place
        self.__ticket_number = ticket_number
        self.__ticket_datetime = date_time
        self.__is_sold = True

    @property
    def is_sold(self):
        return self.__is_sold

    @is_sold.setter
    def is_sold(self, value):
        self.__is_sold = value

    @property
    def ticket_datetime(self):
        return self.__ticket_datetime

    @property
    def price(self):
        return self.__price

    @property
    def place(self):
        return self.__place

    @property
    def ticket_number(self):
        return self.__ticket_number

    @staticmethod
    def get_fields():
        return Ticket.__FIELDS

    def __str__(self):
        return f"Билет №{self.ticket_number} цена: {self.price} место: {self.place} дата: {self.ticket_datetime}"