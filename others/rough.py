# a=60
# b=50
#
# while True:
#     q=a//b
#     r=a%b
#     if r==0:
#         print(b)
#         break
#     else:
#         a=b
#         b=r

# year=int(input("enter the year"))
# if ((year%4==0) and (not (year%100==0))) or (year%400==0):
#     print("Leap Year")


import pandas as pd
import numpy as np
data1=[1,2,3,4,5,6,7,8,9]
s1=pd.Series(data1)
data2=[10,11,12,13,14]
s1=pd.Series(data1)
s2=pd.Series(data2)
print(s1+s2)

array1=np.array([1,2,3,4,5])
array2=np.array([6,7,8])
s1.sort_values(ascending=True,inplace=True)
print(s1)
