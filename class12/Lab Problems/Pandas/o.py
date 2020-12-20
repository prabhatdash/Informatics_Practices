#Aim: Write a python program to delete the last row of the dataframe.

import pandas as pd

data = {'names': ['a1', 'a2', 'a3', 'a4'], "marks": [60, 90, 50, 40]}
df = pd.DataFrame(data)
df.drop(3,inplace=True)
print(df)