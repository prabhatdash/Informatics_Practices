#Aim: Given a series that stores he area of some states in km. Write a pyhthon program to find out the biggest and smallest 3 areas from the given series.
data=[34567,890,450,67892,34677,78902,256711,678291,637632,25723,2367,11789,345,256517]
s1=pd.Series(data)

Sol:
import pandas as pd
data=[34567,890,450,67892,34677,78902,256711,678291,637632,25723,2367,11789,345,256517]
s1=pd.Series(data)
print("The biggest 3 areas:")
print(s1.sort_values().tail(3))
print("The smallest 3 areas:")
print(s1.sort_values().head(3))
