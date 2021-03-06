from classes import some_classes
import logic
from errors import errors
from aiogram import executor
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from telegram.data import config


loop = asyncio.get_event_loop()
bot = Bot(config.token)
dp = Dispatcher(bot, loop=loop)


def main():
    player_1 = some_classes.Player()
    player_2 = some_classes.Player()
    current_game = some_classes.SeaBattleGame(player_1, player_2)

    for ship in player_1.ships:
        print(ship.size)
        ship.x = int(input('x: '))
        ship.y = int(input('y: '))
        try:
            logic.place_ship(player_1, ship)

        except errors.MyError as err:
            print(*err.args)  # print text of error, from errors.py

    while True:
        logic.hit(player_1)
        print(player_1.field)  # there's should be the function for telegram, to notify the user


if __name__ == '__main__':
    from telegram.handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
    # main()
