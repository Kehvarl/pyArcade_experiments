class Tile:
    def __init__(self, block_move=True, block_sight=True, is_wall=False):
        self.block_move = block_move
        self.block_sight = block_sight
        self.is_wall = is_wall

    def block(self, block_state=False, is_wall=False):
        """
        :param bool block_state:
        :param bool is_wall:
        """
        self.block_sight = block_state
        self.block_move = block_state
        self.is_wall = is_wall
