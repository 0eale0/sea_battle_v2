from main import dp, bot

from aiogram.types import Message
from telegram.config import admin_id
from telegram.handlers import text_for_handlers


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Бот запущен')


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=text_for_handlers.dictionary[message.text])
