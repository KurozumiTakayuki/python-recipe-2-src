import asyncio

async def main():
    q = asyncio.Queue(maxsize=1)
    await q.put(1)

    try:
        # 2秒以内にデータを追加
        await asyncio.wait_for(q.put(2), timeout=2)
    except asyncio.TimeoutError:
        print("タイムアウト: キューが満杯です。")

asyncio.run(main())
