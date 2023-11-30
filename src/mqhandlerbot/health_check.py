import asyncio
import sys
import time

import aio_pika
from aiormq import AMQPConnectionError

from mqhandlerbot.main import get_amqp_url


async def check_connection():
    url = get_amqp_url()

    rollback = 1
    while rollback <= 16:
        try:
            await aio_pika.connect_robust(url)
            print("Successfully connection")
            sys.exit(0)
        except AMQPConnectionError:
            print(f"Connection failed. Try again after {rollback} sec.")
            time.sleep(rollback)
            rollback *= 2
    print("Connection filed. Exit.")
    sys.exit(1)


if __name__ == "__main__":
    asyncio.run(check_connection())
