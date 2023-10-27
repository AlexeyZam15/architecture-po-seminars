class Customer:
    __FIELDS = {"id": "customer_id", "имя": "name"}

    def __init__(self, customer_id: int, name: str, telephone: str):
        self.__customer_id = customer_id
        self.__name = name
        self.__telephone = telephone

    @property
    def name(self):
        return self.__name

    @property
    def customer_id(self):
        return self.__customer_id

    def fields(self):
        return self.__FIELDS
