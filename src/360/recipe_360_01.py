import asyncio


async def func1():
    print("Task 1 開始")
    await asyncio.sleep(1)
    print("Task 1 終了")
    return "result1"


async def func2():
    print("Task 2 開始")
    await asyncio.sleep(2)
    print("Task 2 終了")
    return "result2"


async def main():
    t1 = asyncio.create_task(func1())
    t2 = asyncio.create_task(func2())
    result = await asyncio.gather(t1, t2)
    print(result)


asyncio.run(main())
