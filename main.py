"""
PyArcade Roguelike


"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAZE_WIDTH = 40
MAZE_HEIGHT = 30

NATIVE_SPRITE_SIZE = 32
SPRITE_SCALING = (SCREEN_HEIGHT / MAZE_HEIGHT) / NATIVE_SPRITE_SIZE
SPRITE_SIZE = NATIVE_SPRITE_SIZE * SPRITE_SCALING


class RoguelikeArcade(arcade.Window):
    """
    """

    def __init__(self, width, height):
        super().__init__(width, height, "Roguelike Arcade")

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass


if __name__ == "__main__":
    game = RoguelikeArcade(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
