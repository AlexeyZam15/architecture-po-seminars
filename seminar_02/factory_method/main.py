import random

from seminar_02.factory_method.diamond_generator import DiamondGenerator
from seminar_02.factory_method.gem_generator import GemGenerator
from seminar_02.factory_method.gold_generator import GoldGenerator
from seminar_02.factory_method.i_game_item import IGameItem
from seminar_02.factory_method.item_fabric import ItemFabric
from seminar_02.factory_method.silver_generator import SilverGenerator

generators = [GoldGenerator, GemGenerator, DiamondGenerator, SilverGenerator]

fabric_list: [ItemFabric] = [i() for i in generators]

for i in range(20):
    index = random.randint(0, len(fabric_list) - 1)
    fabric: IGameItem = fabric_list[index].create_item()
    fabric.open()
