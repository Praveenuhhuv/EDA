import pandas as pd
import numpy as np

df1=pd.read_csv('C:/Users/dell/Downloads/txn_windows.csv',sep=',')
#rows count
print(df1.count())
print("%"*100)
#jan month oid,cusno,category,product,state
df2=df1[(df1['dat'] >= '01-01-2011') & (df1['dat'] <= '01-31-2011')].sort_values(by='dat') \
    [['oid','cuid','category','product','state']]
print(df2)
print("%"*100)
#rows count
print(len(df2))
print("%"*100)
#july month oid,cusno,category,product,state
df3=df1[(df1['dat'] >= '07-01-2011') & (df1['dat'] <= '07-31-2011')].sort_values(by='dat') \
    [['oid','cuid','category','product','state']]
print(df3)
print("%"*100)
#rows count
print(len(df3))
print("%"*100)
#4. Each category [count desc sort]
df4=df1.groupby('category') ['category'].count()\
    .sort_values(ascending=False)
print(df4)
print('%'*100)
#5. Category full deatils
df5=df1.sort_values(by='category')
print(df5)
print('%'*100)
#6. Each paymethod count
df6=df1.groupby('method') ['method'].count()
print(df6)
print('%'*100)
#7. jan-july month purchase count [include]
df7=df1[(df1['dat'] >= '01-01-2011') & (df1['dat'] <= '07-31-2011')].sort_values(by='pay_amount')
print(df7)
print('%'*100)
#8. Each category total amount
df8=df1.groupby('category') ['pay_amount'].sum().sort_values(ascending=False)
print(df8)
print('%'*100)
#9. Each category maximum amount
df9=df1.groupby('category') ['pay_amount'].max().sort_values(ascending=False)
print(df9)
print('%'*100)
#10. Each category maximum amount
df10=df1.groupby('category') ['pay_amount'].mean().sort_values(ascending=False)
print(df10)
print('%'*100)
#11.total amount by cash and credit card
df11=df1.groupby('method') ['pay_amount'].sum().sort_values(ascending=False)
print(df11)
print('%'*100)
#12. Indoor games ,total amount
df12=df1.loc[(df1['category'] == 'Indoor Games')].groupby('category') ['pay_amount'].sum()
print(df12)
print('%'*100)
#13. Each state count
df13=df1.groupby('state') ['state'].count()
print(df13)