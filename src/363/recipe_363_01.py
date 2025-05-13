import asyncio


async def main():
    # Queueオブジェクトの生成
    q = asyncio.Queue()

    # データを追加する
    await q.put("dataA")
    await q.put("dataB")
    await q.put("dataC")

    while not q.empty():
        # データの取り出し
        data = await q.get()
        print(data, q.qsize())


asyncio.run(main())
