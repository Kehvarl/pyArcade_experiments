from arcade import Sprite


class Entity(Sprite):
    """
    Class that represents a 'sprite' on-screen.

    Attributes:
        :alpha: Transparency of sprite. 0 is invisible, 1 is opaque.
        :angle: Rotation angle in degrees or sprite.
        :boundary_left: Used in movement. Left boundary of moving sprite.
        :boundary_right: Used in movement. Right boundary of moving sprite.
        :boundary_top: Used in movement. Top boundary of moving sprite.
        :boundary_bottom: Used in movement. Bottom boundary of moving sprite.
        :bottom: Set/query the sprite location by using the bottom coordinate. This will be the 'y' of the bottom of the sprite.
        :center_x: X location of the center of the sprite
        :center_y: Y location of the center of the sprite
        :change_x: Movement vector, in the x direction.
        :change_y: Movement vector, in the y direction.
        :change_angle: Change in rotation.
        :collision_radius: Used as a fast-check to see if this item is close enough to another item. If this check works, we do a slower more accurate check.
        :cur_texture_index: Index of current texture being used.
        :filename: Filename of an image that represents the sprite.
        :image_width: Width of the sprite
        :image_height: Height of the sprite
        :left: Set/query the sprite location by using the left coordinate. This will be the 'x' of the left of the sprite.
        :position: A list with the (x, y) of where the sprite is.
        :right: Set/query the sprite location by using the right coordinate. This will be the 'y=x' of the right of the sprite.
        :scale: Scale the image up or down. Scale of 1.0 is original size, 0.5 is 1/2 height and width.
        :sprite_lists: List of all the sprite lists this sprite is part of.
        :transparent: Set to True if this sprite can be transparent.
        :top: Set/query the sprite location by using the top coordinate. This will be the 'y' of the top of the sprite.
        :texture: `Texture` class with the current texture.
        :textures: List of textures associated with this sprite.
        :velocity: Change in x, y expressed as a list. (0, 0) would be not moving.
    """

    def __init__(self,
                 x, y,
                 name: str="default",
                 blocks: bool=False,
                 sprite_size: float = 32,
                 filename: str=None,
                 scale: float=1,
                 image_x: float=0, image_y: float=0,
                 image_width: float=0, image_height: float=0,
                 center_x: float=0, center_y: float=0):
        """
        Create a new sprite.

        Args:
            x (int): Horizontal Map Position
            y (int): Vertical Map Position
            name (str):  Entity Label
            blocks (bool): Entity prevents movement through tile
            sprite_size (float): Size of the sprite
            filename (str): Filename of an image that represents the sprite.
            scale (float): Scale the image up or down. Scale of 1.0 is none.
            image_x (float): Scale the image up or down. Scale of 1.0 is none.
            image_y (float): Scale the image up or down. Scale of 1.0 is none.
            image_width (float): Width of the sprite
            image_height (float): Height of the sprite
            center_x (float): Location of the sprite
            center_y (float): Location of the sprite

        """

        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.name = name
        self.blocks = blocks
        self.sprite_size = sprite_size
        super().__init__(filename,
                         scale,
                         image_x, image_y,
                         image_width, image_height,
                         center_x, center_y)
        self._update_center()

    def _update_center(self):
        self.center_x = self.x * self.sprite_size + self.sprite_size / 2
        self.center_y = self.y * self.sprite_size + self.sprite_size / 2

    def update(self):
        self._update_center()
