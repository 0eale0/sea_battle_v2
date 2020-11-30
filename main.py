import some_classes
import logic


def main():
    player_1 = some_classes.Player()
    player_2 = some_classes.Player()
    current_game = some_classes.SeaBattleGame(player_1, player_2)

    for ship in player_1.ships:
        print(ship.size)
        print(player_1.field)
        ship.x = int(input('x: '))
        ship.y = int(input('y: '))
        logic.place_ship(player_1, ship)
        for line in player_1.field:
            print(*line)


if __name__ == '__main__':
    main()
