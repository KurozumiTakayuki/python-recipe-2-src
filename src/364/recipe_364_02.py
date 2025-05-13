import asyncio

async def main():
    q = asyncio.Queue(maxsize=1)

    try:
        # 2秒以内にデータを取得
        item = await asyncio.wait_for(q.get(), timeout=2)
    except asyncio.TimeoutError:
        print("タイムアウト: キューが空です。")

asyncio.run(main())
