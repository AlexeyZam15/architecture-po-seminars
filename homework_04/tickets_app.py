from homework_04.cash_provider import CashProvider
from homework_04.customer import Customer
from homework_04.tickets_provider import TicketsProvider


class TicketsApp:

    def __init__(self, customer: Customer, cash: CashProvider, ticket_provider: TicketsProvider):
        self.__customer = customer
        self.__cash = cash
        self.__ticket_provider = ticket_provider
        self.__tickets = []
        self.__tickets_fields = self.__ticket_provider.get_fields()

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
        self.__cash.is_authorization = True

    def deathorization(self):
        self.__cash.is_authorization = False
