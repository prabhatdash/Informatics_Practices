# Aim: Write a python program to filter out the duplicate rows in a dataframe.

import pandas as pd
data={"id":[1,2,3,4,4],"marks":[10,20,30,40,40]}
df=pd.DataFrame(data)
print(df)
df['total']=df['marks']+df['id']
print(df[df['marks']==10])
