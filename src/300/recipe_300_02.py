import pandas as pd

# シート名を指定した読み込み（Sheet1という名前のシートを指定）
df = pd.read_excel("MyBook.xlsx", sheet_name="Sheet1")

# シートのインデックスを指定した読み込み（最初のシートを指定）
df = pd.read_excel("MyBook.xlsx", sheet_name=0)  
