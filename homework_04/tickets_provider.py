from homework_04.ticket import Ticket


class TicketsProvider:

    def __init__(self, available_tickets: list[Ticket]):
        self.__available_tickets = available_tickets

    @staticmethod
    def update_ticket(ticket: Ticket):
        ticket.is_sold = True

    def get_tickets(self, search_fields: dict):
        if not search_fields:
            return self.__available_tickets.copy()
        ticket_dir = dir(self.__available_tickets[0])
        search_fields = list(filter(lambda x: x in ticket_dir, search_fields))
        tickets = []
        for i in self.__available_tickets:
            for j in search_fields:
                if search_fields[j] == getattr(i, j):
                    tickets.append(i)
        return tickets
