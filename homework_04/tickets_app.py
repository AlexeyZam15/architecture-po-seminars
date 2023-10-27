from homework_04.cash_provider import CashProvider
from homework_04.customer import Customer
from homework_04.tickets_provider import TicketsProvider


class TicketsApp:

    def __init__(self, customer: Customer, cash: CashProvider, ticket_provider: TicketsProvider):
        self.__customer = customer
        self.__cash = cash
        self.__ticket_provider = ticket_provider
        self.__tickets = []
        self.__tickets_fields = self.__ticket_provider.ticket_fields()
        self.__is_authorized = False

    @property
    def tickets_fields(self):
        return self.__tickets_fields

    @property
    def cash(self):
        return self.__cash

    @property
    def tickets(self):
        return self.__tickets

    def buy_tickets(self, tickets: list):
        if self.__cash.buy(sum([ticket.price for ticket in tickets])):
            self.__ticket_provider.buy_tickets(tickets)
            self.__tickets.extend(tickets)
            return True

    def search_ticket(self, fields: dict):
        return self.__ticket_provider.get_tickets(fields)

    def authorization(self):
        self.__is_authorized = True
        self.__cash.authorization()
        return True

    def deauthorization(self):
        self.__is_authorized = False
        self.__cash.deauthorization()
        return False

    @staticmethod
    def get_object_fields(object_name):
        dict_ = {k: getattr(object_name, v) for k, v in object_name.fields().items()}
        return dict_

    def get_data(self):
        dict_ = {"Пользователь": self.get_object_fields(self.__customer),
                 "Карта": self.get_object_fields(self.__cash),
                 "Поставщик билетов": self.get_object_fields(self.__ticket_provider)
                 }
        return dict_
