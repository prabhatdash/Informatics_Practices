#TO CHECK IF THE NUMBER IS ARMSTRONG OR NOT.
a=input("enter the number:")
x=int(a)
b=len(a)
c=int(b)
sum=0
for i in range(0,c):
    d=int(a[i])**c
    sum+=d
if sum==x:
    print("the number the armstrong")
else:
    print("it is not armstrong")

