import asyncio
import time
import aiohttp
import requests
import logging
import urllib
resources = [
    'https://docs.python.org/3/library/concurrent.futures.html',
    'https://zoom.us/',
    'https://github.com',
    'https://www.reddit.com/',
]


async def fetch_url(url):

    async with aiohttp.request('get', url) as request:
        return url, await request.text()


async def async_main():

    tasks = [
        asyncio.ensure_future(fetch_url(url))
        for url in resources
    ]
    started = time.time()
    for future in asyncio.as_completed(tasks):
        url, _ = await future
        print(url)
    print('Async spent time: {:.2f}'.format(time.time() - started))


def sync_main():

    started = time.time()
    for url in resources:
        requests.get(url)
        print(url)
    print('Sync spent time:  {:.2f}'.format(time.time() - started))


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)
sync_main()
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(async_main())
