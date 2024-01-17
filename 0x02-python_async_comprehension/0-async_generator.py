#!/usr/bin/env python3
"""
module that loop 10 times and asynchronously wait 1 second yeilding
a random number after each second, it doesnt take any arguments
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    module that loop 10 times and asynchronously wait 1 second yeilding
    a random number after each second, it doesnt take any arguments
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
