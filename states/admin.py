from aiogram.dispatcher.filters.state import State, StatesGroup


class AddCategory(StatesGroup):
    name = State()


class AddBook(StatesGroup):
    name = State()
    price = State()
    image = State()
    category = State()


class DeleteBook(StatesGroup):
    name = State()
    ha_yuq= State()