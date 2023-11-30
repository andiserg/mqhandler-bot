import asyncio
import os
import sys
import time

import aio_pika
from aiormq import AMQPConnectionError


async def check_connection():
    address = os.environ.get("AMQP_ADDRESS")
    port = os.environ.get("AMQP_PORT")
    user = os.environ.get("AMQP_USER")
    password = os.environ.get("AMQP_PASSWORD")

    url = f"ampq://{user}:{password}@{address}:{port}/"

    print(url)

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
