import time

import pytest

from aserver.start_server import get_app
from .storm import storm


class TestServer:
    @pytest.fixture
    async def app_address(self, aiohttp_server, aiohttp_unused_port):
        app = get_app()
        server = await aiohttp_server(app, port=aiohttp_unused_port())
        server.start_server()
        yield f'http://{server.host}:{server.port}'
        server.close()

    @pytest.mark.asyncio
    async def test_storm(self, app_address):
        start = time.time()
        success_count = await storm(app_address, 1000)
        estimate = time.time() - start
        assert success_count == 1000
        assert estimate <= 10
