"""function that takes an interger and returns asyncio.Task"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    takes an interger and returns asyncio.Tas
    """
    return asyncio.create_task(wait_random(max_delay))
