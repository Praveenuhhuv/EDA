import numpy as np
a=np.arange(1,21)
for i in a:
    print(i,end=' ')
b=np.arange(1,21).reshape(4,5)
print()
for i in b:
    for j in i:
        print(j,end=' ')
c=np.arange(1,21).reshape(4,5)