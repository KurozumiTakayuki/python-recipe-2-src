from datetime import datetime
from zoneinfo import ZoneInfo

# Asia/Tokyoのタイムゾーンを指定した現在のdatetimeオブジェクトを生成
now_with_tz = datetime.now(tz=ZoneInfo("Asia/Tokyo"))
# now_with_tz = datetime.now(ZoneInfo("Asia/Tokyo"))   # tz=は省略可
print("now datetime:", now_with_tz)
