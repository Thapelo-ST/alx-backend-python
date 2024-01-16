#!/usr/bin/env python3
''' function that returns list of all delays from wait_random'''
wait_n = __import__('1-concurrent_coroutines').wait_n
import time
import asyncio


async def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    
    await wait_n.wait_n(n, max_delay)
    
    end_time = time.time()
    total_time = end_time - start_time
    
    return total_time / n  # average delay
