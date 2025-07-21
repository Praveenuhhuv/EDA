import pandas as pd
import numpy as np
df=pd.read_csv('C:/Users/dell/Downloads/sample4.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','phno','loc']
print(df)
df1=pd.read_csv('C:/Users/dell/Downloads/customer1.txt',sep=',',header=None)
df1.columns=['id','fname','lname','age','prof','country']
print(df1)
df2=pd.read_csv('C:/Users/dell/Downloads/customer5.csv',sep=',')
print(df2)
df3=pd.read_csv('C:/Users/dell/Downloads/movies_cleaned_pandas.csv',sep=',',header=None)
df3.columns=['id','Movie Name','Release year','Rate','Duration']
print(df3)
df4=df[['id','fname','lname','age','phno']].head(2)
print(df4)