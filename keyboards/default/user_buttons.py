from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_menyu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
b1 = KeyboardButton('Kitoblar ro\'yxati')
b2 = KeyboardButton('Mening buyurtmalarim')
b3 = KeyboardButton('Biz haqimizda!')
b4 = KeyboardButton('Shikoyatlar')
user_menyu.add(b1, b2, b3, b4)