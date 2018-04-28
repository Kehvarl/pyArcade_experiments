from game_world.map_factories.simple_dungeon import SimpleDungeon


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
        self.generate_map()

    def generate_map(self, max_rooms=5):
        self.game_map = SimpleDungeon.generate(self.width, self.height, max_rooms)
