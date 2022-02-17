
#Aim: Create a Data Frame quarterly sales where each row contains the item category, item name, and expenditure. Group the rows by the category, and print the total expenditure per category.

#Code:

import pandas as pd
import numpy as np
data={'Item_Category':['book','pen','book','pen','pencil','book','pen','book'],'Item Name':['ip','flair','physics','cello','camlin','bst','natraj','chemistry'], 'Expenditure':[87,92,73,74,50,70,30,60]}
df=pd.DataFrame(data,index=[True,True,True,True,False,False,False,False])
# grouped_data=df.groupby('Item_Category')
# total_expenditure_per_category=grouped_data['Expenditure'].sum()
# print(total_expenditure_per_category)
# print(df)
# print(df.ndim)
print(df.radd())
D1
D2
D1.radd(D2)
D2+D1
# _________________
print(D1.add(D2))