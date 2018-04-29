from random import randint

from game_world.game_map.map_factories.dungeon import Dungeon

from game_world.game_map.game_map import GameMap
from game_world.game_map.map_factories.bsp_components.bsp_leaf import Leaf


class BSPDungeon(Dungeon):
    """
    Generate a Dungeon using the BSP algorithm
    Process:
      Define an area
      Select Horizontal or Vertical
      Divide the area randomly either Horizontally or Vertically
      Repeat in each new area for a pre-defined number of iterations
      Define an space within each area
      Connect adjacent spaces
    """

    # noinspection PyMethodOverriding
    @staticmethod
    def generate(width, height, fill=False):
        rooms_list = []
        root = BSPDungeon._init_tree(width, height)
        game_map = GameMap(width, height)
        game_map.clear_map()

        BSPDungeon._split(root)
        BSPDungeon._generate_rooms(game_map, root, rooms_list, fill)
        BSPDungeon._generate_corridors(game_map, rooms_list)
        game_map.start_x, game_map.start_y = rooms_list[0].center()
        return game_map

    @staticmethod
    def _init_tree(width, height):
        """Set up an empty map grid"""
        return Leaf(0, 0, width, height)

    @staticmethod
    def _split(root):
        """
        Divide the space into leaves on a binary spanning tree
        """
        if root:
            root.split()

    @staticmethod
    def _generate_rooms(game_map, root, rooms_list, fill=False):
        """
        Fill each child node of the tree with a room
        Collect all created rooms into a list
        :param bool fill: If True, rooms take up the entirety of a node
        """
        if root:
            root.generate_room(fill)
        root.get_rooms(rooms_list)
        BSPDungeon._fill_grid(game_map, rooms_list)

    @staticmethod
    def _fill_grid(game_map, rooms_list):
        """
        Draw the rooms into the map grid
        """
        for room in rooms_list:
            for x in range(room.x1, room.x2):
                for y in range(room.y1, room.y2):
                    if x == room.x1 or x == room.x2 - 1 or y == room.y1 or y == room.y2 - 1:
                        game_map.tiles[x][y].block(True)
                    else:
                        game_map.tiles[x][y].block(False)

    @staticmethod
    def _generate_corridors(game_map, rooms_list):
        """
        Add connecting corridors between rooms
        """
        first_room = True
        new_x, new_y = 0, 0
        for room in rooms_list:
            if first_room:
                first_room = False
                new_x, new_y = room.center()
            else:
                prev_x, prev_y = new_x, new_y
                new_x, new_y = room.center()
                # Randomly determine corridor arrangement.
                if randint(0, 1) == 1:
                    # Horizontal tunnel, then Vertical
                    BSPDungeon._create_h_tunnel(game_map, prev_x, new_x, prev_y)
                    BSPDungeon._create_v_tunnel(game_map, prev_y, new_y, new_x)
                else:
                    # Vertical tunnel, then Horizontal
                    BSPDungeon._create_v_tunnel(game_map, prev_y, new_y, prev_x)
                    BSPDungeon._create_h_tunnel(game_map, prev_x, new_x, new_y)

    @staticmethod
    def _create_h_tunnel(game_map, x1, x2, y):
        """
        Create a tunnel
        :param int x1: Start of Tunnel
        :param int x2: End of Tunnel
        :param int y: The y position of the tunnel
        """
        for x in range(min(x1, x2), max(x1, x2) + 1):
            game_map.tiles[x][y].block(False)

    @staticmethod
    def _create_v_tunnel(game_map, y1, y2, x):
        """
        Create a vertical tunnel
        :param int y1: Start of Tunnel
        :param int y2: End of Tunnel
        :param int x: X position of the tunnel
        """
        for y in range(min(y1, y2), max(y1, y2) + 1):
            game_map.tiles[x][y].block(False)


if __name__ == "__main__":
    test_map = GameMap(80, 25)
    dungeon = BSPDungeon.generate(80, 25, fill=True)
    print(dungeon.printable_map())
