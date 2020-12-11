from db import cursor, conn



def insert_player_to_queue(t_id):
    """
    Insert player to the queue if he's only one write start, else insert player to the table
    sea_battle and start game
    """
    command = "SELECT * from in_queue"
    cursor.execute(command)
    queue = cursor.fetchall()  # queue right now

    # if 2 players in the queue
    if len(queue) > 0:
        print('start_game')
        cursor.execute("DELETE FROM in_queue")  # clear table
        pass  # return id's for send_message
    else:
        command = f"INSERT INTO in_queue VALUES({t_id})"
        cursor.execute(command)
        conn.commit()
    print(queue)


if __name__ == "__main__":
    pass
