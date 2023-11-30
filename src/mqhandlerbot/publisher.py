import json
from dataclasses import asdict
from typing import Protocol

import aio_pika
from aio_pika.abc import AbstractRobustConnection

from mqhandlerbot.dto import TgMessage


class PublisherProto(Protocol):
    async def publish(self, message: TgMessage) -> None:
        """Publish a message to the message queue"""
        pass


class PublisherAdapter(PublisherProto):
    def __init__(self, connection: AbstractRobustConnection, queue: str):
        self.connection = connection
        self.queue = queue

    async def publish(self, message: TgMessage) -> None:
        async with self.connection:
            channel = await self.connection.channel()
            data = asdict(message)
            data["time"] = message.time.isoformat()
            encode_message = json.dumps(data).encode()
            await channel.default_exchange.publish(
                aio_pika.Message(body=encode_message), routing_key=self.queue
            )
