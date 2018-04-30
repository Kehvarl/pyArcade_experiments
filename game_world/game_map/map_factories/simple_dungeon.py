from random import randint

from game_world.game_map.rect import Rect

from game_world.game_map.game_map import GameMap
from game_world.game_map.map_factories.dungeon import Dungeon


class SimpleDungeon(Dungeon):
    """
    Generate a dungeon using the algorithm from the RogueBasin tutorial
    Source: http://www.roguebasin.com/index.php?title=Complete_Roguelike_Tutorial,_using_python%2Blibtcod,_part_3
    Process:
        Add randomly-sized rooms to random locations in the map
        If a new room overlaps an existing one, discard it
        After all rooms added
            connect each room with the previous room using a corridor
    """

    # noinspection PyMethodOverriding
    @staticmethod
    def generate(width, height, max_rooms=1, room_min_size=5, room_max_size=10):
        """
        Create initial Map Layout
        :return: GameMap:
        :param width: Width of map in tiles
        :param height: Height of map in tiles
        :param int max_rooms: Number of rooms to attempt to generate
        :param int room_min_size: Smallest allowable room (width or height)
        :param int room_max_size: Largest allowable room (width or height)
        """
        num_rooms = 0
        game_map = GameMap(width, height)
        game_map.clear_map()

        for r in range(max_rooms):
            # random width and height
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            # random position without going out of the boundaries of the map
            x = randint(0, width - w - 1)
            y = randint(0, height - h - 1)

            # Room class stores some useful features
            new_room = Rect(x, y, w, h)

            # run through the other rooms and see if they intersect with this one
            for other_room in game_map.rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # this means there are no intersections, so this room is valid
                # "paint" it to the map's tiles
                SimpleDungeon._create_room(game_map, new_room)

                # if this is the first room, set the start_x and start_y
                if num_rooms == 0:
                    game_map.start_x, game_map.start_y = new_room.center()

                # finally, append the new room to the list
                game_map.rooms.append(new_room)
                num_rooms += 1
        SimpleDungeon._generate_corridors(game_map.rooms, game_map)
        return game_map

    @staticmethod
    def _create_room(game_map, room):
        """
        Set the tiles of a room to be passable
        :param Map.room.Room room: The room in the map
        """
        # Make interior tiles passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                game_map.tiles[x][y].block(False, False)
        for x in range(room.x1 + 1, room.x2):
            game_map.tiles[x][room.y1].wall = True
            game_map.tiles[x][room.y2].wall = True
        for y in range(room.y1 + 1, room.y2):
            game_map.tiles[room.x1][y].wall = True
            game_map.tiles[room.x2][y].wall = True

    @staticmethod
    def _generate_corridors(rooms_list, game_map):
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
                    SimpleDungeon._create_h_tunnel(game_map, prev_x, new_x, prev_y)
                    SimpleDungeon._create_v_tunnel(game_map, prev_y, new_y, new_x)
                else:
                    # Vertical tunnel, then Horizontal
                    SimpleDungeon._create_v_tunnel(game_map, prev_y, new_y, prev_x)
                    SimpleDungeon._create_h_tunnel(game_map, prev_x, new_x, new_y)
                pass

    @staticmethod
    def _create_h_tunnel(game_map, x1, x2, y):
        """
        Create a tunnel
        :param int x1: Start of Tunnel
        :param int x2: End of Tunnel
        :param int y: The y position of the tunnel
        """
        for x in range(min(x1, x2), max(x1, x2) + 1):
            game_map.tiles[x][y].block(False, False)
            game_map.tiles[x][y-1].wall = True
            game_map.tiles[x][y+1].wall = True

    @staticmethod
    def _create_v_tunnel(game_map, y1, y2, x):
        """
        Create a vertical tunnel
        :param int y1: Start of Tunnel
        :param int y2: End of Tunnel
        :param int x: X position of the tunnel
        """
        for y in range(min(y1, y2), max(y1, y2) + 1):
            game_map.tiles[x][y].block(False, False)
            game_map.tiles[x-1][y].wall = True
            game_map.tiles[x+1][y].wall = True


if __name__ == "__main__":
    dungeon = SimpleDungeon.generate(40, 11, 3, 3, 9)
    print(dungeon.printable_map())
