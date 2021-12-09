import asyncio

from application import Application


def start_app(port=80):
    loop = asyncio.get_event_loop()
    app = Application()
    address = loop.run_until_complete(app.app_start('0.0.0.0', port))

    print(f'Application is running on {address}')

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    print('Application is stopping...')
    loop.run_until_complete(app.app_stop())
    loop.close()


if __name__ == '__main__':
    start_app()
