import pandas as pd
import numpy as np
s = pd.Series([1, 3, 5, np.nan, 6, 8])
#print(s)

dates = pd.date_range('20191101', periods=7)
#print(dates)

df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('ABCD'))

#print(df.describe())
#print(df.T)

