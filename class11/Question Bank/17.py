#to print the sum of following series
#a) 1/2²,1/4²,1/6²,1/8²...........1/n²

limit=int(input("enter the limit or last value"))
demo=2
sum=0
for i in range(0,limit):
	val=demo**demo
	sum=sum+1/val
print(sum)

#b)4/4²,5/5²,6/6²........n/n²
 
l=int(input("enter the limit"))
summ=0
for j in range(0,limit):
 	value=(4+1)**2
 	summ=summ+4+1/value
print(summ) 	