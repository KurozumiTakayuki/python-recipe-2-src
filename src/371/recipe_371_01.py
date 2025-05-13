from multiprocessing import Queue

# Queueオブジェクトの生成
q = Queue()

# データを追加する
q.put("dataA")
q.put("dataB")
q.put("dataC")


# データの取り出し
data1 = q.get()
print(data1, q.qsize())
data2 = q.get()
print(data2, q.qsize())
data3 = q.get()
print(data3, q.qsize())
