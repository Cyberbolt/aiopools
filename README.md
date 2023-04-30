# aiopools

[中文版](#中文版)

AIOPools is a Python AsyncIO Semaphore wrapper for building AsyncIO coroutine pools. ThreadPoolExecutor (thread pool) and ProcessPoolExecutor (process pool) similar to concurrent.futures, designed to enable Python code to achieve the highest number of concurrency.

## installation method

Environmental requirements: Python 3.8 and above

1. Enter the command window, create a virtual environment, and enter the following commands in sequence

Linux and macOS:

```bash
python3 -m venv venv # Create a virtual environment
.venv/bin/activate # Activate the virtual environment
```

Windows:

```bash
python -m venv venv # Create a virtual environment
venv\Scripts\activate # activate the virtual environment
```

2. Install AIOPools, enter in sequence


```python
pip install --upgrade pip
pip install aiopools
```

## Link

- GitHub: [https://github.com/Cyberbolt/aiopools](https://github.com/Cyberbolt/aiopools)
- CyberLight: [https://www.cyberlight.xyz/](https://www.cyberlight.xyz/)

## Minimal example

```python
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

```

# 中文版

AIOPools 是 Python AsyncIO Semaphore 的包装器，用于构建 AsyncIO 协程池。类似于 concurrent.futures 的 ThreadPoolExecutor (线程池) 和 ProcessPoolExecutor (进程池)，旨在使 Python 代码达到最高并发数。

## 安装方法

环境要求：Python 3.8 及以上

1.进入命令窗口，创建虚拟环境，依次输入以下命令

Linux 和 macOS:

```bash
python3 -m venv venv # 创建虚拟环境
. venv/bin/activate # 激活虚拟环境
```

Windows:

```bash
python -m venv venv # 创建虚拟环境
venv\Scripts\activate # 激活虚拟环境
```

2.安装 AIOPools，依次输入


```python
pip install --upgrade pip
pip install aiopools
```

## 链接

- GitHub: [https://github.com/Cyberbolt/aiopools](https://github.com/Cyberbolt/aiopools) 
- 电光笔记: [https://www.cyberlight.xyz/](https://www.cyberlight.xyz/)

## 最简示例

```python
'''
    该示例的协程任务数总计 100 个，设置最大允许的协程数 maxio 为 20，则需要运行 5 次才能完成。
'''

import asyncio
from aiopools import AsyncPool


async def block_io(i):
    await asyncio.sleep(1)
    print(i)
    return i


async def main():
    # 设置最大允许的协程数 maxio
    async with AsyncPool(maxio=20) as pool:
        tasks = [pool.create_task(block_io(i)) for i in range(100)]
    
    response = await asyncio.gather(*tasks)
    print(response)
    

if __name__ == '__main__':
    asyncio.run(main())

```
