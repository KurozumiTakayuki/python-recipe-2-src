import asyncio

counter = 0


async def increment():
    global counter
    for _ in range(50):
        value = counter  # データの取り出し
        await asyncio.sleep(0.01)  # ダミー処理
        counter = value + 1  # データの更新


async def main():
    global counter
    counter = 0
    await asyncio.gather(increment(), increment())
    print(f"カウンタの値: {counter}")


asyncio.run(main())
