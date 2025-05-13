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
    result = await asyncio.gather(func1(), func2())
    print(result)


asyncio.run(main())
