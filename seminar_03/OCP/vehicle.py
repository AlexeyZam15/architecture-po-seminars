class Vehicle:
    def __init__(self, max_speed: int, v_type: str):
        self.__max_speed = max_speed
        self.__v_type = v_type

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def v_type(self):
        return self.__v_type

    @max_speed.setter
    def max_speed(self, max_speed: int):
        self.__max_speed = max_speed

    @v_type.setter
    def v_type(self, v_type: str):
        self.__v_type = v_type

    def calculate_allowed_speed(self):
        return self.__max_speed

    def __str__(self):
        return f"Vehicle type: {self.__v_type}, allowed_speed: {self.calculate_allowed_speed()}"
