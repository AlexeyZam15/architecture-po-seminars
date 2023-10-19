from seminar_02.factory_method.gold_reward import GoldReward
from seminar_02.factory_method.i_game_item import IGameItem
from seminar_02.factory_method.item_fabric import ItemFabric


class GoldGenerator(ItemFabric):
    def create_item(self) -> IGameItem:
        print("Создали сундук(золото 🥇)")
        return GoldReward()
