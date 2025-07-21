import pandas as pd
import numpy as np
a=np.arange(1,51)
one=pd.Series(a)[1:9]

print(one.head())
print(one.head(3))
print(one.tail())
print(one.dtype)