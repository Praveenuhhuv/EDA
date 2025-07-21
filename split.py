import numpy as np;
a=np.array([1,5,3,4,5,8,8,7,9,0,7])
b=np.array_split(a,3)[0:2]
print(b)
print(b[0])