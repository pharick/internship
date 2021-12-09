import asyncio

import pytest

from aserver.application import Application
from .storm import storm


class TestServer:
    @pytest.fixture
    async def app_address(self, aiohttp_unused_port):
        port = aiohttp_unused_port()
        app = Application()
        address = await app.app_start('127.0.0.1', port)
        yield address
        await app.app_stop()

    @pytest.mark.asyncio
    async def test_storm(self, app_address, aiohttp_client):
        success_count = await storm(app_address, 1000)
        assert success_count == 1000
