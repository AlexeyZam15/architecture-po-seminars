from homework_04.tickets_app import TicketsApp
from homework_04.views.view import View


class Presenter:
    def __init__(self, view: View, tickets_app: TicketsApp):
        self.__view = view
        self.__tickets_app = tickets_app
        self.__actions = {"Данные аккаунта"}

    def start(self):
        self.__view.intro()
        self.__view.authorization(self.__tickets_app.authorization)
        self.__view.show_data(self.__tickets_app.get_data())
        tickets = self.__tickets_app.search_ticket(self.__view.search_tickets(self.__tickets_app.tickets_fields))
        self.__view.show_list(tickets)
        if self.__view.confirmation("Хотите купить эти билеты?"):
            if self.__tickets_app.buy_tickets(tickets):
                self.__view.show_text("Билеты куплены")
            else:
                self.__view.show_text("Не удалось купить билеты")
        self.__view.show_list(self.__tickets_app.search_ticket({}), "Оставшиеся билеты")
        self.__view.show_data(self.__tickets_app.get_data())
