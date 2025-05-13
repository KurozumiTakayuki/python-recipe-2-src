import threading
import time

# モジュール変数
counter = 0


# 50カウンタを増やす
def increment():
    global counter
    for _ in range(50):
        value = counter  # 読み込み
        time.sleep(0.01)  # ダミーI/O処理
        value += 1  # インクリメント
        counter = value  # 書き込み


# スレッドを作成
threads = []
for _ in range(2):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

# 全スレッドの終了を待機
for thread in threads:
    thread.join()

# 結果を表示
print(f"カウンタの値: {counter}")
