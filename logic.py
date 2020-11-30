def place_ship(player, ship):
    x = ship.x
    y = ship.y
    size = ship.size
    orientation = ship.orientation

    # place z
    for index in range(size):
        for i in range(-1, 2):
            for j in range(-1, 2):
                player.field[y + i][x + j] = 'z'

                if orientation == 'vertical':
                    y += 1
                else:
                    x += 1

    # place ship bazis
    for i in range(size):
        player.field[y][x] = size  # should be not size, but ship

        if orientation == 'vertical':
            y += 1
        else:
            x += 1
