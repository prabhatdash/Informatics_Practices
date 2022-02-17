#Aim: Consider the Datframe df having some missing values (shown as NaN) as shown below:
#Write a program to fill the missing values with zero

import pandas as pd
import numpy as np
df=pd.DataFrame({'a':[1,2],'b':[2,np.NAN],'c':[np.NAN,4]})
print(df)
print("Dataframe after filling missing values")
df.fillna(0,inplace=True)
print(df)