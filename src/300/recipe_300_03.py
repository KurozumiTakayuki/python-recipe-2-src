import pandas as pd

# シート名のリストを指定した読み込み
sheets = pd.read_excel("MyBook.xlsx", sheet_name=["Sheet1", "Sheet2"])

# 全てのシートはsheet_nameにNoneを指定する
# sheets = pd.read_excel("MyBook.xlsx", sheet_name=None)

# 内容を確認する
print(sheets)
