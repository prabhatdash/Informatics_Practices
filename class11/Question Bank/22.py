#sum of even numbers from 1-10
even=[]
for i in range(1,10+1):
	if i%2==0:
		even.append(i)
print(even)
x=sum(even)
print("sum of even numbers=",x)
		
#sum of odd numbers from 50-69
odd=[]
for j in range(50,60+1):
	if j%2!=0:
		odd.append(j)
print(even)
y=sum(odd)
print("sum of odd numbers=",y)		