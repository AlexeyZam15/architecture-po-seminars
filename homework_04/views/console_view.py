from homework_04.views.view import View


class ConsoleView(View):
    __TEXT = "Напишите параметры через пробел в формате: параметр1=значение1 параметр2=значение2 ..."

    def get_fields(self, fields: list[str]):
        print(self.__TEXT)
        print("Доступные параметры:")
        print(*fields)
        fields = [i.split("=") for i in filter(lambda x: x.count("="), input().split(" "))]

        return {i[0]: i[1] for i in fields}

    def show_list(self, objects: list):
        print(*objects, sep="\n")
