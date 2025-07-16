from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def inline_plus(count=1):
    ikm = InlineKeyboardMarkup(row_width=3)
    i1 = InlineKeyboardButton(text='+', callback_data='plus')
    i2 = InlineKeyboardButton(text=f'{count}', callback_data='count')
    i3 = InlineKeyboardButton(text='-', callback_data='menus')
    i4 = InlineKeyboardButton(text='🛒Savatga', callback_data='order')
    ikm.add(i1, i2, i3, i4)
    return ikm


yes_or_no = InlineKeyboardMarkup(row_width=2)
yes = InlineKeyboardButton(text='Ha', callback_data='yes')
no = InlineKeyboardButton(text="Yo'q", callback_data='no')
yes_or_no.add(yes, no)