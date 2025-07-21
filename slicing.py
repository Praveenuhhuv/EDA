import numpy as np
a=np.arange(1,21)
print(a[4:6])
print(a[::-1])
#2d
b=np.arange(1,26).reshape([5,5])
print(b)
print(b[:2,:2])
print(b[1:4:2,1::2])
print(b[0,:])
print(b[:,0])