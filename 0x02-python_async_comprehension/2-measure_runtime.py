#!/usr/bin/env python3
""" running async comprehesion parallel to async gather"""
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """runs async comprehesion parallel to async gather"""
    start_time = perf_counter()
    
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = perf_counter()
    return end_time - start_time