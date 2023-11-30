from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from mqhandlerbot.dto import TgMessage
from mqhandlerbot.publisher import PublisherProto


def dispatcher(publisher: PublisherProto) -> Dispatcher:
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        await message.answer("Привіт, відправ любе повідомлення.")

    @dp.message()
    async def message_handler(message: Message) -> None:
        tg_message = TgMessage(
            message.from_user.username or "unknown",
            message.text or "",
            message.date,
        )
        await publisher.publish(tg_message)

    return dp
