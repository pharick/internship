from aiohttp import web

from aserver.urls import urls


def get_app():
    app = web.Application()
    app.add_routes(urls)
    return app


def main(port=80):
    app = get_app()
    web.run_app(app, port=port)


if __name__ == '__main__':
    main()
