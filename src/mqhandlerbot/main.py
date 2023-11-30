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

    connection = await aio_pika.connect_robust(get_amqp_url())
    publisher = PublisherAdapter(connection, queue)

    dp = dispatcher(publisher)
    bot = Bot(token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


def get_amqp_url() -> str:
    address = os.environ.get("AMQP_ADDRESS")
    port = os.environ.get("AMQP_PORT")
    user = os.environ.get("AMQP_USER")
    password = os.environ.get("AMQP_PASSWORD")

    return f"ampq://{user}:{password}@{address}:{port}/"


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(run_app())
