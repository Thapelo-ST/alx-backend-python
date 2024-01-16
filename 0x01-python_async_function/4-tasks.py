#!/usr/bin/env python3
''' function that returns list of all delays from wait_random'''
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> list[float]:
    """
    Returns a list with n random delays using task_wait_random.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
