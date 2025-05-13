import queue

# Queueオブジェクトの生成
q = queue.Queue()

# データを追加する
q.put("dataA")
q.put("dataB")
q.put("dataC")

while q.qsize():
    # データの取り出し
    data = q.get()
    print(data, q.qsize())
    