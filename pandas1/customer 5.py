import pandas as pd
import numpy as np

df1=pd.read_csv('C:/Users/dell/Downloads/customer5.csv',sep=',')
df2=pd.DataFrame(df1)
sum_prof=df2.groupby('prof')['salary'].sum() \
    .sort_values(asending=False)
print(sum_prof)