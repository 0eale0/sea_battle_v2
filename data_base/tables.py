from db import cursor, conn


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
    hp: int
    x: int
    y: int
    booked_places: str  # all book coords. First list for the 'z', next for the objects like this:
    #  [[(1, 2), (3, 4)], [(0, 0)]] cords in example is random, bus is show structure
    t_id: int
    ship_id: int
    already_place: int
    orientation: str
    cursor.execute("""CREATE TABLE ships
                      (size, hp, x, y, booked_places, t_id, ship_id, 
                      already_place, orientation)""")
    conn.commit()


def create_player():
    t_id: int
    nickname: str
    cursor.execute("""CREATE TABLE player (t_id, nickname)""")
    conn.commit()


def create_sea_battle_game():
    t_id_1: int
    t_id_2: int
    turn: int
    cursor.execute("""CREATE TABLE sea_battle_game (t_id_1, t_id_2, turn)""")


def create_in_queue():
    t_id: int
    cursor.execute("""CREATE TABLE in_queue (t_id)""")
