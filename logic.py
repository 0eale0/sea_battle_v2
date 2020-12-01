def place_ship(player, ship):
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
                    player.field[y + i][x + j] = 'z'

        if orientation == 'vertical':
            y += 1
        else:
            x += 1

    # place ship base
    x = ship.x  # reset x
    y = ship.y  # reset y
    for i in range(size):
        player.field[y][x] = str(size)  # should be not size, but ship

        if orientation == 'vertical':
            y += 1
        else:
            x += 1


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
        if 0 <= x <= 9 and 0 <= y <= 9:
            if player.field[y][x] == '0':
                if orientation == 'vertical':
                    y += 1
                else:
                    x += 1
                continue
        else:
            return False
        return True
