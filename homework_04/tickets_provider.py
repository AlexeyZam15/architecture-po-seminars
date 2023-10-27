from homework_04.ticket import Ticket


class TicketsProvider:
    __FIELDS = {"название": "name", "количество_билетов": "available_tickets_count"}

    def __init__(self, available_tickets: list[Ticket], name: str):
        self.__available_tickets = available_tickets
        self.__name = name
        self.__available_tickets_count = len(self.__available_tickets)

    @property
    def available_tickets_count(self):
        return self.__available_tickets_count

    @property
    def name(self):
        return self.__name

    @staticmethod
    def update_ticket(ticket: Ticket):
        ticket.is_sold = True

    def get_tickets(self, fields: dict):
        if not fields:
            return self.__available_tickets.copy()
        ticket_dir = dir(self.__available_tickets[0])
        filtered_fields = {k: v for k, v in fields.items() if k in ticket_dir}

        tickets = []
        for i in self.__available_tickets:
            for j, v in filtered_fields.items():
                for k in v:
                    if k == str(getattr(i, j)):
                        tickets.append(i)
        return tickets

    @staticmethod
    def ticket_fields():
        return Ticket.fields()

    def buy_tickets(self, tickets: list[Ticket]):
        for ticket in tickets:
            ticket.is_sold = True
            self.__available_tickets.remove(ticket)
        self.__available_tickets_count = len(self.__available_tickets)

    def fields(self):
        return self.__FIELDS
