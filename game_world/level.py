from game_world.game_map.map_factories.game_map_types import GameMapTypes
from game_world.game_map.map_factories.simple_dungeon import SimpleDungeon

from game_world.game_map.map_factories.bsp_dungeon import BSPDungeon


class Level:
    """
    Level
    All necessary information about the current game level
    """

    def __init__(self, width, height, dungeon_level=1):
        """
        Create a new Level for the Game
        :param width: Width of map in tiles
        :param height: Height of map in tiles
        :param dungeon_level:
        """
        self.width = width
        self.height = height
        self.dungeon_level = dungeon_level
        self.game_map = None
        self.player = None

        self.map_type = GameMapTypes.BSP
        self.bsp_fill = False
        self.simple_max_rooms = 5

    def generate_map(self):
        if self.map_type == GameMapTypes.BSP:
            self.game_map = BSPDungeon.generate(self.width, self.height, self.bsp_fill)
        elif self.map_type == GameMapTypes.SIMPLE:
            self.game_map = SimpleDungeon.generate(self.width, self.height, self.simple_max_rooms)
