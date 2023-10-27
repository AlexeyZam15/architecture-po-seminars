from homework_04.ticket import Ticket


class TicketsProvider:
    __FIELDS = {"название": "name", "количество_билетов": "available_tickets_count"}

    def __init__(self, available_tickets: list[Ticket], name: str):
        self.__available_tickets = available_tickets
        self.__sold_tickets: list[Ticket] = []
        self.__name = name

    @property
    def sold_tickets(self):
        return self.__sold_tickets

    @property
    def available_tickets_count(self):
        return len(self.__available_tickets)

    @property
    def name(self):
        return self.__name

    def get_tickets(self, search_fields: dict):
        if not search_fields:
            return self.__available_tickets.copy()
        ticket_dir = dir(self.__available_tickets[0])
        filtered_fields = {k: v for k, v in search_fields.items() if k in ticket_dir}

        tickets = []
        for i in self.__available_tickets:
            for j, v in filtered_fields.items():
                for k in v:
                    if k == str(getattr(i, j)):
                        tickets.append(i)
        return tickets

    def sell_tickets(self, tickets: list[Ticket]):
        for ticket in tickets:
            ticket.is_sold = True
            self.__sold_tickets.append(ticket)
            self.__available_tickets.remove(ticket)

    def fields(self):
        return self.__FIELDS
