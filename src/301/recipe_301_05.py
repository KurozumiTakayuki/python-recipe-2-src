import pandas as pd

# サンプルDataFrameの作成
data = {
    'Name': ['鈴木', '佐藤', '山田'],
    'Age': [24, 27, 22],
    'City': ['大阪', '東京', '札幌']
}
df = pd.DataFrame(data)

# DataFrameをExcelファイルに出力
df.to_excel("OutputBook.xlsx", startrow=1, startcol=2)
