from classes.some_classes import Ship, Player
from errors import errors
import random
from classes.constants_for_classes import height, length


def boom(player, ship):
    for tuple_cell in ship.booked_places[0]:  # work with 'z'
        player.field[tuple_cell] = 'fall'

    for tuple_cell in ship.booked_places[1]:  # work with objects
        player.field[tuple_cell] = 'boom_ship'


def check_place(player, ship) -> bool:
    """
    This function check place for the ship. If it's ok return True, else False
    :return: True or False
    """
    x = ship.x  # reset x
    y = ship.y  # reset y
    size = ship.size
    orientation = ship.orientation

    for i in range(size):
        if 0 <= x <= length - 1 and 0 <= y <= height - 1 and player.field[y, x] == 'zero':
            x, y = change_place(x, y, orientation)
            continue
        else:
            return False
    return True


def change_place(x, y, orientation) -> tuple:
    """
    This function change coords for the next address, in dependence orientation
    """
    if orientation == 'vertical':
        y += 1
    else:
        x += 1

    return x, y


def place_ship(player, ship, booked_places_in_random: list = False):
    """
    WATCH OUT! this function can change the player.field
    Function place the ship in to coords, when it possible
    """
    if not check_place(player, ship):
        raise errors.cant_place
    x = ship.x
    y = ship.y
    size = ship.size
    orientation = ship.orientation

    # place z
    for index in range(size):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= y + i <= height - 1 and 0 <= x + j <= length - 1:
                    player.field[y + i, x + j] = 'z'
                    if isinstance(booked_places_in_random, list):
                        booked_places_in_random.append((y + i, x + j))

                    ship.booked_places_append(0, (y + i, x + j))  # save 'z' coords in the class
        x, y = change_place(x, y, orientation)

    # place ship base
    x = ship.x  # reset x
    y = ship.y  # reset y
    for i in range(size):
        player.field[y, x] = ship  # should be not size, but ship
        if isinstance(booked_places_in_random, list):
            booked_places_in_random.append((y, x))
        ship.booked_places_append(1, (y, x))  # save object coords in the class
        x, y = change_place(x, y, orientation)

    ship.already_place = True  # Save ship status


def hit(player, y, x):  # should take enemy player and coords

    if isinstance(player.field[y, x], Ship):
        player.field[y, x].hp -= 1

        if player.field[y, x].hp == 0:
            boom(player, player.field[y, x])
            return

        player.field[y, x] = 'fire'

    elif player.field[y, x] in ['zero', 'z']:
        player.field[y, x] = 'fall'
        return True
    else:
        raise errors.already_hit  # ERROR, DON'T CHANGE THE TURN!!!


def check_if_win(player: Player):
    for ship in player.ships:
        if ship.hp > 0:
            return False

    return True


def random_place(player: Player):
    booked_places_in_random = []
    for ship in player.ships:
        while not ship.already_place:
            x = random.randrange(0, length)
            y = random.randrange(0, height)
            orientation = random.choice(['vertical', 'horizontal'])

            if (y, x) in booked_places_in_random:
                continue

            ship.x = x
            ship.y = y

            ship.orientation = orientation

            try:
                place_ship(player, ship, booked_places_in_random)
            except errors.MyError as err:
                pass
                # print(*err.args)
