"""
Содержит класс для оплаты услуг.
"""


class CashProvider:
    """Класс для оплаты услуг. Для выполнения действий требуется авторизация"""
    __FIELDS = {"карта": "card", "баланс": "balance"}

    def __init__(self, card: int, balance: int):
        self.__card = card
        self.__balance = balance
        self.__is_authorized = False

    @property
    def is_authorized(self):
        return self.__is_authorized

    @property
    def balance(self):
        if self.__is_authorized:
            return self.__balance

    @property
    def card(self):
        if self.__is_authorized:
            return self.__card

    def buy(self, price: int):
        if self.__is_authorized:
            if self.__balance >= price:
                self.__balance -= price
                return True
        return False

    def authorization(self):
        self.__is_authorized = True
        return True

    def deauthorization(self):
        self.__is_authorized = False
        return False

    def fields(self):
        return self.__FIELDS
