from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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