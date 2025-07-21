import numpy as np
a=np.arange(1,21)
b=np.sort(a)[::-1]
print(b)
c=np.arange(1,26).reshape([5,5])
print(np.sort(c,axis=0))
print(np.sort(c))