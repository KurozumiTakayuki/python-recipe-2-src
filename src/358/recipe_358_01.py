import asyncio


async def func1():
    print("Task 1 開始")
    await asyncio.sleep(1)
    print("Task 1 終了")
    return "Task 1 result"


async def func2():
    print("Task 2 開始")
    await asyncio.sleep(2)
    print("Task 2 終了")
    return "Task 2 result"


async def main():
    result1 = await func1()
    result2 = await func2()
    print(result1, result2)


asyncio.run(main())
