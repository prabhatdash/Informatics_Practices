#TO EVALUATE THE FOLLOWING:
    #SUM OF nth TERM
	#TO CHECK IF AN EQUATION PRODUCES A STRAIGHT LINE OR NOT
	#FIND THE ROOTS OF QUADRATIC EQUATION
	#FIND THE MEAN OF n VALUES
n=int(input("n="))
sum=0
import math
for i in range(0,n):
    f=int(i)
    sum+=f
print(sum,"sum of nth terms:")
k=int(input("enter the number:"))
p=math.sqrt(k)
print(p,'square root:')
s=int(input("enter the number of terms:"))
sum1=0
for d in range(0,s):
    u=int(d)
    sum1+=u
print(sum1/u,"sum of  nth terms:")
m=float(input("enter slope:"))
c=float(input("enter constant"))
y=float(input("y="))
x=float(input("x="))
if y==m*x+c:
    print("It is a straight line")
else:
    print("It is not a straight line")

