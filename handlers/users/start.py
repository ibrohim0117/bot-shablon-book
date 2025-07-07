from aiogram import types
from datetime import datetime
from data import config
from aiogram.dispatcher.filters.builtin import CommandStart

from data.create import insert_user
from keyboards.default.user_buttons import user_menyu
from keyboards.default.admin_buttons import admin_menyu

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # print(config.ADMINS, message.from_id)
    if f"{message.from_id}" in config.ADMINS:
        await message.answer(f"Salom buyuk shaman!", reply_markup=admin_menyu)
    else:
        insert_user(message.from_user.username, message.from_id, datetime.now())
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=user_menyu)
