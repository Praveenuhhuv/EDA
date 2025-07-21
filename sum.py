import numpy as np
a=np.arange(1,21)
b=np.sum(a)
print(b)
c=np.arange(1,26).reshape([5,5])
print(np.sum(c,axis=0))
print(np.sum(c,axis=1))