import asyncio
import json
from os import mkdir, chdir
from shutil import rmtree
from subprocess import call
from random import choice

import aiohttp
from aiohttp import web


async def get_commit_message():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://whatthecommit.com/index.txt') as response:
            if response.ok:
                message = await response.text()
                return message.strip()
            raise web.HTTPError


async def get_commit_messages(n):
    return await asyncio.gather(*(get_commit_message() for _ in range(n)))


async def get_lorem_ipsum():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://fish-text.ru/get?format=json') as response:
            if response.ok:
                data = await response.text()
                data = json.loads(data)
                if data['status'] != 'success':
                    raise web.HTTPError
                return data['text']
            raise web.HTTPError


def write_file(filename):
    content = asyncio.run(get_lorem_ipsum())
    with open(filename, 'w') as f:
        f.write(content)


def generate_repo(dirname, commits=10):
    rmtree(dirname, ignore_errors=True)
    mkdir(dirname)
    chdir(dirname)
    call('git init', shell=True)

    messages = asyncio.run(get_commit_messages(commits))
    filenames = ('main', 'tests', 'application', 'views', 'helpers', 'bootstrap', 'whatever')

    for message in messages:
        filename = choice(filenames)
        write_file(filename)
        call(f'git add {filename}', shell=True)
        call(f'git commit -m "{message}"', shell=True)


if __name__ == '__main__':
    generate_repo('repo')
