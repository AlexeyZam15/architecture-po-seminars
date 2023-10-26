from homework_04.views.view import View


class ConsoleView(View):
    __TEXT = "Напишите параметры через пробел в формате: параметр=значение1,значение2 ..."

    def get_fields(self, fields: dict):
        print(self.__TEXT)
        print("Доступные параметры:")
        print(*fields.keys())
        list_ = [i.split("=") for i in filter(lambda x: x.count("="), input().split(" "))]
        dict_fields = {fields[i[0]]: i[1].split(",") if not i.count(",") else [i[1]] for i in list_}
        # print(f"{dict_fields = }")
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

    def intro(self, text: str):
        print(text)
