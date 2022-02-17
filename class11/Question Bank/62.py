#AIM-to take n no. of elements in a list from user and print it along with their index no.

data=[]
count=0
n=int(input("enter the number of elements in a list:"))
for i in range(n):
    print("enter the value in index number",i,":")
    value=(input())
    data.append(value)
print(data)