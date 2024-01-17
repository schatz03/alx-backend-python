#0-main.py
#!/usr/bin/env python3

import asyncio
from 0-async_generator import async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

