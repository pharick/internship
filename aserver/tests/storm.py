import asyncio

import aiohttp

URL = 'http://127.0.0.1'
REQUEST_COUNT = 1000


async def make_request(url, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if not response.ok:
                        print(f'Request failed: status {response.status}')
                        return False

                    text = await response.text()
                    print(f'Request succeed: {text}')
                    return text == 'Hi'
            except aiohttp.ClientConnectionError:
                print(f'Request failed: connection error')
                return False


async def storm(url, request_count):
    success_count = 0
    semaphore = asyncio.Semaphore(200)
    requests_makers = [make_request(url, semaphore) for i in range(request_count)]
    for future in asyncio.as_completed(requests_makers):
        res = await future
        success_count += res

    return success_count


def main():
    success_count = asyncio.run(storm(URL, REQUEST_COUNT))
    print(f'Result: {success_count} / {REQUEST_COUNT} successful requests')


if __name__ == '__main__':
    main()
