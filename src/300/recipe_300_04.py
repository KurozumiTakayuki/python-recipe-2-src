import pandas as pd

sheets = pd.read_excel("MyBook2.xlsx", index_col='id')
# sheets = pd.read_excel("MyBook2.xlsx", index_col=0)

# 内容を確認する
print(sheets)
