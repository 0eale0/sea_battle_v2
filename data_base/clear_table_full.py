from db import cursor, conn

cursor.execute("DELETE FROM ships")
cursor.execute("DELETE FROM field")
cursor.execute("DELETE FROM in_queue")
cursor.execute("DELETE FROM messages")
cursor.execute("DELETE FROM phase")
cursor.execute("DELETE FROM ships")
cursor.execute("DELETE FROM sea_battle_game")