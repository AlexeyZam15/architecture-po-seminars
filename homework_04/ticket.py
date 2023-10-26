class Ticket:
    __FIELDS = {"цена": "price", "место": "place", "номер": "ticket_number", "дата": "ticket_date",
                "время": "ticket_time"}

    def __init__(self, price: float, place: int, ticket_number: int, date_: str, time_: str):
        self.__price = price
        self.__place = place
        self.__ticket_number = ticket_number
        self.__ticket_date = date_
        self.__ticket_time = time_
        self.__is_sold = True

    @property
    def is_sold(self):
        return self.__is_sold

    @is_sold.setter
    def is_sold(self, value):
        self.__is_sold = value

    @property
    def ticket_date(self):
        return self.__ticket_date

    @property
    def ticket_time(self):
        return self.__ticket_time

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
        return (f"Билет №{self.ticket_number} цена: {self.price} место: {self.place} "
                f"дата: {self.ticket_date} время: {self.ticket_time}")
