import sqlite3
import json  # надо добавить импорт поля и счетчик номер игры


class SaveGame:
    def __init__(self, number_game: str):
        self.con = sqlite3.connect("data_base.db")  # открывает файл где хранятся данные
        self.cursor = self.con.cursor()  # создает курсор для управления таблицой
        self.cursor.execute(
            "create table save_field_" + number_game + "(player1 enum, player2 enum, one_or_zero TINYINT)")

        # создает таблицу save_field_{number_game} и столбцы для таблички
        # где player1, player2 и one_or_zero название стобцов
        # если one_or_zero = 1, то ходит первый игрок иначе второй
        self.con.commit()  # сохраняет изменения

    def __add__(self, field_player1: str, field_player2: str, one_or_zero: int, number_game: str):
        self.cursor.execute("INSERT into save_field_" + number_game + " values (?, ?, ?)",
                            (field_player1, field_player2, one_or_zero))
        # добавляет значение в столбцы
        self.con.commit()

    def __del__(self, number_game: str):
        self.cursor.execute("DROP TABLE save_field_" + number_game)  # удаляет таблицу
        self.con.commit()

    def unpacking(self, number_game: str):
        # извлекает последние внесенные изменения
        for row in self.cursor.execute(
                "SELECT rowid, * FROM save_field_" + number_game + " ORDER BY player1"):
            tuple_info = row
        player_field_1 = json.loads(tuple_info[1])  # начинаем не с нуля так как на нулевом месте номер строки
        player_field_2 = json.loads(tuple_info[2])
        one_or_zero = tuple_info[3]
        return (player_field_1, player_field_2, one_or_zero)
