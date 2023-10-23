class CalculateSalary:

    def __init__(self, base_salary: int, value_time: int):
        self.baseSalary = base_salary
        self.value_time = value_time

    def calculate_salary(self) -> int:
        return self.value_time * 1000
