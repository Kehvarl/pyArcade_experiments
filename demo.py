"""
Starting Template
"""
import os
import json

import arcade

from game_world.game_map.map_factories.game_map_types import GameMapTypes
from game_world.level import Level
from game_world.entity import Entity

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAZE_WIDTH = 40
MAZE_HEIGHT = 30

NATIVE_SPRITE_SIZE = 32
SPRITE_SCALING = (SCREEN_HEIGHT / MAZE_HEIGHT) / NATIVE_SPRITE_SIZE
SPRITE_SIZE = NATIVE_SPRITE_SIZE * SPRITE_SCALING


# noinspection PyAbstractClass
class ArcadeDemo(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, dungeon):
        super().__init__(width, height, "Roguelike Demo", resizable=True)

        arcade.set_background_color(arcade.color.BLACK)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.dungeon = dungeon

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.kobold_texture = None

    def setup(self):
        # Create your sprites and sprite lists here
        with open("tileset/tileset.json", "r") as tileset_config:
            tileset = json.load(tileset_config)

        for section, tiles in tileset.items():
            if not self.dungeon.textures.get("section", False):
                self.dungeon.textures[section] = []

            for texture in tiles:
                self.dungeon.textures[section].append(arcade.load_texture(file_name=texture,
                                                                          scale=SPRITE_SCALING))

        self.kobold_texture = arcade.load_texture(file_name="tileset/orc_new.png",
                                                  scale=SPRITE_SCALING)

        self.dungeon.map_tile_list = arcade.SpriteList()
        self._load_map()

    def _load_map(self):
        self.dungeon.generate_map()
        self.dungeon.populate_map()
        self.dungeon.player.x = self.dungeon.game_map.start_x
        self.dungeon.player.y = self.dungeon.game_map.start_y

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.dungeon.map_tile_list.draw()
        self.dungeon.entities.draw()
        self.dungeon.player.draw()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.dungeon.move(self.dungeon.player)
        self.dungeon.player.update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.color.html
        """
        if key == arcade.key.LEFT:
            self.dungeon.player.dx = -1
        if key == arcade.key.RIGHT:
            self.dungeon.player.dx = 1
        if key == arcade.key.UP:
            self.dungeon.player.dy = 1
        if key == arcade.key.DOWN:
            self.dungeon.player.dy = -1

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.dungeon.player.dx = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.dungeon.player.dy = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        """ User moves the scroll wheel. """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        self._load_map()


if __name__ == "__main__":
    test_map = Level(MAZE_WIDTH, MAZE_HEIGHT, 1, SPRITE_SIZE, SPRITE_SCALING)
    test_map.map_type = GameMapTypes.BSP
    test_map.simple_max_rooms = 10
    test_map.bsp_fill = True
    # test_map.player = Entity(0, 0, None, "Player", False)
    test_map.player = Entity(0, 0, "Player", False, SPRITE_SIZE, "tileset/elf_male.png",
                             SPRITE_SCALING)
    game = ArcadeDemo(SCREEN_WIDTH, SCREEN_HEIGHT, test_map)
    game.setup()
    arcade.run()
