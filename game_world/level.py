from game_world.game_map.map_factories.game_map_types import GameMapTypes
from game_world.game_map.map_factories.simple_dungeon import SimpleDungeon
from game_world.game_map.map_factories.bsp_dungeon import BSPDungeon
from game_world.entity import Entity


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
        self.entities = None

        self.map_type = GameMapTypes.BSP
        self.bsp_fill = False
        self.simple_max_rooms = 5

    def generate_map(self):
        if self.map_type == GameMapTypes.BSP:
            self.game_map = BSPDungeon.generate(self.width, self.height, self.bsp_fill)
        elif self.map_type == GameMapTypes.SIMPLE:
            self.game_map = SimpleDungeon.generate(self.width, self.height, self.simple_max_rooms)

    def populate_map(self):
        self.entities = []
        for e in range(5):
            x, y = self.game_map.random_room().random_point()
            entity = Entity(x, y, "Orc")
            self.entities.append(entity)

    def update(self):
        for entity in self.entities:
            self.move(entity)

    def move(self, entity):
        x = entity.x
        y = entity.y
        dx = entity.dx
        dy = entity.dy
        if not self.game_map.tiles[x+dx][y+dy].block_move:
            entity.x += dx
            entity.y += dy
