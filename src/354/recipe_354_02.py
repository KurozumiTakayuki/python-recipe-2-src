import asyncio

async def fetch_data():
    print("データ取得中...")
    await asyncio.sleep(3)  # 非同期で3秒待機
    print("データ取得完了")
    return "データ"
