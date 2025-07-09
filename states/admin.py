from aiogram.dispatcher.filters.state import State, StatesGroup


class AddCategory(StatesGroup):
    name = State()