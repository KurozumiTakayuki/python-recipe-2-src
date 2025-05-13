import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None]
})

# 平均値で補完
df_fill_mean = df.fillna(df.mean())
# 中央値で補完
df_fill_median = df.fillna(df.median())
# 最頻値で補完
df_fill_mode = df.fillna(df.mode().iloc[0])
