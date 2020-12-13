from aiogram.types import Message
from main import bot
from telegram.data.text_for_handlers import dictionary
from errors.errors import MyError
from data_base import functions_for_work_with_bd


async def start_filter(message: Message):
    t_id = message.from_user.id

    # if player already in queue
    try:
        result = functions_for_work_with_bd.insert_player_to_queue(message)  # [(666),(555)] or False
    except MyError as err:
        await bot.send_message(t_id, *err.args)
        return

    # if only one player in the queue
    if not result:
        await bot.send_message(t_id, dictionary['/start'])

    # start game
    else:
        for t_id_from_result in result:
            print(result)
            await bot.send_message(t_id_from_result[0], dictionary['game_found'])
