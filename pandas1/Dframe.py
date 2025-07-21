import pandas as pd
import numpy as np

lst1=[[101,'vinay','k',27,'bigdata',1000],
      [102,'vivek','ps',30,'python',1503],
      [401, 'prv', 'p', 28, 'python',1750],
      [103,'erd','e',28,'bigdata',1500],
      [132, 'orv', 'o', 30, 'python',324],
      [109,'ghd','p',28,'bigdata',1500],
      [187, 'oiv', 'lk', 30, 'python',3204]]
df=pd.DataFrame(lst1)
df.columns=['id','fname','lname','age','Prof','Salary']
print(df)
print(df.shape)
print(df.size)
print(df.head(3))
print(df.tail(1))
print(df.dtypes)
print(df.describe())
print(df.describe(include='O'))
print(df.describe(include='all'))
df['Gender']=['m','f','m','m','f','f','m']
print(df)
df1=df.drop(['age','Prof'],axis=1)
print(df1)