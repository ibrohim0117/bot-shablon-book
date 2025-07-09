from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.selectt import show_all_categores

admin_menyu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
b1 = KeyboardButton('Mavjud kategoriyalar')
b2 = KeyboardButton("Kategory qo'shish")
b3 = KeyboardButton('Mavjud kitoblar')
b4 = KeyboardButton("Kitob qo'shish")
b5 = KeyboardButton("Kitobni o'zgartirish")
b6 = KeyboardButton("Kitobni o'chirish")
b7 = KeyboardButton("Reklama")
b8 = KeyboardButton("Foydalanuvchilar soni")
admin_menyu.add(b1, b2, b3, b4, b5, b6, b7, b8)


def get_categores():
    keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in show_all_categores():
        keyboards.insert(KeyboardButton(i[0]))
    return keyboards.add(KeyboardButton("BACK🔙"))