import pandas as pd
import numpy as np

df1=pd.read_csv('C:/Users/dell/Downloads/missing_data.csv',sep=',')
df1['Calories'].fillna(300,inplace=True)
df1['Date'].fillna('2020/12/22',inplace=True)
print(df1)
print(df1.isna().sum())
x=df1['Calories'].mean()
df1['Calories'].fillna(x,inplace=True)
print(df1)

y=df1['Calories'].median()
df1['Calories'].fillna(y,inplace=True)
print(df1)

z=df1['Date'].mode()[0]
df1['Calories'].fillna(z,inplace=True)
print(df1)
print("&"*100)

df1.dropna(inplace=True,ignore_index=True)
print(df1)

df1.dropna(subset=['Date'],inplace=True,ignore_index=True)
print(df1)

print("&"*100)
x=df1['Calories'].mean()
for i in df1.index:
    if df1.loc[i,"Calories"]> 400:
        df1.loc[i,'Calories']=x
print(df1)