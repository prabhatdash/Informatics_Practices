#to find the sum of the following series 
#1+1/2+1/4+1/6+1/8.............1/n
limit=int(input("give the limit how many values you want"))
d=2
sum=0
for i in range(0,limit):
	val=d+2
	sum=sum+1/val
print(1+sum)