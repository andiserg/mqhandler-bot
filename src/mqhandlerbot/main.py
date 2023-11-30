import asyncio
import logging
import os
import sys

import aio_pika
from aiogram import Bot
from aiogram.enums import ParseMode

from mqhandlerbot.handlers import dispatcher
from mqhandlerbot.publisher import PublisherAdapter


async def run_app() -> None:
    token = os.environ.get("BOT_TOKEN")
    queue = os.environ.get("BOT_QUEUE")

    connection = await aio_pika.connect_robust("")
    publisher = PublisherAdapter(connection, queue)

    dp = dispatcher(publisher)
    bot = Bot(token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(run_app())
