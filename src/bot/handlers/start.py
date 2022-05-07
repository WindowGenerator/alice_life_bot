import argparse
import logging
from functools import partial
from typing import List

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiohttp.web import Application

from src.bot.keyboards import get_start_keyboard
from src.bot.texts import buttons, start

logger = logging.getLogger(__name__)


def setup(app: Application, dp: Dispatcher) -> None:
    dp.message_handler
    dp.register_message_handler(partial(start_handler, app), commands=["start"])


async def start_handler(
    app: Application, message: types.Message, with_menu: bool = False
) -> None:
    await message.reply(
        start.menu
        if with_menu
        else start.greatings_text.format(full_name=message.from_user.full_name),
        reply_markup=get_start_keyboard(),
    )
