from aiogram import types
from keyboards.default.admin_buttons import get_books

from loader import dp


@dp.message_handler(text="Kitoblar ro'yxati")
async def book_list(message: types.Message):
    await message.answer("Kitoblar ro'yxati", reply_markup=get_books())



# @dp.message_handler()
# async def book_detail(msg: types.Message):
#     if show_detail_book(msg.text):
#         data = show_detail_book(msg.text)
#         book_name = msg.text
#         book_price = data[1]
#         book_image = data[2]
#         await msg.answer_photo(book_image, f"Kitob nomi: {book_name}\nKitob narxi: {book_price}", reply_markup=inline_plus())
#     else:
#         await msg.answer("Bunday kitob bazadan topilmadi!")