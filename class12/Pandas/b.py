
#Aim: Given a Series, print all the elements that are above the 75th percentile.
#Code:

import pandas as pd
import numpy as np
l1=[10,20,30,40,30,45,22,33,37,55,56,44,33,34,36]
print(l1)
df=pd.Series(l1,name='oihoihio')
print(df.index)
print(df.values)
print(df.dtype)
print(df.shape)
print(df.nbytes)
print(df.ndim)
print(df.size)
print(df.hasnans)
print(df.empty)
print(df.name)
df.rename(index={0:100},inplace=True)
print(df.tail())

# checpr
# klimit = np.percentile(df,75)
# print(checklimit)
#
# for i in df:
#     if i > checklimit:
#         print(i)
