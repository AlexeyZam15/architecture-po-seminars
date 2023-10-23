from seminar_03.OCP.vehicle import Vehicle


class Bus(Vehicle):

    def __init__(self, max_speed: int):
        super().__init__(max_speed, "Bus")

    def calculate_allowed_speed(self):
        return super().max_speed * 0.5
