import pandas as pd

# サンプルDataFrameの作成
data = {
    'Name': ['鈴木', '佐藤', '山田'],
    'Age': [24, 27, 22],
    'City': ['大阪', '東京', '札幌']
}
df = pd.DataFrame(data)

# DataFrameをHTMLファイルに出力
df.to_html("output.html", index=False)
