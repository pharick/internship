from aiohttp import web

from aserver.urls import urls


class Application(web.Application):
    def __init__(self):
        super().__init__()
        self.add_routes(urls)
        self.runner = None

    async def app_start(self, host='0.0.0.0', port=80):
        self.runner = web.AppRunner(self)
        await self.runner.setup()
        site = web.TCPSite(self.runner, host, port)

        await site.start()
        return site.name

    async def app_stop(self):
        if self.runner is not None:
            await self.runner.cleanup()
