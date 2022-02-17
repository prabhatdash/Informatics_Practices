#AIM-to create two dynamic list and merge them

list_1=[]
limit=int(input("enter limit"))
for i in range(limit):
    n=input("enter value")
    list_1.append(n)

    print(list_1)

list_2=[]
limit2=int(input('enter limit'))
for i in range(limit2):
    n2=input("enter value")
    list_2.append(n2)

    print(list_2)

data=list_1+list_2
print(data)


