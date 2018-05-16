"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_starting_template
"""
import os
# import random

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
        self.map_list = None
        self.monster_list = None
        self.player = None
        self.wall_textures = None
        self.fill_textures = None
        self.floor_textures = None
        self.kobold_texture = None

    def setup(self):
        # Create your sprites and sprite lists here
        self.dungeon.map_tile_list = arcade.SpriteList()

        self.dungeon.wall_textures = []
        self.dungeon.wall_textures.append(arcade.load_texture(file_name="tileset/dungeon/wall/snake_0.png",
                                                              scale=SPRITE_SCALING))
        self.dungeon.wall_textures.append(arcade.load_texture(file_name="tileset/dungeon/wall/snake_1.png",
                                                              scale=SPRITE_SCALING))
        self.dungeon.wall_textures.append(arcade.load_texture(file_name="tileset/dungeon/wall/snake_2.png",
                                                              scale=SPRITE_SCALING))
        self.dungeon.wall_textures.append(arcade.load_texture(file_name="tileset/dungeon/wall/snake_3.png",
                                                              scale=SPRITE_SCALING))
        self.dungeon.wall_textures.append(arcade.load_texture(file_name="tileset/dungeon/wall/snake_4.png",
                                                              scale=SPRITE_SCALING))

        self.dungeon.fill_textures = []
        self.dungeon.fill_textures.append(arcade.load_texture(file_name="tileset/dungeon/wall/stone_dark_0.png",
                                                              scale=SPRITE_SCALING))
        self.dungeon.fill_textures.append(arcade.load_texture(file_name="tileset/dungeon/wall/stone_dark_1.png",
                                                              scale=SPRITE_SCALING))
        self.dungeon.fill_textures.append(arcade.load_texture(file_name="tileset/dungeon/wall/stone_dark_2.png",
                                                              scale=SPRITE_SCALING))
        self.dungeon.fill_textures.append(arcade.load_texture(file_name="tileset/dungeon/wall/stone_dark_3.png",
                                                              scale=SPRITE_SCALING))

        self.dungeon.floor_textures = []
        self.dungeon.floor_textures.append(arcade.load_texture(file_name="tileset/dungeon/floor/mosaic_10.png",
                                                               scale=SPRITE_SCALING))
        self.dungeon.floor_textures.append(arcade.load_texture(file_name="tileset/dungeon/floor/mosaic_11.png",
                                                               scale=SPRITE_SCALING))
        self.dungeon.floor_textures.append(arcade.load_texture(file_name="tileset/dungeon/floor/mosaic_12.png",
                                                               scale=SPRITE_SCALING))
        self.dungeon.floor_textures.append(arcade.load_texture(file_name="tileset/dungeon/floor/mosaic_13.png",
                                                               scale=SPRITE_SCALING))
        self.dungeon.floor_textures.append(arcade.load_texture(file_name="tileset/dungeon/floor/mosaic_14.png",
                                                               scale=SPRITE_SCALING))

        self.kobold_texture = arcade.load_texture(file_name="tileset/orc_new.png",
                                                  scale=SPRITE_SCALING)

        # self.player = arcade.Sprite("tileset/elf_male.png",
        #                             scale=SPRITE_SCALING)

        self._load_map()

    def _load_map(self):
        self.dungeon.generate_map()
        self.dungeon.populate_map()
        self.dungeon.player.x = self.dungeon.game_map.start_x
        self.dungeon.player.y = self.dungeon.game_map.start_y

    #        self.monster_list = arcade.SpriteList()
    #        for entity in self.dungeon.entities:
    #            monster = arcade.Sprite()
    #            monster.texture = self.kobold_texture
    #            monster.center_x = entity.x * SPRITE_SIZE + SPRITE_SIZE / 2
    #            monster.center_y = entity.y * SPRITE_SIZE + SPRITE_SIZE / 2
    #
    #            self.monster_list.append(monster)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.dungeon.map_tile_list.draw()
        # self.monster_list.draw()
        self.dungeon.player.draw()
        # self.player.draw()

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
    test_map = Level(MAZE_WIDTH, MAZE_HEIGHT, 1, SPRITE_SIZE)
    test_map.map_type = GameMapTypes.BSP
    test_map.simple_max_rooms = 10
    test_map.bsp_fill = True
    # test_map.player = Entity(0, 0, None, "Player", False)
    test_map.player = Entity(0, 0, "Player", False, SPRITE_SIZE, "tileset/elf_male.png",
                             SPRITE_SCALING)
    game = ArcadeDemo(SCREEN_WIDTH, SCREEN_HEIGHT, test_map)
    game.setup()
    arcade.run()
