from aiogram.types import Message, CallbackQuery
from main import bot
from telegram.data.text_for_handlers import dictionary
from errors.errors import MyError
from data_base import functions_for_work_with_bd
from telegram.keyboards.inline import keyboard_generator
from logic import logic_for_aiogram, phases
from data_base.db import cursor, conn


async def start_filter(message: Message):
    t_id = message.from_user.id

    # if player in the next phase
    cursor.execute(f"SELECT player_phase FROM phase WHERE t_id = {t_id}")
    phase = cursor.fetchone()
    if phase:
        if phase[0] != 'in_queue':
            return

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
        await logic_for_aiogram.start_game(t_id=t_id)


async def filter_callback(callback: CallbackQuery):
    await callback.answer(cache_time=0.5)
    cursor.execute(f"SELECT player_phase FROM phase WHERE t_id = {callback.from_user.id}")
    phase = cursor.fetchone()[0]

    if phase == phases.phase_2:
        await logic_for_aiogram.call_back_for_phase_2(callback=callback)

    elif phase == phases.phase_4:
        await logic_for_aiogram.call_back_for_phase_4(callback)
