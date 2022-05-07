from aiogram.dispatcher.filters.state import State, StatesGroup


class Poll(StatesGroup):
    name = State()
    specialization = State()
    where_from = State()
