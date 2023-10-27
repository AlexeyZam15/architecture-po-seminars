"""
Содержит класс для взаимодействия пользователя с терминалом.
"""
from homework_04.views.view import View


class ConsoleView(View):
    """
    Класс консольного представления. Требуется для взаимодействия пользователя с терминалом.
    """
    __TEXT = "Напишите параметры через пробел в формате: параметр=значение1,значение2 ..."

    def get_fields(self, fields: dict):
        print(self.__TEXT)
        print("Доступные параметры:")
        print(*fields.keys())
        list_ = [i.split("=") for i in filter(lambda x: x.count("="), input().split(" "))]
        dict_fields = {fields[i[0]]: i[1].split(",") if not i.count(",") else [i[1]] for i in list_}
        return dict_fields

    def show_list(self, objects: list, text: str = ""):
        if text:
            print(text)
        print(*objects, sep="\n")

    def confirmation(self, text: str):
        print(text)
        res = input("Введите y для подтверждения: ").lower() == "y"
        return res

    def show_text(self, text: str):
        print(text)

    def intro(self):
        print("Добро пожаловать в приложение TicketsApp.")

    def authorization(self, authorization_function):
        print("Авторизация пользователя")
        if authorization_function():
            print("Авторизация прошла успешно")
            return True
        print("Авторизоваться не удалось")
        return False

    def search_tickets(self, fields: dict):
        print("Сначала нужно отобрать билеты.")
        return self.get_fields(fields)

    def show_data(self, data: dict[dict]):
        for k, v in data.items():
            print(k, end=": ")
            for k1, v1 in v.items():
                print(f"{k1}: {v1}", end=" ")
            print()
