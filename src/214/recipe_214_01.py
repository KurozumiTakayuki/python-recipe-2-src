from datetime import datetime
from zoneinfo import ZoneInfo

# 現在時刻のdatetimeオブジェクトを生成
now = datetime.now(tz=ZoneInfo("Asia/Tokyo"))


# ISO 8601形式に変換
iso_string = now.isoformat()

print(iso_string)
