import asyncio

import aiohttp

URL = 'http://127.0.0.1:8080'
REQUEST_COUNT = 1000


async def make_request(i):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(URL) as response:
                if not response.ok:
                    print(f'Request {i} failed: status {response.status}')
                    return False

                text = await response.text()
                print(f'Request {i} succeed: {text}')
                return text == 'Hi'
        except aiohttp.ClientConnectionError:
            print(f'Request {i} failed: connection error')
            return False


async def storm():
    success_count = 0
    requests_makers = [make_request(i + 1) for i in range(REQUEST_COUNT)]
    for future in asyncio.as_completed(requests_makers):
        res = await future
        success_count += res

    print(f'Result: {success_count} / {REQUEST_COUNT} successfull requests')


if __name__ == '__main__':
    asyncio.run(storm())
