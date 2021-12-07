import asyncio
import random

from aiohttp import web


async def handle_request(request):
    print(f'Request from {request.remote} on {request.url}')
    await asyncio.sleep(random.random() + 1)
    return web.Response(text='Hi')


def start_app():
    app = web.Application()
    app.add_routes([
        web.get('/', handle_request),
    ])

    web.run_app(app)


if __name__ == '__main__':
    start_app()
