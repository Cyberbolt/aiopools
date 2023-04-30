import asyncio
from aiopools import AsyncPool


async def block_io(i):
    await asyncio.sleep(1)
    print(i)
    return i


async def main2():
    async with AsyncPool(maxio=100) as pool:
        tasks = []
        for i in range(100):
            tasks.append(
                pool.create_task(block_io(i))
            )
    
    response = await asyncio.gather(*tasks)
    print(response)


async def main():
    async with AsyncPool(maxio=100) as pool:
        tasks = [pool.create_task(block_io(i)) for i in range(100)]
    
    response = await asyncio.gather(*tasks)
    print(response)
    

if __name__ == '__main__':
    asyncio.run(main())
