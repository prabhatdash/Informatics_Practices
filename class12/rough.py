import pandas as pd
data={'company':['bmw','bmw','honda','honda','toyota','toyota'],
      'body style':['sedan','sedan','sedan','sedan','hatchback','hatchback'],
      'wheel base':[101.2,101.2,96.5,96.5,95.7,95.7],
      'no of cylinders':['four','six','four','four','four','four',],
      'price':[16925,20970,12945,10345,5348,6338]
      }
df=pd.DataFrame(data)

print(df.iloc[2:5,])
print("**********")
print(df.loc[:,['company','wheel base','price']])
print("**********")
print(df.T)
print("**********")
df.loc[1,'price']=777
print("**********")
print(df)
print("**********")
max_price=df['price'].max()
for (i,j) in df.iterrows():
    if j[4]==max_price:
        print("Company Name:",j[0])
        break
print(df['company'][2:4])
print(df['company'][2:4])
df['ppp']=df['wheel base']+2
print(df)
print(df[['wheel base','price']].min())