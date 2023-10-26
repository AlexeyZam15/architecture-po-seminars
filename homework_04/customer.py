class Customer:
    def __init__(self, customer_id: int, name: str):
        self.__customer_id = customer_id
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def customer_id(self):
        return self.__customer_id
