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
    # 非同期実行するタスクを作成
    t1 = asyncio.create_task(func1())
    t2 = asyncio.create_task(func2())

    # タスクが完了するのを待機
    t1result = await t1
    t2result = await t2
    print(t1result, t2result)


asyncio.run(main())
