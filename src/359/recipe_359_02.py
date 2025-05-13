import asyncio


# バックグラウンドで動くタスク
async def background():
    for _ in range(5):
        print("Background task: 実行中...")
        await asyncio.sleep(1)  # ダミーのI/O待ち


# メイン処理
async def func():
    print("Main task: 処理開始")
    await asyncio.sleep(3)  # ダミーのI/O待ち
    print("Main task: 処理終了")


# メイン関数
async def main():
    # バックグラウンドタスクを作成
    bg_task = asyncio.create_task(background())

    # メイン処理を実行
    await func()

    # バックグランドタスクの終了を待機
    await bg_task


asyncio.run(main())
