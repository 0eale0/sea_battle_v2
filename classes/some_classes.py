from classes import constants_for_classes
from visual import emojies

#  Static functions for the classes


def create_ships():
    ships = []
    for size in constants_for_classes.size_of_ships:
        ships.append(Ship(size))
    return ships


#  Classes
class SeaBattleGame:
    def __init__(self, player_1, player_2, t_id_1, t_id_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.t_id_1 = t_id_1
        self.t_id_2 = t_id_2
        self.turn = 0  # can be 1 or 2


class Field:
    """
    Create a field for the player with height and length. Next time planning to add some methods
    WATCH OUT THERE'S A NOT int(0), BUT str(0)
    """
    def __init__(self,
                 t_id: int,
                 height: int = constants_for_classes.height,
                 length: int = constants_for_classes.length,
                 field: list = None,
                 visual_field: list = None):

        self.t_id = t_id
        if not field:
            self.__field = [['0'] * length for i in range(height)]
            self.__visual_field = [[emojies.zero] * length for i in range(height)]
        else:
            self.__field = field
            self.__visual_field = visual_field

    def __str__(self):
        result = [' '.join(x) for x in self.__visual_field]
        result = '\n'.join(result)
        return result

    def __setitem__(self, key, data, ship_id=None):
        self.__field[key[0]][key[1]] = data

        if isinstance(data, Ship):  # only for objects emoji can't str(str)
            self.__visual_field[key[0]][key[1]] = ship_id
            return

        else:
            self.__visual_field[key[0]][key[1]] = emojies.dict_for_data[data]

    def __getitem__(self, key):
        return self.__field[key[0]][key[1]]

    def __iter__(self):
        return iter(self.__field)


class Player:
    def __init__(self, t_id: int = 0,
                 nickname: str = 'null',
                 ships: list = None,
                 field: list = None):
        self.field = Field()  # size can be changed
        self.t_id = t_id
        self.nickname = nickname

        if not ships:  # if ships is empty, field too
            self.ships = create_ships()
            self.field = Field()
        else:
            self.ships = ships
            self.field = field


class Ship:
    def __init__(self, size: int,
                 hp: int,
                 x: int,
                 y: int,
                 booked_places: list,
                 t_id: int,
                 ship_id: int,
                 already_place: bool = None,
                 orientation: str = 'vertical'):
        """
        :param orientation: can be "vertical" or "horizontal" STANDARD == VERTICAL!
        """
        # some constants
        self.orientation = orientation
        self.size = size
        self.t_id = t_id
        self.ship_id = ship_id
        if not already_place:  # create ship
            self.hp = size
            self.already_place = False
            self.__x = None
            self.__y = None
            self.booked_places = [[], []]  # all book coords. First list for the 'z', next for the objects like this:
            #  [[(1, 2), (3, 4)], [(0, 0)]] cords in example is random, bus is show structure
        else:  # load ship from bd
            self.hp = hp
            self.already_place = already_place
            self.__x = x
            self.__y = y
            self.booked_places = booked_places

    def __str__(self):
        return str(self.size)

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x_from_user) -> None:
        self.__x = x_from_user

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y_from_user) -> None:
        self.__y = y_from_user
