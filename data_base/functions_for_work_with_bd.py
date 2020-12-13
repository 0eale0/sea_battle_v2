from data_base.db import cursor, conn
from data_base import tables
from errors import errors
from visual import emojies
from aiogram.types import Message
from data_base import functions_for_create_objects
import json


def get_players(table):
    cursor.execute(f"SELECT t_id FROM {table}")
    players = cursor.fetchall()
    players = [tuple_[0] for tuple_ in players]
    return players


def create_phase(t_id):
    players = get_players('phase')
    if t_id in players:
        return
    else:
        cursor.execute("INSERT INTO phase VALUES(?, ?)", (t_id, 'in_queue'))
        conn.commit()


def change_phase(t_id, phase):
    cursor.execute("UPDATE phase SET player_phase = ? WHERE t_id = ?", (phase, t_id))
    conn.commit()
    pass


def insert_player_to_queue(message: Message):
    """
    Insert player to the queue if he's only one write start, else insert player to the table
    sea_battle and start game
    return: False if only one player, and [t_id_1, t_id_2] if 2 players in the queue
    """
    t_id = message.from_user.id
    nickname = message.from_user.username
    command = "SELECT * from in_queue"
    cursor.execute(command)
    queue = cursor.fetchall()  # queue right now
    print(queue)

    if len(queue) == 1 and t_id in queue[0]:  # if already one in queue
        raise errors.already_in_queue

    # if 2 players in the queue
    elif len(queue) == 1:
        cursor.execute("INSERT INTO in_queue VALUES(?, ?)", (t_id, nickname))

        create_phase(t_id)  # create value in table phase
        conn.commit()
        print('start_game')

        players = get_players(table='in_queue')
        for player in players:
            change_phase(player, 'place_ships')

        cursor.execute("SELECT * FROM in_queue")  # get players in the queue
        result = cursor.fetchall()  # [(666, 555)]
        print(result)
        cursor.execute("DELETE FROM in_queue")  # clear table
        conn.commit()

        return result

    else:
        create_phase(t_id)  # create value in table phase

        cursor.execute("INSERT INTO in_queue VALUES(?, ?)", (t_id, nickname))
        conn.commit()
        return False


if __name__ == "__main__":
    pass
