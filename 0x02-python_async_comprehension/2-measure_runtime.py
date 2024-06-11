#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    """
    tasks = [
        asyncio.create_task(async_comprehension()),
        asyncio.create_task(async_comprehension()),
        asyncio.create_task(async_comprehension()),
        asyncio.create_task(async_comprehension()),
    ]
    start = perf_counter()
    await asyncio.gather(*tasks)
    end = perf_counter() - start
    return end
