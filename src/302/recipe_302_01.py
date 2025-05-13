import pandas as pd

# URLやHTMLファイルのパスを指定して読み込み
url = "table_page.html"
tables = pd.read_html(url)

# 最初のテーブルを表示する
df = tables[0]  # 最初のテーブルを選択
print(df.head())
