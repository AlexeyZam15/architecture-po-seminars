from seminar_02.task_01.actor import Actor


class Human(Actor):

    def __init__(self, name):
        super().__init__(name)

    def set_make_order(self, make_order: bool):
        self.is_make_order = make_order

    def set_take_order(self, take_order: bool):
        self.is_take_order = take_order

    @property
    def name(self):
        return super().name()


def main():
    h = Human("Алексей")
    print(f"{h.is_take_order}")
    print(f"{h.is_make_order}")
    h.set_take_order(True)
    h.set_make_order(True)
    print(f"{h.is_take_order}")
    print(f"{h.is_make_order}")


if __name__ == '__main__':
    main()
