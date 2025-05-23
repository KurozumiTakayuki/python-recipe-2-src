import tracemalloc

tracemalloc.start()

# リストを2つ生成
list1 = [x + x for x in range(10000)]
list2 = [x * x for x in range(1000)]

# メモリ使用状況のスナップショットを取得
snapshot = tracemalloc.take_snapshot()

# 結果を行番号と共に上位10件出力
stats = snapshot.statistics('lineno')
for stat in stats[:10]:
    print(stat)

