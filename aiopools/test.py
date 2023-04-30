import asyncio
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

CPU_COUNT = multiprocessing.cpu_count


class SingleAIO:
    def __init__(self, max_io: int = 20):
        self.io_num = 0
        self.max_io = max_io
        
    async def aio_pool(self, func, *args, **kwargs):
        if self.io_num > self.max_io:
            print(self.io_num)
        async with asyncio.TaskGroup() as tg:
            self.io_num += 1
            response = await tg.create_task(func(*args, **kwargs))
            self.io_num -= 1
            return response

    def process(self, func, *args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.aio_pool(func, *args, **kwargs))


class MultiAIO:
    def __init__(self, max_process: int = CPU_COUNT, max_io: int = 20):
        self.saio = SingleAIO(max_io=max_io)
        self.executor = ProcessPoolExecutor(max_workers=max_process)
    
    async def create_task(self, func, *args, **kwargs):
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            self.executor, self.saio.process, func, *args, **kwargs)
        return result

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
