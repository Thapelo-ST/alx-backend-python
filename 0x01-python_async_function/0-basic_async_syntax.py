#!/usr/bin/env python3
''' function that waits a random amount of time '''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    function that takes an agrument(optional) and returns a
    max delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
