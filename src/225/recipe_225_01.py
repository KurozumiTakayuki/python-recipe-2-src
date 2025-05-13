from datetime import datetime

# 現在の日時
dt1 = datetime.now()

# 過去の日時
dt2 = datetime(2024, 11, 3, 12, 34, 56)

# 比較
if dt1 < dt2:
    print("現在の日時は%sより前です" % str(dt2))
elif dt1 > dt2:
    print("現在の日時は%sより後です" % str(dt2))
else:
    print("現在の日時は過去の日時と同じです。")
