from data_base.db import cursor, conn


def create_field():
    t_id: int
    height: int
    length: int
    visual_field: list

    cursor.execute("""CREATE TABLE field
                      (t_id, height, length, visual_field)""")
    conn.commit()


def create_ships():
    size: int
    t_id: int
    ship_id: str
    booked_places: str # all book coords. First list for the 'z', next for the objects like this:
    hp: int
    x: int
    y: int
    #  [[(1, 2), (3, 4)], [(0, 0)]] cords in example is random, bus is show str
    already_place: int
    orientation: str
    cursor.execute("""CREATE TABLE ships
                      (size, t_id, ship_id, booked_places, hp, x, 
                       y, already_place, orientation)""")
    conn.commit()


def create_player():
    t_id: int
    nickname: str
    cursor.execute("""CREATE TABLE player (t_id, nickname)""")
    conn.commit()


def create_phase():
    t_id: int
    player_phase: str
    cursor.execute("""CREATE TABLE phase (t_id, player_phase)""")
    conn.commit()


def create_sea_battle_game():
    t_id_1: int
    t_id_2: int
    turn: int
    cursor.execute("""CREATE TABLE sea_battle_game (t_id_1, t_id_2, turn)""")


def create_in_queue():
    t_id: int
    nickname: str
    cursor.execute("""CREATE TABLE in_queue (t_id, nickname)""")
