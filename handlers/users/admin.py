from aiogram import types
from datetime import datetime
from loader import dp
from aiogram.dispatcher import FSMContext

from data.create import insert_category
from states.admin import AddCategory
from keyboards.default.admin_buttons import get_categores, admin_menyu
from data.config import ADMINS


@dp.message_handler(text="BACK🔙")
async def category_book(message: types.Message):
    await message.answer("Bosh menyu", reply_markup=admin_menyu)


@dp.message_handler(text="Kategory qo'shish")
async def category_book(message: types.Message):
    if f"{message.from_id}" in ADMINS:
        await message.answer("Kategory nomini kiriting")
        await AddCategory.name.set()


@dp.message_handler(state=AddCategory.name)
async def c_name(message: types.Message, state: FSMContext):
    try:
        insert_category(message.text, datetime.now())
        await state.finish()
        await message.answer('Category qo\'shildi!')
    except:
        await message.answer("Category nomi band boshqa nom tanlang")
        await AddCategory.name.set()



@dp.message_handler(text="Mavjud kategoriyalar")
async def category_list(message: types.Message):
    if f"{message.from_id}" in ADMINS:
        await message.answer("Mavjud categoriyalar", reply_markup=get_categores())
