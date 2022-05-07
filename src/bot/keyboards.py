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

from src.bot.texts import buttons, start

logger = logging.getLogger(__name__)


def get_start_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(buttons.poll)
    keyboard.row(buttons.help)

    return keyboard


def get_poll_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(buttons.back)
    keyboard.row(buttons.next)
    keyboard.row(buttons.cancel)

    return keyboard
