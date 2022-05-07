from functools import partial
from typing import List

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiohttp.web import Application

from src.bot.handlers import cancel
from src.bot.handlers import help as _help
from src.bot.handlers import poll, start


def setup(app: Application, dp: Dispatcher) -> None:
    start.setup(app, dp)
    _help.setup(app, dp)
    cancel.setup(app, dp)
    poll.setup(app, dp)
