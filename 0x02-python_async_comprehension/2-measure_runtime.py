#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""
import asyncio
from time import perf_counter
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    """
    tasks: List[asyncio.Task] = [
        asyncio.create_task(async_comprehension()),
        asyncio.create_task(async_comprehension()),
        asyncio.create_task(async_comprehension()),
        asyncio.create_task(async_comprehension()),
    ]
    start: float = perf_counter()
    await asyncio.gather(*tasks)
    end: float = perf_counter() - start
    return end
