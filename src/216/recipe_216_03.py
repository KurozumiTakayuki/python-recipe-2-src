from datetime import datetime
from zoneinfo import ZoneInfo

# タイムゾーンなしのdatetimeオブジェクトを設定
dt = datetime(2024, 9, 1, 10, 30)
print("datetime:", dt)

# タイムゾーンなしにAsia/Tokyoを設定
dt_with_tz = dt.replace(tzinfo=ZoneInfo("Asia/Tokyo"))
print("datetime:", dt_with_tz)

# Asia/TokyoからUTCに付け替え
dt_with_tz = dt.replace(tzinfo=ZoneInfo("UTC"))
print("datetime:", dt_with_tz)
