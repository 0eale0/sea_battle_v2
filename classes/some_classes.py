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
    def __init__(self, player_1, player_2):
        self.players_1 = player_1
        self.players_2 = player_2
        self.turn = 0  # can be 1 or 2

    def hit(self):
        pass


class Field:
    """
    Create a field for the player with height and length. Next time planning to add some methods
    WATCH OUT THERE'S A NOT int(0), BUT str(0)
    """
    def __init__(self,
                 height: int = constants_for_classes.height,
                 length: int = constants_for_classes.length):

        self.__field = [['0'] * length for i in range(height)]
        self.__visual_field = [[emojies.zero] * length for i in range(height)]

    def __str__(self):
        result = [' '.join(x) for x in self.__visual_field]
        result = '\n'.join(result)
        return result

    def __setitem__(self, key, data):
        self.__field[key[0]][key[1]] = data

        if isinstance(data, Ship):  # only for objects emoji can't str(str)
            self.__visual_field[key[0]][key[1]] = str(data)
            return

        else:
            self.__visual_field[key[0]][key[1]] = emojies.dict_for_data[data]

    def __getitem__(self, key):
        return self.__field[key[0]][key[1]]

    def __iter__(self):
        return iter(self.__field)


class Player:
    def __init__(self, t_id: int = 0, nickname: str = 'null'):
        self.field = Field()  # size can be changed
        self.t_id = t_id
        self.nickname = nickname
        self.ships = create_ships()


class Ship:
    def __init__(self, size: int, orientation: str = 'vertical',):
        """
        :param size:
        :param orientation: can be "vertical" or "horizontal" STANDARD == VERTICAL!
        """
        self.size = size
        self.orientation = orientation
        self.already_place = False
        self.hp = size
        self.__x = None
        self.__y = None
        self.booked_places = [[], []]  # all book coords. First list for the 'z', next for the objects like this:
        #  [[(1, 2), (3, 4)], [(0, 0)]] cords in example is random, bus is show structure

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
