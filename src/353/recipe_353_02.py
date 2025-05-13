import queue

# サイズ1の空のキューを作成
q = queue.Queue(maxsize=1)

try:
    # 2秒以内にgetできなければタイムアウト
    item = q.get(timeout=2)
except queue.Empty:
    print("タイムアウト: キューが空です。")
