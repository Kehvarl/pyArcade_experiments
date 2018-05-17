import arcade
from random import choice
from game_world.game_map.map_factories.game_map_types import GameMapTypes
from game_world.game_map.map_factories.simple_dungeon import SimpleDungeon
from game_world.game_map.map_factories.bsp_dungeon import BSPDungeon
from game_world.entity import Entity


class Level:
    """
    Level
    All necessary information about the current game level
    """

    def __init__(self, width, height, dungeon_level=1, sprite_size=32):
        """
        Create a new Level for the Game
        :param width: Width of map in tiles
        :param height: Height of map in tiles
        :param dungeon_level:
        """
        self.width = width
        self.height = height
        self.dungeon_level = dungeon_level
        self.sprite_size = sprite_size

        self.game_map = None
        self.player = None
        self.entities = None
        self.textures = {}

        self.map_type = GameMapTypes.BSP
        self.bsp_fill = False
        self.simple_max_rooms = 5

        self.map_tile_list = None

    def generate_map(self):
        if self.map_type == GameMapTypes.BSP:
            self.game_map = BSPDungeon.generate(self.width, self.height, self.bsp_fill)
        elif self.map_type == GameMapTypes.SIMPLE:
            self.game_map = SimpleDungeon.generate(self.width, self.height, self.simple_max_rooms)

        self.map_tile_list = arcade.SpriteList()
        for y in range(self.height):
            for x in range(self.width):
                map_tile = arcade.Sprite()
                if self.game_map.tiles[x][y].block_sight:
                    if self.game_map.tiles[x][y].wall:
                        map_tile.texture = choice(self.textures['wall_tiles'])
                    else:
                        map_tile.texture = choice(self.textures['fill_tiles'])
                else:
                    map_tile.texture = choice(self.textures['floor_tiles'])
                map_tile.center_x = x * self.sprite_size + self.sprite_size / 2
                map_tile.center_y = y * self.sprite_size + self.sprite_size / 2

                self.map_tile_list.append(map_tile)

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
