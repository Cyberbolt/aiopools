import asyncio
from concurrent.futures import ProcessPoolExecutor


async def test2():
    return 4


async def test():
    async with asyncio.TaskGroup() as tg:
        r = tg.create_task(test2())
    print(await r)
        
if __name__ == '__main__':
    asyncio.run(test())