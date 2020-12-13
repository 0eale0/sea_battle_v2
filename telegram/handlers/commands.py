from main import dp, bot

from aiogram.types import Message
from telegram.data.config import admin_id
from telegram.data import text_for_handlers
from telegram import filters


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Бот запущен')


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await filters.start_filter(message)
