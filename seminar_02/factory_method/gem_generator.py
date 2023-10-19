from seminar_02.factory_method.gem_reward import GemReward
from seminar_02.factory_method.i_game_item import IGameItem
from seminar_02.factory_method.item_fabric import ItemFabric


class GemGenerator(ItemFabric):
    def create_item(self) -> IGameItem:
        print("Создали сундук(изумруды 💚)")
        return GemReward()
