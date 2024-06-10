#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay) -> List[float]:
    """
     an async routine called wait_n that takes in 2 int arguments
     (in this order): n and max_delay
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    delays: List[float] = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)
    return delays
