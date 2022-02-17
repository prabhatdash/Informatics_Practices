#AIM-to create a dynamic list from the user which will take n no. of elements

data=[]
count=0
n=int(input("enter the number of elements in a list:"))
for i in range(n):
    print("enter the value in index number",i,":")
    value=(input())
    data.append(value)
print(data)