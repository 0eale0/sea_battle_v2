from classes import constants_for_classes
from visual import emojies
from data_base.db import cursor, conn
import json
from copy import deepcopy


#  Static functions for the classes


def create_ships():
    ships = []
    for size in constants_for_classes.size_of_ships:
        ships.append(Ship(size))
    return ships


#  Classes

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

        self.length = length
        self.height = height
        self.t_id = t_id
        if not field:
            self.__field = [['0'] * length for i in range(height)]
            self.__visual_field = [['zero'] * length for i in range(height)]
        else:
            self.__field = field
            self.__visual_field = visual_field

    @property
    def field(self):
        return self.__field

    @property
    def visual_field(self):
        return self.__visual_field

    def get_field_with_emoji(self, invisible=False):
        copy_field = deepcopy(self.__visual_field)
        for list_with_cells in copy_field:
            for i in range(self.length):
                if list_with_cells[i] in emojies.dict_for_data.keys():
                    list_with_cells[i] = emojies.dict_for_data[list_with_cells[i]]
                elif list_with_cells[i] in constants_for_classes.ships_ids:
                    if invisible:
                        list_with_cells[i] = emojies.zero
                    else:
                        list_with_cells[i] = emojies.ship
        return copy_field

    def __str__(self):
        field_with_emoji = self.get_field_with_emoji()
        result = [' '.join(x) for x in field_with_emoji]
        result = '\n'.join(result)
        return result

    def __setitem__(self, key, data, ship_id=None):
        self.__field[key[0]][key[1]] = data

        if isinstance(data, Ship):  # only for objects emoji can't str(str)
            self.__visual_field[key[0]][key[1]] = data.ship_id

        else:
            self.__visual_field[key[0]][key[1]] = data

        # save changes in db
        cursor.execute("UPDATE field SET visual_field = ? WHERE t_id = ?", (json.dumps(self.__visual_field), self.t_id))
        conn.commit()

    def __getitem__(self, key):
        return self.__field[key[0]][key[1]]

    def __iter__(self):
        return iter(self.__field)


class Player:
    def __init__(self, t_id: int = 0,
                 enemy_id: int = 1,
                 nickname: str = 'null',
                 ships: list = None,
                 field: Field = None):

        self.t_id = t_id
        self.nickname = nickname
        self.enemy_id = enemy_id

        if not ships:  # if ships is empty, field too
            self.ships = create_ships()
            self.field = Field()
        else:
            self.ships = ships
            self.field = field


class Ship:
    def __init__(self, size: int,
                 t_id: int,
                 ship_id: int,
                 booked_places: list = None,
                 hp: int = 0,
                 x: int = 0,
                 y: int = 0,
                 already_place: bool = None,
                 orientation: str = 'vertical'):
        """
        :param orientation: can be "vertical" or "horizontal" STANDARD == VERTICAL!
        """
        # some constants
        self.__orientation = orientation
        self.size = size
        self.t_id = t_id
        self.ship_id = ship_id
        if not already_place:  # create ship
            self.__hp = size
            self.__already_place = False
            self.__x = 0
            self.__y = 0
            self.__booked_places = [[], []]  # all book coords. First list for the 'z', next for the objects like this:
            #  [[(1, 2), (3, 4)], [(0, 0)]] cords in example is random, bus is show structure
        else:  # load ship from bd
            self.__hp = hp
            self.__already_place = already_place
            self.__x = x
            self.__y = y
            self.__booked_places = booked_places

    def __str__(self):
        return str(self.size)

    @property
    def booked_places(self) -> list:
        return self.__booked_places

    @booked_places.setter
    def booked_places(self, list_from_user) -> None:
        self.__already_place = list_from_user
        cursor.execute("UPDATE ships SET booked_places = ?"
                       " WHERE t_id = ? AND ship_id = ?", (json.dumps(self.__booked_places),
                                                           self.t_id,
                                                           self.ship_id))
        conn.commit()

    def booked_places_append(self, key, tuple_with_coords):
        self.__booked_places[key].append(tuple_with_coords)
        cursor.execute("UPDATE ships SET booked_places = ?"
                       " WHERE t_id = ? AND ship_id = ?", (json.dumps(self.__booked_places),
                                                           self.t_id,
                                                           self.ship_id))
        conn.commit()

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation_from_user) -> None:
        self.__orientation = orientation_from_user
        cursor.execute("UPDATE ships SET orientation = ? WHERE t_id = ? AND ship_id = ?", (self.__orientation,
                                                                                           self.t_id,
                                                                                           self.ship_id))
        conn.commit()

    @property
    def already_place(self) -> bool:
        return self.__already_place

    @already_place.setter
    def already_place(self, bool_from_user) -> None:
        self.__already_place = bool_from_user
        cursor.execute("UPDATE ships SET already_place = ? WHERE t_id = ? AND ship_id = ?", (self.__already_place,
                                                                                             self.t_id,
                                                                                             self.ship_id))
        conn.commit()

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, hp_from_user) -> None:
        self.__hp = hp_from_user
        cursor.execute("UPDATE ships SET hp = ? WHERE t_id = ? AND ship_id = ?", (self.__hp,
                                                                                  self.t_id,
                                                                                  self.ship_id))
        conn.commit()

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x_from_user) -> None:
        self.__x = x_from_user
        cursor.execute("UPDATE ships SET x = ? WHERE t_id = ? AND ship_id = ?", (self.__x,
                                                                                 self.t_id,
                                                                                 self.ship_id))
        conn.commit()

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y_from_user) -> None:
        self.__y = y_from_user
        cursor.execute("UPDATE ships SET y = ? WHERE t_id = ? AND ship_id = ?", (self.__y,
                                                                                 self.t_id,
                                                                                 self.ship_id))
        conn.commit()


class SeaBattleGame:
    def __init__(self, player_1: Player, player_2: Player, t_id_1: int, t_id_2: int, turn=1):
        self.player_1 = player_1
        self.player_2 = player_2
        self.t_id_1 = t_id_1
        self.t_id_2 = t_id_2
        self.__turn = turn  # can be 1 or 2

    @property
    def turn(self):
        return self.__turn

    def change_turn(self):
        self.__turn = 2 if self.__turn == 1 else 1
        # change turn in the bd, in the column, where at least one id correct
        cursor.execute("UPDATE sea_battle_game SET turn = ?"
                       " WHERE t_id_1 = ? OR t_id_2 = ? ", (self.__turn, self.t_id_1, self.t_id_1))
        conn.commit()
