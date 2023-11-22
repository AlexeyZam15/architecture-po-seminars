class User:
    def __init__(self, user_id: int, name: str):
        self.__user_id = user_id
        self.__name = name

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

