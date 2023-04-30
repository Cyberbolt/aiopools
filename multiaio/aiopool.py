import asyncio


async def test(i):
    await asyncio.sleep(1)
    print(i)
    multiaio = 1


async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(100):
            tg.create_task(test(i))
    print("completed")


if __name__ == '__main__':
    asyncio.run(main())
