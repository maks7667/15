import aiohttp
import asyncio
import time

async def load_data_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def load_data_parallel(urls):
    tasks = [load_data_async(url) for url in urls]
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Total time: {end_time - start_time} seconds")

if __name__ == "__main__":
    start_time = time.time()
    urls = ["https://fanfics.me/character1964"] * 100  
    asyncio.run(load_data_parallel(urls))