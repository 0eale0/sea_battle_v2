from main import dp, bot
from aiogram.types import Message, CallbackQuery
from telegram.keyboards.inline import keyboard_generator
from telegram.filters import main_filter
from classes import some_classes
from data_base.db import cursor, conn
import asyncio


# Send keyboard with field to user
async def phase_place_ships(player: some_classes.Player):
    keyboard = keyboard_generator.get_keyboard_phase_2(player)
    msg_with_keyboard = await bot.send_message(chat_id=player.t_id,
                                               text='Ваш противник кто-то кто-то',
                                               reply_markup=keyboard)

    cursor.execute("INSERT INTO messages VALUES(?, ?)", (msg_with_keyboard.message_id,
                                                         player.t_id))
    conn.commit()

    '''await bot.edit_message_reply_markup(chat_id=message.from_user.id,
                                        message_id=msg_with_keyboard.message_id,
                                        reply_markup=keyboard_2)'''


@dp.callback_query_handler()
async def get_callback(call: CallbackQuery):
    await call.answer(cache_time=1)

    await main_filter.filter_callback(callback=call)

    # callback_data = call.data

    # await bot.send_message(call.from_user.id, callback_data)


async def edit_message_after_ready(player):
    cursor.execute(f"SELECT * FROM messages WHERE t_id = {player.t_id}")
    msg_id = cursor.fetchone()[0]
    keyboard = keyboard_generator.get_actual_keyboard(player)
    await bot.edit_message_reply_markup(chat_id=player.t_id,
                                        message_id=msg_id,
                                        reply_markup=keyboard)


async def edit_message_after_hit(player, player_for_hit):
    cursor.execute(f"SELECT * FROM messages WHERE t_id = {player.t_id}")
    msg_id = cursor.fetchone()[0]
    if player.t_id != player_for_hit.t_id:
        keyboard = keyboard_generator.get_actual_keyboard(player_for_hit, invisible=True)
    else:
        keyboard = keyboard_generator.get_actual_keyboard(player_for_hit)

    await bot.edit_message_reply_markup(chat_id=player.t_id,
                                        message_id=msg_id,
                                        reply_markup=keyboard)


async def edit_message_after_random(player):
    cursor.execute(f"SELECT * FROM messages WHERE t_id = {player.t_id}")
    msg_id = cursor.fetchone()[0]
    keyboard = keyboard_generator.get_keyboard_phase_2(player)
    await bot.edit_message_reply_markup(chat_id=player.t_id,
                                        message_id=msg_id,
                                        reply_markup=keyboard)
