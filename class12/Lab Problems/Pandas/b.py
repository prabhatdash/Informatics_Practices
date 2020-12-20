
#Aim: Given a Series, print all the elements that are above the 75th percentile.
#Code:

import pandas as pd
import numpy as np
l1=[10,20,30,40,30,45,22,33,37,55,56,44,33,34,36]
print(l1)
df=pd.Series(l1)
checklimit = np.percentile(df,75)
print(checklimit)

for i in df:
    if i > checklimit:
        print(i)
