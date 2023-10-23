from seminar_03.OCP.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, max_speed: int):
        super().__init__(max_speed, "Car")

    def calculate_allowed_speed(self):
        return super().max_speed * 0.8
