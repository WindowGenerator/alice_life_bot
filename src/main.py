import asyncio
import logging
import signal
import sqlite3
from typing import AsyncGenerator

import aiohttp
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiohttp.web import Application, run_app

from src.bot import handlers
from src.config import DB_NAME, configuration
from src.db.repository import UserInfo

logger = logging.getLogger(__name__)
logger.setLevel(configuration["logging_level"])


async def bot_ctx(app: Application) -> AsyncGenerator:
    bot = Bot(configuration["token"], validate_token=True)

    app["bot"] = bot

    yield

    await bot.close()


async def dispatcher_ctx(app: Application) -> AsyncGenerator:
    loop = asyncio.get_event_loop()

    dp = Dispatcher(app["bot"], storage=MemoryStorage())

    handlers.setup(app, dp)

    task = asyncio.create_task(dp.start_polling(), name="bot task")

    yield

    dp.stop_polling()
    await dp.wait_closed()

    task.cancel()
    await task


async def db_ctx(app: Application) -> AsyncGenerator:
    # conn = sqlite3.connect(DB_NAME)
    app["repository"] = UserInfo(None)
    yield


def sig_handler(loop: asyncio.AbstractEventLoop, sig: str) -> None:
    logging.info(f"Receive interrupt signal: {sig}")
    loop.stop()


def main():
    loop = asyncio.get_event_loop()

    loop.add_signal_handler(signal.SIGINT, sig_handler, loop, "SIGINT")
    loop.add_signal_handler(signal.SIGTERM, sig_handler, loop, "SIGTERM")

    app = Application()
    app.cleanup_ctx.append(db_ctx)
    app.cleanup_ctx.append(bot_ctx)
    app.cleanup_ctx.append(dispatcher_ctx)

    try:
        run_app(app)
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt")
    finally:
        loop.stop()
        loop.close()

    logger.info("Shutdown :(")


if __name__ == "__main__":
    main()
