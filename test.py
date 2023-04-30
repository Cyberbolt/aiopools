'''
     The total number of coroutine tasks in this example is 100. If the maximum allowed number of coroutines maxio is set to 20, it needs to run 5 times to complete.
'''

import asyncio
from aiopools import AsyncPool


async def block_io(i):
     await asyncio. sleep(1)
     print(i)
     return i


async def main():
     # Set the maximum number of coroutines allowed maxio
     async with AsyncPool(maxio=20) as pool:
         tasks = [pool. create_task(block_io(i)) for i in range(100)]
    
     response = await asyncio. gather(*tasks)
     print(response)
    

if __name__ == '__main__':
     asyncio. run(main())
