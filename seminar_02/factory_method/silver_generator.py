from seminar_02.factory_method.i_game_item import IGameItem
from seminar_02.factory_method.item_fabric import ItemFabric
from seminar_02.factory_method.silver_reward import SilverReward


class SilverGenerator(ItemFabric):
    def create_item(self) -> IGameItem:
        print("Создали сундук(серебро 🥈)")
        return SilverReward()
