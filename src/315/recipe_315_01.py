import pandas as pd

# マルチインデックスの生成
index = pd.MultiIndex.from_tuples(
    [('A', 2024), ('A', 2025), ('B', 2024), ('B', 2025), ('C', 2024), ('C', 2025)],
    names=['Category', 'Year']
)

# DataFrameのデータ
data = {'Sales': [10, 20, 30, 40, 50, 60], 'Revenue': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data, index=index)
print(df)
