# Aim: Write a python program to filter out the duplicate rows in a dataframe.

import pandas as pd
data={"name":['a1','a2','a3','a4','a4'],"id":[1,2,3,4,4],"marks":[10,20,30,40,40]}
df=pd.DataFrame(data)
df.drop_duplicates(inplace=True)
print(df)
