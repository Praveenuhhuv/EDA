import pandas as pd
import numpy as np

a=pd.Series([3,5,6,7,8])
b=pd.Series([4,1,2,3,4])
c=a.add(b)
print(c)
d=a.sub(b)
print(d)
m=a.mul(b)
print(m)
di=a.div(b)
print(di)
join=a._append(b)
print(join)
join_in=a._append(b,ignore_index=True)
print(join_in)