from seminar_02.factory_method.diamond_reward import DiamondReward
from seminar_02.factory_method.i_game_item import IGameItem
from seminar_02.factory_method.item_fabric import ItemFabric


class DiamondGenerator(ItemFabric):
    def create_item(self) -> IGameItem:
        print("Создали сундук(алмазы 💎)")
        return DiamondReward()
