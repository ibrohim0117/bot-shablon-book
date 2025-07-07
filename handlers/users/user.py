from aiogram import types

from loader import dp


@dp.message_handler(text="Kitoblar ro'yxati")
async def books(message: types.Message):
    await message.answer("Hozircha kitoblar mavjud emas!")