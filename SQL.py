import sqlite3
import json  # надо добавить импорт поля и счетчик номер игры


class SaveGame:
    def __init__(self, number_game: int):
        self.con = sqlite3.connect("data_save_base_№" + number_game + ".db")  # создает файл где хранятся данные
        self.cursor = self.con.cursor()  # создает курсор для управления таблицой
        self.cursor.execute("create table save_field (player1 enum, player2 enum, one_or_zero TINYINT)")
        # создает таблицу save_field и столбцы для таблички где player1, player2 и one_or_zero название стобцов
        # если one_or_zero = 1, то ходит первый игрок иначе второй

    def __add__(self, field_player1: str, field_player2: str, one_or_zero: int):
        self.cursor.execute("INSERT into save_field values (?, ?, ?)", (field_player1, field_player2, one_or_zero))
        # добавляет значение в столбцы

    def __del__(self):
        self.cursor.execute("DELETE FROM save_field")  # удаляет всю инфу с таблицы

    def save(self):
        self.con.commit()  # сохраняет таблицу обязательно делай иначе ничего не сохранится

    def unpacking(self):
        for row in self.cursor.execute(
                "SELECT rowid, * FROM save_field ORDER BY player1"):  # кастыльный но рабочий метод извлечения инфы
            tuple_info = row
        player_field_1 = json.loads(tuple_info[1])  # начинаем не с нуля так как на нулевом месте номер строки
        player_field_2 = json.loads(tuple_info[2])
        one_or_zero = tuple_info[3]
        return (player_field_1, player_field_2, one_or_zero)
