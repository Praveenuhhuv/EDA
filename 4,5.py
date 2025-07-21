import numpy as np
a=np.array([[1,3,4,6,6],[7,7,8,5,8],[1,2,3,4,9],[1,2,3,4,9]])
print(a.shape)
b=a.reshape([1,2,10])
c=a.flatten()
print(b)
print(c)