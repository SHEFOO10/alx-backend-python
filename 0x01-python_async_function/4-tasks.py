#!/usr/bin/env python3
"""
4. Tasks
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
     an async routine called wait_n that takes in 2 int arguments
     (in this order): n and max_delay
    """
    tasks: List[asyncio.Task[float]] = [
        wait_random(max_delay) for i in range(n)
        ]
    delays: List[float] = []
    for future in asyncio.as_completed(tasks):
        delay: float = await future
        delays.append(delay)
    return delays
