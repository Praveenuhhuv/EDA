import pandas as pd
import numpy as np
df=pd.read_csv('C:/Users/dell/Downloads/sample4.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','phno','loc']
print(df)
print('%'*100)
df1=df.loc[df['age']>22] [['fname','lname','age']]
print(df1)
print('%'*100)
df2=df.loc[df['age']==23] [['fname','lname','age']]
print(df2)
print('%'*100)
df3=df.loc[df['loc']=='Chennai'] [['fname','lname','age','phno']]
print(df3)
print('%'*100)
df4=df.loc[(df['age']==23) & (df['loc']=='Chennai'), ['fname','lname','age','loc']]
print(df4)
print('%'*100)
df10=pd.read_csv('C:/Users/dell/Downloads/customer1.txt',sep=',',header=None)
df10.columns=['id','fname','lname','age','prof','country']
print(df10)
print(df.isna().sum())
print('%'*100)
fd=df.iloc[3:6]
print(fd)