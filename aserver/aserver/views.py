import asyncio
import random

from aiohttp import web


async def index(request):
    await asyncio.sleep(random.random() + 1)
    return web.Response(text='Hi')
