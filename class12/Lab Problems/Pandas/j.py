#Aim: Use iteritems() to extract data from dataframe column wise.

import pandas as pd
data={
      "y1":{"q1":1000,"q2":2000,"q3":3000,"q4":4000},
      "y2":{"q1":5000,"q2":6000,"q3":7000,"q4":8000},
      "y3":{"q1":9000,"q2":10000,"q3":11000,"q4":12000}
      }
df=pd.DataFrame(data)


for col in df.iteritems():
    print(col)
