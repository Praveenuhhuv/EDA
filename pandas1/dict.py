

import pandas as pd
import numpy as np

a=pd.Series ({'id':101,'fname':'praveen','lname':'p','age':23,'prof':'dataseince','salary':10000},
             index=['fname','age','id','prof','salary'])
print(a)
b=pd.Series([6,2,1,9],index=[1,0,2,3])
print(b)