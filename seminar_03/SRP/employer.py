class Employer:
    def __init__(self, name: str, value_time: int):
        self.name = name

    def __str__(self):
        return f"Employer: {self.name}"
