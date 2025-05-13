import asyncio


async def increment(queue: asyncio.Queue):
    for _ in range(50):
        # カウンタの値を安全に取得
        value = await queue.get()  # Queueから値を取得
        await asyncio.sleep(0.01)  # ダミー処理
        value += 1
        await queue.put(value)  # 更新後の値をQueueに戻す


async def main():
    queue = asyncio.Queue()
    # 初期値をQueueに設定
    await queue.put(0)

    # 2つのincrementタスクを並列で実行
    await asyncio.gather(increment(queue), increment(queue))

    # 最終的な値を取得
    counter = await queue.get()
    print(f"カウンタの値: {counter}")


asyncio.run(main())
