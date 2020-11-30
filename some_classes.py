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

    def place_ship(self):
        pass

    def hit(self):
        pass


class Field:
    """
    Create a field for the player with height and length. Next time planning to add some methods
    """
    def __init__(self,
                 height: int = constants_for_classes.height,
                 length: int = constants_for_classes.length):

        self.field = [[0] * length for i in range(height)]

    def __str__(self):
        pass  # there's should be visual for user


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
        self.x = None
        self.y = None
        self.booked_places = []  # all book coords
