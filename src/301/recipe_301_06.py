import pandas as pd

# サンプルDataFrameの作成
data = {
    'Name': ['鈴木', '佐藤', '山田'],
    'Age': [24, 27, 22],
    'City': ['大阪', '東京', '札幌']
}
df = pd.DataFrame(data)

# DataFrameをExcelファイルに出力
with pd.ExcelWriter("OutputBook.xlsx") as writer:
 df1.to_excel(writer, sheet_name="Sheet1")
 df2.to_excel(writer, sheet_name="Sheet2")
 