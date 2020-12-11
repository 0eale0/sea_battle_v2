from classes import some_classes
from data_base.db import cursor, conn
import sqlite3
# Info from db

# For ship
size: int
hp: int
x: int
y: int
booked_places: list
t_id: int
already_place: bool
orientation: str


def create_ships(tuples_with_basic_info, tuple_with_booked_places): # It's difference because booked_place is list
    for i in range(len(tuples_with_basic_info)):  # count of ships


