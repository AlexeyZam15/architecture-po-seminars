from seminar_02.factory_method.i_game_item import IGameItem


class GemReward(IGameItem):
    def open(self):
        print("Открыли сундук с изумрудом 💚")
