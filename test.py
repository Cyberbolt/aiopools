import asyncio
from multiaio import MultiAIO


async def test(i):
    return i


async def main():
    async with asyncio.TaskGroup() as tg:
        ma = MultiAIO()
        r = tg.create_task(ma.create_task(test, 223))
    # async with MultiAIO() as ma:
    #     r = await ma.create_task(test, 223)
    print(await r)
        

if __name__ == '__main__':
    asyncio.run(main())
