from seminar_02.factory_method.i_game_item import IGameItem


class SilverReward(IGameItem):
    def open(self):
        print("Открыли сундук с серебром 🥈")
