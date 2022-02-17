#Aim: Write a python program to create the following dataframe and update the marks of the student Alex.

import pandas as pd
data={"name":['Alex','Mohan','Rohan','Bhushan'],"Marks":[20,30,40,50]}
df=pd.DataFrame(data)
print("Before Updating")
print(df)
df.iloc[0,1]=40
print("After Updating")
print(df)
