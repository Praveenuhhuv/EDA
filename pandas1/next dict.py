import pandas as pd
import numpy as np

dict={'id':[1,2,3,4,5],'fname':['arun','praveen','sonu','aromal','aswin'],'lname':['j','l',
    'h','h','f'],'age':[11,22,33,44,55]}
df=pd.DataFrame(dict)
print(df)
print(df.shape)