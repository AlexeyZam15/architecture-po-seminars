from homework_04.customer import Customer


class CashProvider:
    def __init__(self, card: int, balance: int):
        self.__card = card
        self.__balance = balance
        # self.__is_authorization = False

    @property
    def card(self):
        return self.__card

    # @property
    # def is_authorization(self):
    #     return self.__is_authorization
    #
    # @is_authorization.setter
    # def is_authorization(self, value):
    #     self.__is_authorization = value

    # def withdraw(self, amount: int):
    #     if self.__is_authorization and amount < self.__balance:
    #         self.__balance -= amount
    #         return True
    #     return False
    #
    # def deposit(self, amount: int):
    #     if self.__is_authorization:
    #         self.__balance += amount
    #         return True
    #     return False

    def buy(self, price: int):
        # if self.__is_authorization:
        if self.__balance >= price:
            self.__balance -= price
            return True
        return False
