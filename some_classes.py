class SeaBattleGame:
    def __init__(self, player_1, player_2):
        self.players_1 = player_1
        self.players_2 = player_2


class Field:
    """
    Create a field for the player with height and length. Next time planning to add some methods
    """
    def __init__(self, height: int = 10, length: int = 10):
        self.field = [[0] * length for x in range(height)]


class Player:
    def __init__(self, t_id : int = 0, nickname: str = 'null'):
        self.field = Field()  # size can be changed
        self.t_id = t_id
        self.nickname = nickname


class Ship:
    def __init__(self, size: int, orientation: str,):
        """
        :param size:
        :param orientation: can be "vertical" or "horizontal"
        """
        self.size = size
        self.orientation = orientation
        self.already_place = False
        self.hp = size
