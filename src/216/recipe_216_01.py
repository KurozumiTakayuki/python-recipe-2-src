from datetime import datetime
from zoneinfo import ZoneInfo

# Asia/Tokyoのタイムゾーンを指定したdatetimeオブジェクトを生成
dt_with_tz = datetime(2024, 9, 1, 10, 30, tzinfo=ZoneInfo("Asia/Tokyo"))
print("datetime:", dt_with_tz)
