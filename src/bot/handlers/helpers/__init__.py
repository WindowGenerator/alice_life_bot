import logging
from typing import Callable

from aiogram.types import Message

logger = logging.getLogger(__name__)


def is_message_with(text: str) -> Callable:
    def inner(message: Message) -> bool:
        return message.text and message.text.lower() == text.lower()

    return inner
