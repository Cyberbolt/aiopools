import asyncio


class AsyncPool:
    
    def __init__(self, maxio: int = 20):
        '''
            maxio: The maximum number of coroutines allowed by the system.
        '''
        self.semaphore = asyncio.Semaphore(maxio)
        self.tasks = []
    
    async def create_task(self, task):
        async with self.semaphore:
            return await task

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
