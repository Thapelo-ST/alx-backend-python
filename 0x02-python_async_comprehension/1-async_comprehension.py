#!/usr/bin/env python3
"""
creating and async comprehension that takes no argument
coroutines 10 random numbers using a comprehention from previous file
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    executes async generator in a co routine called async_generator 
    without taking arguments
    """
    return [n async for n in async_generator()]