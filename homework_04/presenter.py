from homework_04.tickets_app import TicketsApp
from homework_04.views.view import View


class Presenter:
    def __init__(self, view: View, tickets_app: TicketsApp):
        self.__view = view
        self.__tickets_app = tickets_app

    def start(self):
        self.__view.intro("Добро пожаловать в приложение TicketsApp.")
        self.__view.show_text("Сначала нужно отобрать билеты.")
        tickets = self.__tickets_app.search_ticket(self.__view.get_fields(self.__tickets_app.tickets_fields))
        self.__view.show_list(tickets)
        if self.__view.confirmation("Хотите купить эти билеты?"):
            if self.__tickets_app.buy_tickets(tickets):
                self.__view.show_text("Билеты куплены")
            else:
                self.__view.show_text("Не удалось купить билеты")
        self.__view.show_list(self.__tickets_app.search_ticket({}), "Оставшиеся билеты")
