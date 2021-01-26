#Aim: Write a python program to create a series to store the marks of students and display the marks greater than n.
import pandas as pd
data=list()
limit=int(input("Enter the total no of students"))

for i in range(0,limit):
    print("Enter the marks of student no:",i+1)
    marks=int(input())
    data.append(marks)

print("Display the marks of students greater than:")
max_marks=int(input())
s1=pd.Series(data)
print(s1[s1>max_marks])
