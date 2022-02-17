#to store the age of your 5 best freinds in a list and display the nunber which are eligable to vote
sum=0
age=[]
for i in range(0,5):
	x=int(input("enter the age of freind:"))
	age.append(x)
print(age)
for j in age:
	if j>=18:
		sum+=1
print(sum)

	