from main import dp, bot
from aiogram.types import Message, CallbackQuery
from telegram.keyboards.inline.keyboard_generator import keyboard, keyboard_2


# Send keyboard with field to user
async def phase_3(player_tele_id):
    msg_with_keyboard = await bot.send_message(chat_id=player_tele_id,
                                               text='Ваш противник кто-то кто-то',
                                               reply_markup=keyboard)

    '''await bot.edit_message_reply_markup(chat_id=message.from_user.id,
                                        message_id=msg_with_keyboard.message_id,
                                        reply_markup=keyboard_2)'''


@dp.callback_query_handler()
async def get_callback(call: CallbackQuery):
    await call.answer(cache_time=1)

    callback_data = call.data

    await bot.send_message(call.from_user.id, callback_data)
