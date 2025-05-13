import threading
import queue
import time

# スレッドセーフなキューを作成
counter_queue = queue.Queue()
counter_queue.put(0)  # 初期値をキューに格納


# カウンタを増やす関数
def increment():
    for _ in range(50):
        # キューから値を取り出して更新し、再度キューに戻す
        value = counter_queue.get()  # 読み込み
        time.sleep(0.01)  # ダミーI/O処理
        value += 1  # インクリメント
        counter_queue.put(value)  # 書き込み


# スレッドを作成
threads = []
for _ in range(2):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

# 全スレッドの終了を待機
for thread in threads:
    thread.join()

# 結果を取得して表示
result = counter_queue.get()
print(f"カウンタの値: {result}")
