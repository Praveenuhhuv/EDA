import pandas as pd
import numpy as np

df1=pd.read_csv('C:/Users/dell/Downloads/heart.csv',sep=',')
print(len(df1))
df2=df1.groupby('target') ['target'].count()
print(df2)
df3=df1.loc[(df1['age'] > 75)]
print(df3)
df4=df1.loc[(df1['age'] < 45)].groupby('target') ['target'].count()
print(df4)
df5=df1.sort_values(by='age',ascending=False).head(3)
print(df5)
x=df1.iloc[:,:-1]
print(x)
y=df1.iloc[:,-1]
print(y)