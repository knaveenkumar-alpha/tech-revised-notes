# import asyncio
# import time
#
# import aiohttp
# from jupyter_server.utils import fetch
#
#
# async def by_aiohttp_concurrency(total: int):
#     # use aiohttp
#
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         url = "http://httpbin.org/ip"
#         for _ in range(total):
#             tasks.append(asyncio.create_task(fetch(url, session)))
#
#         original_result = await asyncio.gather(*tasks)
#         for res in original_result:
#             print(res)
#
#
# if __name__ == "__main__":
#     total = 100
#
#     start_time = time.time()
#     asyncio.run(by_aiohttp_concurrency(total))
#     print("--- It took %s seconds ---" % (time.time() - start_time))
#
# import requests
# import time
#
#
# def by_request(total: int):
#     with requests.Session() as session:
#         url = "http://httpbin.org/ip"
#
#         for _ in range(total):
#             res = session.get(url)
#             print(res.json())
#
#
# if __name__ == "__main__":
#     total = 100
#
#     start_time = time.time()
#     by_request(total)
#     print("--- It took %s seconds ---" % (time.time() - start_time))
#

# from concurrent.futures import ThreadPoolExecutor, as_completed
# import requests
# import time
#
#
# def by_request_threadpool(total: int):
#     def _request(session):
#         url = "http://httpbin.org/ip"
#         res = session.get(url)
#         return res.json()
#
#     session = requests.Session()
#
#     with ThreadPoolExecutor(max_workers=16) as executor:
#         future_to_index = {executor.submit(_request, session): i for i in range(total)}
#         for future in as_completed(future_to_index):
#             data = future.result()
#             print(data)
#
#     session.close()
#
#
# if __name__ == "__main__":
#     total = 100
#
#     start_time = time.time()
#     by_request_threadpool(total)
#     print("--- It took %s seconds ---" % (time.time() - start_time))


import asyncio
import aiohttp
import time

import nest_asyncio

nest_asyncio.apply()


async def by_aiohttp(total: int):
    # use aiohttp
    async with aiohttp.ClientSession() as session:
        url = "http://httpbin.org/ip"

        for _ in range(total):
            res = await session.get(url)
            print(await res.json())

    start_time = time.time()
    asyncio.run(by_aiohttp(total))
    print("--- It took %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    total = 10

    start_time = time.time()
    asyncio.run(by_aiohttp(total))
    print("--- It took %s seconds ---" % (time.time() - start_time))


# import nest_asyncio
#
# nest_asyncio.apply()
# import asyncio
#
#
# async def echo(x):
#     for i in range(0, 5):
#         print(x, i)
#         sleep(1)
#
#
# def testNested():
#     for i in range(0, 5):
#         asyncio.get_event_loop().create_task(echo(i))
#     inner()
#
#
# def inner():
#     for i in range(5, 10):
#         asyncio.get_event_loop().create_task(echo(i))
#     sleep(20)
#
#
# def sleep(z):
#     asyncio.run(asyncio.sleep(z))
#
#
# testNested()
