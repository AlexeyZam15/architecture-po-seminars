from homework_04.ticket import Ticket


class TicketsProvider:

    def __init__(self, available_tickets: list[Ticket]):
        self.__available_tickets = available_tickets

    @staticmethod
    def update_ticket(ticket: Ticket):
        ticket.is_sold = True

    def get_tickets(self, fields: dict):
        if not fields:
            return self.__available_tickets.copy()
        ticket_dir = dir(self.__available_tickets[0])
        # print(f"{ticket_dir = }")
        # print(f"{fields = }")
        filtered_fields = {k: v for k, v in fields.items() if k in ticket_dir}
        # print(f"{filtered_fields = }")
        tickets = []
        for i in self.__available_tickets:
            for j, v in filtered_fields.items():
                for k in v:
                    # print(f"{k = } {getattr(i, j) = }")
                    if k == str(getattr(i, j)):
                        tickets.append(i)
        return tickets

    @staticmethod
    def get_fields():
        return Ticket.get_fields()

    def buy_tickets(self, tickets: list[Ticket]):
        for ticket in tickets:
            ticket.is_sold = True
            self.__available_tickets.remove(ticket)
