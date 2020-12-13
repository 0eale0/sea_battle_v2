from classes import some_classes
from data_base.db import cursor, conn
import sqlite3
import json
from classes.constants_for_classes import ships_ids, height, length


# For ship
def get_dict_with_args(keys, tuple_with_info: list):
    result = dict(zip(keys, tuple_with_info))
    return result


def create_ships(t_id, tuples_with_basic_info: list = False):  # It's difference because booked_place is list
    """
    this function create list objects(ship), it can download it from bd or create new, return list with objects
    """
    ships = []
    if not tuples_with_basic_info:  # If create ships
        for ship_id in ships_ids:
            size = int(float(ship_id))  # first number it's size
            ship = some_classes.Ship(size=size,
                                     t_id=t_id,
                                     ship_id=ship_id)
            # for save in db
            tuple_with_args = (size,
                               t_id,
                               ship_id,
                               json.dumps(ship.booked_places),
                               ship.hp,
                               ship.x,
                               ship.y,
                               ship.already_place,
                               ship.orientation)

            cursor.execute("INSERT INTO ships VALUES(?,?,?,?,?,?,?,?,?)", tuple_with_args)
            conn.commit()
            ships.append(ship)
        return ships
    else:  # download it from bd and create objects
        keys = ('size', 't_id', 'ship_id', 'booked_places', 'hp', 'x', 'y', 'already_place', 'orientation')
        for info in tuples_with_basic_info:
            dict_with_args = get_dict_with_args(keys, info)
            ship = some_classes.Ship(**dict_with_args)
            ships.append(ship)

        return ships


def create_field(t_id, tuples_with_basic_info: list = False, ships: list = False):
    if not tuples_with_basic_info:
        field = some_classes.Field(t_id, height, length)
        return field

    else:
        keys = ('t_id', 'height', 'length', 'visual_field')
        dict_with_args = get_dict_with_args(keys, tuples_with_basic_info[0])
        dict_with_args['field'] = json.loads(dict_with_args['visual_field'])
        dict_with_args['visual_field'] = json.loads(dict_with_args['visual_field'])

        for list_with_cells in dict_with_args['field']:  # visual_field = [[1, 2, 3], [3, 2, 1]] 12 X 8
            for i in range(length):
                if list_with_cells[i] in ships_ids:
                    for ship in ships:
                        list_with_cells[i] = ship
        field = some_classes.Field(**dict_with_args)
        return field


def create_player(t_id, enemy_id, field, ships, ):
    player = some_classes.Player(t_id=t_id,
                                 enemy_id=enemy_id,
                                 field=field,
                                 ships=ships)
    return player


def create_current_game(player_1: some_classes.Player, player_2: some_classes.Player):
    t_id_1 = player_1.t_id
    t_id_2 = player_2.t_id
    current_game = some_classes.SeaBattleGame(player_1=player_1,
                                              player_2=player_2,
                                              t_id_1=t_id_1,
                                              t_id_2=t_id_2)
    return current_game


def collect_full_player(t_id):
    cursor.execute(f"SELECT * FROM ships WHERE t_id = {t_id}")
    tuple_with_basic_info_for_ships = cursor.fetchall()
    if not tuple_with_basic_info_for_ships:
        ships = create_ships(t_id)
        field = create_field(t_id)

        cursor.execute(f"SELECT * FROM in_queue WHERE t_id != {t_id}")
        enemy_id = cursor.fetchall()[0][0]  # [(t_id, nickname)]

        player = create_player(t_id, enemy_id, field, ships)

        return player


def collect_current_game_from_in_queue():
    cursor.execute("SELECT * FROM in_queue")
    players_ids = cursor.fetchall()

    players_objects = []

    for player_id in players_ids:
        player = collect_full_player(player_id[0])
        players_objects.append(player)

    player_1 = players_objects[0]
    player_2 = players_objects[1]
    t_id_1 = player_1.t_id
    t_id_2 = player_2.t_id

    current_game = some_classes.SeaBattleGame(player_1=player_1,
                                              player_2=player_2,
                                              t_id_1=t_id_1,
                                              t_id_2=t_id_2)

    return current_game


game = collect_current_game_from_in_queue()
#game.change_turn()

print(game)

