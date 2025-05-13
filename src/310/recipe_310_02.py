import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# NaN を 0 で埋める
df['A'] = df['A'].fillna(0)

print(df)
