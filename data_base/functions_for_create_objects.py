from classes import some_classes
from data_base.db import cursor, conn
import sqlite3
import json
from classes.constants_for_classes import ships_ids, height, length


# For ship
def get_dict_with_args(keys, tuple_with_info: list):
    result = dict(zip(keys, tuple_with_info))
    return result


def check_player_in_bd(t_id):
    cursor.execute(f"SELECT * FROM player WHERE t_id = {t_id}")
    return bool(cursor.fetchall())


def create_ships_for_random(t_id):

    # clear ships and field
    cursor.execute(f"DELETE FROM ships WHERE t_id = {t_id}")
    cursor.execute(f"DELETE FROM field WHERE t_id = {t_id}")
    conn.commit()

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
        # ships.append(ship)
    create_field(t_id)
    conn.commit()


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

    else:  # download it from bd and create objects
        keys = ('size', 't_id', 'ship_id', 'booked_places', 'hp', 'x', 'y', 'already_place', 'orientation')
        for info in tuples_with_basic_info:
            dict_with_args = get_dict_with_args(keys, info)
            dict_with_args['booked_places'] = json.loads(dict_with_args['booked_places'])
            ship = some_classes.Ship(**dict_with_args)
            ships.append(ship)

    return ships


def create_field(t_id, tuples_with_basic_info: list = False, ships: list = False):
    if not tuples_with_basic_info:
        field = some_classes.Field(t_id, height, length)
        tuple_with_args = (t_id,
                           height,
                           length,
                           json.dumps(field.visual_field))

        cursor.execute("INSERT INTO field VALUES(?, ?, ?, ?)", tuple_with_args)
        conn.commit()

        return field

    else:
        keys = ('t_id', 'height', 'length', 'visual_field')
        dict_with_args = get_dict_with_args(keys, tuples_with_basic_info[0])
        dict_with_args['field'] = json.loads(dict_with_args['visual_field'])
        dict_with_args['visual_field'] = json.loads(dict_with_args['visual_field'])

        cursor.execute(f"SELECT * FROM ships WHERE t_id = {t_id}")
        tuples_with_basic_info_for_ships = cursor.fetchall()
        ships = create_ships(t_id, tuples_with_basic_info=tuples_with_basic_info_for_ships)

        for list_with_cells in dict_with_args['field']:  # visual_field = [[1, 2, 3], [3, 2, 1]] 12 X 8
            for i in range(length):
                if list_with_cells[i] in ships_ids:
                    for ship in ships:
                        if ship.ship_id == list_with_cells[i]:
                            list_with_cells[i] = ship
        field = some_classes.Field(**dict_with_args)
        return field


def create_player(t_id, enemy_id, field, ships):

    # if player not in bd
    if not(check_player_in_bd(t_id)):
        cursor.execute(f"SELECT nickname FROM in_queue WHERE t_id = {t_id}")
        nickname = cursor.fetchall()[0][0]

        tuple_with_args = (t_id, nickname)
        cursor.execute("INSERT INTO player VALUES(?, ?)", tuple_with_args)  #WARNING!
        conn.commit()

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


def collect_full_player(t_id, enemy_id):
    cursor.execute(f"SELECT * FROM ships WHERE t_id = {t_id}")
    tuple_with_basic_info_for_ships = cursor.fetchall()

    cursor.execute(f"SELECT * FROM field WHERE t_id = {t_id}")
    tuple_with_basic_info_for_field = cursor.fetchall()

    ships = create_ships(t_id, tuple_with_basic_info_for_ships)
    field = create_field(t_id, tuple_with_basic_info_for_field)

    player = create_player(t_id, enemy_id, field, ships)

    return player


def collect_current_game_from_in_queue(t_id=False):
    if not t_id:
        cursor.execute("SELECT * FROM in_queue")
        players_ids = cursor.fetchall()
        t_id_1 = players_ids[0][0]
        t_id_2 = players_ids[1][0]
        players_ids = [t_id_1, t_id_2]
    else:
        cursor.execute(f"SELECT * FROM sea_battle_game WHERE t_id_1 = ? OR t_id_2 = ?", (t_id, t_id))
        players_ids = cursor.fetchone()
        t_id_1 = players_ids[0]
        t_id_2 = players_ids[1]
        players_ids = [t_id_1, t_id_2]

    players_objects = []

    player = collect_full_player(t_id_1, t_id_2)
    players_objects.append(player)

    player = collect_full_player(t_id_2, t_id_1)
    players_objects.append(player)

    player_1 = players_objects[0]
    player_2 = players_objects[1]
    t_id_1 = player_1.t_id
    t_id_2 = player_2.t_id

    cursor.execute("SELECT turn FROM sea_battle_game WHERE t_id_1 = ? OR t_id_2 = ?", (t_id_1, t_id_1))
    turn_in_tuple = cursor.fetchall()  # [(turn)]

    if not turn_in_tuple:
        turn = 1
        cursor.execute("INSERT INTO sea_battle_game VALUES(?, ?, ?)", (t_id_1, t_id_2, turn))
    else:
        turn = turn_in_tuple[0][0]

    current_game = some_classes.SeaBattleGame(player_1=player_1,
                                              player_2=player_2,
                                              t_id_1=t_id_1,
                                              t_id_2=t_id_2,
                                              turn=turn)

    cursor.execute("DELETE FROM in_queue")  # clear table
    conn.commit()

    return current_game


'''game = collect_current_game_from_in_queue()
game.change_turn()

game: some_classes.SeaBattleGame

logic.hit(game.player_1)

print(game.player_1.field)

print(game)'''
