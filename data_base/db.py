import sqlite3

conn = sqlite3.connect("data_base/my_db.db")
cursor = conn.cursor()

all_t_id = "SELECT * from sea_battle"
insert_t_id = "INSERT INTO sea_battle VALUES('23', 'game')"


def insert_player_to_game(t_id: int, current_game: str):
    command = f"INSERT INTO sea_battle VALUES({t_id}, {current_game})"
    cursor.execute(command)
    conn.commit()
# ,

# cursor.execute("INSERT INTO ships VALUES(4, 4, 0, 0, 666, 1, 'vertical')")
# cursor.execute("SELECT * FROM ships t_id")
# result = cursor.fetchall()
# tables.create_in_queue()
# cursor.execute("INSERT INTO in_queue VALUES(666, 666)")
# conn.commit()
