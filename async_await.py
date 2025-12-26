import time
from asyncio import run, gather, sleep


async def func1():
    print("func1")
    await sleep(4)
    return "Hello from func1"


async def func2():
    print("func2")
    await sleep(3)
    return "Hello from func2"


async def func3():
    print("func3")
    await sleep(5)
    return "Hello from func3"


async def func4():
    return await gather(func1(), func2(), func3())


start = time.time()
l = run(func4())
end = time.time()
print(l)
print(end - start)
