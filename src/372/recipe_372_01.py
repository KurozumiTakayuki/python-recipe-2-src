from multiprocessing import Queue
import queue

# サイズ1のキューを作成
q = Queue(maxsize=1)

# 最初の要素をキューに追加
q.put(1)

try:
    # 2秒以内にputできなければタイムアウト
    q.put(2, timeout=2)
except queue.Full:
    print("タイムアウト: キューが満杯です。")
