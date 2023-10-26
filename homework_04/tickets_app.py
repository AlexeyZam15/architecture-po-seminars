from homework_04.cash_provider import CashProvider
from homework_04.customer import Customer
from homework_04.ticket import Ticket
from homework_04.tickets_provider import TicketsProvider
from homework_04.views.view import View


class TicketsApp:

    def __init__(self, customer: Customer, cash: CashProvider, ticket_provider: TicketsProvider):
        self.__customer = customer
        self.__cash = cash
        self.__ticket_provider = ticket_provider
        self.__tickets: list[Ticket] = []
        self.__tickets_fields = Ticket.get_fields()

    @property
    def tickets_fields(self):
        return self.__tickets_fields

    @property
    def cash(self):
        return self.__cash

    @property
    def tickets(self):
        return self.__tickets

    def buy_ticket(self, ticket: Ticket):
        if self.__cash.buy(ticket.price):
            self.__tickets.append(ticket)

    def search_ticket(self, fields: dict):
        return self.__ticket_provider.get_tickets(fields)

    def authorization(self):
        self.__cash.is_authorization = True

    def deathorization(self):
        self.__cash.is_authorization = False
