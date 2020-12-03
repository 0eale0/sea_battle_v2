from classes import constants_for_classes


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
        if 0 <= x <= 9 and 0 <= y <= 9 and player.field[y, x] == '0':
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


def place_ship(player, ship):
    """
    WATCH OUT! this function can change the player.field
    Function place the ship in to coords, when it possible
    """
    if not check_place(player, ship):
        return False
    x = ship.x
    y = ship.y
    size = ship.size
    orientation = ship.orientation

    # place z
    for index in range(size):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= y + i <= 9 and 0 <= x + j <= 9:
                    player.field[y + i, x + j] = 'z'

        x, y = change_place(x, y, orientation)

    # place ship base
    x = ship.x  # reset x
    y = ship.y  # reset y
    for i in range(size):
        player.field[y, x] = ship  # should be not size, but ship

        x, y = change_place(x, y, orientation)


def hit(player):
    coordinats = [int(i) for i in input('y/x: ').split()]
    x = coordinats[0]
    y = coordinats[1]
    if str(type(player.field[y, x])) == "<class 'classes.some_classes.Ship'>":
        player.field[y, x].hp -= 1
        if player.field[y, x].hp == 0:
            pass
        player.field[y, x] = '+'
    else:
        player.field[y, x] = '*'
    # TODO атака корабля/клетки
    # TODO продолжение хода при попадане
    # Todo создание битого поля при уничтожение корабля
