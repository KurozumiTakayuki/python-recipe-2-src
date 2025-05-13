from datetime import datetime

# ISO 8601形式の文字列
iso_string = "2024-10-13T15:30:00+09:00"

# ISO 8601形式の文字列をdatetimeに変換
dt = datetime.fromisoformat(iso_string)
print(type(dt), dt)
