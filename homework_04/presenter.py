from homework_04.tickets_app import TicketsApp
from homework_04.views.view import View


class Presenter:
    def __init__(self, view: View, tickets_app: TicketsApp):
        self.__view = view
        self.__tickets_app = tickets_app

    def start(self):
        print("Добро пожаловать в приложение TicketsApp.")
        print("Сначала нужно отобрать билеты.")
        self.__view.show_list(
            self.__tickets_app.search_ticket(self.__view.get_fields(self.__tickets_app.tickets_fields.keys())))
