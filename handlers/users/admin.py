from aiogram import types
from datetime import datetime
from loader import dp
from aiogram.dispatcher import FSMContext

from data.create import insert_category, insert_book
from states.admin import AddCategory, AddBook
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


# add book
@dp.message_handler(text="Kitob qo'shish")
async def add_book(message: types.Message):
    if f"{message.from_id}" in ADMINS:
        await message.answer("Kitob nomini kiriting")
        await AddBook.name.set()


@dp.message_handler(state=AddBook.name)
async def book_name_f(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Kitob narxini kiriting")
    await AddBook.price.set()


@dp.message_handler(state=AddBook.price)
async def book_price_f(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Kitob rasmini kiriting")
    await AddBook.image.set()


@dp.message_handler(state=AddBook.image, content_types=types.ContentTypes.PHOTO)
async def book_image_f(message: types.Message, state: FSMContext):
    image_data = message.photo[1].file_id
    await state.update_data(rasm=image_data)
    await message.answer("Kategory tanlang", reply_markup=get_categores())
    await AddBook.category.set()



@dp.message_handler(state=AddBook.category)
async def book_category_f(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get('name')
    price = data.get('price')
    image_data = data.get('rasm')
    date = datetime.now()
    category = message.text
    insert_book(name, price, image_data, date, category)
    await message.answer("Kitob qushildi", reply_markup=admin_menyu)
    await state.finish()





    





