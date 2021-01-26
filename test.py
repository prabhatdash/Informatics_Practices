#Aim: Use iteritems() to extract data from dataframe column wise.

import pandas as pd
data={
      "y1":{"q1":1000,"q2":2000,"q3":3000,"q4":4000},
      "y2":{"q1":5000,"q2":6000,"q3":7000,"q4":8000},
      "y3":{"q1":9000,"q2":10000,"q3":11000,"q4":12000}
      }
df=pd.DataFrame(data)


df['y1']=df['y1']+1
df.drop(['y1','y2'],inplace=True,axis=1)
print(df)
# df.drop('y3',inplace=True,axis=1)
# print(df[['y1','y2']].min())
