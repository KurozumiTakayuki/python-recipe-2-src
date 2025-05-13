import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# 前方補完
df_ffill = df.ffill()
print(df_ffill)

# 後方補完
df_bfill = df.bfill()
print(df_bfill)
