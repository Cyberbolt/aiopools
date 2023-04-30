import asyncio
from aiopools import AsyncPool


async def block_io(i):
    await asyncio.sleep(1)
    print(i)
    return i


async def main():
    async with asyncio.Semaphore(100):
        tasks = [asyncio.create_task(block_io(i)) for i in range(100)]
    
    response = await asyncio.gather(*tasks)
    print(response)
    

if __name__ == '__main__':
    asyncio.run(main())
