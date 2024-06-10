#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer argument (max_delay)
with default of 10
named wait_random that waits for a random delay between 0 and max_delay
(included and float value) seconds
and eventually returns it.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    """
    waitTime: float = random.uniform(0, max_delay)
    return await asyncio.sleep(waitTime, result=waitTime)
