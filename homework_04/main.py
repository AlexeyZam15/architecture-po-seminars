from datetime import datetime

from homework_04.cash_provider import CashProvider
from homework_04.customer import Customer
from homework_04.presenter import Presenter
from homework_04.ticket import Ticket
from homework_04.tickets_app import TicketsApp
from homework_04.tickets_provider import TicketsProvider
from homework_04.views.console_view import ConsoleView

customer = Customer(1, "Алексей")
cash_provider = CashProvider(345345345)
available_tickets = [Ticket(i * 10000, i * 10, i, datetime.now().replace(microsecond=0)) for i in range(1, 11)]
tickets_provider = TicketsProvider(available_tickets)

p = Presenter(ConsoleView(), TicketsApp(customer, cash_provider, tickets_provider))
p.start()
