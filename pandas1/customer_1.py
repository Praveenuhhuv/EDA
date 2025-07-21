import pandas as pd
import numpy as np

df10=pd.read_csv('C:/Users/dell/Downloads/customer1.txt',sep=',',header=None)
df10.columns=['id','fname','lname','age','prof','Location']
x=df10.iloc[:,:-1]
print(x)
print('%'*100)
y=df10.iloc[:,-1]
print(y)
print('%'*100)
af=df10.sort_values(by='age',ascending=False)#make it dec
print(af)
print('%'*100)
max_prof=df10.groupby('prof')['age'].max()
print(max_prof)
print('%'*100)
min_prof=df10.groupby('prof')['age'].min() \
    .sort_values(ascending=False)
print(min_prof)
print('%'*100)
sum_prof=df10.groupby('prof')['age'].sum()
print(sum_prof)
print('%'*100)
avg_prof=df10.groupby('prof')['age'].mean()
print(avg_prof)

