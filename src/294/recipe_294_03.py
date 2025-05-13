import pandas as pd
s = pd.Series(['2025-04-01 10:00:00', '2025-04-02 11:00:00', '2025-04-03 12:00:00'],
dtype='datetime64[ns]')
print(s.dtype)
