import numpy as np
import pandas as pd
a=np.arange(1,21)
b=np.max(a)
print(b)
c=np.arange(1,26).reshape([5,5])
print(np.max(c,axis=0))
print(np.min(c))
