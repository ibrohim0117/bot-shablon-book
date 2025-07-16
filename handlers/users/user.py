from aiogram import types
from keyboards.default.admin_buttons import get_books
from data.selectt import show_detail_book, show_all_book_name

from loader import dp


@dp.message_handler(text="Kitoblar ro'yxati")
async def book_list(message: types.Message):
    await message.answer("Kitoblar ro'yxati", reply_markup=get_books())



@dp.message_handler(lambda msg: (msg.text, ) in show_all_book_name())
async def book_detail(msg: types.Message):
    data = show_detail_book(msg.text)
    book_name = msg.text
    book_price = data[1]
    book_image = data[2]
    await msg.answer_photo(book_image, f"Kitob nomi: {book_name}\nKitob narxi: {book_price}", reply_markup=inline_plus())
    