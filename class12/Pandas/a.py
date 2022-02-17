
# Aim: Create a pandas series from a dictionary of values and an ndarray
# Code:

import pandas as pd
import numpy as np

di = {'a': 1, 'b': 2, 'c': 3}
df1 = pd.Series(di)
print(df1)
print('*' * 40)
arr = np.array([1, 2, 3, 4])
df2 = pd.Series(arr)
print(df2.sort_values())

# df=pd.DataFrame(data)
# print(df)
# print(df.iloc[0].mean())
# index_list=df.index.values
# col_list=df.columns
#
# print(col_list)
# print(index_list)
#
# for j in index_list:
#     mean_row=df.iloc[j].mean()
#     for i in col_list:
#         temp=df.loc[j][i]
#         value=temp-mean_row
#         print(value)


# df[df.values < 0] = 0
#
# print(df)
