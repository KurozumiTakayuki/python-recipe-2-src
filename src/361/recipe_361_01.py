import asyncio


async def func1():
    print("タスクを開始しました。")
    try:
        await asyncio.sleep(5)  # ダミー処理
    except asyncio.CancelledError as e:
        print("タスクがキャンセルされました。")
        return "canceled"

    print("タスクが完了しました。")
    return "done"


async def main():
    # タスクを作成
    task = asyncio.create_task(func1())

    # 少し待ってからタスクをキャンセル
    await asyncio.sleep(1)
    task.cancel()
    status = await task
    print("status", status)


asyncio.run(main())
