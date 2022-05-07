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

from src.bot.handlers.cancel import cancel_handler
from src.bot.handlers.helpers import is_message_with
from src.bot.handlers.start import start_handler
from src.bot.keyboards import get_poll_keyboard, get_start_keyboard
from src.bot.states import Poll
from src.bot.texts import buttons, poll, start

logger = logging.getLogger(__name__)


def setup(app: Application, dp: Dispatcher) -> None:
    dp.register_message_handler(
        partial(poll_handler, app), is_message_with(buttons.poll)
    )
    dp.register_message_handler(partial(process_name, app), state=Poll.name)
    dp.register_message_handler(
        partial(process_specialization, app), state=Poll.specialization
    )
    dp.register_message_handler(partial(process_where, app), state=Poll.where_from)


async def poll_handler(app: Application, message: types.Message) -> None:
    await Poll.name.set()
    await message.reply(poll.question_name, reply_markup=get_poll_keyboard())


async def process_name(
    app: Application, message: types.Message, state: FSMContext
) -> None:
    async with state.proxy() as proxy:
        text = message.text

        if is_message_with(buttons.back)(message):
            await state.finish()
            await start_handler(app, message=message, with_menu=True)
        elif is_message_with(buttons.next)(message):
            if "name" not in proxy:
                await Poll.name.set()
                return

            await Poll.specialization.set()
            await message.reply(
                poll.question_specialization, reply_markup=get_poll_keyboard()
            )

        elif is_message_with(buttons.cancel)(message):
            await cancel_handler(message, state)
            await message.reply(start.menu, reply_markup=get_start_keyboard())
        else:
            proxy["name"] = message.text.strip()
            await Poll.specialization.set()
            await message.reply(poll.question_specialization)


async def process_specialization(
    app: Application, message: types.Message, state: FSMContext
) -> None:
    async with state.proxy() as proxy:
        text = message.text

        if is_message_with(buttons.back)(message):
            await Poll.name.set()
            await message.reply(poll.question_name, reply_markup=get_poll_keyboard())
        elif is_message_with(buttons.next)(message):
            if "specialization" in proxy:
                text = poll.question_where
                await Poll.where_from.set()
            else:
                text = poll.question_specialization
                await Poll.specialization.set()

            await message.reply(text, reply_markup=get_poll_keyboard())
        elif is_message_with(buttons.cancel)(message):
            await cancel_handler(message, state)
            await message.reply(start.menu, reply_markup=get_start_keyboard())
        else:
            proxy["specialization"] = message.text.strip()
            await Poll.where_from.set()
            await message.reply(poll.question_where)


async def process_where(
    app: Application, message: types.Message, state: FSMContext
) -> None:
    async with state.proxy() as proxy:
        text = message.text

        if is_message_with(buttons.back)(message):
            await Poll.specialization.set()
            await message.reply(
                poll.question_specialization, reply_markup=get_poll_keyboard()
            )
        elif is_message_with(buttons.next)(message):
            await Poll.where.set()
            await message.reply(poll.question_where, reply_markup=get_poll_keyboard())
        elif is_message_with(buttons.cancel)(message):
            await cancel_handler(message, state)
            await message.reply(start.menu, reply_markup=get_start_keyboard())
        else:
            proxy["where"] = message.text.strip()

            await state.finish()
            await start_handler(app, message=message, with_menu=True)
