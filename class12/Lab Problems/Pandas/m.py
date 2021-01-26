#Aim: Write a python program to export the data of a dataframe to a csv file.

import pandas as pd

data = {'names': ['a1', 'a2', 'a3', 'a4'], "marks": [60, 90, 50, 40]}
df = pd.DataFrame(data)
df.to_csv("marksheet.csv")