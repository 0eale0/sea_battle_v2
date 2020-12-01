import constants_for_classes

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

    def __str__(self):
        result = [' '.join(x) for x in self.__field]
        result = '\n'.join(result)
        return result

    def __setitem__(self, key):
        #print(key)
        return self.__field[key]

    def __getitem__(self, key):
        print(key)
        return self.__field[key]


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
        self.booked_places = []  # all book coords

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x_from_user) -> None:
        self.__x = x_from_user - 1  # -1 for list (0-9)

    @property
    def y(self) -> int:
        return self.__x

    @y.setter
    def y(self, y_from_user) -> None:
        self.__y = y_from_user - 1  # -1 for list (0-9)

